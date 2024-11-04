# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainFaGaHk.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(458, 430)
        self.lbl_Title = QLabel(MainWindow)
        self.lbl_Title.setObjectName(u"lbl_Title")
        self.lbl_Title.setGeometry(QRect(130, 10, 191, 16))
        font = QFont()
        font.setPointSize(11)
        self.lbl_Title.setFont(font)
        self.lbl_from = QLabel(MainWindow)
        self.lbl_from.setObjectName(u"lbl_from")
        self.lbl_from.setGeometry(QRect(10, 50, 49, 21))
        self.lbl_from.setLayoutDirection(Qt.RightToLeft)
        self.lbl_from.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_to = QLabel(MainWindow)
        self.lbl_to.setObjectName(u"lbl_to")
        self.lbl_to.setGeometry(QRect(10, 170, 51, 20))
        self.lbl_to.setLayoutDirection(Qt.LeftToRight)
        self.lbl_to.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_from = QLineEdit(MainWindow)
        self.line_from.setObjectName(u"line_from")
        self.line_from.setGeometry(QRect(70, 50, 311, 22))
        self.line_to = QLineEdit(MainWindow)
        self.line_to.setObjectName(u"line_to")
        self.line_to.setGeometry(QRect(70, 170, 311, 22))
        self.text_Status = QPlainTextEdit(MainWindow)
        self.text_Status.setObjectName(u"text_Status")
        self.text_Status.setEnabled(True)
        self.text_Status.setGeometry(QRect(60, 270, 341, 121))
        self.text_Status.setTextInteractionFlags(Qt.NoTextInteraction)
        self.btn_Start = QPushButton(MainWindow)
        self.btn_Start.setObjectName(u"btn_Start")
        self.btn_Start.setGeometry(QRect(240, 240, 75, 24))
        self.btn_Stop = QPushButton(MainWindow)
        self.btn_Stop.setObjectName(u"btn_Stop")
        self.btn_Stop.setEnabled(True)
        self.btn_Stop.setGeometry(QRect(320, 240, 75, 24))
        self.lbl_Status = QLabel(MainWindow)
        self.lbl_Status.setObjectName(u"lbl_Status")
        self.lbl_Status.setGeometry(QRect(0, 270, 51, 20))
        self.lbl_Status.setLayoutDirection(Qt.LeftToRight)
        self.lbl_Status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.btn_Exit = QPushButton(MainWindow)
        self.btn_Exit.setObjectName(u"btn_Exit")
        self.btn_Exit.setGeometry(QRect(320, 400, 75, 24))
        self.lbl_Interval = QLabel(MainWindow)
        self.lbl_Interval.setObjectName(u"lbl_Interval")
        self.lbl_Interval.setGeometry(QRect(10, 200, 51, 20))
        self.lbl_Interval.setLayoutDirection(Qt.LeftToRight)
        self.lbl_Interval.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_hours = QLineEdit(MainWindow)
        self.line_hours.setObjectName(u"line_hours")
        self.line_hours.setGeometry(QRect(70, 200, 71, 22))
        self.line_hours.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lbl_hours = QLabel(MainWindow)
        self.lbl_hours.setObjectName(u"lbl_hours")
        self.lbl_hours.setGeometry(QRect(150, 200, 71, 20))
        self.lbl_hours.setLayoutDirection(Qt.LeftToRight)
        self.lbl_hours.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_openFrom = QPushButton(MainWindow)
        self.btn_openFrom.setObjectName(u"btn_openFrom")
        self.btn_openFrom.setGeometry(QRect(390, 50, 21, 24))
        self.btn_openTo = QPushButton(MainWindow)
        self.btn_openTo.setObjectName(u"btn_openTo")
        self.btn_openTo.setGeometry(QRect(390, 170, 21, 24))
        self.btn_append = QPushButton(MainWindow)
        self.btn_append.setObjectName(u"btn_append")
        self.btn_append.setGeometry(QRect(310, 80, 75, 24))
        self.cb_Items = QComboBox(MainWindow)
        self.cb_Items.setObjectName(u"cb_Items")
        self.cb_Items.setGeometry(QRect(70, 110, 311, 22))
        self.btn_delItem = QPushButton(MainWindow)
        self.btn_delItem.setObjectName(u"btn_delItem")
        self.btn_delItem.setGeometry(QRect(390, 110, 41, 24))
        self.lbl_backupList = QLabel(MainWindow)
        self.lbl_backupList.setObjectName(u"lbl_backupList")
        self.lbl_backupList.setGeometry(QRect(10, 110, 49, 21))
        self.lbl_backupList.setLayoutDirection(Qt.RightToLeft)
        self.lbl_backupList.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_counter = QLabel(MainWindow)
        self.lbl_counter.setObjectName(u"lbl_counter")
        self.lbl_counter.setGeometry(QRect(70, 140, 311, 21))
        self.lbl_counter.setLayoutDirection(Qt.LeftToRight)
        self.lbl_counter.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_Signature = QLabel(MainWindow)
        self.lbl_Signature.setObjectName(u"lbl_Signature")
        self.lbl_Signature.setGeometry(QRect(10, 400, 111, 20))
        self.lbl_Signature.setLayoutDirection(Qt.LeftToRight)
        self.lbl_Signature.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Backup your FCKING DATA", None))
        self.lbl_Title.setText(QCoreApplication.translate("MainWindow", u"Backup your FCKING DATA", None))
        self.lbl_from.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.lbl_to.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.line_from.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The Folder you want to Backup as .zip", None))
        self.line_to.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Destination Folder Where the Backup.zip should be saved", None))
        self.text_Status.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data Backup Tool made by Radix (M.Pikulski)", None))
        self.btn_Start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_Stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.lbl_Status.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.btn_Exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.lbl_Interval.setText(QCoreApplication.translate("MainWindow", u"Intervall:", None))
        self.line_hours.setPlaceholderText("1")
        self.lbl_hours.setText(QCoreApplication.translate("MainWindow", u"Minutes(s)", None))
        self.btn_openFrom.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.btn_openTo.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.btn_append.setText(QCoreApplication.translate("MainWindow", u"Append", None))
        self.btn_delItem.setText(QCoreApplication.translate("MainWindow", u"Del", None))
        self.lbl_backupList.setText(QCoreApplication.translate("MainWindow", u"Backup:", None))
        self.lbl_counter.setText(QCoreApplication.translate("MainWindow", u"0 Files Choosen", None))
        self.lbl_Signature.setText(QCoreApplication.translate("MainWindow", u"Made By M.Pikulski", None))
    # retranslateUi

