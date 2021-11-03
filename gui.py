# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_designKTzzVw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 702)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(221, 221, 221, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: 0px;\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 777, 682))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.body = QStackedWidget(self.scrollAreaWidgetContents)
        self.body.setObjectName(u"body")
        self.body.setMinimumSize(QSize(650, 0))
        self.register_2 = QWidget()
        self.register_2.setObjectName(u"register_2")
        self.verticalLayout_16 = QVBoxLayout(self.register_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_37 = QFrame(self.register_2)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(0, 81))
        self.frame_37.setMaximumSize(QSize(16777215, 81))
        self.frame_37.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_37)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(9, 9, 9, 2)
        self.frame_40 = QFrame(self.frame_37)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(50, 50))
        self.frame_41.setMaximumSize(QSize(50, 50))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_24.addWidget(self.frame_41)

        self.label_16 = QLabel(self.frame_40)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: 25pt \"Century Gothic\";\n"
"font: 63 34pt \"Bahnschrift SemiBold\";\n"
"font: 26pt \"Bahnschrift SemiCondensed\";")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_16)

        self.frame_42 = QFrame(self.frame_40)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(50, 50))
        self.frame_42.setMaximumSize(QSize(50, 50))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_24.addWidget(self.frame_42)


        self.verticalLayout_13.addWidget(self.frame_40)

        self.frame_43 = QFrame(self.frame_37)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMaximumSize(QSize(16777215, 1))
        self.frame_44.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_25.addWidget(self.frame_44)


        self.verticalLayout_13.addWidget(self.frame_43)


        self.verticalLayout_16.addWidget(self.frame_37)

        self.frame_45 = QFrame(self.register_2)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 0))
        self.frame_45.setMaximumSize(QSize(16777215, 16777215))
        self.frame_45.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_45)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_46 = QFrame(self.frame_45)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_46)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_17 = QLabel(self.frame_47)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(180, 180))
        self.label_17.setMaximumSize(QSize(180, 180))
        self.label_17.setPixmap(QPixmap(u"data/img/register_border.png"))

        self.horizontalLayout_19.addWidget(self.label_17)


        self.verticalLayout_17.addWidget(self.frame_47)

        self.frame_54 = QFrame(self.frame_46)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMaximumSize(QSize(16777215, 16777215))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_54)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_48 = QFrame(self.frame_54)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_26.addWidget(self.frame_49)

        self.label_18 = QLabel(self.frame_48)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(150, 0))
        self.label_18.setMaximumSize(QSize(150, 16777215))
        self.label_18.setStyleSheet(u"font: 14pt \"Bahnschrift SemiCondensed\";")

        self.horizontalLayout_26.addWidget(self.label_18)

        self.email_register = QLineEdit(self.frame_48)
        self.email_register.setObjectName(u"email_register")
        self.email_register.setMinimumSize(QSize(0, 30))
        self.email_register.setMaximumSize(QSize(410, 16777215))
        self.email_register.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);\n"
"font: 11pt \"Century Gothic\";")

        self.horizontalLayout_26.addWidget(self.email_register)

        self.frame_50 = QFrame(self.frame_48)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_26.addWidget(self.frame_50)


        self.verticalLayout_8.addWidget(self.frame_48)

        self.frame_55 = QFrame(self.frame_54)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.frame_56 = QFrame(self.frame_55)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_27.addWidget(self.frame_56)

        self.label_19 = QLabel(self.frame_55)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(150, 0))
        self.label_19.setMaximumSize(QSize(150, 16777215))
        self.label_19.setStyleSheet(u"font: 14pt \"Bahnschrift SemiCondensed\";")

        self.horizontalLayout_27.addWidget(self.label_19)

        self.password_register = QLineEdit(self.frame_55)
        self.password_register.setObjectName(u"password_register")
        self.password_register.setMinimumSize(QSize(0, 30))
        self.password_register.setMaximumSize(QSize(410, 16777215))
        self.password_register.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);\n"
"font: 11pt \"Century Gothic\";")
        self.password_register.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_27.addWidget(self.password_register)

        self.frame_57 = QFrame(self.frame_55)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_27.addWidget(self.frame_57)


        self.verticalLayout_8.addWidget(self.frame_55)

        self.frame_58 = QFrame(self.frame_54)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.frame_63 = QFrame(self.frame_58)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_30.addWidget(self.frame_63)

        self.label_22 = QLabel(self.frame_58)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(150, 0))
        self.label_22.setMaximumSize(QSize(150, 16777215))
        self.label_22.setStyleSheet(u"font: 14pt \"Bahnschrift SemiCondensed\";")

        self.horizontalLayout_30.addWidget(self.label_22)

        self.confirmpassword_register = QLineEdit(self.frame_58)
        self.confirmpassword_register.setObjectName(u"confirmpassword_register")
        self.confirmpassword_register.setMinimumSize(QSize(0, 30))
        self.confirmpassword_register.setMaximumSize(QSize(410, 16777215))
        self.confirmpassword_register.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);\n"
"font: 11pt \"Century Gothic\";")
        self.confirmpassword_register.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_30.addWidget(self.confirmpassword_register)

        self.frame_64 = QFrame(self.frame_58)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_30.addWidget(self.frame_64)


        self.verticalLayout_8.addWidget(self.frame_58)


        self.verticalLayout_17.addWidget(self.frame_54)


        self.verticalLayout_14.addWidget(self.frame_46)

        self.frame_59 = QFrame(self.frame_45)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMaximumSize(QSize(16777215, 140))
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_59)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_60 = QFrame(self.frame_59)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.registerbutton_register = QPushButton(self.frame_60)
        self.registerbutton_register.setObjectName(u"registerbutton_register")
        self.registerbutton_register.setMinimumSize(QSize(60, 60))
        self.registerbutton_register.setMaximumSize(QSize(351, 16777215))
        self.registerbutton_register.setStyleSheet(u"QPushButton {	\n"
"	border-radius: 30px;\n"
"	background-color: rgba(102, 97, 234, 70);\n"
"	color: rgb(0,0,0);\n"
"	font: 18pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(72, 67, 181, 80);\n"
"	color: rgb(255,255,255);\n"
"	font: 18pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(72, 67, 181, 130);\n"
"	color: rgb(240,240,240);\n"
"	font: 18pt \"Bahnschrift SemiCondensed\";\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../../Gonpachiro/images/icons/home icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.registerbutton_register.setIcon(icon)
        self.registerbutton_register.setIconSize(QSize(40, 40))

        self.horizontalLayout_28.addWidget(self.registerbutton_register)


        self.verticalLayout_15.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.frame_59)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMaximumSize(QSize(16777215, 38))
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.frame_62 = QFrame(self.frame_61)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMaximumSize(QSize(120, 16777215))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_29.addWidget(self.frame_62)

        self.label_20 = QLabel(self.frame_61)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(220, 0))
        self.label_20.setMaximumSize(QSize(16777215, 20))
        self.label_20.setStyleSheet(u"font: 11pt \"Century Gothic\";")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.label_20)

        self.loginbutton_register = QPushButton(self.frame_61)
        self.loginbutton_register.setObjectName(u"loginbutton_register")
        self.loginbutton_register.setMaximumSize(QSize(16777215, 16777215))
        self.loginbutton_register.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginbutton_register.setStyleSheet(u"font: 12pt \"Bahnschrift SemiCondensed\";\n"
"text-align: left;")

        self.horizontalLayout_29.addWidget(self.loginbutton_register)


        self.verticalLayout_15.addWidget(self.frame_61)


        self.verticalLayout_14.addWidget(self.frame_59)


        self.verticalLayout_16.addWidget(self.frame_45)

        self.frame_65 = QFrame(self.register_2)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.frame_65)

        self.body.addWidget(self.register_2)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.verticalLayout_10 = QVBoxLayout(self.login)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_21 = QFrame(self.login)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 81))
        self.frame_21.setMaximumSize(QSize(16777215, 81))
        self.frame_21.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_21)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(9, 9, 9, 2)
        self.frame_28 = QFrame(self.frame_21)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_28)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(50, 50))
        self.frame_31.setMaximumSize(QSize(50, 50))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frame_31)

        self.label_14 = QLabel(self.frame_28)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 25pt \"Century Gothic\";\n"
