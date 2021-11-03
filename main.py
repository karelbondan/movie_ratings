import ctypes
import sys
import re
import platform
import time

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
        self._info = QMessageBox()
        self._info.setWindowTitle("Movie Ratings")
        self._info.setWindowIcon(QtGui.QIcon('data/img/icon.ico'))
        self._regex_email = r'[a-zA-Z0-9]+([._][a-zA-Z0-9]+)*@([a-z0-9|A-Z0-9]+\.)+[a-z0-9|A-Z0-9]{2,}$'
        self._regex_password = '(?=.*[a-zA-Z])(?=.*[0-9!#$%&()*+,.;<=>?@\[\]^_{}~])[a-zA-Z0-9!#$%&()*+,.;<=>?@\[\]^_{}~]{8,}'
        self._movie_all = []
        self._review_all = []
        self._user_all = []
        self._previous_search = ''
        self._movie = None
        self._movie_synopsis = []
        self._movie_prohibited_char = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
        self._database = database.DatabaseFilm()

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
            for item in self._database.getMovie(str(self.ui.sortmovie_movielist.currentText())):
                movie_name = item[1].replace(' ', '_')
                for i in self._movie_prohibited_char:
                    if i in movie_name:
                        movie_name = movie_name.replace(i, '_')
                try:
                    open(f'data/img/poster/{movie_name}.jpg')
                except FileNotFoundError:
                    urllib.request.urlretrieve(item[-1], f'data/img/poster/{movie_name}.jpg')
                movie_cover(movie_name)
                self.ui.movielist_movielist.addItem(
                    QListWidgetItem(QIcon(f'data/img/poster/{movie_name}.jpg'), f'{item[1]}\n★{item[-2]}'))
                self._movie_synopsis.append(item[-3])
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

        def setWidget(widget):
            widget_name = str(widget)[str(widget).find('"'):str(widget).rfind(')')].replace('"', '')
            print(widget_name)

            if widget_name == 'moviedetail':
                self._movie = self.ui.movielist_movielist.currentItem().text()
                self._movie = self._movie.split('\n')
                self.ui.movietitle_moviedetails.setText(self._movie[0])
                self.ui.ratingscount_moviedetails.setText(
                    f'{self._movie[1][1:]} based on NULL reviews')
                self.ui.synopsis_moviedetails.setText(self._movie_all[self.ui.movielist_movielist.currentRow()][
                                                          -3])  # set synopsis retrieved from the database
                # self.ui.reviewslist_moviedetails.addItem() ## set 5 first reviews retrieved from the database
                self._visited.append(self.ui.body.currentIndex())
                movie_cover(self._movie[0])
                self.ui.body.setCurrentWidget(widget)

            elif widget_name == 'movielist' or widget_name == 'login':
                self._visited.clear()
                self.ui.body.setCurrentWidget(widget)

            else:
                self._visited.append(self.ui.body.currentIndex())
                self.ui.body.setCurrentWidget(widget)

        def back():
            widget = int(self._visited.pop())
            self.ui.body.setCurrentIndex(widget)

        def register():
            email = self.ui.email_register.text().strip()
            password = self.ui.password_register.text()
            confirm = self.ui.confirmpassword_register.text()
            email_valid = re.match(self._regex_email, email)
            password_valid = re.match(self._regex_password, password)

            if email == "" or password == "" or confirm == "":
                self._info.setText("Fields must not be empty.")
                self._info.show()
            elif not email_valid:
                self._info.setText("Please enter a valid email address.")
                self._info.show()
            elif len(password) < 8:
                self._info.setText("Password length must be a minimum of 8 characters long.")
                self._info.show()
            elif not password_valid:
                self._info.setText(
                    "Password must have a combination of minimum one letter of any kind and either digits "
                    "or punctuations. (example: George123#)")
                self._info.show()
            elif password != confirm:
                self._info.setText("Passwords do not match, please re-check your input.")
                self._info.show()
            else:
                # do mysql command that stores the credentials to the server.
                # the info box below is only a temporary statement
                self._info.setText("Success!")
                self._info.show()
                self.ui.body.setCurrentWidget(self.ui.login)

        def login():
            email = self.ui.email_login.text().strip()
            password = self.ui.password_login.text()
            email_valid = re.match(self._regex_email, email)

            if not email_valid:
                self._info.setText("Please enter a valid email address")
                self._info.show()
            else:
                # do something with mysql syntax that logs the user in
                # the info box below is only a temporary statement
                self._info.setText("Success!")
                self._info.show()
                self.ui.body.setCurrentWidget(self.ui.movielist)

        def logout():
            # logs the user out
            # the info box below is only a temporary statement
            self._info.setText("Success!")
            self._info.show()

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

        # configuring stacked widget - profile
        self.ui.backbutton_profile.clicked.connect(lambda: back())
        self.ui.homebutton_profile.clicked.connect(lambda: setWidget(self.ui.movielist))
        self.ui.logoutbutton_profile.clicked.connect(lambda: setWidget(self.ui.login))
        # self.ui.deleteaccountbutton_profile.clicked.connect(lambda: deleteAccount()) ## create a method to delete user from database
        self.ui.myreviewsbutton_profile.clicked.connect(lambda: setWidget(self.ui.myreviews))
        # self.ui.confirmchangesbutton_profile.clicked.connect(lambda: changePassword()) ## create a method to change password

        # configuring stacked widget - my reviews
        self.ui.backbutton_myreviews.clicked.connect(lambda: back())

        # showing the dialog box
        self.ui.body.setCurrentWidget(self.ui.movielist)

        # listing all movies and reviews
        all_movies()

        # showing the main window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Wolf - Movie Ratings")
    sys.exit(app.exec_())
