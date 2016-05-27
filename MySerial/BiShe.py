# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmmain.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmMain(object):
    def setupUi(self, frmMain):
        frmMain.setObjectName("frmMain")
        frmMain.resize(663, 543)


        # frmMain.setSizeGripEnabled(True)
        # 是整个页面的整体布局
        self.verticalLayout = QtWidgets.QVBoxLayout(frmMain)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        # 用来放置最上面menu的控件
        self.widget_title = QtWidgets.QWidget(frmMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        print(self.widget_title.sizePolicy().hasHeightForWidth())
        # sizePolicy.setHeightForWidth(True)
        # sizePolicy.setWidthForHeight(True)
        self.widget_title.setSizePolicy(sizePolicy)
        self.widget_title.setMinimumSize(QtCore.QSize(100, 28))
        self.widget_title.setObjectName("widget_title")

        # 用来布局menu 里的控件
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_title)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # 放置图标
        self.lab_Ico = QtWidgets.QLabel(self.widget_title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_Ico.sizePolicy().hasHeightForWidth())
        self.lab_Ico.setSizePolicy(sizePolicy)
        self.lab_Ico.setMinimumSize(QtCore.QSize(30, 0))
        self.lab_Ico.setText("")
        self.lab_Ico.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_Ico.setObjectName("lab_Ico")
        self.horizontalLayout_2.addWidget(self.lab_Ico)


        # lab_Title 自定义UI演示(作者:jacky QQ:1193610322)
        self.lab_Title = QtWidgets.QLabel(self.widget_title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_Title.sizePolicy().hasHeightForWidth())
        self.lab_Title.setSizePolicy(sizePolicy)
        self.lab_Title.setStyleSheet("")
        self.lab_Title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_Title.setObjectName("lab_Title")

        self.horizontalLayout_2.addWidget(self.lab_Title)


        # 用来放置图标的控件
        self.widget_menu = QtWidgets.QWidget(self.widget_title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_menu.sizePolicy().hasHeightForWidth())
        self.widget_menu.setSizePolicy(sizePolicy)
        self.widget_menu.setObjectName("widget_menu")

        # 因为图标要放置最小化 最大化 关闭 所以用了一个水平布局
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_menu)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # btnMenu_Min lab_Title
        self.btnMenu_Min = QtWidgets.QPushButton(self.widget_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMenu_Min.sizePolicy().hasHeightForWidth())
        self.btnMenu_Min.setSizePolicy(sizePolicy)
        self.btnMenu_Min.setMinimumSize(QtCore.QSize(40, 0))
        self.btnMenu_Min.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnMenu_Min.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnMenu_Min.setText("")
        self.btnMenu_Min.setFlat(True)
        self.btnMenu_Min.setObjectName("btnMenu_Min")
        self.horizontalLayout.addWidget(self.btnMenu_Min)

        # 最大化按钮
        self.btnMenu_Max = QtWidgets.QPushButton(self.widget_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMenu_Max.sizePolicy().hasHeightForWidth())
        self.btnMenu_Max.setSizePolicy(sizePolicy)
        self.btnMenu_Max.setMinimumSize(QtCore.QSize(40, 0))
        self.btnMenu_Max.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnMenu_Max.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnMenu_Max.setText("")
        self.btnMenu_Max.setFlat(True)
        self.btnMenu_Max.setObjectName("btnMenu_Max")
        self.horizontalLayout.addWidget(self.btnMenu_Max)

        # 关闭按钮
        self.btnMenu_Close = QtWidgets.QPushButton(self.widget_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMenu_Close.sizePolicy().hasHeightForWidth())
        self.btnMenu_Close.setSizePolicy(sizePolicy)
        self.btnMenu_Close.setMinimumSize(QtCore.QSize(40, 0))
        self.btnMenu_Close.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnMenu_Close.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnMenu_Close.setText("")
        self.btnMenu_Close.setFlat(True)
        self.btnMenu_Close.setObjectName("btnMenu_Close")
        self.horizontalLayout.addWidget(self.btnMenu_Close)

        # 把最小化 最大化 关闭 所在的布局放进horizontalLayout_2
        self.horizontalLayout_2.addWidget(self.widget_menu)
        self.verticalLayout.addWidget(self.widget_title)


        self.widget_main = QtWidgets.QWidget(frmMain)
        self.widget_main.setStyleSheet("")
        self.widget_main.setObjectName("widget_main")

        # 整个内容布局的最高层
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_main)
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")


        self.groupBox_3 = QtWidgets.QGroupBox(self.widget_main)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)


        self.cboxStyle = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboxStyle.sizePolicy().hasHeightForWidth())
        self.cboxStyle.setSizePolicy(sizePolicy)
        self.cboxStyle.setObjectName("cboxStyle")
        # for i in range(10):
        #     self.cboxStyle.addItem("COM"+str(i));
        self.horizontalLayout_6.addWidget(self.cboxStyle)

        self.label2 = QtWidgets.QLabel(self.groupBox_3)
        self.label2.setObjectName("label2")
        self.horizontalLayout_6.addWidget(self.label2)


        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("115200")
        self.comboBox.addItem("9600")
        self.comboBox.addItem("200")
        self.horizontalLayout_6.addWidget(self.comboBox)

        # self.spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        # self.spinBox.setObjectName("spinBox")
        # self.horizontalLayout_6.addWidget(self.spinBox)


        self.btnChangeStyle = QtWidgets.QPushButton(self.groupBox_3)
        self.btnChangeStyle.setMinimumSize(QtCore.QSize(90, 0))
        self.btnChangeStyle.setObjectName("btnChangeStyle")
        self.horizontalLayout_6.addWidget(self.btnChangeStyle)


        self.verticalLayout_9.addWidget(self.groupBox_3)

        # 下面是第三部分
        self.tabWidget = QtWidgets.QTabWidget(self.widget_main)
        self.tabWidget.setObjectName("tabWidget")

        #第六个标签开始
        # 第五个标签开始
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")

        # # 第五个标签里面的布局
        # self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_5)
        # self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        # self.verticalLayout_7.setSpacing(6)
        # self.verticalLayout_7.setObjectName("verticalLayout_7")
        #
        #
        # self.textBrowser = QtWidgets.QTextBrowser(self.tab_5)
        # self.textBrowser.setObjectName("textBrowser")
        #
        #
        # self.verticalLayout_7.addWidget(self.textBrowser)
        # self.tabWidget.addTab(self.tab_5, "")

        # 第四个标签开始
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")

        # 第四个标签里面的布局
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        # 第四个标签里面的控件
        self.textEdit = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit.setObjectName("textEdit")

        self.verticalLayout_6.addWidget(self.textEdit)
        self.tabWidget.addTab(self.tab_4, "")
        # 第四个标签结束

        # 将整个6个标签加入布局
        self.verticalLayout_9.addWidget(self.tabWidget)

        # 将整个内容布局的部分加入到这个verticalLayout布局
        self.verticalLayout.addWidget(self.widget_main)
        self.retranslateUi(frmMain)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmMain)

    def retranslateUi(self, frmMain):
        _translate = QtCore.QCoreApplication.translate
        self.lab_Title.setText(_translate("frmMain", "(作者:jacky QQ:1193610322)"))
        self.btnMenu_Min.setToolTip(_translate("frmMain", "最小化111"))
        self.btnMenu_Max.setToolTip(_translate("frmMain", "最大化"))
        self.btnMenu_Close.setToolTip(_translate("frmMain", "关闭"))
        self.label.setText(_translate("frmMain", "串口"))
        self.label2.setText(_translate("frmMain", "波特率"))
        self.btnChangeStyle.setText(_translate("frmMain", "open"))

        # self.plainTextEdit.setPlainText('');
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("frmMain", 'data'))