"font: 63 34pt \"Bahnschrift SemiBold\";\n"
"font: 26pt \"Bahnschrift SemiCondensed\";")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_14)

        self.frame_32 = QFrame(self.frame_28)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(50, 50))
        self.frame_32.setMaximumSize(QSize(50, 50))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frame_32)


        self.verticalLayout_9.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_21)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(16777215, 1))
        self.frame_30.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_21.addWidget(self.frame_30)


        self.verticalLayout_9.addWidget(self.frame_29)


        self.verticalLayout_10.addWidget(self.frame_21)

        self.frame_33 = QFrame(self.login)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 0))
        self.frame_33.setMaximumSize(QSize(16777215, 16777215))
        self.frame_33.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_33)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_38 = QFrame(self.frame_33)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_38)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_24 = QFrame(self.frame_38)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.frame_24)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(180, 180))
        self.label_13.setMaximumSize(QSize(180, 180))
        self.label_13.setPixmap(QPixmap(u"data/img/login_border.png"))

        self.horizontalLayout_18.addWidget(self.label_13)


        self.verticalLayout_7.addWidget(self.frame_24)

        self.frame_53 = QFrame(self.frame_38)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_53)

        self.frame_22 = QFrame(self.frame_38)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_27 = QFrame(self.frame_22)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frame_27)

        self.label = QLabel(self.frame_22)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))
        self.label.setMaximumSize(QSize(150, 16777215))
        self.label.setStyleSheet(u"font: 14pt \"Bahnschrift\";")

        self.horizontalLayout_17.addWidget(self.label)

        self.email_login = QLineEdit(self.frame_22)
        self.email_login.setObjectName(u"email_login")
        self.email_login.setMinimumSize(QSize(0, 30))
        self.email_login.setMaximumSize(QSize(410, 16777215))
        self.email_login.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);\n"
"font: 11pt \"Century Gothic\";")

        self.horizontalLayout_17.addWidget(self.email_login)

        self.frame_26 = QFrame(self.frame_22)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frame_26)


        self.verticalLayout_7.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_38)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_51 = QFrame(self.frame_23)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_51)

        self.label_12 = QLabel(self.frame_23)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(150, 0))
        self.label_12.setMaximumSize(QSize(150, 16777215))
        self.label_12.setStyleSheet(u"font: 14pt \"Bahnschrift SemiCondensed\";")

        self.horizontalLayout_16.addWidget(self.label_12)

        self.password_login = QLineEdit(self.frame_23)
        self.password_login.setObjectName(u"password_login")
        self.password_login.setMinimumSize(QSize(0, 30))
        self.password_login.setMaximumSize(QSize(410, 16777215))
        self.password_login.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);\n"
"font: 11pt \"Century Gothic\";")
        self.password_login.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_16.addWidget(self.password_login)

        self.frame_52 = QFrame(self.frame_23)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_52)


        self.verticalLayout_7.addWidget(self.frame_23)

        self.frame_25 = QFrame(self.frame_38)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_25)


        self.verticalLayout_12.addWidget(self.frame_38)

        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(16777215, 140))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_34)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_39 = QFrame(self.frame_34)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.loginbutton_login = QPushButton(self.frame_39)
        self.loginbutton_login.setObjectName(u"loginbutton_login")
        self.loginbutton_login.setMinimumSize(QSize(60, 60))
        self.loginbutton_login.setMaximumSize(QSize(351, 16777215))
        self.loginbutton_login.setStyleSheet(u"QPushButton {	\n"
"	border-radius: 30px;\n"
"	background-color: rgba(102, 97, 234, 70);\n"
"	color: rgb(0,0,0);\n"
"	font: 18pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(72, 67, 181, 80);\n"
"	color: rgb(255,255,255);\n"
"	font: 18pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(72, 67, 181, 130);\n"
"	color: rgb(240,240,240);\n"
"	font: 18pt \"Bahnschrift SemiCondensed\";\n"
"}")
        self.loginbutton_login.setIcon(icon)
        self.loginbutton_login.setIconSize(QSize(40, 40))

        self.horizontalLayout_23.addWidget(self.loginbutton_login)


        self.verticalLayout_11.addWidget(self.frame_39)

        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(16777215, 38))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(90, 16777215))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_22.addWidget(self.frame_36)

        self.label_2 = QLabel(self.frame_35)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(220, 0))
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setStyleSheet(u"font: 11pt \"Century Gothic\";")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_2)

        self.registerbutton_login = QPushButton(self.frame_35)
        self.registerbutton_login.setObjectName(u"registerbutton_login")
        self.registerbutton_login.setStyleSheet(u"font: 12pt \"Bahnschrift SemiCondensed\";\n"
"text-align: left;")

        self.horizontalLayout_22.addWidget(self.registerbutton_login)


        self.verticalLayout_11.addWidget(self.frame_35)


        self.verticalLayout_12.addWidget(self.frame_34)

        self.frame_66 = QFrame(self.frame_33)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_66)


        self.verticalLayout_10.addWidget(self.frame_33)

        self.body.addWidget(self.login)
        self.movielist = QWidget()
        self.movielist.setObjectName(u"movielist")
        self.verticalLayout = QVBoxLayout(self.movielist)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.frame_8 = QFrame(self.movielist)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 81))
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 9, 9, 2)
        self.frame_16 = QFrame(self.frame_8)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_16)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 25pt \"Century Gothic\";\n"
"font: 63 34pt \"Bahnschrift SemiBold\";\n"
"font: 26pt \"Bahnschrift SemiCondensed\";")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_10)

        self.profilebutton_movielist = QPushButton(self.frame_16)
        self.profilebutton_movielist.setObjectName(u"profilebutton_movielist")
        self.profilebutton_movielist.setMinimumSize(QSize(50, 50))
        self.profilebutton_movielist.setMaximumSize(QSize(50, 50))
        self.profilebutton_movielist.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"data/img/login_border.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profilebutton_movielist.setIcon(icon1)
        self.profilebutton_movielist.setIconSize(QSize(40, 40))

        self.horizontalLayout_13.addWidget(self.profilebutton_movielist)


        self.verticalLayout_6.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_8)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 1))
        self.frame_18.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.frame_18)


        self.verticalLayout_6.addWidget(self.frame_17)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.movielist)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(61, 31))
        self.label_3.setStyleSheet(u"font: 13pt \"Bahnschrift SemiCondensed\";")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.sortmovie_movielist = QComboBox(self.frame_9)
        self.sortmovie_movielist.addItem("")
        self.sortmovie_movielist.addItem("")
        self.sortmovie_movielist.addItem("")
        self.sortmovie_movielist.setObjectName(u"sortmovie_movielist")
        self.sortmovie_movielist.setMaximumSize(QSize(171, 31))
        self.sortmovie_movielist.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);\n"
"font: 12pt \"Century Gothic\";")

        self.horizontalLayout_5.addWidget(self.sortmovie_movielist)

        self.frame_19 = QFrame(self.frame_9)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_19)

        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(61, 31))
        self.label_11.setStyleSheet(u"font: 13pt \"Bahnschrift SemiCondensed\";")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.searchmovie_movielist = QLineEdit(self.frame_9)
        self.searchmovie_movielist.setObjectName(u"searchmovie_movielist")
        self.searchmovie_movielist.setMaximumSize(QSize(171, 31))
        self.searchmovie_movielist.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);\n"
