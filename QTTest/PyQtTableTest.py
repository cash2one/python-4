# -*- coding: utf-8 -*-
"""图标"""
import sys

from PyQt5 import Qt,QtWidgets,QtCore,QtGui


class MyTable(QtWidgets.QTableWidget):
    def __init__(self,parent=None):
        self.colorDict={};
        super(MyTable,self).__init__(parent)
        self.setColumnCount(5);
        self.setRowCount(100);
        self.cellEntered.connect(self.__cellEnterred);
        self.createRightActions();
        self.setHoverRowColor(200,A=50);
        header=("name","last modify time","type","size");
        self.setTableHorizontalHeader(header);
        self.setMouseTracking(True);
        self.setHorizontalHeaderDefaultColumnWidth(200)
        self.setWindowIcon(QtGui.QIcon("image/5.jpg"))

        # self.setColumnWidth(1,400);
        self.setItem(0,0,QtWidgets.QTableWidgetItem(self.tr("性别")))
        self.setItem(0,1,QtWidgets.QTableWidgetItem(self.tr("姓名")))
        self.setItem(0,2,QtWidgets.QTableWidgetItem(self.tr("出生日期")))
        self.setItem(0,3,QtWidgets.QTableWidgetItem(self.tr("职业")))
        self.setItem(0,4,QtWidgets.QTableWidgetItem(self.tr("收入")))
        self.setItem(1,2,QtWidgets.QTableWidgetItem("asdfas"))
        # print(self.item(3,2).text());
        for i in range(1,100):
            lbp1=QtWidgets.QLabel()
            lbp1.setPixmap(QtGui.QPixmap("image/4.jpg"))

            self.setCellWidget(i,0,lbp1)
            twi1=QtWidgets.QTableWidgetItem("Tom")

            # print("**********************")
            # print(twi1.background())
            self.setItem(i,1,twi1)
            # 日历时间选择
            dte1=QtWidgets.QDateTimeEdit()
            dte1.setDateTime(QtCore.QDateTime.currentDateTime())
            dte1.setDisplayFormat("yyyy/mm/dd")

            dte1.setCalendarPopup(True)
            self.setCellWidget(i,2,dte1)
            #选择下拉框
            cbw=QtWidgets.QComboBox()
            cbw.addItem("Worker")
            cbw.addItem("Famer")
            cbw.addItem("Doctor")
            cbw.addItem("Lawyer")
            cbw.addItem("Soldier")
            self.setCellWidget(i,3,cbw)
            sb1=QtWidgets.QSpinBox()
            sb1.setRange(1000,10000)
            self.setCellWidget(i,4,sb1)

        # print(self.rowCount())
        # self.removeRow()
        # print(self.item(3,2).text());

    def getNumberOfRows(self):
        return self.rowCount();

    def setTableHorizontalHeader(self,headerStringList):
        if(headerStringList!=None):
            headerlistcopy = [];
            for i in headerStringList:
                headerlistcopy.append(self.tr(i));
        self.setHorizontalHeaderLabels(headerlistcopy);
    #
    #设置默认的每行的宽度  如果想改变单个宽度  可以使用setColumnWidth
    def setHorizontalHeaderDefaultColumnWidth(self,intSize):
        self.horizontalHeader().setDefaultSectionSize(intSize);

    def setHorizontalHeaderDefaultRowWidth(self,intSize):
        self.horizontalHeader().setFixedHeight(intSize);

    def setColumnWidth(self,column,width):
        super(MyTable,self).setColumnWidth(column,width);

    def setRowWidth(self,row,width):
        super(MyTable,self).setRowHeight(row,width);

    def setverticalHeaderDefaultRowWidth(self,intwidth):
        self.verticalHeader().setDefaultSectionSize(intwidth);

    def getNumberOfColumns(self):
        return self.columnCount();

    def getCurrentRow(self):
        return self.currentRow();

    def getCurrentColumn(self):
        return self.currentColumn();

    def getCellWidgets(self,row,column):
        return self.cellWidget(row,column);

    def setMaxColumn(self,column):
        self.setColumnCount(column);


    def setMaxRow(self,row):
        self.setColumnCount(row);

    def setCellItem(self, row, column, QTableWidgetItem):
        self.setItem(column, row, QTableWidgetItem);

    def getCellItem(self, row,column):
        self.item(row,column);

    def setHorizontalHeaderShow(self,BoolShowOrNotShow):
        self.horizontalHeader().setVisible(BoolShowOrNotShow);

    def setVerticalHeaderShow(self,BoolShowOrNotShow):
        self.verticalHeader().setVisible(BoolShowOrNotShow);

    def setSelectedBackgroundColor(self,R,G,B):
        self.setStyleSheet("selection-background-color:"+"rgb("+str(R)+","+str(G)+","+str(B)+");"); #设置选中背景色


    def __cellEnterred(self):
        pass;


    def setHoverRowColor(self,R=0,G=100,B=120,A = 255 ):
        self.setStyleSheet("QTableView::item:hover{background-color:" +"rgba("+str(R)+","+str(G)+","+str(B)+","+str(A)+");}");


    def setHorizontalHeaderBackgroundColor(self,R,G,B):
        self.horizontalHeader().setStyleSheet("QHeaderView::section{background:"+"rgb("+str(R)+","+str(G)+","+str(B)+");}"); #设置表头背景色


    #intSelect默认等于1 代表你可以选择按单元格选择  =2 代表以行为单位选择 = 3 代表选择一列
    def setSelectModel(self,intSelect=1 ):
        if intSelect == 1:
            self.setSelectionBehavior(self.SelectItems);
        elif intSelect == 2:
            self.setItemDelegate(NoFocusDelegate());
            self.setSelectionBehavior(self.SelectRows);
        elif intSelect == 3:
            self.setItemDelegate(NoFocusDelegate());
            self.setSelectionBehavior(self.SelectColumns);

    def unionCells(self,left,top,length,height):
        self.setSpan(left,top,length,height);
        # self.clearSpans()


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

    def __actionNameTest(self):
        print("actions");

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

    def mouseMoveEvent(self,event):
        row = self.indexAt(event.pos()).row();
        # self.selectRow(row);
        # self.updateRow(row);


    def leaveEvent(self, event):
        pass;


