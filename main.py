import ctypes
import sys
import re
import platform
import time
import datetime
from datetime import date

import PyQt5
from PyQt5.QtWidgets import qApp
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent, QTimer, QSortFilterProxyModel)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QPainterPath)
from PySide2.QtWidgets import *
from gui import Ui_MainWindow
import cv2
import urllib.request
import database

myappid = u'wolf.wolf.movie_ratings.1.0.0'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class MainWindow(QMainWindow):
    # initial constructor
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.reviewslist_moviedetails.setWordWrap(True)
        self.ui.reviewslist_myreviews.setWordWrap(True)
        self._visited = []
        self._regex_email = r'[a-zA-Z0-9]+([._][a-zA-Z0-9]+)*@([a-z0-9|A-Z0-9]+\.)+[a-z0-9|A-Z0-9]{2,}$'
        self._regex_password = '(?=.*[a-zA-Z])(?=.*[0-9!#$%&()*+,.;<=>?@\[\]^_{}~])[a-zA-Z0-9!#$%&()*+,.;<=>?@\[\]^_{}~]{8,}'
        self._movie_all = []
        self._review_all = []
        self._user_all = []
        self._star_button = [self.ui.starbutton_1, self.ui.starbutton_2, self.ui.starbutton_3, self.ui.starbutton_4,
                             self.ui.starbutton_5, self.ui.starbutton_6, self.ui.starbutton_7, self.ui.starbutton_8,
                             self.ui.starbutton_9, self.ui.starbutton_10]
        self._rating_phrases = ['Absolute trash, not even worth a penny', 'Trash', 'Trash, but still tolerable',
                                'This movie is a joke', 'Still watchable', 'Meh', 'Ok', 'Good', 'Amazing',
                                'Masterpiece']
        self._previous_search = ''
        self._movie = None
        self._movie_synopsis = []
        self._movie_prohibited_char = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
        self._database = database.DatabaseFilm()

        def show_message_box(message: str):
            self._info = QMessageBox()
            self._info.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
            self._info.setWindowTitle("Movie Ratings")
            self._info.setWindowIcon(QtGui.QIcon('data/img/icon.ico'))
            self._info.setText(message)
            return self._info.show()

        def refresh():
            self._database = database.DatabaseFilm()

        def refreshList(search=''):
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

        def all_movies():
            self.ui.movielist_movielist.clear()
            self._movie_synopsis.clear()
            self._movie_all.clear()
            for item in self._database.getAllMovie(str(self.ui.sortmovie_movielist.currentText())):
                movie_name = item[1].replace(' ', '_')
                for i in self._movie_prohibited_char:
                    if i in movie_name:
                        movie_name = movie_name.replace(i, '_')
                try:
                    open(f'data/img/poster/{movie_name}.jpg')
                except FileNotFoundError:
                    urllib.request.urlretrieve(item[-2], f'data/img/poster/{movie_name}.jpg')
                movie_cover(movie_name)
                self.ui.movielist_movielist.addItem(
                    QListWidgetItem(QIcon(f'data/img/poster/{movie_name}.jpg'), f'{item[1]}\n{item[2]}\n★ {item[-3]}'))
                self._movie_synopsis.append(item[-4])
                self._movie_all.append(item)

        def movie_cover(movie_name: str):
            if ' ' in movie_name:
                movie_name = movie_name.replace(' ', '_')
                for i in self._movie_prohibited_char:
                    if i in movie_name:
                        movie_name = movie_name.replace(i, '_')

            try:
                open(f'data/img/poster/{movie_name}.jpg')
            except FileNotFoundError:
                urllib.request.urlretrieve(self._movie_all[self.ui.movielist_movielist.currentRow()][-1],
                                           f'data/img/poster/{movie_name}.jpg')
                movie_cover(movie_name)

            picname = f'data/img/poster/{movie_name}.jpg'
            image = cv2.imread(picname)

            width = 161
            height = 236
            dimension = (width, height)

            resized_img = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)

            cv2.imwrite(f'{picname}', resized_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            self.ui.movieposter_moviedetails.setPixmap(picname)

        def star_button_clicked(star=-1):
            for i in range(len(self._star_button)):
                self._star_button[i].setIcon(QtGui.QIcon('data/img/star_default_small.png'))
            self.ui.expressionstar_reviewnow.setText('')
            if star != -1:
                for j in range(star):
                    if j <= star:
                        self._star_button[j].setIcon(QtGui.QIcon('data/img/star_filled_small.png'))
                    else:
                        self._star_button[j].setIcon(QtGui.QIcon('data/img/star_default_small.png'))
                    self.ui.expressionstar_reviewnow.setText(self._rating_phrases[star - 1])

        def get_reviews(index=5):
            self.ui.reviewslist_moviedetails.clear()
            self.ui.alluserreviewslist_allreviews.clear()
            try:
                reviews = self._database.getReview(self._movie_all[self.ui.movielist_movielist.currentRow()][0])
                userIDs = []
                for count, review in enumerate(reviews):
                    userIDs.append(review[2])
                    self.ui.alluserreviewslist_allreviews.addItem(
                        QListWidgetItem(QIcon('data/img/login_border_small.png'),
                                        f'{self._database.getUser(review[2])[0][0]}'
                                        f'\n★ {review[-1]}'
                                        f'\n{review[-2]}'
                                        f'\n__________________________________________________________________________________________'))
                    if count <= index:
                        self.ui.reviewslist_moviedetails.addItem(
                            QListWidgetItem(QIcon('data/img/login_border_small.png'),
                                            f'{self._database.getUser(review[2])[0][0]}'
                                            f'\n★ {review[-1]}'
                                            f'\n{review[-2]}'
                                            f'\n__________________________________________________________________________________________'))

                print(reviews)
                print(self._database.getCurrentUser())
                if self._database.getCurrentUser()[0][0] in userIDs:
                    self.ui.writereviewframe_moviedetails.hide()
                    self.ui.myreviewframe_moviedetails.show()
                    self.ui.myrating_moviedetails.setText(
                        f"My Review - ★ {self._database.getIndividualReview(self._database.getCurrentUser()[0][0])[-1][-1]}")
                    self.ui.myreviewdesc_moviedetails.setText(
                        self._database.getIndividualReview(self._database.getCurrentUser()[0][0])[-1][-2])

                    self.ui.writereviewframe_allreviews.hide()
                    self.ui.myrewiewframe_allreviews.show()
                    self.ui.myrating_allreviews.setText(
                        f"My Review - ★ {self._database.getIndividualReview(self._database.getCurrentUser()[0][0])[-1][-1]}")
                    self.ui.myreviewdesc_allreviews.setText(
                        self._database.getIndividualReview(self._database.getCurrentUser()[0][0])[-1][-2])
                else:
                    self.ui.writereviewframe_moviedetails.show()
                    self.ui.myreviewframe_moviedetails.hide()

                    self.ui.writereviewframe_allreviews.show()
                    self.ui.myrewiewframe_allreviews.hide()
            except:
                pass

        def setWidget(widget, condition='normal'):
            widget_name = str(widget)[str(widget).find('"'):str(widget).rfind(')')].replace('"', '')
            print(widget_name)

            if widget_name == 'moviedetail':
                self._movie = self.ui.movielist_movielist.currentItem().text()
                self._movie = self._movie.split('\n')
                print(self._movie)
                self.ui.movietitle_moviedetails.setText(self._movie[0])
                self.ui.ratingscount_moviedetails.setText(
                    f'{self._movie[-1][2:]} based on {self._movie_all[self.ui.movielist_movielist.currentRow()][-1]} reviews')
                self.ui.synopsis_moviedetails.setText(self._movie_all[self.ui.movielist_movielist.currentRow()][
                                                          -4])  # set synopsis retrieved from the database
                # self.ui.reviewslist_moviedetails.addItem() ## set 5 first reviews retrieved from the database
                self._visited.append(self.ui.body.currentIndex())
                movie_cover(self._movie[0])
                get_reviews()
                self.ui.body.setCurrentWidget(widget)

            elif widget_name == 'movielist' or widget_name == 'login':
                self._visited.clear()
                self.ui.body.setCurrentWidget(widget)

            elif widget_name == 'reviewmovie' and condition == 'new':
                self._visited.append(self.ui.body.currentIndex())
                self.ui.reviewdesc_textbox_reviewnow.setText('')
                self.ui.body.setCurrentWidget(widget)
                star_button_clicked()

            elif widget_name == 'reviewmovie' and condition == 'edit':
                self._visited.append(self.ui.body.currentIndex())
                self.ui.reviewdesc_textbox_reviewnow.setText(self.ui.myreviewdesc_moviedetails.text())
                star_button_clicked(int(self.ui.myrating_moviedetails.text()[-1]))
                self.ui.body.setCurrentWidget(widget)

            else:
                self._visited.append(self.ui.body.currentIndex())
                self.ui.body.setCurrentWidget(widget)

            self.ui.scrollArea.verticalScrollBar().setValue(0)

        def back():
            widget = int(self._visited.pop())
            self.ui.body.setCurrentIndex(widget)
            self.ui.scrollArea.verticalScrollBar().setValue(0)

        def register():
            email = self.ui.email_register.text().strip().lower()
            username = self.ui.username_register.text().strip().lower()
            fname = self.ui.firstname_register.text().strip().lower().capitalize()
            lname = self.ui.lastname_register.text().strip().lower().capitalize()
            password = self.ui.password_register.text()
            confirm = self.ui.confirmpassword_register.text()
            email_valid = re.match(self._regex_email, email)
            password_valid = re.match(self._regex_password, password)

            if email == "" or username == "" or fname == "" or lname == "" or password == "" or confirm == "":
                show_message_box("Input fields must not be empty.")
            elif not email_valid:
                show_message_box("Please enter a valid email address.")
            elif len(password) < 8:
                show_message_box("Password length must be a minimum of 8 characters long.")
            elif not password_valid:
                show_message_box("Password must have a combination of minimum one letter of any kind and either digits "
                                 "or punctuations. (example: George123#)")
            elif password != confirm:
                show_message_box("Passwords do not match, please re-check your input.")
            else:
                try:
                    self._database.register(username, email, fname, lname, password)
                    show_message_box(f"Thank you for registering, {fname}! Please login to continue.")
                    self.ui.body.setCurrentWidget(self.ui.login)
                    self.ui.email_register.clear()
                    self.ui.username_register.clear()
                    self.ui.password_register.clear()
                    self.ui.confirmpassword_register.clear()
                except database.UserExistError:
                    show_message_box(
                        f"A user with email address {email} already exist. "
                        f"Please login or create an account using a different email.")
                except database.UsernameExistError:
                    show_message_box(f"Username {username} is already taken, please choose another username.")

        def login():
            useremail = self.ui.useremail_login.text().strip()
            password = self.ui.password_login.text()

            if useremail == "" or password == "":
                show_message_box("Input fields must not be empty")

            try:
                self._database.login(useremail, password)
                show_message_box("Success!")
                self.ui.firstlastname_profile.setText(
                    f'{self._database.getCurrentUser()[0][3]} {self._database.getCurrentUser()[0][4]}')
                self.ui.registeredsince_profile.setText(
                    f'{self._database.getCurrentUser()[0][-2].strftime("%d %B %Y")}')
                self.ui.emailinfo_profile.setText(f'Email: {self._database.getCurrentUser()[0][2]}')
                self.ui.usernameinfo_profile.setText(f'Username: {self._database.getCurrentUser()[0][1]}')
                self.ui.body.setCurrentWidget(self.ui.movielist)
                self.ui.useremail_login.clear()
                self.ui.password_login.clear()
            except database.InvalidCredentialsError:
                print('login failed. please check your credentails')
                show_message_box("Wrong password. Please recheck your credentials.")
            except database.NoUserFoundError:
                print('no user found. please register first')
                show_message_box("No user with such credentials found. Please make a new account first.")

        def logout():
            self._database.logout()
            show_message_box("Logged out. Please login again")
            setWidget(self.ui.login)

        # setting the app icon to show on the taskbar
        self.setWindowIcon(QtGui.QIcon('data/img/icon.ico'))

        # configuring stacked widget - register
        self.ui.registerbutton_register.clicked.connect(lambda: register())
        self.ui.loginbutton_register.clicked.connect(lambda: self.ui.body.setCurrentWidget(self.ui.login))

        # configuring stacked widget - login
        self.ui.loginbutton_login.clicked.connect(lambda: login())
        self.ui.registerbutton_login.clicked.connect(lambda: self.ui.body.setCurrentWidget(self.ui.register_2))

        # configuring stacked widget - movie list
        self.ui.profilebutton_movielist.clicked.connect(lambda: setWidget(self.ui.profile))
        self.ui.viewdetailsbutton_movielist.clicked.connect(lambda: setWidget(self.ui.moviedetail))
        self.ui.sortmovie_movielist.currentIndexChanged.connect(lambda: all_movies())
        self.ui.searchmovie_movielist.returnPressed.connect(lambda: refreshList(self.ui.searchmovie_movielist.text()))
        self.ui.searchbutton_movielist.clicked.connect(lambda: refreshList(self.ui.searchmovie_movielist.text()))

        # configuring stacked widget - movie details
        self.ui.profilebutton_moviedetails.clicked.connect(lambda: setWidget(self.ui.profile))
        self.ui.backbutton_moviedetails.clicked.connect(lambda: back())
        self.ui.writereviewbutton_moviedetails.clicked.connect(lambda: setWidget(self.ui.reviewmovie, 'new'))
        self.ui.editreviewbutton_moviedetails.clicked.connect(lambda: setWidget(self.ui.reviewmovie, 'edit'))
        # self.ui.deletereviewbutton_moviedetails.clicked.connect(lambda: delete_review()) ## create a method to delete user review
        self.ui.viewallbutton_moviedetails.clicked.connect(lambda: setWidget(self.ui.reviewlist))

        # configuring stacked widget - profile
        self.ui.backbutton_profile.clicked.connect(lambda: back())
        self.ui.homebutton_profile.clicked.connect(lambda: setWidget(self.ui.movielist))
        self.ui.logoutbutton_profile.clicked.connect(lambda: logout())
        # self.ui.deleteaccountbutton_profile.clicked.connect(lambda: deleteAccount()) ## create a method to delete user from database
        self.ui.myreviewsbutton_profile.clicked.connect(lambda: setWidget(self.ui.myreviews))
        # self.ui.confirmchangesbutton_profile.clicked.connect(lambda: changePassword()) ## create a method to change password

        # configuring stacked widget - my reviews
        self.ui.backbutton_myreviews.clicked.connect(lambda: back())

        # configuring stacked widget - review list
        self.ui.backbutton_allreviews.clicked.connect(lambda: back())
        self.ui.homebutton_allreviews.clicked.connect(lambda: setWidget(self.ui.movielist))
        self.ui.writereviewbutton_allreviews.clicked.connect(lambda: setWidget(self.ui.reviewmovie, 'new'))
        self.ui.editreviewbutton_allreviews.clicked.connect(lambda: setWidget(self.ui.reviewmovie, 'edit'))
        # self.ui.deletereviewbutton_moviedetails.clicked.connect(lambda: delete_review()) ## create a method to delete user review

        # configuring stacked widget - review movie
        # self.ui.submitreviewbutton_reviewnow.clicked.connect(lambda: publishReview()) ## create a method to store user review
        self.ui.backbutton_reviewnow.clicked.connect(lambda: back())
        self.ui.homebutton_reviewnow.clicked.connect(lambda: setWidget(self.ui.movielist))
        self.ui.starbutton_1.clicked.connect(lambda: star_button_clicked(1))
        self.ui.starbutton_2.clicked.connect(lambda: star_button_clicked(2))
        self.ui.starbutton_3.clicked.connect(lambda: star_button_clicked(3))
        self.ui.starbutton_4.clicked.connect(lambda: star_button_clicked(4))
        self.ui.starbutton_5.clicked.connect(lambda: star_button_clicked(5))
        self.ui.starbutton_6.clicked.connect(lambda: star_button_clicked(6))
        self.ui.starbutton_7.clicked.connect(lambda: star_button_clicked(7))
        self.ui.starbutton_8.clicked.connect(lambda: star_button_clicked(8))
        self.ui.starbutton_9.clicked.connect(lambda: star_button_clicked(9))
        self.ui.starbutton_10.clicked.connect(lambda: star_button_clicked(10))

        # showing the dialog box
        self.ui.body.setCurrentWidget(self.ui.movielist)

        # listing all movies and reviews
        all_movies()

        self.ui.myreviewframe_moviedetails.hide()
        # showing the main window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Wolf - Movie Ratings")
    sys.exit(app.exec_())