"font: 12pt \"Century Gothic\";")

        self.horizontalLayout_5.addWidget(self.searchmovie_movielist)

        self.searchbutton_movielist = QPushButton(self.frame_9)
        self.searchbutton_movielist.setObjectName(u"searchbutton_movielist")
        self.searchbutton_movielist.setMinimumSize(QSize(0, 30))
        self.searchbutton_movielist.setMaximumSize(QSize(30, 16777215))
        self.searchbutton_movielist.setStyleSheet(u"QPushButton {	\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {	\n"
"	background-color: rgba(72, 67, 181, 80);\n"
"	color: rgb(255,255,255);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(72, 67, 181, 130);\n"
"	color: rgb(255,255,255);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"data/img/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchbutton_movielist.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.searchbutton_movielist)


        self.verticalLayout.addWidget(self.frame_9)

        self.frame_20 = QFrame(self.movielist)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.movielist_movielist = QListWidget(self.frame_20)
        icon3 = QIcon()
        icon3.addFile(u"../../../Pictures/Projects/Draw (SAI is here)/15drazeros.jpg", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem = QListWidgetItem(self.movielist_movielist)
        __qlistwidgetitem.setIcon(icon3);
        icon4 = QIcon()
        icon4.addFile(u"../../../Pictures/Projects/Photoshop/poster.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem1 = QListWidgetItem(self.movielist_movielist)
        __qlistwidgetitem1.setIcon(icon4);
        icon5 = QIcon()
        icon5.addFile(u"../../../Pictures/Projects/Photoshop/college/bnmc/bnmc konten edu feed/week 4_5_slide 6.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem2 = QListWidgetItem(self.movielist_movielist)
        __qlistwidgetitem2.setIcon(icon5);
        icon6 = QIcon()
        icon6.addFile(u"../../../Pictures/asasasasasa.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem3 = QListWidgetItem(self.movielist_movielist)
        __qlistwidgetitem3.setIcon(icon6);
        icon7 = QIcon()
        icon7.addFile(u"../../../Pictures/andrias.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem4 = QListWidgetItem(self.movielist_movielist)
        __qlistwidgetitem4.setIcon(icon7);
        icon8 = QIcon()
        icon8.addFile(u"../../../Pictures/Season_2_poster.jpg", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem5 = QListWidgetItem(self.movielist_movielist)
        __qlistwidgetitem5.setIcon(icon8);
        self.movielist_movielist.setObjectName(u"movielist_movielist")
        self.movielist_movielist.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);\n"
"font: 11pt \"Century Gothic\";\n"
"icon-size: 125px;\n"
"border: 0px;")

        self.horizontalLayout_15.addWidget(self.movielist_movielist)


        self.verticalLayout.addWidget(self.frame_20)

        self.frame_7 = QFrame(self.movielist)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.viewdetailsbutton_movielist = QPushButton(self.frame_7)
        self.viewdetailsbutton_movielist.setObjectName(u"viewdetailsbutton_movielist")
        self.viewdetailsbutton_movielist.setMinimumSize(QSize(0, 40))
        self.viewdetailsbutton_movielist.setMaximumSize(QSize(120, 40))
        self.viewdetailsbutton_movielist.setStyleSheet(u"QPushButton {	\n"
"	border-radius: 20px;\n"
"	background-color: rgba(102, 97, 234, 70);\n"
"	color: rgb(0,0,0);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(72, 67, 181, 80);\n"
"	color: rgb(255,255,255);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(72, 67, 181, 130);\n"
"	color: rgb(255,255,255);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.viewdetailsbutton_movielist)


        self.verticalLayout.addWidget(self.frame_7)

        self.body.addWidget(self.movielist)
        self.moviedetail = QWidget()
        self.moviedetail.setObjectName(u"moviedetail")
        self.verticalLayout_4 = QVBoxLayout(self.moviedetail)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.frame_3 = QFrame(self.moviedetail)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 81))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 2)
        self.frame_13 = QFrame(self.frame_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.backbutton_moviedetails = QPushButton(self.frame_13)
        self.backbutton_moviedetails.setObjectName(u"backbutton_moviedetails")
        self.backbutton_moviedetails.setMinimumSize(QSize(50, 50))
        self.backbutton_moviedetails.setMaximumSize(QSize(50, 50))
        self.backbutton_moviedetails.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_11.addWidget(self.backbutton_moviedetails)

        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 25pt \"Century Gothic\";\n"
"font: 63 34pt \"Bahnschrift SemiBold\";\n"
"font: 26pt \"Bahnschrift SemiCondensed\";")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_4)

        self.profilebutton_moviedetails = QPushButton(self.frame_13)
        self.profilebutton_moviedetails.setObjectName(u"profilebutton_moviedetails")
        self.profilebutton_moviedetails.setMinimumSize(QSize(50, 50))
        self.profilebutton_moviedetails.setMaximumSize(QSize(50, 50))
        self.profilebutton_moviedetails.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"")
        self.profilebutton_moviedetails.setIcon(icon1)
        self.profilebutton_moviedetails.setIconSize(QSize(40, 40))

        self.horizontalLayout_11.addWidget(self.profilebutton_moviedetails)


        self.verticalLayout_5.addWidget(self.frame_13)

        self.frame_15 = QFrame(self.frame_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_15)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 1))
        self.frame_14.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.frame_14)


        self.verticalLayout_5.addWidget(self.frame_15)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.moviedetail)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setSpacing(16)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.movieposter_moviedetails = QLabel(self.frame_2)
        self.movieposter_moviedetails.setObjectName(u"movieposter_moviedetails")
        self.movieposter_moviedetails.setMinimumSize(QSize(161, 236))
        self.movieposter_moviedetails.setMaximumSize(QSize(161, 241))
        self.movieposter_moviedetails.setStyleSheet(u"border: 1px solid rgb(0,0,0);")

        self.horizontalLayout_10.addWidget(self.movieposter_moviedetails)

        self.frame_12 = QFrame(self.frame_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_12)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_12)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.movietitle_moviedetails = QLabel(self.frame_4)
        self.movietitle_moviedetails.setObjectName(u"movietitle_moviedetails")
        self.movietitle_moviedetails.setStyleSheet(u"font: 19pt \"Century Gothic\";\n"
"font: 63 28pt \"Bahnschrift SemiBold Condensed\";")
        self.movietitle_moviedetails.setWordWrap(True)

        self.horizontalLayout_9.addWidget(self.movietitle_moviedetails)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_12)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 41))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.ratingscount_moviedetails = QLabel(self.frame_5)
        self.ratingscount_moviedetails.setObjectName(u"ratingscount_moviedetails")
        self.ratingscount_moviedetails.setMaximumSize(QSize(16777215, 41))
        self.ratingscount_moviedetails.setStyleSheet(u"font: 12pt \"Century Gothic\";\n"
"font: 25 16pt \"Bahnschrift Semilight SemiCondensed\";\n"
"font: 18pt \"Bahnschrift SemiLight SemiConde\";")

        self.horizontalLayout_7.addWidget(self.ratingscount_moviedetails)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_12)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 9, 0)
        self.synopsis_moviedetails = QLabel(self.frame_6)
        self.synopsis_moviedetails.setObjectName(u"synopsis_moviedetails")
        self.synopsis_moviedetails.setStyleSheet(u"font: 11pt \"Century Gothic\";")
        self.synopsis_moviedetails.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.synopsis_moviedetails.setWordWrap(True)

        self.horizontalLayout_8.addWidget(self.synopsis_moviedetails)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.horizontalLayout_10.addWidget(self.frame_12)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_10 = QFrame(self.moviedetail)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 31))
        self.label_9.setMaximumSize(QSize(16777215, 31))
        self.label_9.setStyleSheet(u"font: 15pt \"Century Gothic\";\n"
"font: 20pt \"Bahnschrift SemiCondensed\";")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.viewallbutton_moviedetails = QPushButton(self.frame_11)
        self.viewallbutton_moviedetails.setObjectName(u"viewallbutton_moviedetails")
        self.viewallbutton_moviedetails.setMinimumSize(QSize(75, 31))
        self.viewallbutton_moviedetails.setMaximumSize(QSize(75, 31))
        self.viewallbutton_moviedetails.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 15px;\n"
"	font: 10pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 15px;\n"
"	font: 10pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.viewallbutton_moviedetails)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.reviewslist_moviedetails = QListWidget(self.frame_10)
        QListWidgetItem(self.reviewslist_moviedetails)
        QListWidgetItem(self.reviewslist_moviedetails)
        QListWidgetItem(self.reviewslist_moviedetails)
        self.reviewslist_moviedetails.setObjectName(u"reviewslist_moviedetails")
        self.reviewslist_moviedetails.setStyleSheet(u"font: 9.5pt \"Century Gothic\";")
        self.reviewslist_moviedetails.setProperty("isWrapping", False)
        self.reviewslist_moviedetails.setSortingEnabled(False)

        self.verticalLayout_2.addWidget(self.reviewslist_moviedetails)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.body.addWidget(self.moviedetail)
        self.profile = QWidget()
        self.profile.setObjectName(u"profile")
        self.verticalLayout_24 = QVBoxLayout(self.profile)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_85 = QFrame(self.profile)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMinimumSize(QSize(0, 81))
        self.frame_85.setMaximumSize(QSize(16777215, 81))
        self.frame_85.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_85)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(9, 9, 9, 2)
        self.frame_86 = QFrame(self.frame_85)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.backbutton_profile = QPushButton(self.frame_86)
        self.backbutton_profile.setObjectName(u"backbutton_profile")
        self.backbutton_profile.setMinimumSize(QSize(50, 50))
        self.backbutton_profile.setMaximumSize(QSize(50, 50))
        self.backbutton_profile.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_37.addWidget(self.backbutton_profile)

        self.label_29 = QLabel(self.frame_86)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font: 25pt \"Century Gothic\";\n"
