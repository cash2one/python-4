# coding = utf-8
from PyQt5 import QtWidgets,QtCore
# from widget import Ui_frmMain;

import sys

def test(can):
    print("test")
    print(can)

def test2(can):
    print("test2")
    # 得到里面的值
    print(can.text(1))
    print(can)
_translate = QtCore.QCoreApplication.translate
app= QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget();
widget.resize(663, 543)
layout = QtWidgets.QHBoxLayout(widget);
treeWidget = QtWidgets.QTreeWidget(widget)
treeWidget.setColumnCount(2)
treeWidget.setObjectName("treeWidget")
# 这个代表插入三行
# 有下面俩种方式
# item_0 = QtWidgets.QTreeWidgetItem(treeWidget)
# item_0 = QtWidgets.QTreeWidgetItem(treeWidget)
# item_0 = QtWidgets.QTreeWidgetItem(treeWidget)
for i in range(3):
    item_0 = QtWidgets.QTreeWidgetItem(treeWidget)
    item_2 = QtWidgets.QTreeWidgetItem(item_0);
    item_2.setText(0,"ceshi");
    item_2.setText(1,"desc")
    item_0.addChild(item_2);
    item_3 = QtWidgets.QTreeWidgetItem(item_0);
    item_3.setText(0,"ceshi");
    item_3.setText(1,"desc")
    item_0.addChild(item_3);
    treeWidget.addTopLevelItem(item_0)
    # treeWidget.setHeaderItem(item_0)
treeWidget.headerItem().setText(0, _translate("widget", "学号"))
treeWidget.headerItem().setText(1, _translate("widget", "成绩"))
# __sortingEnabled = treeWidget.isSortingEnabled()
# treeWidget.setSortingEnabled(False)
treeWidget.topLevelItem(0).setText(0, _translate("widget", "061104023"))
treeWidget.topLevelItem(0).setText(1, _translate("widget", "105"))
treeWidget.topLevelItem(1).setText(0, _translate("widget", "061104056"))
treeWidget.topLevelItem(1).setText(1, _translate("widget", "245"))
treeWidget.topLevelItem(2).setText(0, _translate("widget", "061104065"))
treeWidget.topLevelItem(2).setText(1, _translate("widget", "265"))
# treeWidget.setSortingEnabled(__sortingEnabled)

layout.addWidget(treeWidget)
treeWidget.clicked.connect(test);
treeWidget.itemClicked.connect(test2)

qss = QtCore.QFile("test.qss")
qss.open(QtCore.QFile.ReadOnly)
app.setStyleSheet(str(qss.readAll(),"utf-8"))

widget.show();

app.exec_()