# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/ADD.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(472, 465)
        Dialog.setMaximumSize(QtCore.QSize(472, 16777215))
        Dialog.setStyleSheet("QWidget {\n"
"    font-family: Rubik;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.calendarWidget.setAutoFillBackground(True)
        self.calendarWidget.setStyleSheet("QCalendarWidget QToolButton {\n"
"height:14px;\n"
"font-size:15px;\n"
"icon-size:16px,16px;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"font-size:10px;\n"
"font-weight: bold;\n"
"color:#05B8CC;\n"
"\n"
"}")
        self.calendarWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.NoHorizontalHeader)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_4.addWidget(self.comboBox_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Настройки товара"))
        self.lineEdit.setToolTip(_translate("Dialog", "Название"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Парацетамол...."))
        self.comboBox.setToolTip(_translate("Dialog", "Лекарственная форма препарата"))
        self.comboBox.setItemText(0, _translate("Dialog", "ЖИДКОЕ (капли, настойка, настои, сироп, суспензия, эмульсия)"))
        self.comboBox.setItemText(1, _translate("Dialog", "ТВЕРДОЕ (капсула, таблетка, порошки, гранулы, драже, карамель, карандаш)"))
        self.comboBox.setItemText(2, _translate("Dialog", "МЯГКОЕ (крем, мазь, гель, суппозитории, паста)"))
        self.comboBox.setItemText(3, _translate("Dialog", "АЭРОЗОЛЬ"))
        self.textEdit.setToolTip(_translate("Dialog", "Способ пременения и дозы"))
        self.textEdit.setPlaceholderText(_translate("Dialog", "Способ пременения кратко..."))
        self.calendarWidget.setToolTip(_translate("Dialog", "Срок годности"))
        self.lineEdit_2.setToolTip(_translate("Dialog", "ссылка на инструкцию или лекарство"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "https://www.lsgeotar.ru/paratsetamol-18079.html"))
        self.pushButton.setText(_translate("Dialog", "ДОБАВИТЬ"))
        self.groupBox.setTitle(_translate("Dialog", "Удалить препарат из базы"))
        self.pushButton_2.setText(_translate("Dialog", "Удалить"))
        self.pushButton_3.setText(_translate("Dialog", " Закрыть окно "))