"font: 63 34pt \"Bahnschrift SemiBold\";\n"
"font: 26pt \"Bahnschrift SemiCondensed\";")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_29)

        self.homebutton_profile = QPushButton(self.frame_86)
        self.homebutton_profile.setObjectName(u"homebutton_profile")
        self.homebutton_profile.setMinimumSize(QSize(50, 50))
        self.homebutton_profile.setMaximumSize(QSize(50, 50))
        self.homebutton_profile.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_37.addWidget(self.homebutton_profile)


        self.verticalLayout_22.addWidget(self.frame_86)

        self.frame_89 = QFrame(self.frame_85)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_90 = QFrame(self.frame_89)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMaximumSize(QSize(16777215, 1))
        self.frame_90.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_38.addWidget(self.frame_90)


        self.verticalLayout_22.addWidget(self.frame_89)


        self.verticalLayout_24.addWidget(self.frame_85)

        self.frame_68 = QFrame(self.profile)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.frame_69 = QFrame(self.frame_68)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_69)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_74 = QFrame(self.frame_69)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_74)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_97 = QFrame(self.frame_74)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_23 = QLabel(self.frame_97)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(180, 180))
        self.label_23.setMaximumSize(QSize(180, 180))
        self.label_23.setPixmap(QPixmap(u"data/img/login_border.png"))

        self.horizontalLayout_31.addWidget(self.label_23)


        self.verticalLayout_25.addWidget(self.frame_97)

        self.firstlastname_profile = QLabel(self.frame_74)
        self.firstlastname_profile.setObjectName(u"firstlastname_profile")
        self.firstlastname_profile.setStyleSheet(u"font: 19pt \"Century Gothic\";\n"
"font: 63 28pt \"Bahnschrift SemiBold Condensed\";")
        self.firstlastname_profile.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.firstlastname_profile)

        self.frame_72 = QFrame(self.frame_74)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMaximumSize(QSize(16777215, 36))
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_31 = QLabel(self.frame_72)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 0))
        self.label_31.setMaximumSize(QSize(16777215, 16777215))
        self.label_31.setStyleSheet(u"font: 11pt \"Bahnschrift SemiCondensed\";")
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.label_31)

        self.registeredsince_profile = QLabel(self.frame_72)
        self.registeredsince_profile.setObjectName(u"registeredsince_profile")
        self.registeredsince_profile.setMinimumSize(QSize(0, 0))
        self.registeredsince_profile.setMaximumSize(QSize(16777215, 16777215))
        self.registeredsince_profile.setStyleSheet(u"font: 10pt \"Century Gothic\";")

        self.horizontalLayout_32.addWidget(self.registeredsince_profile)


        self.verticalLayout_25.addWidget(self.frame_72)

        self.frame_73 = QFrame(self.frame_74)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.frame_76 = QFrame(self.frame_73)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_33.addWidget(self.frame_76)

        self.frame_75 = QFrame(self.frame_73)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(168, 190))
        self.frame_75.setMaximumSize(QSize(16777215, 200))
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_75)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.logoutbutton_profile = QPushButton(self.frame_75)
        self.logoutbutton_profile.setObjectName(u"logoutbutton_profile")
        self.logoutbutton_profile.setMinimumSize(QSize(150, 40))
        self.logoutbutton_profile.setMaximumSize(QSize(150, 40))
        self.logoutbutton_profile.setStyleSheet(u"QPushButton {	\n"
"	border-radius: 20px;\n"
"	background-color: rgba(102, 97, 234, 70);\n"
"	color: rgb(0,0,0);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(72, 67, 181, 80);\n"
"	color: rgb(255,255,255);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(72, 67, 181, 130);\n"
"	color: rgb(255,255,255);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"")

        self.verticalLayout_18.addWidget(self.logoutbutton_profile)

        self.deleteaccountbutton_profile = QPushButton(self.frame_75)
        self.deleteaccountbutton_profile.setObjectName(u"deleteaccountbutton_profile")
        self.deleteaccountbutton_profile.setMinimumSize(QSize(150, 40))
        self.deleteaccountbutton_profile.setMaximumSize(QSize(150, 40))
        self.deleteaccountbutton_profile.setStyleSheet(u"QPushButton {	\n"
"	border-radius: 20px;\n"
"	background-color: rgba(102, 97, 234, 70);\n"
"	color: rgb(0,0,0);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(72, 67, 181, 80);\n"
"	color: rgb(255,255,255);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(72, 67, 181, 130);\n"
"	color: rgb(255,255,255);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"")

        self.verticalLayout_18.addWidget(self.deleteaccountbutton_profile)

        self.myreviewsbutton_profile = QPushButton(self.frame_75)
        self.myreviewsbutton_profile.setObjectName(u"myreviewsbutton_profile")
        self.myreviewsbutton_profile.setMinimumSize(QSize(150, 40))
        self.myreviewsbutton_profile.setMaximumSize(QSize(150, 40))
        self.myreviewsbutton_profile.setStyleSheet(u"QPushButton {	\n"
"	border-radius: 20px;\n"
"	background-color: rgba(102, 97, 234, 70);\n"
"	color: rgb(0,0,0);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(72, 67, 181, 80);\n"
"	color: rgb(255,255,255);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(72, 67, 181, 130);\n"
"	color: rgb(255,255,255);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"")

        self.verticalLayout_18.addWidget(self.myreviewsbutton_profile)


        self.horizontalLayout_33.addWidget(self.frame_75)

        self.frame_78 = QFrame(self.frame_73)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_33.addWidget(self.frame_78)

        self.frame_77 = QFrame(self.frame_73)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_33.addWidget(self.frame_77)


        self.verticalLayout_25.addWidget(self.frame_73)


        self.verticalLayout_20.addWidget(self.frame_74)


        self.horizontalLayout_40.addWidget(self.frame_69)

        self.frame_71 = QFrame(self.frame_68)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_40.addWidget(self.frame_71)

        self.frame_70 = QFrame(self.frame_68)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_70)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_80 = QFrame(self.frame_70)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_80)
        self.verticalLayout_19.setSpacing(15)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_24 = QLabel(self.frame_80)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 0))
        self.label_24.setMaximumSize(QSize(16777215, 16777215))
        self.label_24.setStyleSheet(u"font: 16pt \"Bahnschrift SemiCondensed\";")

        self.verticalLayout_19.addWidget(self.label_24)

        self.emailinfo_profile = QLabel(self.frame_80)
        self.emailinfo_profile.setObjectName(u"emailinfo_profile")
        self.emailinfo_profile.setMinimumSize(QSize(0, 0))
        self.emailinfo_profile.setMaximumSize(QSize(16777215, 16777215))
        self.emailinfo_profile.setStyleSheet(u"font: 12pt \"Century Gothic\";")

        self.verticalLayout_19.addWidget(self.emailinfo_profile)

        self.emailinfo_profile_2 = QLabel(self.frame_80)
        self.emailinfo_profile_2.setObjectName(u"emailinfo_profile_2")
        self.emailinfo_profile_2.setMinimumSize(QSize(0, 0))
        self.emailinfo_profile_2.setMaximumSize(QSize(16777215, 16777215))
        self.emailinfo_profile_2.setStyleSheet(u"font: 12pt \"Century Gothic\";")

        self.verticalLayout_19.addWidget(self.emailinfo_profile_2)


        self.verticalLayout_23.addWidget(self.frame_80)

        self.frame_93 = QFrame(self.frame_70)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMaximumSize(QSize(16777215, 30))
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)

        self.verticalLayout_23.addWidget(self.frame_93)

        self.frame_81 = QFrame(self.frame_70)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_33 = QLabel(self.frame_81)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 0))
        self.label_33.setMaximumSize(QSize(16777215, 16777215))
        self.label_33.setStyleSheet(u"font: 16pt \"Bahnschrift SemiCondensed\";")

        self.horizontalLayout_39.addWidget(self.label_33)


        self.verticalLayout_23.addWidget(self.frame_81)

        self.frame_82 = QFrame(self.frame_70)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_35 = QLabel(self.frame_82)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(150, 0))
        self.label_35.setMaximumSize(QSize(150, 16777215))
        self.label_35.setStyleSheet(u"font: 12pt \"Century Gothic\";")

        self.horizontalLayout_36.addWidget(self.label_35)

        self.password_profile = QLineEdit(self.frame_82)
        self.password_profile.setObjectName(u"password_profile")
        self.password_profile.setMinimumSize(QSize(0, 30))
        self.password_profile.setMaximumSize(QSize(410, 16777215))
        self.password_profile.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);\n"
