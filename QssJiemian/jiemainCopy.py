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
        sizePolicy.setHeightForWidth(self.widget_title.sizePolicy().hasHeightForWidth())
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

        # lab_Title 自定义UI演示(作者:刘典武 QQ:517216493)
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
        self.horizontalLayout_6.addWidget(self.cboxStyle)


        self.spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_6.addWidget(self.spinBox)


        self.btnChangeStyle = QtWidgets.QPushButton(self.groupBox_3)
        self.btnChangeStyle.setMinimumSize(QtCore.QSize(90, 0))
        self.btnChangeStyle.setObjectName("btnChangeStyle")
        self.horizontalLayout_6.addWidget(self.btnChangeStyle)


        self.verticalLayout_9.addWidget(self.groupBox_3)


        # 中间的groupBox
        self.groupBox = QtWidgets.QGroupBox(self.widget_main)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        # 对中间的groupBox 设置布局
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")


        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # 今天天气不错的那个控件
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        # 消息框
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMinimumSize(QtCore.QSize(90, 0))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)

        # 询问框
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setMinimumSize(QtCore.QSize(90, 0))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)

        # 错误框
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setMinimumSize(QtCore.QSize(90, 0))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)

        # 输入框
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setMinimumSize(QtCore.QSize(90, 0))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        # 消息框按钮下面还有一个水平布局  horizontalLayout_5
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        # 男
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")

        self.horizontalLayout_5.addWidget(self.radioButton)

        # 女
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")

        self.horizontalLayout_5.addWidget(self.radioButton_2)

        # 中国
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_5.addWidget(self.checkBox)

        # 美国
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_5.addWidget(self.checkBox_2)

        # 测试项目1
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox)

        # 时间编辑
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox)
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout_5.addWidget(self.timeEdit)

        # 不可用按钮
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(90, 0))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_5.addWidget(self.pushButton_4)

        # 将这个水平按钮 中间的垂直布局中
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        # 接着中间垂直布局的 第三个水平布局
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        # 第一个时间编辑
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_7.addWidget(self.dateEdit)

        # 第二个时间编辑
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.horizontalLayout_7.addWidget(self.dateTimeEdit_2)

        # 有日历显示下来的第一个时间编辑
        self.dateEdit_2 = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_7.addWidget(self.dateEdit_2)

        # 有日历显示下来的第二个时间编辑
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_7.addWidget(self.dateTimeEdit)

        # 将这个水平布局加入到垂直布局
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        # 进度条
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 20))
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setObjectName("progressBar")

        # 将进度条加入到中间的垂直布局中
        self.verticalLayout_2.addWidget(self.progressBar)


        self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        # 将其加入中间的垂直布局中
        self.verticalLayout_2.addWidget(self.horizontalSlider)


        # 滚动条
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.groupBox)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")

        # 将其加入中间的垂直布局中
        self.verticalLayout_2.addWidget(self.horizontalScrollBar)

        # 将中间的一整个大的groupBox 加入垂直布局中
        self.verticalLayout_9.addWidget(self.groupBox)

        # *******************************************************
        # 中间的部分到此结束

        # 下面是第三部分
        self.tabWidget = QtWidgets.QTabWidget(self.widget_main)
        self.tabWidget.setObjectName("tabWidget")


        # tab1 页面 也就是选项一
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        # 选项一标签里面的布局
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # 那个有学号 和成绩的布局
        self.treeWidget = QtWidgets.QTreeWidget(self.tab)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)


        self.verticalLayout_3.addWidget(self.treeWidget)
        self.tabWidget.addTab(self.tab, "")
        #第一个tab 到此结束了


        # 定义第二个tab
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        # 第二个tab 的布局
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # 第二个tab布局里面的table 表
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)


        self.verticalLayout_4.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tab_2, "")
        # 第二个tab 到此结束了

        # 第三个tab开始
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        # 第三个tab里面的布局
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        # 第三个布局里面的widget
        self.toolBox = QtWidgets.QToolBox(self.tab_3)
        self.toolBox.setObjectName("toolBox")

        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page.setObjectName("page")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 66, 16))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")


        self.verticalLayout_5.addWidget(self.toolBox)
        self.tabWidget.addTab(self.tab_3, "")
        # 第三个tab 到此结束了


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


        # 第五个标签开始
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")

        # 第五个标签里面的布局
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")


        self.textBrowser = QtWidgets.QTextBrowser(self.tab_5)
        self.textBrowser.setObjectName("textBrowser")


        self.verticalLayout_7.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.tab_5, "")
        # 第五个标签结束


        #第六个标签开始
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")

        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.frame = QtWidgets.QFrame(self.tab_6)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_3.addWidget(self.plainTextEdit)
        self.verticalLayout_8.addWidget(self.frame)
        self.tabWidget.addTab(self.tab_6, "")
        # 第六个标签到此结束

        # 将整个6个标签加入布局
        self.verticalLayout_9.addWidget(self.tabWidget)



        # 将整个内容布局的部分加入到这个verticalLayout布局
        self.verticalLayout.addWidget(self.widget_main)

        self.retranslateUi(frmMain)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(frmMain)

    def retranslateUi(self, frmMain):
        _translate = QtCore.QCoreApplication.translate
        self.lab_Title.setText(_translate("frmMain", "自定义UI演示(作者:刘典武 QQ:517216493)"))
        self.btnMenu_Min.setToolTip(_translate("frmMain", "最小化111"))
        self.btnMenu_Max.setToolTip(_translate("frmMain", "最大化"))
        self.btnMenu_Close.setToolTip(_translate("frmMain", "关闭"))
        self.label.setText(_translate("frmMain", "风格样式"))
        self.btnChangeStyle.setText(_translate("frmMain", "主窗体"))
        self.lineEdit.setText(_translate("frmMain", "今天天气不错"))
        self.pushButton.setText(_translate("frmMain", "信息框"))
        self.pushButton_2.setText(_translate("frmMain", "询问框"))
        self.pushButton_3.setText(_translate("frmMain", "错误框"))
        self.pushButton_5.setText(_translate("frmMain", "输入框"))
        self.radioButton.setText(_translate("frmMain", "男"))
        self.radioButton_2.setText(_translate("frmMain", "女"))
        self.checkBox.setText(_translate("frmMain", "中国"))
        self.checkBox_2.setText(_translate("frmMain", "美国"))
        self.comboBox.setItemText(0, _translate("frmMain", "测试项目1"))
        self.comboBox.setItemText(1, _translate("frmMain", "测试项目2"))
        self.comboBox.setItemText(2, _translate("frmMain", "测试项目3"))
        self.pushButton_4.setText(_translate("frmMain", "不可用按钮"))
        self.treeWidget.headerItem().setText(0, _translate("frmMain", "学号"))
        self.treeWidget.headerItem().setText(1, _translate("frmMain", "成绩"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("frmMain", "061104023"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("frmMain", "105"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("frmMain", "061104056"))
        self.treeWidget.topLevelItem(1).setText(1, _translate("frmMain", "245"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("frmMain", "061104065"))
        self.treeWidget.topLevelItem(2).setText(1, _translate("frmMain", "265"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmMain", "选项卡1"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("frmMain", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("frmMain", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("frmMain", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("frmMain", "学号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("frmMain", "成绩"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("frmMain", "061104023"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("frmMain", "105"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("frmMain", "061104025"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("frmMain", "108"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("frmMain", "061104056"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("frmMain", "235"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmMain", "选项卡2"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("frmMain", "学生信息管理"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("frmMain", "教师信息管理"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("frmMain", "选项卡3"))
        self.textEdit.setHtml(_translate("frmMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.假如你想要一件东西，就放它走。它若能回来找你，就永远属于你；它若不回来，那根本就不是你的。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.一个人会落泪，是因为痛；一个人之所以痛，是因为在乎；一个人之所以在乎，是因为有感觉；一个人之所以有感觉，仅因为你是一个人！所以，你有感觉，在乎，痛过，落泪了，说明你是完整不能再完整的一个人。难过的时候，原谅自己，只不过是一个人而已，没有必要把自己看的这么坚不可摧。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.如果真的有一天，某个回不来的人消失了，某个离不开的人离开了，也没关系。时间会把最正确的人带到你的身边，在此之前，你所要做的，是好好的照顾自己。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.你可以沉默不语，不管我的着急；你可以不回信息，不顾我的焦虑；你可以将我的关心，说成让你烦躁的原因；你可以把我的思念，丢在角落不屑一顾。你可以对着其他人微笑，你可以给别人拥抱，你可以对全世界好，却忘了我一直的伤心。------ 你不过是仗着我喜欢你，而那，却是唯一让我变得卑微的原因。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.生命中有一些人与我们擦肩了，却来不及遇见；遇见了，却来不及相识；相识了，却来不及熟悉；熟悉了，却还是要说再见。------ 对自己好点，因为一辈子不长；对身边的人好点，因为下辈子不一定能遇见。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6.0岁出场，10岁成长，20岁彷徨，30岁定向，40岁打拼，50岁回望，60岁告老，70岁搓麻，80岁晒太阳，90岁躺床上，100岁挂墙上。生的伟大，死的凄凉，能牵手的时候，请别肩并肩，能拥抱的时候，请别手牵手，能相爱的时候，请别说分开。一生就这么短暂而已。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7.时候，希望自己快点长大，长大了，却发现遗失了童年；单身时，开始羡慕恋人的甜蜜，恋爱时，怀念单身时的自由。——— 很多事物，没有得到时总觉得美好，得到之后才开始明白：“我们得到的同时也在失去。”</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8.面对， 不一定最难过。 孤独， 不一定不快乐。 得到， 不一定能长久。 失去， 不一定不再拥有。 不要因为寂寞而错爱， 不要因為错爱而寂寞一生。</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("frmMain", "选项卡4"))
        self.textBrowser.setHtml(_translate("frmMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.假如你想要一件东西，就放它走。它若能回来找你，就永远属于你；它若不回来，那根本就不是你的。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.一个人会落泪，是因为痛；一个人之所以痛，是因为在乎；一个人之所以在乎，是因为有感觉；一个人之所以有感觉，仅因为你是一个人！所以，你有感觉，在乎，痛过，落泪了，说明你是完整不能再完整的一个人。难过的时候，原谅自己，只不过是一个人而已，没有必要把自己看的这么坚不可摧。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.如果真的有一天，某个回不来的人消失了，某个离不开的人离开了，也没关系。时间会把最正确的人带到你的身边，在此之前，你所要做的，是好好的照顾自己。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.你可以沉默不语，不管我的着急；你可以不回信息，不顾我的焦虑；你可以将我的关心，说成让你烦躁的原因；你可以把我的思念，丢在角落不屑一顾。你可以对着其他人微笑，你可以给别人拥抱，你可以对全世界好，却忘了我一直的伤心。------ 你不过是仗着我喜欢你，而那，却是唯一让我变得卑微的原因。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.生命中有一些人与我们擦肩了，却来不及遇见；遇见了，却来不及相识；相识了，却来不及熟悉；熟悉了，却还是要说再见。------ 对自己好点，因为一辈子不长；对身边的人好点，因为下辈子不一定能遇见。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6.0岁出场，10岁成长，20岁彷徨，30岁定向，40岁打拼，50岁回望，60岁告老，70岁搓麻，80岁晒太阳，90岁躺床上，100岁挂墙上。生的伟大，死的凄凉，能牵手的时候，请别肩并肩，能拥抱的时候，请别手牵手，能相爱的时候，请别说分开。一生就这么短暂而已。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7.时候，希望自己快点长大，长大了，却发现遗失了童年；单身时，开始羡慕恋人的甜蜜，恋爱时，怀念单身时的自由。——— 很多事物，没有得到时总觉得美好，得到之后才开始明白：“我们得到的同时也在失去。”</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8.面对， 不一定最难过。 孤独， 不一定不快乐。 得到， 不一定能长久。 失去， 不一定不再拥有。 不要因为寂寞而错爱， 不要因為错爱而寂寞一生。</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("frmMain", "选项卡5"))
        self.plainTextEdit.setPlainText(_translate("frmMain", "1.假如你想要一件东西，就放它走。它若能回来找你，就永远属于你；它若不回来，那根本就不是你的。\n"
"2.一个人会落泪，是因为痛；一个人之所以痛，是因为在乎；一个人之所以在乎，是因为有感觉；一个人之所以有感觉，仅因为你是一个人！所以，你有感觉，在乎，痛过，落泪了，说明你是完整不能再完整的一个人。难过的时候，原谅自己，只不过是一个人而已，没有必要把自己看的这么坚不可摧。\n"
"3.如果真的有一天，某个回不来的人消失了，某个离不开的人离开了，也没关系。时间会把最正确的人带到你的身边，在此之前，你所要做的，是好好的照顾自己。\n"
"4.你可以沉默不语，不管我的着急；你可以不回信息，不顾我的焦虑；你可以将我的关心，说成让你烦躁的原因；你可以把我的思念，丢在角落不屑一顾。你可以对着其他人微笑，你可以给别人拥抱，你可以对全世界好，却忘了我一直的伤心。------ 你不过是仗着我喜欢你，而那，却是唯一让我变得卑微的原因。\n"
"5.生命中有一些人与我们擦肩了，却来不及遇见；遇见了，却来不及相识；相识了，却来不及熟悉；熟悉了，却还是要说再见。------ 对自己好点，因为一辈子不长；对身边的人好点，因为下辈子不一定能遇见。\n"
"6.0岁出场，10岁成长，20岁彷徨，30岁定向，40岁打拼，50岁回望，60岁告老，70岁搓麻，80岁晒太阳，90岁躺床上，100岁挂墙上。生的伟大，死的凄凉，能牵手的时候，请别肩并肩，能拥抱的时候，请别手牵手，能相爱的时候，请别说分开。一生就这么短暂而已。\n"
"7.时候，希望自己快点长大，长大了，却发现遗失了童年；单身时，开始羡慕恋人的甜蜜，恋爱时，怀念单身时的自由。——— 很多事物，没有得到时总觉得美好，得到之后才开始明白：“我们得到的同时也在失去。”\n"
"8.面对， 不一定最难过。 孤独， 不一定不快乐。 得到， 不一定能长久。 失去， 不一定不再拥有。 不要因为寂寞而错爱， 不要因為错爱而寂寞一生。"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("frmMain", "选项卡6"))

