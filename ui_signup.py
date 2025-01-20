# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QStatusBar, QWidget)

import sqlite3 as sq
from ui_search import Ui_HomePage as hp
import hashlib

class Ui_SignupPage(object):
    

    def showNext(self):
        # shows the next window when called
        self.window = QMainWindow()
        self.ui = hp()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def setupUi(self, SignupPage):
        # sets up all the moving parts within the graphical user interface
        global signedUp; signedUp = False
        if not SignupPage.objectName():
            SignupPage.setObjectName(u"SignupPage")
        SignupPage.resize(800, 600)

        self.actionRequest_Help = QAction(SignupPage)
        self.actionRequest_Help.setObjectName(u"actionRequest_Help")
        self.actionEnter_Code = QAction(SignupPage)
        self.actionEnter_Code.setObjectName(u"actionEnter_Code")

        self.centralwidget = QWidget(SignupPage)
        self.centralwidget.setObjectName(u"centralwidget")

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 20, 331, 171))
        font = QFont()
        font.setPointSize(60)
        self.label.setFont(font)

        self.enterFirst = QLineEdit(self.centralwidget)
        self.enterFirst.setObjectName(u"enterFirst")
        self.enterFirst.setGeometry(QRect(320, 150, 181, 31))

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 280, 81, 16))

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 320, 81, 16))

        self.submitButton = QPushButton(self.centralwidget)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setGeometry(QRect(330, 390, 151, 41))
        self.submitButton.clicked.connect(self.editClear and self.unique)

        self.enterLast = QLineEdit(self.centralwidget)
        self.enterLast.setObjectName(u"enterLast")
        self.enterLast.setGeometry(QRect(320, 190, 181, 31))

        self.enterEmail = QLineEdit(self.centralwidget)
        self.enterEmail.setObjectName(u"enterEmail")
        self.enterEmail.setGeometry(QRect(320, 230, 181, 31))

        self.enterUsername = QLineEdit(self.centralwidget)
        self.enterUsername.setObjectName(u"enterUsername")
        self.enterUsername.setGeometry(QRect(320, 270, 181, 31))

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(250, 160, 81, 16))

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 360, 111, 16))

        self.enterPassword = QLineEdit(self.centralwidget)
        self.enterPassword.setObjectName(u"enterPassword")
        self.enterPassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.enterPassword.setGeometry(QRect(320, 310, 181, 31))

        self.retypePassword = QLineEdit(self.centralwidget)
        self.retypePassword.setObjectName(u"retypePassword")
        self.retypePassword.setGeometry(QRect(320, 350, 181, 31))
        self.retypePassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 200, 81, 16))

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(280, 240, 81, 16))

        SignupPage.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(SignupPage)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 42))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuStaff_Login = QMenu(self.menubar)
        self.menuStaff_Login.setObjectName(u"menuStaff_Login")
        SignupPage.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SignupPage)
        self.statusbar.setObjectName(u"statusbar")
        SignupPage.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuStaff_Login.menuAction())
        self.menuHelp.addAction(self.actionRequest_Help)
        self.menuStaff_Login.addAction(self.actionEnter_Code)

        self.retranslateUi(SignupPage)

        QMetaObject.connectSlotsByName(SignupPage)

    # setupUi
    def retranslateUi(self, SignupPage):
        SignupPage.setWindowTitle(QCoreApplication.translate("SignupPage", u"SignupPage", None))
        self.actionRequest_Help.setText(QCoreApplication.translate("SignupPage", u"Request Help", None))
        self.actionEnter_Code.setText(QCoreApplication.translate("SignupPage", u"Enter Code", None))
        self.label.setText(QCoreApplication.translate("SignupPage", u"Sign Up", None))
        self.label_2.setText(QCoreApplication.translate("SignupPage", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("SignupPage", u"Password", None))
        self.submitButton.setText(QCoreApplication.translate("SignupPage", u"Sign Up", None))
#if QT_CONFIG(whatsthis)
        self.enterEmail.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.enterEmail.setInputMask("")
        self.enterEmail.setText("")
        self.label_4.setText(QCoreApplication.translate("SignupPage", u"First Name", None))
        self.label_5.setText(QCoreApplication.translate("SignupPage", u"Retype Password", None))
        self.label_6.setText(QCoreApplication.translate("SignupPage", u"Last Name", None))
        self.label_7.setText(QCoreApplication.translate("SignupPage", u"Email", None))
        self.menuHelp.setTitle(QCoreApplication.translate("SignupPage", u"Help", None))
        self.menuStaff_Login.setTitle(QCoreApplication.translate("SignupPage", u"Staff Login", None))
    # retranslateUi
    def editClear(self):
        self.enterPassword.clear()
        self.retypePassword.clear()

        # clears the password incase the user inputted passwords dont match




    # cant have a password shorter than 8 chars
    # cant have a username shorter than 6 chars
    def dbCheck(self, username, email):
        # checks if the inputted username and email are unique within the database

        conn = sq.connect('auctionhouse.db')
        curs = conn.cursor()
        

        sql = 'SELECT Username, Email FROM Users'

        curs.execute(sql)
        allEntries = curs.fetchall()


        for i in range(len(allEntries)):
            if (username + email) == ''.join(allEntries[i]):
                print("already in users")
                print(''.join(allEntries[i]))
                return False
            print(allEntries[i])
            
        return True
    
    def unique(self):
        username = self.enterUsername.text()
        password = self.enterEmail.text()

        if self.dbCheck(username, password) == True:
            if self.errorCheck() == True:
                self.signUp()
            
        else:
            print("not signing you up")
    
    def errorCheck(self):
        checked = False
        username = self.enterUsername.text()
        password = self.enterPassword.text()
        present = False
        conn = sq.connect('auctionhouse.db')
        curs = conn.cursor()

        sql = 'SELECT Username, Password FROM Users'

        curs.execute(sql)
        allEntries = curs.fetchall()

        for i in range(len(allEntries)):
            if (username + password) == ''.join(allEntries[i]):
                print(allEntries[i])
                present = True
                break
                

        if not checked:
            if (len(username) >= 6 and len(password) >= 8) and present == False:
                print("signing you up")
                checked = True
            elif (len(username) < 6 or len(password) < 8):
                print("your password/username isn't long enough\nusername min. 6 chars\npassword min. 8 chars ")
                self.enterPassword.clear()
                self.retypePassword.clear()
            else:
                print("invalid login")
                self.enterPassword.clear()
                self.retypePassword.clear()

        return checked
            

    def signUp(self):
        # enters the users data into the database, signing them up
        conn = sq.connect('auctionhouse.db')
        c = conn.cursor()

        user = str(self.enterUsername.text())
        password = str(self.enterPassword.text())
        email = str(self.enterEmail.text())
        fname = str(self.enterFirst.text())
        lname = str(self.enterLast.text())
        val = None
        password = str(self.hashPass(password))


        sql = "INSERT INTO Users (Fname, Lname, Email, Username, Password) VALUES ('" + fname + "', '" + lname + "', '" + email + "', '" + user + "', '" + password + "');"
        sql = str(sql)
        c.execute(sql)
        conn.commit()

        self.showNext()

        

    def hashPass(self, password):
        password = str(password)
        hashObject = hashlib.sha256(password.encode('utf-8'))
        hexDigit = hashObject.hexdigest()

        return hexDigit

        

            
        
        



        
    # cant have the same username cant have the same email.