"font: 11pt \"Century Gothic\";")

        self.horizontalLayout_36.addWidget(self.password_profile)

        self.frame_87 = QFrame(self.frame_82)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMaximumSize(QSize(16777215, 16777215))
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_36.addWidget(self.frame_87)


        self.verticalLayout_23.addWidget(self.frame_82)

        self.frame_91 = QFrame(self.frame_70)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_34 = QLabel(self.frame_91)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(150, 0))
        self.label_34.setMaximumSize(QSize(150, 16777215))
        self.label_34.setStyleSheet(u"font: 12pt \"Century Gothic\";")

        self.horizontalLayout_35.addWidget(self.label_34)

        self.newpassword_profile = QLineEdit(self.frame_91)
        self.newpassword_profile.setObjectName(u"newpassword_profile")
        self.newpassword_profile.setMinimumSize(QSize(0, 30))
        self.newpassword_profile.setMaximumSize(QSize(410, 16777215))
        self.newpassword_profile.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);\n"
"font: 11pt \"Century Gothic\";")

        self.horizontalLayout_35.addWidget(self.newpassword_profile)

        self.frame_88 = QFrame(self.frame_91)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_35.addWidget(self.frame_88)


        self.verticalLayout_23.addWidget(self.frame_91)

        self.frame_121 = QFrame(self.frame_70)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_121)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_43 = QLabel(self.frame_121)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(150, 0))
        self.label_43.setMaximumSize(QSize(150, 16777215))
        self.label_43.setStyleSheet(u"font: 12pt \"Century Gothic\";")

        self.horizontalLayout_54.addWidget(self.label_43)

        self.confirmnewpassword_profile = QLineEdit(self.frame_121)
        self.confirmnewpassword_profile.setObjectName(u"confirmnewpassword_profile")
        self.confirmnewpassword_profile.setMinimumSize(QSize(0, 30))
        self.confirmnewpassword_profile.setMaximumSize(QSize(410, 16777215))
        self.confirmnewpassword_profile.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);\n"
"font: 11pt \"Century Gothic\";")

        self.horizontalLayout_54.addWidget(self.confirmnewpassword_profile)

        self.frame_95 = QFrame(self.frame_121)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_54.addWidget(self.frame_95)


        self.verticalLayout_23.addWidget(self.frame_121)

        self.frame_83 = QFrame(self.frame_70)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.confirmchangesbutton_profile = QPushButton(self.frame_83)
        self.confirmchangesbutton_profile.setObjectName(u"confirmchangesbutton_profile")
        self.confirmchangesbutton_profile.setMinimumSize(QSize(150, 40))
        self.confirmchangesbutton_profile.setMaximumSize(QSize(150, 40))
        self.confirmchangesbutton_profile.setStyleSheet(u"QPushButton {	\n"
"	border-radius: 20px;\n"
"	background-color: rgba(102, 97, 234, 70);\n"
"	color: rgb(0,0,0);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(72, 67, 181, 80);\n"
"	color: rgb(255,255,255);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(72, 67, 181, 130);\n"
"	color: rgb(255,255,255);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"")

        self.horizontalLayout_34.addWidget(self.confirmchangesbutton_profile)

        self.frame_96 = QFrame(self.frame_83)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_34.addWidget(self.frame_96)


        self.verticalLayout_23.addWidget(self.frame_83)

        self.frame_92 = QFrame(self.frame_70)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(0, 120))
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)

        self.verticalLayout_23.addWidget(self.frame_92)


        self.horizontalLayout_40.addWidget(self.frame_70)


        self.verticalLayout_24.addWidget(self.frame_68)

        self.frame_84 = QFrame(self.profile)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)

        self.verticalLayout_24.addWidget(self.frame_84)

        self.body.addWidget(self.profile)
        self.myreviews = QWidget()
        self.myreviews.setObjectName(u"myreviews")
        self.verticalLayout_32 = QVBoxLayout(self.myreviews)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_67 = QFrame(self.myreviews)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(0, 81))
        self.frame_67.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_67)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(9, 9, 9, 2)
        self.frame_94 = QFrame(self.frame_67)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_94)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.backbutton_myreviews = QPushButton(self.frame_94)
        self.backbutton_myreviews.setObjectName(u"backbutton_myreviews")
        self.backbutton_myreviews.setMinimumSize(QSize(50, 50))
        self.backbutton_myreviews.setMaximumSize(QSize(50, 50))
        self.backbutton_myreviews.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_48.addWidget(self.backbutton_myreviews)

        self.label_27 = QLabel(self.frame_94)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: 25pt \"Century Gothic\";\n"
"font: 63 34pt \"Bahnschrift SemiBold\";\n"
"font: 26pt \"Bahnschrift SemiCondensed\";")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.label_27)

        self.homebutton_myreviews = QPushButton(self.frame_94)
        self.homebutton_myreviews.setObjectName(u"homebutton_myreviews")
        self.homebutton_myreviews.setMinimumSize(QSize(50, 50))
        self.homebutton_myreviews.setMaximumSize(QSize(50, 50))
        self.homebutton_myreviews.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_48.addWidget(self.homebutton_myreviews)


        self.verticalLayout_31.addWidget(self.frame_94)

        self.frame_113 = QFrame(self.frame_67)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_113)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_119 = QFrame(self.frame_113)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setMaximumSize(QSize(16777215, 1))
        self.frame_119.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_52.addWidget(self.frame_119)


        self.verticalLayout_31.addWidget(self.frame_113)


        self.verticalLayout_32.addWidget(self.frame_67)

        self.frame_120 = QFrame(self.myreviews)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_120)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.reviewslist_myreviews = QListWidget(self.frame_120)
        icon9 = QIcon()
        icon9.addFile(u"C:/Users/karel/Pictures/the-truth-about-king-comes-out-in-this-weeks-episode-of-the-owl-house.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem6 = QListWidgetItem(self.reviewslist_myreviews)
        __qlistwidgetitem6.setIcon(icon9);
        self.reviewslist_myreviews.setObjectName(u"reviewslist_myreviews")
        self.reviewslist_myreviews.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);\n"
"font: 11pt \"Century Gothic\";\n"
"icon-size: 125px;\n"
"border: 0px;")

        self.horizontalLayout_53.addWidget(self.reviewslist_myreviews)


        self.verticalLayout_32.addWidget(self.frame_120)

        self.body.addWidget(self.myreviews)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_30 = QVBoxLayout(self.page)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_79 = QFrame(self.page)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(0, 81))
        self.frame_79.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_79)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(9, 9, 9, 2)
        self.frame_98 = QFrame(self.frame_79)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.backbutton_allreviews = QPushButton(self.frame_98)
        self.backbutton_allreviews.setObjectName(u"backbutton_allreviews")
        self.backbutton_allreviews.setMinimumSize(QSize(50, 50))
        self.backbutton_allreviews.setMaximumSize(QSize(50, 50))
        self.backbutton_allreviews.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_43.addWidget(self.backbutton_allreviews)

        self.moviename_allreviews = QLabel(self.frame_98)
        self.moviename_allreviews.setObjectName(u"moviename_allreviews")
        self.moviename_allreviews.setStyleSheet(u"font: 25pt \"Century Gothic\";\n"
"font: 63 34pt \"Bahnschrift SemiBold\";\n"
"font: 26pt \"Bahnschrift SemiCondensed\";\n"
"font: 19pt \"Century Gothic\";\n"
"font: 63 28pt \"Bahnschrift SemiBold Condensed\";")
        self.moviename_allreviews.setAlignment(Qt.AlignCenter)
        self.moviename_allreviews.setWordWrap(True)

        self.horizontalLayout_43.addWidget(self.moviename_allreviews)

        self.homebutton_allreviews = QPushButton(self.frame_98)
        self.homebutton_allreviews.setObjectName(u"homebutton_allreviews")
        self.homebutton_allreviews.setMinimumSize(QSize(50, 50))
        self.homebutton_allreviews.setMaximumSize(QSize(50, 50))
        self.homebutton_allreviews.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_43.addWidget(self.homebutton_allreviews)


        self.verticalLayout_33.addWidget(self.frame_98)

        self.frame_114 = QFrame(self.frame_79)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_114)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_123 = QFrame(self.frame_114)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setMaximumSize(QSize(16777215, 1))
        self.frame_123.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_57.addWidget(self.frame_123)


        self.verticalLayout_33.addWidget(self.frame_114)


        self.verticalLayout_30.addWidget(self.frame_79)

        self.myrewiewframe_allreviews = QFrame(self.page)
        self.myrewiewframe_allreviews.setObjectName(u"myrewiewframe_allreviews")
        self.myrewiewframe_allreviews.setMaximumSize(QSize(16777215, 170))
        self.myrewiewframe_allreviews.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.myrewiewframe_allreviews.setFrameShape(QFrame.StyledPanel)
        self.myrewiewframe_allreviews.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.myrewiewframe_allreviews)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_102 = QFrame(self.myrewiewframe_allreviews)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.myrating_allreviews = QLabel(self.frame_102)
        self.myrating_allreviews.setObjectName(u"myrating_allreviews")
        self.myrating_allreviews.setStyleSheet(u"font: 16pt \"Bahnschrift SemiCondensed\";")

        self.horizontalLayout_41.addWidget(self.myrating_allreviews)

        self.editreviewbutton_allreviews = QPushButton(self.frame_102)
        self.editreviewbutton_allreviews.setObjectName(u"editreviewbutton_allreviews")
        self.editreviewbutton_allreviews.setMinimumSize(QSize(75, 31))
        self.editreviewbutton_allreviews.setMaximumSize(QSize(75, 31))
        self.editreviewbutton_allreviews.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 15px;\n"
