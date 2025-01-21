# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget, QCommandLinkButton)

import sqlite3 as sqlite
from ui_search import Ui_HomePage as hp
from ui_signup import Ui_SignupPage as sp
import hashlib

class Ui_LoginPage(object):
    
    def showNext(self):
        # opens the home page when called.
        self.window = QMainWindow()
        self.ui = hp()
        self.ui.setupUi(self.window)
        self.window.show()


    def showSignup(self):
        # shows the signup page of the program when called
        self.window = QMainWindow()
        self.ui = sp()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, LoginPage):
        # sets up the moving parts for the page
        if not LoginPage.objectName():
            LoginPage.setObjectName(u"LoginPage")
        LoginPage.resize(800, 600)
        self.loggedIn = False
        self.actionRequest_Help = QAction(LoginPage)
        self.actionRequest_Help.setObjectName(u"actionRequest_Help")
        self.actionEnter_Code = QAction(LoginPage)
        self.actionEnter_Code.setObjectName(u"actionEnter_Code")
        self.centralwidget = QWidget(LoginPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 20, 331, 171))
        font = QFont()
        font.setPointSize(60)
        self.label.setFont(font)
        self.enterUser = QLineEdit(self.centralwidget)
        self.enterUser.setObjectName(u"lineEdit")
        self.enterUser.setGeometry(QRect(310, 180, 181, 31))
        self.enterUser.setPlaceholderText("Username")

        self.enterPass = QLineEdit(self.centralwidget)
        self.enterPass.setObjectName(u"enterPass")
        self.enterPass.setGeometry(QRect(310, 240, 181, 31))
        self.enterPass.setPlaceholderText("Password")
        self.enterPass.setEchoMode(QLineEdit.EchoMode.Password)
        # hides the password

        self.commandLinkButton = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(320, 330, 141, 31))
        self.commandLinkButton.clicked.connect(self.showSignup)
        LoginPage.setCentralWidget(self.centralwidget)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 190, 81, 16))

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 250, 81, 16))

        self.submit = QPushButton(self.centralwidget)
        self.submit.setObjectName(u"Submit")
        self.submit.setGeometry(QRect(320, 280, 151, 41))
        self.submit.clicked.connect(self.login) #this calls the function and has it do the action once the log in button is pressed.

        LoginPage.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LoginPage)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 42))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuStaff_Login = QMenu(self.menubar)
        self.menuStaff_Login.setObjectName(u"menuStaff_Login")
        LoginPage.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LoginPage)
        self.statusbar.setObjectName(u"statusbar")
        LoginPage.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuStaff_Login.menuAction())
        self.menuHelp.addAction(self.actionRequest_Help)
        self.menuStaff_Login.addAction(self.actionEnter_Code)

        self.retranslateUi(LoginPage)

        QMetaObject.connectSlotsByName(LoginPage)
    # setupUi

    def retranslateUi(self, LoginPage):
        LoginPage.setWindowTitle(QCoreApplication.translate("LoginPage", u"LoginPage", None))
        self.actionRequest_Help.setText(QCoreApplication.translate("LoginPage", u"Request Help", None))
        self.actionEnter_Code.setText(QCoreApplication.translate("LoginPage", u"Enter Code", None))
        self.label.setText(QCoreApplication.translate("LoginPage", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("LoginPage", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("LoginPage", u"Password", None))
        self.submit.setText(QCoreApplication.translate("LoginPage", u"Log In", None))
        self.menuHelp.setTitle(QCoreApplication.translate("LoginPage", u"Help", None))
        self.menuStaff_Login.setTitle(QCoreApplication.translate("LoginPage", u"Staff Login", None))
    # retranslateUi
        
    def printText(self):
        print(self.lineEdit.text())
        print(self.enterPass.text())
        self.enterPass.clear()
        # delete procedure once everything is complete
        # takes the user input within the line edit and outputs it, then clears the password line edit so the user can retype if they have to.

    def loadDb(self):
        
        conn = sqlite.connect('auctionhouse.db')
        curs = conn.cursor()

        sql = 'SELECT Username, Password FROM Users'

        curs.execute(sql)
        rows = curs.fetchall()
        conn.commit()

        global elements
        elements = []

        for i in range(len(rows)):

            x = ''.join(rows[i])
            elements.append(x)

        curs.close()

    def login(self):
        # logs the user into the database if the username and password matches the ones in the database.
        self.loadDb()
        username = self.enterUser.text()
        password = self.enterPass.text()
        passToVerify = hashlib.sha256(password.encode('utf-8')).hexdigest()

        for i in range(len(elements)):
            auth = username + passToVerify
            if auth == elements[i]:
                print("logged in")
                self.loggedIn = True
                self.showNext()
                
                break



