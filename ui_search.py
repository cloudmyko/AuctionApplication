# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollBar, QSizePolicy, QStatusBar, QWidget)

class Ui_HomePage(object):
    def setupUi(self, HomePage):
        if not HomePage.objectName():
            HomePage.setObjectName(u"HomePage")
        HomePage.resize(800, 600)
        self.actionRequest_Help = QAction(HomePage)
        self.actionRequest_Help.setObjectName(u"actionRequest_Help")
        self.actionEnter_Code = QAction(HomePage)
        self.actionEnter_Code.setObjectName(u"actionEnter_Code")
        self.centralwidget = QWidget(HomePage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(280, 10, 281, 21))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(580, 10, 100, 32))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 140, 581, 311))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(160, 10, 103, 32))
        self.verticalScrollBar = QScrollBar(self.centralwidget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(770, 50, 20, 471))
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)
        HomePage.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(HomePage)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 42))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuStaff_Login = QMenu(self.menubar)
        self.menuStaff_Login.setObjectName(u"menuStaff_Login")
        HomePage.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(HomePage)
        self.statusbar.setObjectName(u"statusbar")
        HomePage.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuStaff_Login.menuAction())
        self.menuHelp.addAction(self.actionRequest_Help)
        self.menuStaff_Login.addAction(self.actionEnter_Code)

        self.retranslateUi(HomePage)

        QMetaObject.connectSlotsByName(HomePage)
    # setupUi

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(QCoreApplication.translate("HomePage", u"HomePage", None))
        self.actionRequest_Help.setText(QCoreApplication.translate("HomePage", u"Request Help", None))
        self.actionEnter_Code.setText(QCoreApplication.translate("HomePage", u"Enter Code", None))
        self.pushButton.setText(QCoreApplication.translate("HomePage", u"search", None))
        self.label.setText(QCoreApplication.translate("HomePage", u"Items and Itemnames and prices", None))
        self.comboBox.setCurrentText("")
        self.menuHelp.setTitle(QCoreApplication.translate("HomePage", u"Help", None))
        self.menuStaff_Login.setTitle(QCoreApplication.translate("HomePage", u"Staff Login", None))
    # retranslateUi