"	font: 10pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 15px;\n"
"	font: 10pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_41.addWidget(self.editreviewbutton_allreviews)

        self.deletereviewbutton_allreviews = QPushButton(self.frame_102)
        self.deletereviewbutton_allreviews.setObjectName(u"deletereviewbutton_allreviews")
        self.deletereviewbutton_allreviews.setMinimumSize(QSize(75, 31))
        self.deletereviewbutton_allreviews.setMaximumSize(QSize(75, 31))
        self.deletereviewbutton_allreviews.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 15px;\n"
"	font: 10pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 15px;\n"
"	font: 10pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_41.addWidget(self.deletereviewbutton_allreviews)


        self.verticalLayout_29.addWidget(self.frame_102)

        self.scrollArea_2 = QScrollArea(self.myrewiewframe_allreviews)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMaximumSize(QSize(16777215, 121))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 759, 121))
        self.horizontalLayout_47 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.myreviewdesc_allreviews = QLabel(self.scrollAreaWidgetContents_2)
        self.myreviewdesc_allreviews.setObjectName(u"myreviewdesc_allreviews")
        self.myreviewdesc_allreviews.setMaximumSize(QSize(16777215, 103))
        self.myreviewdesc_allreviews.setStyleSheet(u"font: 11pt \"Century Gothic\";")
        self.myreviewdesc_allreviews.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.myreviewdesc_allreviews.setWordWrap(True)

        self.horizontalLayout_47.addWidget(self.myreviewdesc_allreviews)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_29.addWidget(self.scrollArea_2)


        self.verticalLayout_30.addWidget(self.myrewiewframe_allreviews)

        self.frame_122 = QFrame(self.page)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_122)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_21 = QLabel(self.frame_122)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font: 16pt \"Bahnschrift SemiCondensed\";")

        self.verticalLayout_28.addWidget(self.label_21)

        self.alluserreviewslist_allreviews = QListWidget(self.frame_122)
        icon10 = QIcon()
        icon10.addFile(u"data/img/login_border_small.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem7 = QListWidgetItem(self.alluserreviewslist_allreviews)
        __qlistwidgetitem7.setIcon(icon10);
        self.alluserreviewslist_allreviews.setObjectName(u"alluserreviewslist_allreviews")
        self.alluserreviewslist_allreviews.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);\n"
