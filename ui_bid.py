# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bid.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSpinBox, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_BidPage(object):
    def setupUi(self, BidPage):
        if not BidPage.objectName():
            BidPage.setObjectName(u"BidPage")
        BidPage.resize(800, 600)
        self.actionRequest_Help = QAction(BidPage)
        self.actionRequest_Help.setObjectName(u"actionRequest_Help")
        self.actionEnter_Code = QAction(BidPage)
        self.actionEnter_Code.setObjectName(u"actionEnter_Code")
        self.centralwidget = QWidget(BidPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 120, 361, 251))
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"SpinBox")
        self.spinBox.setGeometry(QRect(500, 290, 201, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(500, 210, 191, 71))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(500, 140, 181, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(550, 320, 100, 32))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(500, 360, 271, 161))
        BidPage.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(BidPage)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 42))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuStaff_Login = QMenu(self.menubar)
        self.menuStaff_Login.setObjectName(u"menuStaff_Login")
        BidPage.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(BidPage)
        self.statusbar.setObjectName(u"statusbar")
        BidPage.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuStaff_Login.menuAction())
        self.menuHelp.addAction(self.actionRequest_Help)
        self.menuStaff_Login.addAction(self.actionEnter_Code)

        self.retranslateUi(BidPage)

        QMetaObject.connectSlotsByName(BidPage)
    # setupUi 
        

    def retranslateUi(self, BidPage):
        BidPage.setWindowTitle(QCoreApplication.translate("BidPage", u"BidPage", None))
        self.actionRequest_Help.setText(QCoreApplication.translate("BidPage", u"Request Help", None))
        self.actionEnter_Code.setText(QCoreApplication.translate("BidPage", u"Enter Code", None))
        self.label.setText(QCoreApplication.translate("BidPage", u"IMAGE", None))
        self.label_2.setText(QCoreApplication.translate("BidPage", u"Price:", None))
        self.label_3.setText(QCoreApplication.translate("BidPage", u"Item Name", None))
        self.pushButton.setText(QCoreApplication.translate("BidPage", u"Bid", None))
        self.label_4.setText(QCoreApplication.translate("BidPage", u"Item Description", None))
        self.menuHelp.setTitle(QCoreApplication.translate("BidPage", u"Help", None))
        self.menuStaff_Login.setTitle(QCoreApplication.translate("BidPage", u"Staff Login", None))
    # retranslateUi

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode

    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertAtBegin(data)
            return
        
        position = 0
        currentNode = self.head
        while (currentNode != None and position+1 != index):
            position += 1
            currentNode = currentNode.next

        if currentNode != None:
            newNode = Node(data)
            newNode.next = currentNode.next
        else:
            print("index doesnt exist")

    def insertAtEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        
        currentNode = self.head
        while (currentNode.next):
            currentNode = currentNode.next

        currentNode.next = newNode

    def updateNode(self, val, index):
        currentNode = self.head
        pos = 0
        if pos == index:
            currentNode.data = val
        else:
            while (currentNode != None and pos != index):
                pos += 1
                currentNode = currentNode.next

            if currentNode != None:
                currentNode.data = val
            else:
                print("index, item dont exist")
    
    def removeFirst(self):
        if (self.head == None):
            return
        
        self.head = self.head.next

    def removeLast(self):
        if self.head == None:
            return
        
        checkNode = self.head
        while (checkNode.next != None and checkNode.next.next != None):
            checkNode = checkNode.next

        checkNode.next = None

    def removeData(self, data):
        currentNode = self.head

        if currentNode.data == data:
            self.removeFirst()
            return
        
        while currentNode is not None and currentNode.next.data != data:
            currentNode = currentNode.next

        if currentNode is None:
            return
        else:
            currentNode.next = currentNode.next.next

    def traversal(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next

    def sizeCheck(self):
        size = 0
        if self.head:
            currentNode = self.head
            while currentNode:
                size += 1
                currentNode = currentNode.next
            return size
        else:
            return 0

    def initImages(self):
        slideshow = linkedList()
        self.insertAtEnd()


        