import ctypes
import sys
import re
import platform

import PyQt5
from PyQt5.QtWidgets import qApp
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent, QTimer, QSortFilterProxyModel)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QPainterPath)
from PySide2.QtWidgets import *
from [jeneng file gui mu sing wis diconvert jadi file py] import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # lebokke kodemu ng kene
        
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Wolf - Movie Ratings")
    sys.exit(app.exec_())