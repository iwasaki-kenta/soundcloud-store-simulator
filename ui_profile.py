#-------------------------------------------------------------------------------
# Name:        breakBeats
# Purpose:     A SoundCloud-integrated music store simulation.
# Author:      Kenta Iwasaki
# Created:     08/03/2014
# Copyright:   (c) Kenta Iwasaki 2014
#-------------------------------------------------------------------------------

# PyQT Framework Module Imports
from PyQt5 import QtCore, QtGui, QtWidgets

# A layout container for the Profile Dialog's context.
class Ui_ProfileDialog(object):
    # Initiates and defines all the GUI elements along with their properties.
    def setupUi(self, ProfileDialog):
        ProfileDialog.setObjectName("ProfileDialog")
        ProfileDialog.resize(380, 290)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProfileDialog.sizePolicy().hasHeightForWidth())
        ProfileDialog.setSizePolicy(sizePolicy)
        ProfileDialog.setMinimumSize(QtCore.QSize(380, 290))
        ProfileDialog.setMaximumSize(QtCore.QSize(380, 290))
        self.groupBox = QtWidgets.QGroupBox(ProfileDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 120, 371, 131))
        self.groupBox.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 18, 341, 111))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.txtGender = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.txtGender.setObjectName("txtGender")
        self.txtGender.addItem("")
        self.txtGender.addItem("")
        self.gridLayout_2.addWidget(self.txtGender, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.txtBirth = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtBirth.setObjectName("txtBirth")
        self.gridLayout_2.addWidget(self.txtBirth, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.txtName = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtName.setObjectName("txtName")
        self.gridLayout_2.addWidget(self.txtName, 0, 1, 1, 1)
        self.txtCountry = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txtCountry.setObjectName("txtCountry")
        self.gridLayout_2.addWidget(self.txtCountry, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(ProfileDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 371, 91))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 351, 74))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.txtPassword = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.txtPassword.setClearButtonEnabled(False)
        self.txtPassword.setObjectName("txtPassword")
        self.gridLayout.addWidget(self.txtPassword, 1, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.txtEmail = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtEmail.setObjectName("txtEmail")
        self.gridLayout.addWidget(self.txtEmail, 2, 1, 1, 2)
        self.txtUsername = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtUsername.setObjectName("txtUsername")
        self.gridLayout.addWidget(self.txtUsername, 0, 1, 1, 2)
        self.btnSaveInfo = QtWidgets.QPushButton(ProfileDialog)
        self.btnSaveInfo.setGeometry(QtCore.QRect(10, 260, 361, 23))
        self.btnSaveInfo.setObjectName("btnSaveInfo")

        self.retranslateUi(ProfileDialog)
        QtCore.QMetaObject.connectSlotsByName(ProfileDialog)

    # Set's string constant values for the UI elements.
    def retranslateUi(self, ProfileDialog):
        _translate = QtCore.QCoreApplication.translate
        ProfileDialog.setWindowTitle(_translate("ProfileDialog", "breakBeats :: Profile Info"))
        self.groupBox.setTitle(_translate("ProfileDialog", "Personal Information"))
        self.txtGender.setItemText(0, _translate("ProfileDialog", "Male"))
        self.txtGender.setItemText(1, _translate("ProfileDialog", "Female"))
        self.label_7.setText(_translate("ProfileDialog", "Gender:"))
        self.label_4.setText(_translate("ProfileDialog", "Date of Birth: "))
        self.label_6.setText(_translate("ProfileDialog", "Country: "))
        self.label_3.setText(_translate("ProfileDialog", "Name:"))
        self.groupBox_2.setTitle(_translate("ProfileDialog", "Account Information"))
        self.label.setText(_translate("ProfileDialog", "Username:"))
        self.label_2.setText(_translate("ProfileDialog", "Password:"))
        self.label_5.setText(_translate("ProfileDialog", "E-Mail Address:"))
        self.btnSaveInfo.setText(_translate("ProfileDialog", "Save Info"))

