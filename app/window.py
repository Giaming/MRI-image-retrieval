# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 960)
        Form.setMaximumSize(QtCore.QSize(1200, 960))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        Form.setFont(font)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_left = QtWidgets.QFrame(Form)
        self.frame_left.setGeometry(QtCore.QRect(0, 0, 240, 960))
        self.frame_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left.setObjectName("frame_left")
        self.frame_query = QtWidgets.QFrame(self.frame_left)
        self.frame_query.setGeometry(QtCore.QRect(0, 200, 240, 240))
        self.frame_query.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_query.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_query.setObjectName("frame_query")
        self.label_query = QtWidgets.QLabel(self.frame_query)
        self.label_query.setGeometry(QtCore.QRect(8, 8, 224, 224))
        self.label_query.setText("")
        self.label_query.setObjectName("label_query")
        self.load_image_btn = QtWidgets.QPushButton(self.frame_left)
        self.load_image_btn.setGeometry(QtCore.QRect(50, 560, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.load_image_btn.setFont(font)
        self.load_image_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.load_image_btn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.load_image_btn.setAutoDefault(False)
        self.load_image_btn.setDefault(False)
        self.load_image_btn.setFlat(False)
        self.load_image_btn.setObjectName("load_image_btn")
        self.retrieval_btn = QtWidgets.QPushButton(self.frame_left)
        self.retrieval_btn.setGeometry(QtCore.QRect(50, 680, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.retrieval_btn.setFont(font)
        self.retrieval_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.retrieval_btn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.retrieval_btn.setObjectName("retrieval_btn")
        self.line = QtWidgets.QFrame(self.frame_left)
        self.line.setGeometry(QtCore.QRect(235, 0, 5, 960))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.plot_btn = QtWidgets.QPushButton(self.frame_left)
        self.plot_btn.setGeometry(QtCore.QRect(50, 800, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.plot_btn.setFont(font)
        self.plot_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plot_btn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.plot_btn.setObjectName("plot_btn")
        self.label = QtWidgets.QLabel(self.frame_left)
        self.label.setGeometry(QtCore.QRect(10, 30, 211, 121))
        self.label.setObjectName("label")
        self.frame_right = QtWidgets.QFrame(Form)
        self.frame_right.setGeometry(QtCore.QRect(240, 0, 960, 960))
        self.frame_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_right.setObjectName("frame_right")
        self.frame_result1 = QtWidgets.QFrame(self.frame_right)
        self.frame_result1.setGeometry(QtCore.QRect(0, 0, 240, 240))
        self.frame_result1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result1.setObjectName("frame_result1")
        self.label_res1 = QtWidgets.QLabel(self.frame_result1)
        self.label_res1.setGeometry(QtCore.QRect(15, 0, 210, 210))
        self.label_res1.setText("")
        self.label_res1.setObjectName("label_res1")
        self.label1 = QtWidgets.QLabel(self.frame_result1)
        self.label1.setGeometry(QtCore.QRect(15, 212, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label1.setFont(font)
        self.label1.setText("")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.frame_result2 = QtWidgets.QFrame(self.frame_right)
        self.frame_result2.setGeometry(QtCore.QRect(240, 0, 240, 240))
        self.frame_result2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result2.setObjectName("frame_result2")
        self.label_res2 = QtWidgets.QLabel(self.frame_result2)
        self.label_res2.setGeometry(QtCore.QRect(15, 0, 210, 210))
        self.label_res2.setText("")
        self.label_res2.setObjectName("label_res2")
        self.label2 = QtWidgets.QLabel(self.frame_result2)
        self.label2.setGeometry(QtCore.QRect(15, 212, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label2.setFont(font)
        self.label2.setText("")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.frame_result3 = QtWidgets.QFrame(self.frame_right)
        self.frame_result3.setGeometry(QtCore.QRect(480, 0, 240, 240))
        self.frame_result3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result3.setObjectName("frame_result3")
        self.label_res3 = QtWidgets.QLabel(self.frame_result3)
        self.label_res3.setGeometry(QtCore.QRect(15, 0, 210, 210))
        self.label_res3.setText("")
        self.label_res3.setObjectName("label_res3")
        self.label3 = QtWidgets.QLabel(self.frame_result3)
        self.label3.setGeometry(QtCore.QRect(15, 212, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label3.setFont(font)
        self.label3.setText("")
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.frame_result4 = QtWidgets.QFrame(self.frame_right)
        self.frame_result4.setGeometry(QtCore.QRect(720, 0, 240, 240))
        self.frame_result4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result4.setObjectName("frame_result4")
        self.label_res4 = QtWidgets.QLabel(self.frame_result4)
        self.label_res4.setGeometry(QtCore.QRect(15, 0, 210, 210))
        self.label_res4.setText("")
        self.label_res4.setObjectName("label_res4")
        self.label4 = QtWidgets.QLabel(self.frame_result4)
        self.label4.setGeometry(QtCore.QRect(15, 212, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label4.setFont(font)
        self.label4.setText("")
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setObjectName("label4")
        self.frame_result8 = QtWidgets.QFrame(self.frame_right)
        self.frame_result8.setGeometry(QtCore.QRect(720, 240, 240, 240))
        self.frame_result8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result8.setObjectName("frame_result8")
        self.label_res8 = QtWidgets.QLabel(self.frame_result8)
        self.label_res8.setGeometry(QtCore.QRect(15, 0, 210, 210))
        self.label_res8.setText("")
        self.label_res8.setObjectName("label_res8")
        self.label8 = QtWidgets.QLabel(self.frame_result8)
        self.label8.setGeometry(QtCore.QRect(15, 212, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label8.setFont(font)
        self.label8.setText("")
        self.label8.setAlignment(QtCore.Qt.AlignCenter)
        self.label8.setObjectName("label8")
        self.frame_result5 = QtWidgets.QFrame(self.frame_right)
        self.frame_result5.setGeometry(QtCore.QRect(0, 240, 240, 240))
        self.frame_result5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result5.setObjectName("frame_result5")
        self.label_res5 = QtWidgets.QLabel(self.frame_result5)
        self.label_res5.setGeometry(QtCore.QRect(15, 0, 210, 210))
        self.label_res5.setText("")
        self.label_res5.setObjectName("label_res5")
        self.label5 = QtWidgets.QLabel(self.frame_result5)
        self.label5.setGeometry(QtCore.QRect(15, 212, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label5.setFont(font)
        self.label5.setText("")
        self.label5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5.setObjectName("label5")
        self.frame_result6 = QtWidgets.QFrame(self.frame_right)
        self.frame_result6.setGeometry(QtCore.QRect(240, 240, 240, 240))
        self.frame_result6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result6.setObjectName("frame_result6")
        self.label_res6 = QtWidgets.QLabel(self.frame_result6)
        self.label_res6.setGeometry(QtCore.QRect(15, 0, 210, 210))
        self.label_res6.setText("")
        self.label_res6.setObjectName("label_res6")
        self.label6 = QtWidgets.QLabel(self.frame_result6)
        self.label6.setGeometry(QtCore.QRect(15, 212, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label6.setFont(font)
        self.label6.setText("")
        self.label6.setAlignment(QtCore.Qt.AlignCenter)
        self.label6.setObjectName("label6")
        self.frame_result7 = QtWidgets.QFrame(self.frame_right)
        self.frame_result7.setGeometry(QtCore.QRect(480, 240, 240, 240))
        self.frame_result7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result7.setObjectName("frame_result7")
        self.label_res7 = QtWidgets.QLabel(self.frame_result7)
        self.label_res7.setGeometry(QtCore.QRect(15, 0, 210, 210))
        self.label_res7.setText("")
        self.label_res7.setObjectName("label_res7")
        self.label7 = QtWidgets.QLabel(self.frame_result7)
        self.label7.setGeometry(QtCore.QRect(15, 212, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label7.setFont(font)
        self.label7.setText("")
        self.label7.setAlignment(QtCore.Qt.AlignCenter)
        self.label7.setObjectName("label7")
        self.frame_result12 = QtWidgets.QFrame(self.frame_right)
        self.frame_result12.setGeometry(QtCore.QRect(720, 480, 240, 240))
        self.frame_result12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result12.setObjectName("frame_result12")
        self.label_res12 = QtWidgets.QLabel(self.frame_result12)
        self.label_res12.setGeometry(QtCore.QRect(15, 0, 210, 210))
        self.label_res12.setText("")
        self.label_res12.setObjectName("label_res12")
        self.label12 = QtWidgets.QLabel(self.frame_result12)
        self.label12.setGeometry(QtCore.QRect(15, 212, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label12.setFont(font)
        self.label12.setText("")
        self.label12.setAlignment(QtCore.Qt.AlignCenter)
        self.label12.setObjectName("label12")
        self.frame_result9 = QtWidgets.QFrame(self.frame_right)
        self.frame_result9.setGeometry(QtCore.QRect(0, 480, 240, 240))
        self.frame_result9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result9.setObjectName("frame_result9")
        self.label_res9 = QtWidgets.QLabel(self.frame_result9)
        self.label_res9.setGeometry(QtCore.QRect(15, 0, 210, 210))
        self.label_res9.setText("")
        self.label_res9.setObjectName("label_res9")
        self.label9 = QtWidgets.QLabel(self.frame_result9)
        self.label9.setGeometry(QtCore.QRect(15, 212, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label9.setFont(font)
        self.label9.setText("")
        self.label9.setAlignment(QtCore.Qt.AlignCenter)
        self.label9.setObjectName("label9")
        self.frame_result11 = QtWidgets.QFrame(self.frame_right)
        self.frame_result11.setGeometry(QtCore.QRect(480, 480, 240, 240))
        self.frame_result11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result11.setObjectName("frame_result11")
        self.label_res11 = QtWidgets.QLabel(self.frame_result11)
        self.label_res11.setGeometry(QtCore.QRect(15, 0, 210, 210))
        self.label_res11.setText("")
        self.label_res11.setObjectName("label_res11")
        self.label11 = QtWidgets.QLabel(self.frame_result11)
        self.label11.setGeometry(QtCore.QRect(15, 212, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label11.setFont(font)
        self.label11.setText("")
        self.label11.setAlignment(QtCore.Qt.AlignCenter)
        self.label11.setObjectName("label11")
        self.frame_result10 = QtWidgets.QFrame(self.frame_right)
        self.frame_result10.setGeometry(QtCore.QRect(240, 480, 240, 240))
        self.frame_result10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result10.setObjectName("frame_result10")
        self.label_res10 = QtWidgets.QLabel(self.frame_result10)
        self.label_res10.setGeometry(QtCore.QRect(15, 0, 210, 210))
        self.label_res10.setText("")
        self.label_res10.setObjectName("label_res10")
        self.label10 = QtWidgets.QLabel(self.frame_result10)
        self.label10.setGeometry(QtCore.QRect(15, 212, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label10.setFont(font)
        self.label10.setText("")
        self.label10.setAlignment(QtCore.Qt.AlignCenter)
        self.label10.setObjectName("label10")
        self.frame_result16 = QtWidgets.QFrame(self.frame_right)
        self.frame_result16.setGeometry(QtCore.QRect(720, 720, 240, 240))
        self.frame_result16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result16.setObjectName("frame_result16")
        self.label_res16 = QtWidgets.QLabel(self.frame_result16)
        self.label_res16.setGeometry(QtCore.QRect(15, 0, 210, 210))
        self.label_res16.setText("")
        self.label_res16.setObjectName("label_res16")
        self.label16 = QtWidgets.QLabel(self.frame_result16)
        self.label16.setGeometry(QtCore.QRect(15, 212, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label16.setFont(font)
        self.label16.setText("")
        self.label16.setAlignment(QtCore.Qt.AlignCenter)
        self.label16.setObjectName("label16")
        self.frame_result15 = QtWidgets.QFrame(self.frame_right)
        self.frame_result15.setGeometry(QtCore.QRect(480, 720, 240, 240))
        self.frame_result15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result15.setObjectName("frame_result15")
        self.label_res15 = QtWidgets.QLabel(self.frame_result15)
        self.label_res15.setGeometry(QtCore.QRect(15, 0, 210, 210))
        self.label_res15.setText("")
        self.label_res15.setObjectName("label_res15")
        self.label15 = QtWidgets.QLabel(self.frame_result15)
        self.label15.setGeometry(QtCore.QRect(15, 212, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label15.setFont(font)
        self.label15.setText("")
        self.label15.setAlignment(QtCore.Qt.AlignCenter)
        self.label15.setObjectName("label15")
        self.frame_result13 = QtWidgets.QFrame(self.frame_right)
        self.frame_result13.setGeometry(QtCore.QRect(0, 720, 240, 240))
        self.frame_result13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result13.setObjectName("frame_result13")
        self.label_res13 = QtWidgets.QLabel(self.frame_result13)
        self.label_res13.setGeometry(QtCore.QRect(15, 0, 210, 210))
        self.label_res13.setText("")
        self.label_res13.setObjectName("label_res13")
        self.label13 = QtWidgets.QLabel(self.frame_result13)
        self.label13.setGeometry(QtCore.QRect(15, 212, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label13.setFont(font)
        self.label13.setText("")
        self.label13.setAlignment(QtCore.Qt.AlignCenter)
        self.label13.setObjectName("label13")
        self.frame_result14 = QtWidgets.QFrame(self.frame_right)
        self.frame_result14.setGeometry(QtCore.QRect(240, 720, 240, 240))
        self.frame_result14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_result14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_result14.setObjectName("frame_result14")
        self.label_res14 = QtWidgets.QLabel(self.frame_result14)
        self.label_res14.setGeometry(QtCore.QRect(15, 0, 210, 210))
        self.label_res14.setText("")
        self.label_res14.setObjectName("label_res14")
        self.label14 = QtWidgets.QLabel(self.frame_result14)
        self.label14.setGeometry(QtCore.QRect(15, 212, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label14.setFont(font)
        self.label14.setText("")
        self.label14.setAlignment(QtCore.Qt.AlignCenter)
        self.label14.setObjectName("label14")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.load_image_btn.setText(_translate("Form", "载入图片"))
        self.retrieval_btn.setText(_translate("Form", "检索"))
        self.plot_btn.setText(_translate("Form", "画图"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Tutorial：</span></p><p>step1: 点击载入图片</p><p>step2: 点击检索</p><p><br/></p><p align=\"center\"><br/></p></body></html>"))
        Form.setWindowTitle("图像检索：基于vgg16的方法")
        Form.setWindowIcon(QIcon('logo.png'))
