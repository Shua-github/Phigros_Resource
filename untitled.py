# -*- coding: utf-8 -*-
import configparser
import os

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
def a(b):
    return str(b).lower()

class Ui_Form(object):
    def setupUi(self, Form):
        self.cwd = os.getcwd()
        Form.setObjectName("Form")
        Form.resize(437, 345)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.checkBox.setTabletTracking(False)
        self.checkBox.setAcceptDrops(False)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 50, 71, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 70, 101, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 90, 101, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(Form)
        self.checkBox_6.setGeometry(QtCore.QRect(20, 110, 71, 16))
        self.checkBox_6.setObjectName("checkBox_6")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(70, 140, 281, 21))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(350, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 180, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 140, 54, 21))
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 180, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def slot_btn_chooseFile(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,"选取文件",self.cwd,"Apk Files (*.apk)")
        self.textEdit.setText(fileName_choose)
    def extract_apk_file(self):
        self.checkboxstate()
        os.system('python gameInformation.py {}'.format(self.textEdit.toPlainText()))
        os.system('python resource.py {}'.format(self.textEdit.toPlainText()))
    def build_pez_file(self):
        os.system('python phira.py')
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.checkBox.setText(_translate("Form", "头像"))
        self.checkBox_2.setText(_translate("Form", "铺面"))
        self.checkBox_3.setText(_translate("Form", "曲绘"))
        self.checkBox_4.setText(_translate("Form", "曲绘（模糊）"))
        self.checkBox_5.setText(_translate("Form", "曲绘（低质量）"))
        self.checkBox_6.setText(_translate("Form", "音乐"))
        self.pushButton.setText(_translate("Form", "浏览"))
        self.pushButton_2.setText(_translate("Form", "提取"))
        self.label.setText(_translate("Form", "apk路径"))
        self.pushButton_3.setText(_translate("Form", "生成自制铺"))
        self.pushButton_2.clicked.connect(self.extract_apk_file)
        self.pushButton.clicked.connect(self.slot_btn_chooseFile)
        self.pushButton_3.clicked.connect(self.build_pez_file)
    def checkboxstate(self):
        chkl = []
        chk1Status = a(bool(self.checkBox.isChecked()))
        chkl.append(chk1Status)
        chk2Status = a(bool(self.checkBox_2.isChecked()))
        chkl.append(chk2Status)
        chk3Status = a(bool(self.checkBox_3.isChecked()))
        chkl.append(chk3Status)
        chk4Status = a(bool(self.checkBox_4.isChecked()))
        chkl.append(chk4Status)
        chk5Status = a(bool(self.checkBox_5.isChecked()))
        chkl.append(chk5Status)
        chk6Status = a(bool(self.checkBox_6.isChecked()))
        chkl.append(chk6Status)
        config = configparser.ConfigParser()
        config.read('config.ini',encoding='utf-8')
        config.set('TYPES', 'avatar', chkl[0])
        config.set('TYPES', 'Chart', chkl[1])
        config.set('TYPES', 'IllustrationBlur', chkl[2])
        config.set('TYPES', 'IllustrationLowRes', chkl[3])
        config.set('TYPES', 'Illustration', chkl[4])
        config.set('TYPES', 'music', chkl[5])
        with open('config.ini', 'w', encoding='utf-8') as f:
            config.write(f)