"font: 11pt \"Century Gothic\";\n"
"icon-size: 125px;\n"
"border: 0px;")

        self.verticalLayout_28.addWidget(self.alluserreviewslist_allreviews)


        self.verticalLayout_30.addWidget(self.frame_122)

        self.frame_108 = QFrame(self.page)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_108)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.writereviewbutton_allreviews = QPushButton(self.frame_108)
        self.writereviewbutton_allreviews.setObjectName(u"writereviewbutton_allreviews")
        self.writereviewbutton_allreviews.setMinimumSize(QSize(150, 40))
        self.writereviewbutton_allreviews.setMaximumSize(QSize(150, 40))
        self.writereviewbutton_allreviews.setStyleSheet(u"QPushButton {	\n"
"	border-radius: 20px;\n"
"	background-color: rgba(102, 97, 234, 70);\n"
"	color: rgb(0,0,0);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(72, 67, 181, 80);\n"
"	color: rgb(255,255,255);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(72, 67, 181, 130);\n"
"	color: rgb(255,255,255);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"")

        self.horizontalLayout_46.addWidget(self.writereviewbutton_allreviews)


        self.verticalLayout_30.addWidget(self.frame_108)

        self.body.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_27 = QVBoxLayout(self.page_2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_100 = QFrame(self.page_2)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMinimumSize(QSize(0, 81))
        self.frame_100.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_100)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(9, 9, 9, 2)
        self.frame_101 = QFrame(self.frame_100)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.backbutton_reviewnow = QPushButton(self.frame_101)
        self.backbutton_reviewnow.setObjectName(u"backbutton_reviewnow")
        self.backbutton_reviewnow.setMinimumSize(QSize(50, 50))
        self.backbutton_reviewnow.setMaximumSize(QSize(50, 50))
        self.backbutton_reviewnow.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_42.addWidget(self.backbutton_reviewnow)

        self.moviename_reviewnow = QLabel(self.frame_101)
        self.moviename_reviewnow.setObjectName(u"moviename_reviewnow")
        self.moviename_reviewnow.setStyleSheet(u"font: 25pt \"Century Gothic\";\n"
"font: 63 34pt \"Bahnschrift SemiBold\";\n"
"font: 26pt \"Bahnschrift SemiCondensed\";\n"
"font: 19pt \"Century Gothic\";\n"
"font: 63 28pt \"Bahnschrift SemiBold Condensed\";")
        self.moviename_reviewnow.setAlignment(Qt.AlignCenter)
        self.moviename_reviewnow.setWordWrap(True)

        self.horizontalLayout_42.addWidget(self.moviename_reviewnow)

        self.homebutton_reviewnow = QPushButton(self.frame_101)
        self.homebutton_reviewnow.setObjectName(u"homebutton_reviewnow")
        self.homebutton_reviewnow.setMinimumSize(QSize(50, 50))
        self.homebutton_reviewnow.setMaximumSize(QSize(50, 50))
        self.homebutton_reviewnow.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 0, 0, 30);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_42.addWidget(self.homebutton_reviewnow)


        self.verticalLayout_34.addWidget(self.frame_101)

        self.frame_115 = QFrame(self.frame_100)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_115)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.frame_125 = QFrame(self.frame_115)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setMaximumSize(QSize(16777215, 1))
        self.frame_125.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_59.addWidget(self.frame_125)


        self.verticalLayout_34.addWidget(self.frame_115)


        self.verticalLayout_27.addWidget(self.frame_100)

        self.frame_103 = QFrame(self.page_2)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_103)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_7 = QLabel(self.frame_103)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 16pt \"Bahnschrift SemiCondensed\";")

        self.verticalLayout_21.addWidget(self.label_7)

        self.reviewdesc_textbox_reviewnow = QTextEdit(self.frame_103)
        self.reviewdesc_textbox_reviewnow.setObjectName(u"reviewdesc_textbox_reviewnow")
        self.reviewdesc_textbox_reviewnow.setStyleSheet(u"background-color: rgba(255, 255, 255, 255);\n"
"font: 11pt \"Century Gothic\";")

        self.verticalLayout_21.addWidget(self.reviewdesc_textbox_reviewnow)


        self.verticalLayout_27.addWidget(self.frame_103)

        self.frame_124 = QFrame(self.page_2)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_124.setFrameShape(QFrame.StyledPanel)
        self.frame_124.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_124)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_8 = QLabel(self.frame_124)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 16pt \"Bahnschrift SemiCondensed\";")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_26.addWidget(self.label_8)

        self.expressionstar_reviewnow = QLabel(self.frame_124)
        self.expressionstar_reviewnow.setObjectName(u"expressionstar_reviewnow")
        self.expressionstar_reviewnow.setStyleSheet(u"font: 19pt \"Century Gothic\";\n"
"font: 63 20pt \"Bahnschrift SemiBold Condensed\";\n"
"font: 14pt \"Century Gothic\";")
        self.expressionstar_reviewnow.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.expressionstar_reviewnow)

        self.frame_104 = QFrame(self.frame_124)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.frame_105 = QFrame(self.frame_104)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_44.addWidget(self.frame_105)

        self.starbutton_1 = QPushButton(self.frame_104)
        self.starbutton_1.setObjectName(u"starbutton_1")
        self.starbutton_1.setMinimumSize(QSize(55, 55))
        self.starbutton_1.setMaximumSize(QSize(55, 55))
        icon11 = QIcon()
        icon11.addFile(u"data/img/star_filled_small.png", QSize(), QIcon.Normal, QIcon.Off)
        self.starbutton_1.setIcon(icon11)
        self.starbutton_1.setIconSize(QSize(55, 55))

        self.horizontalLayout_44.addWidget(self.starbutton_1)

        self.starbutton_2 = QPushButton(self.frame_104)
        self.starbutton_2.setObjectName(u"starbutton_2")
        self.starbutton_2.setMinimumSize(QSize(55, 55))
        self.starbutton_2.setMaximumSize(QSize(55, 55))
        self.starbutton_2.setIcon(icon11)
        self.starbutton_2.setIconSize(QSize(55, 55))

        self.horizontalLayout_44.addWidget(self.starbutton_2)

        self.starbutton_3 = QPushButton(self.frame_104)
        self.starbutton_3.setObjectName(u"starbutton_3")
        self.starbutton_3.setMinimumSize(QSize(55, 55))
        self.starbutton_3.setMaximumSize(QSize(55, 55))
        self.starbutton_3.setIcon(icon11)
        self.starbutton_3.setIconSize(QSize(55, 55))

        self.horizontalLayout_44.addWidget(self.starbutton_3)

        self.starbutton_4 = QPushButton(self.frame_104)
        self.starbutton_4.setObjectName(u"starbutton_4")
        self.starbutton_4.setMinimumSize(QSize(55, 55))
        self.starbutton_4.setMaximumSize(QSize(55, 55))
        self.starbutton_4.setIcon(icon11)
        self.starbutton_4.setIconSize(QSize(55, 55))

        self.horizontalLayout_44.addWidget(self.starbutton_4)

        self.starbutton_5 = QPushButton(self.frame_104)
        self.starbutton_5.setObjectName(u"starbutton_5")
        self.starbutton_5.setMinimumSize(QSize(55, 55))
        self.starbutton_5.setMaximumSize(QSize(55, 55))
        self.starbutton_5.setIcon(icon11)
        self.starbutton_5.setIconSize(QSize(55, 55))

        self.horizontalLayout_44.addWidget(self.starbutton_5)

        self.starbutton_6 = QPushButton(self.frame_104)
        self.starbutton_6.setObjectName(u"starbutton_6")
        self.starbutton_6.setMinimumSize(QSize(55, 55))
        self.starbutton_6.setMaximumSize(QSize(55, 55))
        self.starbutton_6.setIcon(icon11)
        self.starbutton_6.setIconSize(QSize(55, 55))

        self.horizontalLayout_44.addWidget(self.starbutton_6)

        self.starbutton_7 = QPushButton(self.frame_104)
        self.starbutton_7.setObjectName(u"starbutton_7")
        self.starbutton_7.setMinimumSize(QSize(55, 55))
        self.starbutton_7.setMaximumSize(QSize(55, 55))
        self.starbutton_7.setIcon(icon11)
        self.starbutton_7.setIconSize(QSize(55, 55))

        self.horizontalLayout_44.addWidget(self.starbutton_7)

        self.starbutton_8 = QPushButton(self.frame_104)
        self.starbutton_8.setObjectName(u"starbutton_8")
        self.starbutton_8.setMinimumSize(QSize(55, 55))
        self.starbutton_8.setMaximumSize(QSize(55, 55))
        self.starbutton_8.setIcon(icon11)
        self.starbutton_8.setIconSize(QSize(55, 55))

        self.horizontalLayout_44.addWidget(self.starbutton_8)

        self.starbutton_9 = QPushButton(self.frame_104)
        self.starbutton_9.setObjectName(u"starbutton_9")
        self.starbutton_9.setMinimumSize(QSize(55, 55))
        self.starbutton_9.setMaximumSize(QSize(55, 55))
        icon12 = QIcon()
        icon12.addFile(u"data/img/star_default_small.png", QSize(), QIcon.Normal, QIcon.Off)
        self.starbutton_9.setIcon(icon12)
        self.starbutton_9.setIconSize(QSize(55, 55))

        self.horizontalLayout_44.addWidget(self.starbutton_9)

        self.starbutton_10 = QPushButton(self.frame_104)
        self.starbutton_10.setObjectName(u"starbutton_10")
        self.starbutton_10.setMinimumSize(QSize(55, 55))
        self.starbutton_10.setMaximumSize(QSize(55, 55))
        self.starbutton_10.setIcon(icon12)
        self.starbutton_10.setIconSize(QSize(55, 55))

        self.horizontalLayout_44.addWidget(self.starbutton_10)

        self.frame_106 = QFrame(self.frame_104)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_44.addWidget(self.frame_106)


        self.verticalLayout_26.addWidget(self.frame_104)


        self.verticalLayout_27.addWidget(self.frame_124)

        self.frame_107 = QFrame(self.page_2)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setStyleSheet(u"background-color: rgb(255, 255, 255, 0)")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_107)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.submitreviewbutton_reviewnow = QPushButton(self.frame_107)
        self.submitreviewbutton_reviewnow.setObjectName(u"submitreviewbutton_reviewnow")
        self.submitreviewbutton_reviewnow.setMinimumSize(QSize(150, 40))
        self.submitreviewbutton_reviewnow.setMaximumSize(QSize(150, 40))
        self.submitreviewbutton_reviewnow.setStyleSheet(u"QPushButton {	\n"
"	border-radius: 20px;\n"
"	background-color: rgba(102, 97, 234, 70);\n"
"	color: rgb(0,0,0);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(72, 67, 181, 80);\n"
"	color: rgb(255,255,255);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(72, 67, 181, 130);\n"
"	color: rgb(255,255,255);\n"
"	font: 12pt \"Bahnschrift SemiCondensed\";\n"
"}\n"
"")

        self.horizontalLayout_45.addWidget(self.submitreviewbutton_reviewnow)


        self.verticalLayout_27.addWidget(self.frame_107)

        self.body.addWidget(self.page_2)

        self.horizontalLayout_2.addWidget(self.body)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.horizontalLayout_3.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.body.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.registerbutton_register.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Already have an account?", None))
        self.loginbutton_register.setText(QCoreApplication.translate("MainWindow", u"Login now!", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_13.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.loginbutton_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Don't have an account?", None))
        self.registerbutton_login.setText(QCoreApplication.translate("MainWindow", u"Register now!", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Movie List", None))
        self.profilebutton_movielist.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sort by:", None))
        self.sortmovie_movielist.setItemText(0, QCoreApplication.translate("MainWindow", u"Name", None))
        self.sortmovie_movielist.setItemText(1, QCoreApplication.translate("MainWindow", u"Ratings (Best-Worst)", None))
        self.sortmovie_movielist.setItemText(2, QCoreApplication.translate("MainWindow", u"Ratings (Worst-Best)", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.searchmovie_movielist.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Movie Name", None))
        self.searchbutton_movielist.setText("")

        __sortingEnabled = self.movielist_movielist.isSortingEnabled()
        self.movielist_movielist.setSortingEnabled(False)
        ___qlistwidgetitem = self.movielist_movielist.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Title: HTTYD\n"
"Ratings: 5.5\n"
"User ratings total: 90293", None));
        ___qlistwidgetitem1 = self.movielist_movielist.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Title: Onwards\n"
"Ratings: 5.5\n"
"User ratings total: 90293", None));
        ___qlistwidgetitem2 = self.movielist_movielist.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Title: Sex Education\n"
"Ratings: 5.5\n"
"User ratings total: 90293", None));
        ___qlistwidgetitem3 = self.movielist_movielist.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Name: Test\n"
"Title: Inside Job\n"
"Ratings: 5.5\n"
"User ratings total: 90293", None));
        ___qlistwidgetitem4 = self.movielist_movielist.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Name: Test\n"
"Title: The Witcher\n"
"Ratings: 5.5\n"
"User ratings total: 90293", None));
        ___qlistwidgetitem5 = self.movielist_movielist.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Name: Test\n"