#这个类是用来在 选择一行或者一列的时候没有 虚线 参考网页http://blog.chinaunix.net/uid-25900151-id-3974759.html
class NoFocusDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        super(NoFocusDelegate, self).__init__(parent)

    def paint(self, QPainter, QStyleOptionViewItem, QModelIndex):
        itemOption = QtWidgets.QStyleOptionViewItem(QStyleOptionViewItem)
        if (itemOption.state & QtWidgets.QStyle.State_HasFocus):
            itemOption.state = itemOption.state ^ QtWidgets.QStyle.State_HasFocus;

        # if (QStyleOptionViewItem.state & QtWidgets.QStyle.State_MouseOver):
        #     return super(NoFocusDelegate,self).paint(QPainter, itemOption, QModelIndex);

        # print("******************")
        # print(QModelIndex);
        super(NoFocusDelegate,self).paint(QPainter, itemOption, QModelIndex);


# if(__name__ == "__main__"):
app=QtWidgets.QApplication(sys.argv)
myqq=MyTable()
print(myqq.getNumberOfColumns())
print(myqq.getNumberOfRows())
myqq.setWindowTitle("My Table")
myqq.show()
myqq.setverticalHeaderDefaultRowWidth(100)
myqq.setRowWidth(2,20);
myqq.setSelectModel(2);
myqq.setVerticalHeaderShow(False);
# myqq.setRowColor(0)
# myqq.
# myqq.unionCells(1,1,2,3)
# myqq.setHorizontalHeaderDefaultRowWidth(500)
# myqq.setverticalHeaderDefaultRowWidth(50);
# myqq.setHorizontalHeaderBackgroundColor(255,0,0);
# myqq.setSelectedBackgroundColor(255,0,0);
# print(myqq.getCellWidgets(2,3));

# print(hasattr(NoFocusDelegate(),"paint"))
app.exec_()