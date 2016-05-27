# coding = utf-8
import sys
from PyQt5 import Qt,QtWidgets,QtCore,QtGui
# from widget import Ui_frmMain;

import sys

# 如果QtTreeWidget只有根元素 那么就像excel 表格一样了 相比QtTableWidget
# QtTreeWidget能够选择一行 QtTableWidget还没有找到选择一行的方法
class MyPyQtTreeWidget(QtWidgets.QTreeWidget):

    def __init__(self):
        super(MyPyQtTreeWidget,self).__init__();
        self.itemClicked.connect(self.myItemClicked)
        self.itemDoubleClicked.connect(self.myItemDoubleClicked)
        self.createRightActions()
        self.Alignment = 0x4|0x80;

    def setAlignment(self,int):
        self.Alignment = int;

    def getAlignment(self):
        return self.Alignment;

    def setHeaderHidden(self, bool):
        super(MyPyQtTreeWidget,self).setHeaderHidden(bool);

    def setHeaderContent(self,strList):
        column = self.columnCount();
        for i in range(column):
            if(i<=len(strList)-1):
                # self.headerItem().setTextAlignment(i,0x4|0x80);
                self.headerItem().setText(i,strList[i]);
            else:
                self.headerItem().setText(i,"");

    def setColumnCount(self, p_int):
        super(MyPyQtTreeWidget,self).setColumnCount(p_int);
        column = self.columnCount()
        for i in range(column):
            self.headerItem().setTextAlignment(i,self.Alignment);

    def getColumnCount(self):
        return super(MyPyQtTreeWidget, self).columnCount();

    def pushRoot(self,strList):
        root = QtWidgets.QTreeWidgetItem();

        column = self.columnCount();
        for i in range(column):
            # http://doc.qt.io/qt-5/qtreewidgetitem.html#setTextAlignment
            root.setTextAlignment(i,self.Alignment);
            if(i <= len(strList)-1):
                root.setText(i,strList[i]);
            else:
                root.setText(i,"");
        self.addTopLevelItem(root);
        return  root;

    def insertRoot(self,index,strList):
        root = QtWidgets.QTreeWidgetItem();
        column = self.columnCount();
        for i in range(column):
            root.setTextAlignment(i,self.Alignment);
            if(i <= len(strList)-1):

                root.setText(i,strList[i]);
            else:
                root.setText(i,"");
        # 如果index超过topLevelItemCount的最大数量 那么就插入到最后
        if index > self.topLevelItemCount():
            index = self.topLevelItemCount();
        self.insertTopLevelItem(index,root)
        return root;

    def pushChild(self,QTreeWidgetItem,strList):
        child = QtWidgets.QTreeWidgetItem();
        column = self.columnCount();
        for i in range(column):
            child.setTextAlignment(i,self.Alignment);
            if(i <= len(strList)-1):
                child.setText(i,strList[i]);
            else:
                child.setText(i,"");
        QTreeWidgetItem.addChild(child);
        return child;

    def insertChild(self,QTreeWidgetItem,index,strList):
        child = QtWidgets.QTreeWidgetItem();
        column = self.columnCount();
        for i in range(column):
            child.setTextAlignment(i,self.Alignment);
            if(i <= len(strList)-1):
                child.setText(i,strList[i]);
            else:
                child.setText(i,"");
        # 如果index超过childCount的最大数量 那么就插入到最后
        if QTreeWidgetItem.childCount()>index:
            index = QTreeWidgetItem.childCount();
        QTreeWidgetItem.insertChild(index,child);
        return child;

    # 返回指定的QTreeWidgetItem在同一级的index  这样insertChild 可以使用
    def getIndexOfItem(self,QTreeWidgetItem):
        return self.indexFromItem(QTreeWidgetItem).row();

    def deleteRootOrChild(self,QTreeWidgetItem):
        if 0 == QTreeWidgetItem.parent():
            QTreeWidgetItem.takeChildren();
            self.takeTopLevelItem(QTreeWidgetItem);
        else:
            QTreeWidgetItem.parent().removeChild(QTreeWidgetItem);

    def getCurrentItem(self):
        return super(MyPyQtTreeWidget,self).currentItem();

    def getAllQTreeWidgetText(self,whichQTreeeWidgetItem):
        column = self.columnCount();
        myList = [];
        for i in range(column):
            myList.append(whichQTreeeWidgetItem.text(i));
        return myList;

    def updateQTreeWidget(self,whichQTreeeWidgetItem,strList):
        column = self.columnCount();
        for i in range(column):
            if (i<=len(strList)-1):
                whichQTreeeWidgetItem.setText(i,strList[i]);
            else:
                whichQTreeeWidgetItem.setText(i,"");

    def getItemParent(self,whichQTreeeWidgetItem):
        return whichQTreeeWidgetItem.parent();

    def myItemClicked(self,can):
        # can 代表被点击的item对象
        print(can)

    def myItemDoubleClicked(self, can):
        print(can)

    def deleteAllItem(self):
        self.clear();

    # 只会返回一层的child  不会吧孩子的孩子也返回
    def getAllChildOfItem(self,whichQTreeeWidgetItem):
        myList = [];
        for i in range(whichQTreeeWidgetItem.columnCount()):
            myList.append(whichQTreeeWidgetItem.child(i));
        return  myList;
    #创建右键的按钮
    def createRightActions(self):
        self.pop_menu =  QtWidgets.QMenu();
        self.action_name =  QtWidgets.QAction( self);

        # 下面提供了 绑定响应菜单的消息  如果想响应菜单 按下面提供回调函数
        # self.action_name.triggered.connect(self.__actionNameTest)
        self.action_size =  QtWidgets.QAction( self);
        self.action_type =   QtWidgets.QAction( self);
        self.action_date =   QtWidgets.QAction( self);
        self.action_open =   QtWidgets.QAction( self);
        self.action_download =   QtWidgets.QAction( self);
        self.action_flush =   QtWidgets.QAction( self);
        self.action_delete =   QtWidgets.QAction( self);
        self.action_rename =   QtWidgets.QAction( self);
        self.action_create_folder =   QtWidgets.QAction(self);
        # self.action_name.setDisabled(True);
        self.action_open.setText(self.tr("打开"));
        self.action_download.setText(self.tr("下载"));
        self.action_flush.setText(self.tr("刷新"));
        self.action_delete.setText(self.tr("删除"));
        self.action_rename.setText(self.tr("重命名"));
        self.action_create_folder.setText(self.tr("新建文件夹"));
        self.action_name.setText(self.tr("名称"));
        self.action_size.setText(self.tr("大小"));
        self.action_type.setText(self.tr("项目类型"));
        self.action_date.setText(self.tr("修改日期"));
        # QtWidgets.QInputDialog.getItem
        #设置快捷键
        self.action_flush.setShortcut(QtGui.QKeySequence.Refresh);

    #重写方法实现自定义右键菜单
    def contextMenuEvent(self,event):
        # self.setContextMenuPolicy()
        self.pop_menu.clear(); #清除原有菜单
        point = event.pos(); #得到窗口坐标
        print(point)
        item = self.indexAt(point);
        print(item)
        # print("zjiasd")
        if(item != None):
            self.pop_menu.addAction(self.action_download);
            self.pop_menu.addAction(self.action_flush);
            self.pop_menu.addSeparator();
            self.pop_menu.addAction(self.action_delete);
            self.pop_menu.addAction(self.action_rename);
            self.pop_menu.addSeparator();
            self.pop_menu.addAction(self.action_create_folder);
            sort_style = self.pop_menu.addMenu("排序");
            sort_style.addAction(self.action_name);
            sort_style.addAction(self.action_size);
            sort_style.addAction(self.action_type);
            sort_style.addAction(self.action_date);

            #菜单出现的位置为当前鼠标的位置
            self.pop_menu.exec(QtGui.QCursor.pos());
            event.accept();


if(__name__=="__main__"):
    app= QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget();
    widget.resize(663, 543)
    layout = QtWidgets.QHBoxLayout(widget);

    treeWidget = MyPyQtTreeWidget();
    treeWidget.setColumnCount(2)
    root = treeWidget.pushRoot(["tree","ji"])
    child =  treeWidget.pushChild(root,["ceshi","child"])
    child2 =  treeWidget.pushChild(child,["ceshi","child2"])
    child1 = treeWidget.insertChild(root,2,["second","chenayng"]);
    child1.setIcon(0,QtGui.QIcon("../image/btn_ok.png"))
    root2 = treeWidget.insertRoot(1,["roo2","ni"])
    layout.addWidget(treeWidget)

    qss = QtCore.QFile("test.qss")
    qss.open(QtCore.QFile.ReadOnly)
    app.setStyleSheet(str(qss.readAll(),"utf-8"))

    widget.show();

    print(treeWidget.getAllChildOfItem(root))
    print(treeWidget.getIndexOfItem(child))
    print(treeWidget.getIndexOfItem(root2))
    treeWidget.updateQTreeWidget(root2,["root222","chena"])
    app.exec_()