"Title: Spongebob\n"
"Ratings: 5.5\n"
"User ratings total: 90293", None));
        self.movielist_movielist.setSortingEnabled(__sortingEnabled)

        self.viewdetailsbutton_movielist.setText(QCoreApplication.translate("MainWindow", u"View Details", None))
        self.backbutton_moviedetails.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Movie Details", None))
        self.profilebutton_moviedetails.setText("")
        self.movieposter_moviedetails.setText(QCoreApplication.translate("MainWindow", u"IMAGE HERE", None))
        self.movietitle_moviedetails.setText(QCoreApplication.translate("MainWindow", u"How to Train Your Dragon: The Hidden World ", None))
        self.ratingscount_moviedetails.setText(QCoreApplication.translate("MainWindow", u"Ratings: 9.1 based on 982392 reviews", None))
        self.synopsis_moviedetails.setText(QCoreApplication.translate("MainWindow", u"When Hiccup discovers Toothless isn't the only Night Fury, he must seek \"The Hidden World\", a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"User Reviews", None))
        self.viewallbutton_moviedetails.setText(QCoreApplication.translate("MainWindow", u"View All", None))

        __sortingEnabled1 = self.reviewslist_moviedetails.isSortingEnabled()
        self.reviewslist_moviedetails.setSortingEnabled(False)
        ___qlistwidgetitem6 = self.reviewslist_moviedetails.item(0)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\n"
"<Username>\n"
"Ratings: 10 \n"
"When I saw this film tonight, I was completely bowled over from start to finish. I have simply never seen a better looking computer generated film nor a film that used 3-D to such wonderful effect. Finally--a film that doesn't look like the 3_D doesn't look like it was tossed in as an afterthought--but was clearly intended as one all along. However, I will warn you NOT to waste your time seeing it in 2-D---the film loses too much of its artistry. Now I know some of you will think I am a total sap for saying this, but the film literally brought tears to my eyes because it was so beautiful. I simply couldn't believe how special and artistic this movie was--it completely exceeded my expectations. This is because the advertising campaign make this movie look like it's just another kids' movie--and nothing more. But, with a lovely plot, interesting characters, the best CGI on Earth, a terrific sound track and lots of surprises, this simply is a joy to watch. Nornally when I revi"
                        "ew a film I try to talk about the film's flaws...but I simply couldn't find any. At last, a 3-D CGI film that actually manages to be better looking than last year's \"Up\"! It is hard to imagine a film being any better--though I am sure five years from now, I will be seeing even better 3-D and computer generated films...and it boggles the mind! See this film!\n"
"\n"
"UPDATE: I saw this on a huge home television. While the wonderful 3-D was missing, the film still had the nicest CGI and was nearly as entertaining as it was in the theater.\n"
"__________________________________________________________________________________________________________________", None));
        ___qlistwidgetitem7 = self.reviewslist_moviedetails.item(1)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\n"
"<Username>\n"
"Ratings: 10\n"
"I love animation, always have done, always will do, and I was blown away by How to Train Your Dragon. Granted, not all Dreamworks movies are bad, Prince of Egypt is one of the most stirring and evocative films let alone animated films I have seen, Shrek was very original and funny and Spirit:Stallion of the Cimarron is their most underrated I feel. I will say too, How to Train Your Dragon along with Prince of Egypt is my absolute favourite of Dreamworks, and one of the best of 2010.\n"
"\n"
"The story is very engaging; there is nothing too sophisticated for kids and nothing too childish for adults. It is instead an intelligent, moving story that moves along at a good pace, and I for one didn't find it that predictable, and I loved the bonding scenes between Toothless and Hiccup which were suitably poignant. The script is also very strong, it is thoughtful and touching at times but also amusing when it needs to be.\n"
"\n"
"The characters are another strength. Hiccup is appea"
                        "ling as a protagonist, and Toothless is really quite cute for a dragon. Hiccup's father Stoick is a good character too, he is gruff and such but you can tell he cares for his son. The voice acting too I had no problem with, to me they did fit well with the characters, Jay Baruchal's excitement and enthusiasm contrasts wonderfully with Gerard Butler's restrained, gruff yet sensitive performance.\n"
"\n"
"Where How to Train Your Dragon really excels though are in its visuals and music score. The animation is outstanding, while the characters are modelled convincingly the real revelations are in the stunning flying sequences and the beautiful lavish backgrounds. Oh and the fight sequences are equally spectacular, haunting but also very gripping and almost epic. John Powell's score is a revelation, and one of my favourite scores in a film of recent times. Sometimes soaring, sometimes dramatic, sometimes energetic, in fact no matter what mood is conveyed, the score compliments it to perfection.\n"
"\n"
"So overall,"
                        " there is very little else to say about this film, other than to say it is a must-see in my opinion. 10/10 Bethany Cox\n"
"__________________________________________________________________________________________________________________", None));
        ___qlistwidgetitem8 = self.reviewslist_moviedetails.item(2)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\n"
"<Username>\n"
"Ratings: 10\n"
"Hiccup (Jay Baruchel) and his village is constantly attacked by dragons. Weakling Hiccup isn't much help. He befriends an injured dragon missing part of his tail fin. He helps it by making a prosthetic tail. In the meanwhile, he becomes a great study of dragons. Instead of fighting them, he's able to subdue them.\n"
"\n"
"DreamWorks has created a beautiful 3D animation. The story is a beautiful one of friendship between the boy and the dragon. Jay Baruchel is really terrific as the geeky boy. The whole group of kids have real charisma. I especially like the training sessions, and how the boy's relationship with the dragon pays off.\n"
"__________________________________________________________________________________________________________________", None));
        self.reviewslist_moviedetails.setSortingEnabled(__sortingEnabled1)

        self.backbutton_profile.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.homebutton_profile.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_23.setText("")
        self.firstlastname_profile.setText(QCoreApplication.translate("MainWindow", u"Dai Xiez", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Registered since", None))
        self.registeredsince_profile.setText(QCoreApplication.translate("MainWindow", u"29 October 2021", None))
        self.logoutbutton_profile.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.deleteaccountbutton_profile.setText(QCoreApplication.translate("MainWindow", u"Delete Account", None))
        self.myreviewsbutton_profile.setText(QCoreApplication.translate("MainWindow", u"My Reviews", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"User Info", None))
        self.emailinfo_profile.setText(QCoreApplication.translate("MainWindow", u"Email: user@email.com", None))
        self.emailinfo_profile_2.setText(QCoreApplication.translate("MainWindow", u"Username: daixiez", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Change password", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Current Pass.", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"New Pass.", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Confirm New Pass.", None))
        self.confirmchangesbutton_profile.setText(QCoreApplication.translate("MainWindow", u"Confirm change", None))
        self.backbutton_myreviews.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"My Reviews", None))
        self.homebutton_myreviews.setText(QCoreApplication.translate("MainWindow", u"Home", None))

        __sortingEnabled2 = self.reviewslist_myreviews.isSortingEnabled()
        self.reviewslist_myreviews.setSortingEnabled(False)
        ___qlistwidgetitem9 = self.reviewslist_myreviews.item(0)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Onward\n"
"\u260510\n"
"This movie is amazing! I teared up a bit towards the ending of the movie. Didn't thought it would be that sad.", None));
        self.reviewslist_myreviews.setSortingEnabled(__sortingEnabled2)

        self.backbutton_allreviews.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.moviename_allreviews.setText(QCoreApplication.translate("MainWindow", u"How To Train Your Dragon", None))
        self.homebutton_allreviews.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.myrating_allreviews.setText(QCoreApplication.translate("MainWindow", u"My Review - \u26059", None))
        self.editreviewbutton_allreviews.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.deletereviewbutton_allreviews.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.myreviewdesc_allreviews.setText(QCoreApplication.translate("MainWindow", u"This movie is amazing! I teared up a bit towards the ending of the movie. Didn't thought it would be that sad.", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"User Reviews", None))

        __sortingEnabled3 = self.alluserreviewslist_allreviews.isSortingEnabled()
        self.alluserreviewslist_allreviews.setSortingEnabled(False)
        ___qlistwidgetitem10 = self.alluserreviewslist_allreviews.item(0)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"daixiez\n"
"This movie is amazing! I teared up a bit towards the ending of the movie. Didn't thought it would be that sad.", None));
        self.alluserreviewslist_allreviews.setSortingEnabled(__sortingEnabled3)

        self.writereviewbutton_allreviews.setText(QCoreApplication.translate("MainWindow", u"Write Review", None))
        self.backbutton_reviewnow.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.moviename_reviewnow.setText(QCoreApplication.translate("MainWindow", u"How To Train Your Dragon", None))
        self.homebutton_reviewnow.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Review description", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"How would you rate this movie? ", None))
        self.expressionstar_reviewnow.setText(QCoreApplication.translate("MainWindow", u"I love it!", None))
        self.starbutton_1.setText("")
        self.starbutton_2.setText("")
        self.starbutton_3.setText("")
        self.starbutton_4.setText("")
        self.starbutton_5.setText("")
        self.starbutton_6.setText("")
        self.starbutton_7.setText("")
        self.starbutton_8.setText("")
        self.starbutton_9.setText("")
        self.starbutton_10.setText("")
        self.submitreviewbutton_reviewnow.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
    # retranslateUi

