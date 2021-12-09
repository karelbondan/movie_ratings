import subprocess
try:
    import ctypes
    import re
    import signal
    import sys
    import urllib.request
    import bcrypt
    import cv2
    from PySide2 import QtGui
    from PySide2.QtCore import (Qt, Signal, QObject, Slot, QThread, QTimer)
    from PySide2.QtGui import (QIcon, QMovie)
    from PySide2.QtWidgets import *
except ImportError:
    subprocess.call('pip install -r requirements.txt', shell=True, cwd='')

import database
from gui import Ui_MainWindow

myappid = u'wolf.wolf.movie_ratings.1.0.0'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

_database = database.DatabaseFilm()


class Worker(QObject):
    # signals
    film = Signal(str, list)
    status = Signal(str)
    review = Signal(int, list, str)
    my_review = Signal(str, list)
    movie_found = Signal(int, list)
    register_status = Signal(str, str, str)
    login_status = Signal(str, str, list)
    change_pass_status = Signal(bool, str, str)
    logout_status = Signal(bool)
    del_acc_status = Signal(bool)
    current_user_review_exist = Signal(bool, list)
    review_successful = Signal(bool, str, list)
    delete_successful = Signal(bool, list, object)

    # methods
    def __init__(self):
        QObject.__init__(self)
        self._prohibited_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '·']
        # self._database = database.DatabaseFilm()

    def _strip_movie_name(self, movie_name: str):
        if ' ' in movie_name:
            movie_name = movie_name.replace(' ', '_')
            for i in self._prohibited_chars:
                if i in movie_name:
                    movie_name = movie_name.replace(i, '_')
        return movie_name

    def _movie_cover(self, movie_name: str, item: list):
        movie_name = self._strip_movie_name(movie_name)
        picname = f'data/img/poster/{movie_name}.jpg'
        try:
            open(f'data/img/poster/{movie_name}.jpg')
        except FileNotFoundError:
            urllib.request.urlretrieve(item[-2],
                                       f'data/img/poster/{movie_name}.jpg')
        try:
            image = cv2.imread(picname)

            width = 161
            height = 236
            dimension = (width, height)

            print(movie_name)
            resized_img = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)

            cv2.imwrite(f'{picname}', resized_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            pass

    @Slot(str)
    def all_movies(self, sort: str):
        self.status.emit("Updating ratings...")
        _database.updateRatings()
        self.status.emit("Querying movies from database...")
        movies = list(_database.getAllMovie(sort))
        for item in movies:
            self.status.emit(f"Listing movies... {item[1]}")
            movie_name = self._strip_movie_name(item[1])
            try:
                open(f'data/img/poster/{movie_name}.jpg')
            except FileNotFoundError:
                urllib.request.urlretrieve(item[-2], f'data/img/poster/{movie_name}.jpg')
            self._movie_cover(movie_name, item)
            self.film.emit(movie_name, item)
            # print(movie_name)
        self.status.emit("OK")

    @Slot(int, list)
    def search(self, movie_id: int, movie_list: list):
        self.status.emit("Updating movie review...")
        for index in range(len(movie_list)):
            if movie_id == movie_list[index][0]:
                self.movie_found.emit(index, _database.getMovieByID(movie_id))
        self.status.emit("OK")

    @Slot(list, int)
    def get_reviews(self, movie_list: list, movie_id: int):
        self.status.emit("Updating movie review...")
        _database.updateSpecificMovie(movie_id)
        self.status.emit("Getting reviews...")
        self.current_user_review_exist.emit(False, [])
        reviews = _database.getReview(movie_id)
        self.status.emit("Listing reviews...")
        for index, review in enumerate(reviews):
            self.review.emit(index, review, _database.getUser(review[2])[0][0])
            if _database.getCurrentUser()[0][0] == review[2]:
                my_review = _database.getIndividualReview(_database.getCurrentUser()[0][0], review[1])
                self.current_user_review_exist.emit(True, my_review)
        self.search(movie_id, movie_list)
        self.status.emit("OK")

    @Slot(str, str, str, str, str)
    def register(self, username, email, firstname, lastname, password):
        try:
            if _database.register(username, email, firstname, lastname, password):
                self.register_status.emit("Success", username, email)
                self.status.emit("OK")
            else:
                self.register_status.emit("Failed", username, email)
                self.status.emit("Failed")
        except database.UserExistError:
            self.register_status.emit("User", username, email)
            self.status.emit("Failed")
        except database.UsernameExistError:
            self.register_status.emit("Username", username, email)
            self.status.emit("Failed")

    @Slot(str, str)
    def login(self, useremail: str, password: str):
        self.status.emit("Logging in...")
        try:
            if _database.login(useremail, password):
                self.login_status.emit("Success", useremail, list(_database.getCurrentUser()))
                self.status.emit("OK")
            else:
                self.login_status.emit("Failed", useremail, [])
                self.status.emit("Failed")
        except database.InvalidCredentialsError:
            self.login_status.emit("Credentials", useremail, [])
            self.status.emit("Failed")
        except database.NoUserFoundError:
            self.login_status.emit("Record", useremail, [])
            self.status.emit("Failed")

    @Slot(str, str, str, bool)
    def change_password(self, current_pass: str, new_pass: str, new_pass_confirmation: str, password_valid: bool):
        self.status.emit("Changing password...")
        current_account_pass = _database.getCurrentUser()[0][-1]
        if current_pass == "" or new_pass == "" or new_pass_confirmation == "":
            self.change_pass_status.emit(False, 'Fields', _database.getCurrentUser()[0][1])
            self.status.emit("Failed")
        elif not bcrypt.checkpw(current_pass.encode(), current_account_pass.encode()):
            self.change_pass_status.emit(False, 'Credentials', _database.getCurrentUser()[0][1])
            self.status.emit("Failed")
        elif len(new_pass) < 8:
            self.change_pass_status.emit(False, 'Lesser', _database.getCurrentUser()[0][1])
            self.status.emit("Failed")
        elif not password_valid:
            self.change_pass_status.emit(False, 'Valid', _database.getCurrentUser()[0][1])
            self.status.emit("Failed")
        elif new_pass != new_pass_confirmation:
            self.change_pass_status.emit(False, 'Input', _database.getCurrentUser()[0][1])
            self.status.emit("Failed")
        else:
            hashed_pw = bcrypt.hashpw(new_pass.encode(), bcrypt.gensalt()).decode('utf-8')
            if _database.updatePassword(_database.getCurrentUser()[0][0], hashed_pw):
                self.change_pass_status.emit(True, 'Normal', _database.getCurrentUser()[0][1])
                self.status.emit("OK")
            else:
                self.change_pass_status.emit(False, 'Failed', _database.getCurrentUser()[0][1])
                self.status.emit("Failed")

    @Slot()
    def logout(self):
        self.status.emit("Logging out...")
        if _database.logout():
            self.logout_status.emit(True)
            self.status.emit("OK")
        else:
            self.logout_status.emit(False)
            self.status.emit("Failed")

    @Slot()
    def delete_account(self):
        self.status.emit("Deleting account...")
        if _database.deleteAccount(_database.getCurrentUser()[0][0]):
            self.del_acc_status.emit(True)
            self.status.emit("OK")
        else:
            self.del_acc_status.emit(False)
            self.status.emit("Failed")

    @Slot()
    def my_reviews(self):
        self.status.emit("Getting your reviews...")
        reviews = list(_database.getMyReview(_database.getCurrentUser()[0][0]))
        for review in reviews:
            self.my_review.emit(_database.getMovieName(review[1])[0][0], review)
        self.status.emit("OK")

    @Slot(int, int, str, int)
    def add_review(self, movieID: int, userID: int, reviewDesc: str, ratings: int):
        self.status.emit("Adding review...")
        userID = _database.getCurrentUser()[0][0]
        if _database.publishRatings(movieID, userID, reviewDesc, ratings):
            new_movie_details = _database.getMovieByID(movieID)[0]
            self.review_successful.emit(True, 'normal', new_movie_details)
            self.status.emit("OK")
        else:
            self.review_successful.emit(False, 'normal', [])
            self.status.emit("Failed")

    @Slot(int, int, str, int, str)
    def update_review(self, movieID: int, userID: int, reviewDesc: str, ratings: int, condition: str):
        self.status.emit("Updating review...")
        userID = _database.getCurrentUser()[0][0]
        if _database.updateReview(movieID, userID, reviewDesc, ratings):
            new_movie_details = _database.getMovieByID(movieID)[0]
            self.review_successful.emit(True, condition, new_movie_details)
            self.status.emit("OK")
        else:
            self.review_successful.emit(False, condition, [])
            self.status.emit("Failed")

    @Slot(int, int, object)
    def delete_review(self, userID: int, movieID: int, widget: object):
        userID = _database.getCurrentUser()[0][0]
        self.status.emit("Deleting review...")
        if _database.deleteRatings(userID, movieID):
            new_movie_details = _database.getMovieByID(movieID)[0]
            self.delete_successful.emit(True, new_movie_details, widget)
            self.status.emit("OK")
        else:
            self.delete_successful.emit(False, [], widget)
            self.status.emit("Failed")


class MainWindow(QMainWindow):
    all_movies_requested = Signal(str)
    query = Signal(str)
    review_requested = Signal(list, int)
    reg = Signal(str, str, str, str, str)
    log_in = Signal(str, str)
    change_pass = Signal(str, str, str, bool)
    log_out = Signal()
    del_acc = Signal()
    my_rev = Signal()
    rev_search = Signal(int, list)
    add_review = Signal(int, int, str, int)
    update_review = Signal(int, int, str, int, str)
    del_review = Signal(int, int, object)

    def __init__(self):
        QMainWindow.__init__(self)
        # splash screen
        self._splash = subprocess.Popen('python splash.py', shell=True,
                                        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.reviewslist_moviedetails.setWordWrap(True)
        self.ui.reviewslist_myreviews.setWordWrap(True)
        self.ui.alluserreviewslist_allreviews.setWordWrap(True)
        self._visited = []
        self._regex_email = r'[a-zA-Z0-9]+([._][a-zA-Z0-9]+)*@([a-z0-9|A-Z0-9]+\.)+[a-z0-9|A-Z0-9]{2,}$'
        self._regex_password = '(?=.*[a-zA-Z])(?=.*[0-9!#$%&()*+,.;<=>?@\[\]^_{}~])[a-zA-Z0-9!#$%&()*+,.;<=>?@\[\]^_{}~]{8,}'
        self._movie_all = []
        self._review_all = []
        self._movie_my_review = []
        self._user_all = []
        self._user_id_reviews = []
        self._star_button = [self.ui.starbutton_1, self.ui.starbutton_2, self.ui.starbutton_3, self.ui.starbutton_4,
                             self.ui.starbutton_5, self.ui.starbutton_6, self.ui.starbutton_7, self.ui.starbutton_8,
                             self.ui.starbutton_9, self.ui.starbutton_10]
        self._rating_phrases = ['Absolute trash, not even worth a penny', 'Trash', 'Trash, but still tolerable',
                                'This movie is a joke', 'Still watchable', 'Meh', 'Ok', 'Good', 'Amazing',
                                'Masterpiece']
        self._rating_star = 0
        self._previous_search = ''
        self._movie = None
        self._movie_synopsis = []
        self._movie_prohibited_char = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '·']
        self._small_user_icon = QtGui.QIcon('data/img/login_border_small.png')
        self._star_default = QtGui.QIcon('data/img/star_default_small.png')
        self._star_filled = QtGui.QIcon('data/img/star_filled_small.png')
        self._app_icon = QtGui.QIcon('data/img/icon.ico')
        self._loading_gif = QMovie('data/img/loading20.gif')
        self.ui.loading_icon.setMovie(self._loading_gif)
        self._loading_gif.start()

        # worker and thread
        self.worker = Worker()
        self.worker_movies = Worker()
        self.worker_reviews = Worker()
        self.worker_my_reviews = Worker()
        self.worker_thread = QThread()
        self.worker_movies_thread = QThread()
        self.worker_reviews_thread = QThread()
        self.worker_my_reviews_thread = QThread()

        self.worker_movies.film.connect(self.add_movie_to_list)
        self.worker.status.connect(self.set_status)
        self.worker_movies.status.connect(self.set_status)
        self.worker_reviews.status.connect(self.set_status)
        self.worker_my_reviews.status.connect(self.set_status)
        self.worker.register_status.connect(self.register_final)
        self.worker.login_status.connect(self.login_final)
        self.worker.change_pass_status.connect(self.change_pass_final)
        self.worker.logout_status.connect(self.logout_final)
        self.worker.del_acc_status.connect(self.delete_account_final)
        self.worker_reviews.review.connect(self.reviews)
        self.worker_reviews.movie_found.connect(self.update_specific)
        self.worker_my_reviews.my_review.connect(self.set_my_reviews)
        self.worker_my_reviews.movie_found.connect(self.update_specific)
        self.worker.review_successful.connect(self.review_success)
        self.worker.delete_successful.connect(self.delete_success)
        self.worker_reviews.current_user_review_exist.connect(self.review_exist)

        self.all_movies_requested.connect(self.worker_movies.all_movies)
        self.review_requested.connect(self.worker_reviews.get_reviews)
        self.my_rev.connect(self.worker_my_reviews.my_reviews)
        self.rev_search.connect(self.worker_my_reviews.search)
        self.add_review.connect(self.worker.add_review)
        self.update_review.connect(self.worker.update_review)
        self.del_review.connect(self.worker.delete_review)
        self.reg.connect(self.worker.register)
        self.log_in.connect(self.worker.login)
        self.change_pass.connect(self.worker.change_password)
        self.log_out.connect(self.worker.logout)
        self.del_acc.connect(self.worker.delete_account)

        # moving to thread
        self.worker.moveToThread(self.worker_thread)
        self.worker_movies.moveToThread(self.worker_movies_thread)
        self.worker_reviews.moveToThread(self.worker_reviews_thread)
        self.worker_my_reviews.moveToThread(self.worker_my_reviews_thread)
        self.worker_thread.start()
        self.worker_movies_thread.start()
        self.worker_reviews_thread.start()
        self.worker_my_reviews_thread.start()

        # setting the app icon to show on the taskbar
        self.setWindowIcon(self._app_icon)

        # configuring stacked widget - register
        self.ui.registerbutton_register.clicked.connect(lambda: self.register())
        self.ui.loginbutton_register.clicked.connect(lambda: self.ui.body.setCurrentWidget(self.ui.login))

        # configuring stacked widget - login
        self.ui.loginbutton_login.clicked.connect(lambda: self.login())
        self.ui.registerbutton_login.clicked.connect(lambda: self.ui.body.setCurrentWidget(self.ui.register_2))

        # configuring stacked widget - movie list
        self.ui.profilebutton_movielist.clicked.connect(lambda: self.set_widget(self.ui.profile))
        self.ui.viewdetailsbutton_movielist.clicked.connect(lambda: self.set_widget(self.ui.moviedetail))
        self.ui.movielist_movielist.itemDoubleClicked.connect(lambda: self.set_widget(self.ui.moviedetail))
        self.ui.sortmovie_movielist.currentIndexChanged.connect(lambda: self.all_movies_call())
        self.ui.searchmovie_movielist.returnPressed.connect(
            lambda: self.refresh_list(self.ui.searchmovie_movielist.text()))
        self.ui.searchbutton_movielist.clicked.connect(lambda: self.refresh_list(self.ui.searchmovie_movielist.text()))
        self.ui.refreshbutton_movielist.clicked.connect(lambda: self.all_movies_call())

        # configuring stacked widget - movie details
        self.ui.profilebutton_moviedetails.clicked.connect(lambda: self.set_widget(self.ui.profile))
        self.ui.backbutton_moviedetails.clicked.connect(lambda: self.back())
        self.ui.writereviewbutton_moviedetails.clicked.connect(lambda: self.set_widget(self.ui.reviewmovie, 'new'))
        self.ui.editreviewbutton_moviedetails.clicked.connect(lambda: self.set_widget(self.ui.reviewmovie, 'edit'))
        self.ui.deletereviewbutton_moviedetails.clicked.connect(lambda: self.delete_review(self.ui.moviedetail))
        self.ui.viewallbutton_moviedetails.clicked.connect(lambda: self.set_widget(self.ui.allreviews))
        self.ui.refreshbutton_moviedetails.clicked.connect(lambda: self.get_reviews())

        # configuring stacked widget - profile
        self.ui.backbutton_profile.clicked.connect(lambda: self.back())
        self.ui.homebutton_profile.clicked.connect(lambda: self.set_widget(self.ui.movielist))
        self.ui.logoutbutton_profile.clicked.connect(lambda: self.logout())
        self.ui.deleteaccountbutton_profile.clicked.connect(lambda: self.delete_account())
        self.ui.myreviewsbutton_profile.clicked.connect(lambda: self.set_widget(self.ui.myreviews))
        self.ui.confirmchangesbutton_profile.clicked.connect(lambda: self.change_password())

        # configuring stacked widget - my reviews
        self.ui.backbutton_myreviews.clicked.connect(lambda: self.back())
        self.ui.homebutton_myreviews.clicked.connect(lambda: self.set_widget(self.ui.movielist))
        self.ui.reviewslist_myreviews.itemDoubleClicked.connect(lambda: self.set_widget(self.ui.reviewmovie, 'my'))
        self.ui.editreviewbutton_myreviews.clicked.connect(lambda: self.set_widget(self.ui.reviewmovie, 'my'))
        self.ui.deletereviewbutton_myreviews.clicked.connect(lambda: self.set_widget(self.ui.myreviews))

        # configuring stacked widget - review list
        self.ui.backbutton_allreviews.clicked.connect(lambda: self.back())
        self.ui.homebutton_allreviews.clicked.connect(lambda: self.set_widget(self.ui.movielist))
        self.ui.writereviewbutton_allreviews.clicked.connect(lambda: self.set_widget(self.ui.reviewmovie, 'new'))
        self.ui.editreviewbutton_allreviews.clicked.connect(lambda: self.set_widget(self.ui.reviewmovie, 'edit'))
        self.ui.deletereviewbutton_allreviews.clicked.connect(lambda: self.delete_review(self.ui.allreviews))
        self.ui.refreshbutton_allreviews.clicked.connect(lambda: self.get_reviews())

        # configuring stacked widget - review movie
        self.ui.submitreviewbutton_reviewnow.clicked.connect(lambda: self.publish_review())
        self.ui.updatereviewbutton_reviewnow.clicked.connect(lambda: self.publish_review('update'))
        self.ui.updatereviewbutton_myrev_reviewnow.clicked.connect(lambda: self.publish_review('update_my'))
        self.ui.backbutton_reviewnow.clicked.connect(lambda: self.back())
        self.ui.homebutton_reviewnow.clicked.connect(lambda: self.set_widget(self.ui.movielist))
        self.ui.starbutton_1.clicked.connect(lambda: self.star_button_clicked(1))
        self.ui.starbutton_2.clicked.connect(lambda: self.star_button_clicked(2))
        self.ui.starbutton_3.clicked.connect(lambda: self.star_button_clicked(3))
        self.ui.starbutton_4.clicked.connect(lambda: self.star_button_clicked(4))
        self.ui.starbutton_5.clicked.connect(lambda: self.star_button_clicked(5))
        self.ui.starbutton_6.clicked.connect(lambda: self.star_button_clicked(6))
        self.ui.starbutton_7.clicked.connect(lambda: self.star_button_clicked(7))
        self.ui.starbutton_8.clicked.connect(lambda: self.star_button_clicked(8))
        self.ui.starbutton_9.clicked.connect(lambda: self.star_button_clicked(9))
        self.ui.starbutton_10.clicked.connect(lambda: self.star_button_clicked(10))

        # listing all movies and reviews
        self.all_movies_call()

        # showing the main window
        self._splash.send_signal(signal.CTRL_BREAK_EVENT)
        self.ui.body.setCurrentWidget(self.ui.login)
        self.show()

    @Slot(str)
    def set_status(self, status: str):
        self.ui.status_main.setText(f"Status: {status}")
        if status == "OK" or status == "Failed":
            timer = QTimer(self)
            self.ui.loading_icon.hide()
            timer.singleShot(2000, self.ui.status_main.hide)
        else:
            self.ui.status_main.show()
            self.ui.loading_icon.show()

    def show_message_box(self, message: str):
        self._info = QMessageBox()
        self._info.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self._info.setWindowTitle("Movie Ratings")
        self._info.setWindowIcon(self._app_icon)
        self._info.setText(message)
        return self._info.show()

    def strip_movie_name(self, movie_name: str):
        if ' ' in movie_name:
            movie_name = movie_name.replace(' ', '_')
            for i in self._movie_prohibited_char:
                if i in movie_name:
                    movie_name = movie_name.replace(i, '_')
        return movie_name

    def movie_cover(self, movie_name: str):
        movie_name = self.strip_movie_name(movie_name)
        picname = f'data/img/poster/{movie_name}.jpg'
        try:
            open(picname)
        except FileNotFoundError:
            print(self._movie_all[self.ui.movielist_movielist.currentRow()])
            urllib.request.urlretrieve(self._movie_all[self.ui.movielist_movielist.currentRow()][-2],
                                       f'data/img/poster/{movie_name}.jpg')
            try:
                image = cv2.imread(picname)

                width = 161
                height = 236
                dimension = (width, height)

                print(movie_name)
                resized_img = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)

                cv2.imwrite(f'{picname}', resized_img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            except:
                pass

        self.ui.movieposter_moviedetails.setPixmap(picname)

    def star_button_clicked(self, star=-1):
        self._rating_star = star
        for i in range(len(self._star_button)):
            self._star_button[i].setIcon(self._star_default)
        self.ui.expressionstar_reviewnow.setText('')
        if star != -1:
            for j in range(star):
                if j <= star:
                    self._star_button[j].setIcon(self._star_filled)
                else:
                    self._star_button[j].setIcon(self._star_default)
                self.ui.expressionstar_reviewnow.setText(self._rating_phrases[star - 1])

    def register(self):
        email = self.ui.email_register.text().strip().lower()
        username = self.ui.username_register.text().strip().lower()
        firstname = self.ui.firstname_register.text().strip().lower().capitalize()
        lastname = self.ui.lastname_register.text().strip().lower().capitalize()
        password = self.ui.password_register.text()
        confirm = self.ui.confirmpassword_register.text()
        email_valid = re.match(self._regex_email, email)
        password_valid = re.match(self._regex_password, password)

        if email == "" or username == "" or firstname == "" or lastname == "" or password == "" or confirm == "":
            self.show_message_box("Input fields must not be empty.")
        elif not email_valid:
            self.show_message_box("Please enter a valid email address.")
        elif len(password) < 8:
            self.show_message_box("Password must contain at least 8 characters.")
        elif not password_valid:
            self.show_message_box(
                "Password must have a combination of minimum one letter of any kind and either digits "
                "or punctuations. (example: George123#)")
        elif password != confirm:
            self.show_message_box("Passwords do not match, please re-check your input.")
        else:
            self.reg.emit(username, email, firstname, lastname, password)

    @Slot(str, str, str)
    def register_final(self, condition: str, username: str, email: str):
        if condition == 'Success':
            self.show_message_box(f"Thank you for registering, {username}! Please login to continue.")
            self.ui.body.setCurrentWidget(self.ui.login)
            self.ui.email_register.clear()
            self.ui.username_register.clear()
            self.ui.password_register.clear()
            self.ui.confirmpassword_register.clear()
        elif condition == "User":
            self.show_message_box(
                f"A user with email address {email} already exist. "
                f"Please login or create an account using a different email.")
        elif condition == "Username":
            self.show_message_box(f"Username {username} is already taken, please choose another username.")
        else:
            self.show_message_box("Something unexpected happened. Please check your network connection"
                                  "or relaunch the application.")

    def login(self):
        useremail = self.ui.useremail_login.text().strip()
        password = self.ui.password_login.text()

        if useremail == "" or password == "":
            self.show_message_box("Input fields must not be empty")
        else:
            self.log_in.emit(useremail, password)

    @Slot(str, str, list)
    def login_final(self, condition: str, useremail: str, user_info: list):
        if condition == "Success":
            self.ui.firstlastname_profile.setText(f'{user_info[0][3]} {user_info[0][4]}')
            self.ui.registeredsince_profile.setText(f'{user_info[0][-2].strftime("%d %B %Y")}')
            self.ui.emailinfo_profile.setText(f'Email: {user_info[0][2]}')
            self.ui.usernameinfo_profile.setText(f'Username: {user_info[0][1]}')
            self.show_message_box(f"Welcome, {useremail}! Glad to have you back.")
            self.set_widget(self.ui.movielist)
            self.ui.useremail_login.clear()
            self.ui.password_login.clear()
        elif condition == "Credentials":
            self.show_message_box("Wrong password. Please recheck your credentials.")
        elif condition == "Record":
            self.show_message_box("No user with such credentials found. Please make a new account first.")
        else:
            self.show_message_box("Something unexpected happened. Please check your network connection"
                                  "or relaunch the application.")

    def change_password(self):
        current_pass = self.ui.currentpassword_profile.text()
        new_pass = self.ui.newpassword_profile.text()
        new_pass_confirmation = self.ui.confirmnewpassword_profile.text()
        password_valid = re.match(self._regex_password, new_pass)
        if password_valid:
            self.change_pass.emit(current_pass, new_pass, new_pass_confirmation, True)
        else:
            self.change_pass.emit(current_pass, new_pass, new_pass_confirmation, False)

    @Slot(bool, str, str)
    def change_pass_final(self, succeeded: bool, condition: str, username: str):
        if succeeded:
            self.show_message_box(f"Success! Password changed for account {username}")
            self.ui.currentpassword_profile.clear()
            self.ui.newpassword_profile.clear()
            self.ui.confirmnewpassword_profile.clear()
        else:
            if condition == "Fields":
                self.show_message_box("Input fields must not be empty.")
            elif condition == "Credentials":
                self.show_message_box("Wrong password. Please recheck your credentials")
            elif condition == "Lesser":
                self.show_message_box("Password must contain at least 8 characters.")
            elif condition == "Valid":
                self.show_message_box(
                    "Password must have a combination of minimum one letter of any kind and either digits "
                    "or punctuations. (example: George123#)")
            elif condition == "Input":
                self.show_message_box("Passwords do not match, please re-check your input.")
            else:
                self.show_message_box("Something unexpected happened. "
                                      "Please check your network connection or relaunch the application. "
                                      "User password remains the same as before.")

    def logout(self):
        self.log_out.emit()

    @Slot(bool)
    def logout_final(self, succeeded: bool):
        if succeeded:
            self.show_message_box("Logged out. Please login again")
            self.set_widget(self.ui.login)
        else:
            self.show_message_box("Something unexpected happened. Please check your network connection"
                                  "or relaunch the application.")

    def delete_account(self):
        self._confirmation = QMessageBox()
        self._confirmation.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self._confirmation.setWindowIcon(self._app_icon)
        question = self._confirmation.question(self, 'Movie Ratings', 'Are you sure you want to delete your account? '
                                                                      'All your reviews you have so far will be deleted '
                                                                      'and your deleted account will not be recoverable.',
                                               self._confirmation.Yes | self._confirmation.No)

        if question == self._confirmation.Yes:
            self.del_acc.emit()
        else:
            pass

    @Slot(bool)
    def delete_account_final(self, succeeded: bool):
        if succeeded:
            self.show_message_box("Your account and all its data has been successfully deleted. "
                                  "Thank you for using our service this far!")
            self.set_widget(self.ui.login)
            self.all_movies_call()
        else:
            self.show_message_box("Something unexpected happened. Please check your network connection"
                                  "or relaunch the application.")

    def refresh_list(self, search=''):
        if search == self._previous_search:
            pass
        else:
            for item in range(len(self._movie_all)):
                movie_name = self._movie_all[item][1]
                list_item = self.ui.movielist_movielist.item(item)
                if search.lower() not in movie_name.lower():
                    list_item.setHidden(True)
                else:
                    list_item.setHidden(False)
            self._previous_search = search

    def all_movies_call(self):
        self.ui.movielist_movielist.clear()
        self._movie_synopsis.clear()
        self._movie_all.clear()

        self.all_movies_requested.emit(str(self.ui.sortmovie_movielist.currentText()))

    def add_movie_to_list(self, movie_name: str, movie_item: list):
        self.ui.movielist_movielist.addItem(
            QListWidgetItem(QIcon(f'data/img/poster/{movie_name}.jpg'),
                            f'{movie_item[1]}\n{movie_item[2]}\n★ {movie_item[-3]}'))
        self._movie_synopsis.append(movie_item[-4])
        self._movie_all.append(movie_item)
        # print(movie_item)

    def get_reviews(self):
        self.ui.reviewslist_moviedetails.clear()
        self.ui.alluserreviewslist_allreviews.clear()
        self.review_requested.emit(self._movie_all,
                                   self._movie_all[self.ui.movielist_movielist.currentRow()][0])

    @Slot(int, list, str)
    def reviews(self, index: int, review: list, username: str):
        self._user_id_reviews.append(review[2])
        self.ui.alluserreviewslist_allreviews.addItem(
            QListWidgetItem(self._small_user_icon,
                            f'{username}'
                            f'\n★ {review[-1]}'
                            f'\n\n{review[-2]}'
                            f'\n\nDate reviewed: {review[-3].strftime("%d %B %Y")}'
                            f'\n__________________________________________________________________________________________'))
        if index <= 5:
            self.ui.reviewslist_moviedetails.addItem(
                QListWidgetItem(self._small_user_icon,
                                f'{username}'
                                f'\n★ {review[-1]}'
                                f'\n\n{review[-2]}'
                                f'\n\nDate reviewed: {review[-3].strftime("%d %B %Y")}'
                                f'\n__________________________________________________________________________________________'))

    @Slot(bool)
    def review_exist(self, review_exists: bool, my_review: list):
        if review_exists:
            self.ui.writereviewframe_moviedetails.hide()
            self.ui.myreviewframe_moviedetails.show()
            print(my_review)
            self.ui.myrating_moviedetails.setText(
                f"My Review - ★ {my_review[-1][-1]}")
            self.ui.myreviewdesc_moviedetails.setText(my_review[-1][-2])

            self.ui.writereviewframe_allreviews.hide()
            self.ui.myrewiewframe_allreviews.show()
            self.ui.myrating_allreviews.setText(
                f"My Review - ★ {my_review[-1][-1]}")
            self.ui.myreviewdesc_allreviews.setText(my_review[-1][-2])
        else:
            self.ui.writereviewframe_moviedetails.show()
            self.ui.myreviewframe_moviedetails.hide()

            self.ui.writereviewframe_allreviews.show()
            self.ui.myrewiewframe_allreviews.hide()

    def my_reviews(self):
        self.ui.reviewslist_myreviews.clear()
        self._movie_my_review.clear()
        self.my_rev.emit()

    @Slot(str, list)
    def set_my_reviews(self, movie_name: str, review: list):
        self._movie_my_review.append(review)
        self.ui.reviewslist_myreviews.addItem(QListWidgetItem(self._small_user_icon,
                                                              f"{movie_name}\n"
                                                              f"★ {review[-1]}"
                                                              f"\n\n{review[-2]}"
                                                              f"\n\nDate reviewed: {review[-3].strftime('%d %B %Y')}\n"
                                                              f"__________________________________________________________________________________________"))

    def publish_review(self, condition='normal'):
        if self.ui.reviewdesc_textbox_reviewnow.toPlainText().strip() == "":
            self.show_message_box("Please enter at least one word")
        elif self._rating_star == -1:
            self.show_message_box("Please input your rating")
        elif condition == 'update' or condition == 'update_my':
            if condition == 'update':
                movie_id = self._movie_all[self.ui.movielist_movielist.currentRow()][0]
            else:
                movie_id = self._movie_my_review[self.ui.reviewslist_myreviews.currentRow()][1]
                print(self._movie_my_review)
            self.update_review.emit(movie_id, 1,
                                    self.ui.reviewdesc_textbox_reviewnow.toPlainText()
                                    .replace("'", "\\'")
                                    .replace('"', '\\"'),
                                    self._rating_star, condition
                                    )

        else:
            self.add_review.emit(self._movie_all[self.ui.movielist_movielist.currentRow()][0], 1,
                                 self.ui.reviewdesc_textbox_reviewnow.toPlainText()
                                 .replace("'", "\\'")
                                 .replace('"', '\\"'),
                                 self._rating_star)

    @Slot(bool, str, list)
    def review_success(self, succeeded: bool, condition: str, updated_movie: list):
        if succeeded:
            self.show_message_box("Success! Thank you for reviewing this movie.")
            if condition == 'update':
                self.set_widget(self.ui.moviedetail)
            elif condition == 'update_my':
                self.rev_search.emit(self._movie_my_review[self.ui.reviewslist_myreviews.currentRow()][1],
                                     self._movie_all)
                self.set_widget(self.ui.myreviews)
            else:
                self.set_widget(self.ui.moviedetail)
            self._visited.pop()
            self._visited.pop()  # yes two times.
            if condition != 'update_my':
                self.ui.movielist_movielist.currentItem().setText(
                    f'{updated_movie[1]}\n{updated_movie[2]}\n★ {updated_movie[-3]}')
                self._movie_all[self.ui.movielist_movielist.currentRow()] = updated_movie
                self.ui.ratingscount_moviedetails.setText(
                    f'{updated_movie[-3]} based on {self._movie_all[self.ui.movielist_movielist.currentRow()][-1]} reviews')
        else:
            self.show_message_box(
                "Something unexpected happened. Please try again later or relaunch the application")

    @Slot(int, list)
    def update_specific(self, index: int, updated_movie: list):
        self.ui.movielist_movielist.item(index).setText(
            f'{updated_movie[0][1]}\n{updated_movie[0][2]}\n★ {updated_movie[0][-3]}')
        print(self._movie_all[index])
        print(updated_movie)
        # self._movie_all[index] = updated_movie
        self.ui.ratingscount_moviedetails.setText(
            f'{updated_movie[0][-3]} based on {updated_movie[0][-1]} reviews')

    def delete_review(self, widget):
        self._confirmation = QMessageBox()
        self._confirmation.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self._confirmation.setWindowIcon(self._app_icon)
        question = self._confirmation.question(self, 'Movie Ratings', 'Are you sure you want to delete your review?',
                                               self._confirmation.Yes | self._confirmation.No)

        if question == self._confirmation.Yes:
            user_id = 1  # _database.getCurrentUser()[0][0]
            movie_id = self._movie_all[self.ui.movielist_movielist.currentRow()][0]
            self.del_review.emit(user_id, movie_id, widget)
        else:
            pass

    @Slot(bool, list, object)
    def delete_success(self, succeeded: bool, updated_movie: list, widget: object):
        if succeeded:
            self.show_message_box("Success! Review has been deleted.")
            self.ui.movielist_movielist.currentItem().setText(
                f'{updated_movie[1]}\n{updated_movie[2]}\n★ {updated_movie[-3]}')
            self._movie_all[self.ui.movielist_movielist.currentRow()] = updated_movie
            self.ui.ratingscount_moviedetails.setText(
                f'{updated_movie[-3]} based on {self._movie_all[self.ui.movielist_movielist.currentRow()][-1]} reviews')
            self.set_widget(widget)
        else:
            self.show_message_box(
                "Something unexpected happened. Please try again later or relaunch the application")

    def back(self):
        widget = int(self._visited.pop())
        self.ui.body.setCurrentIndex(widget)
        self.ui.scrollArea.verticalScrollBar().setValue(0)

    def set_widget(self, widget, condition='normal'):
        widget_name = str(widget)[str(widget).find('"'):str(widget).rfind(')')].replace('"', '')
        print(widget_name)

        if widget_name == 'moviedetail':
            self.get_reviews()
            self._movie = self.ui.movielist_movielist.currentItem().text()
            self._movie = self._movie.split('\n')
            print(self._movie)
            self.ui.movietitle_moviedetails.setText(self._movie[0])
            self.ui.ratingscount_moviedetails.setText(
                f'{self._movie[-1][2:]} based on {self._movie_all[self.ui.movielist_movielist.currentRow()][-1]} reviews')
            self.ui.synopsis_moviedetails.setText(self._movie_all[self.ui.movielist_movielist.currentRow()][
                                                      -4])
            self._visited.append(self.ui.body.currentIndex())
            self.movie_cover(self._movie[0])
            self.ui.body.setCurrentWidget(widget)

        elif widget_name == 'movielist' or widget_name == 'login':
            self._visited.clear()
            self.ui.body.setCurrentWidget(widget)

        elif widget_name == 'reviewmovie' and condition == 'new':
            self.ui.updatereviewframe_reviewnow.hide()
            self.ui.updatereviewframe_myrev_reviewnow.hide()
            self.ui.submitreviewframe_reviewnow.show()
            self._visited.append(self.ui.body.currentIndex())
            self.ui.reviewdesc_textbox_reviewnow.setText('')
            self.ui.moviename_reviewnow.setText(self._movie_all[self.ui.movielist_movielist.currentRow()][1])
            self.ui.body.setCurrentWidget(widget)
            self.star_button_clicked()

        elif widget_name == 'reviewmovie' and condition == 'edit':
            self.ui.updatereviewframe_reviewnow.show()
            self.ui.updatereviewframe_myrev_reviewnow.hide()
            self.ui.submitreviewframe_reviewnow.hide()
            self._visited.append(self.ui.body.currentIndex())
            self.ui.reviewdesc_textbox_reviewnow.setText(self.ui.myreviewdesc_moviedetails.text())
            self.star_button_clicked(int(self.ui.myrating_moviedetails.text()[-2:]))
            self.ui.moviename_reviewnow.setText(self._movie_all[self.ui.movielist_movielist.currentRow()][1])
            self.ui.body.setCurrentWidget(widget)

        elif widget_name == 'reviewmovie' and condition == 'my':
            review_details = self.ui.reviewslist_myreviews.currentItem().text().split('\n')
            self.ui.updatereviewframe_reviewnow.hide()
            self.ui.updatereviewframe_myrev_reviewnow.show()
            self.ui.submitreviewframe_reviewnow.hide()
            self._visited.append(self.ui.body.currentIndex())
            self.ui.reviewdesc_textbox_reviewnow.setText(review_details[3])
            self.star_button_clicked(int(review_details[1][-2:]))
            self.ui.moviename_reviewnow.setText(review_details[0])
            self.ui.body.setCurrentWidget(widget)

        elif widget_name == 'myreviews':
            self._visited.append(self.ui.body.currentIndex())
            self.my_reviews()
            self.ui.body.setCurrentWidget(widget)

        elif widget_name == 'allreviews':
            self._visited.append(self.ui.body.currentIndex())
            self.get_reviews()
            self.ui.moviename_allreviews.setText(self._movie_all[self.ui.movielist_movielist.currentRow()][1])
            self.ui.body.setCurrentWidget(widget)

        else:
            self._visited.append(self.ui.body.currentIndex())
            self.ui.body.setCurrentWidget(widget)

        self.ui.scrollArea.verticalScrollBar().setValue(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Wolf - Movie Ratings")
    sys.exit(app.exec_())
