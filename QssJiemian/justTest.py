# coding = utf-8
import sys
from PyQt5 import Qt,QtWidgets,QtCore,QtGui
# from widget import Ui_frmMain;

import sys

def test(can):
    print("test")

    print(can)

def test2(can):
    print("test2")
    print(can.text(1))
    print(can)
_translate = QtCore.QCoreApplication.translate
app= QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget();
widget.resize(663, 543)
layout = QtWidgets.QHBoxLayout(widget);
treeWidget = QtWidgets.QTreeWidget(widget)
treeWidget.setObjectName("treeWidget")
item_0 = QtWidgets.QTreeWidgetItem(treeWidget)
item_0 = QtWidgets.QTreeWidgetItem(treeWidget)
item_0 = QtWidgets.QTreeWidgetItem(treeWidget)
treeWidget.headerItem().setText(0, _translate("widget", "学号"))
treeWidget.headerItem().setText(1, _translate("widget", "成绩"))
__sortingEnabled = treeWidget.isSortingEnabled()
treeWidget.setSortingEnabled(False)
treeWidget.topLevelItem(0).setText(0, _translate("widget", "061104023"))
treeWidget.topLevelItem(0).setText(1, _translate("widget", "105"))
treeWidget.topLevelItem(1).setText(0, _translate("widget", "061104056"))
treeWidget.topLevelItem(1).setText(1, _translate("widget", "245"))
treeWidget.topLevelItem(2).setText(0, _translate("widget", "061104065"))
treeWidget.topLevelItem(2).setText(1, _translate("widget", "265"))
treeWidget.setSortingEnabled(__sortingEnabled)
layout.addWidget(treeWidget)
treeWidget.clicked.connect(test);
treeWidget.itemClicked.connect(test2)
qss = QtCore.QFile("test.qss")
qss.open(QtCore.QFile.ReadOnly)
app.setStyleSheet(str(qss.readAll(),"utf-8"))

widget.show();

app.exec_()