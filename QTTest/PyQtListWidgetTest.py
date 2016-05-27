# coding = utf-8
import sys
from PyQt5 import Qt,QtWidgets,QtCore,QtGui

class MyListWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(MyListWidget,self).__init__( parent)
        self.setWindowTitle('ListWidget')
        # self.List = QtWidgets.QListWidget(self)
        self.setSortingEnabled(1);
        item = ['OaK','Banana','Apple','Orange','Grapes','Jayesh','OaK','Banana','Apple','Orange','Grapes','Jayesh']
        listItem = []
        layout = QtWidgets.QHBoxLayout();
        layout.addWidget(QtWidgets.QLabel("Test"))
        cbw=QtWidgets.QComboBox()
        cbw.addItem("Worker")
        cbw.addItem("Famer")
        cbw.addItem("Doctor")
        cbw.addItem("Lawyer")
        cbw.addItem("Soldier")
        layout.addWidget(cbw);
        for lst in item:
            listItem.append(QtWidgets.QListWidgetItem(lst))
        for i in range(len(listItem)):
            self.insertItem(i+1,listItem[i])
        self.itemClicked.connect(self.test);

        # self.setCentralWidget(self.List)

    def getItems(self):
        list=[];
        print(self.model())
        for i in range(self.count()):
            list.append(self.item(i));
        # print(list)
        return list;

    def test(self,index):

        #index 表示被点击的那个控件
        print(self.indexFromItem(index).row())
        print("test");

app = QtWidgets.QApplication(sys.argv)
tb = MyListWidget()
tb.show()
print(len(tb.getItems()));
app.exec_()