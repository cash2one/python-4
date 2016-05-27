# coding = utf-8
import sys
from PyQt5 import Qt,QtWidgets,QtCore,QtGui

class MyListWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(MyListWidget,self).__init__( parent)
        self.setWindowTitle('ListWidget')
        # self.List = QtWidgets.QListWidget(self)
        # self.setSortingEnabled(1);
        item = ['OaK','Banana','Apple','Orange','Grapes','Jayesh','OaK','Banana','Apple','Orange','Grapes','Jayesh']

        res = self.createItem();
        self.addItem(res[0]);
        self.setItemWidget(res[0],res[1])

        res = self.createItem();
        self.addItem(res[0]);
        self.setItemWidget(res[0],res[1])
        self.itemClicked.connect(self.test);
        # listItem = []
        # layout = QtWidgets.QHBoxLayout;
        # layout.addWidget(QtWidgets.QLabel("Test"))
        # cbw=QtWidgets.QComboBox()
        # cbw.addItem("Worker")
        # cbw.addItem("Famer")
        # cbw.addItem("Doctor")
        # cbw.addItem("Lawyer")
        # cbw.addItem("Soldier")
        # layout.addWidget(cbw);
        # for lst in item:
        #     listItem.append(QtWidgets.QListWidgetItem(lst))
        # for i in range(len(listItem)):
        #     pass;
        #

        # self.setCentralWidget(self.List)
    """
        函数概述
        下面这个函数是测试能否在listView 自定义控件  比如说每一行 左边是一个图片右边是一个按钮
        并且下面测试了自定义按钮的样式  是通过setStyleSheet设置的
        关于布局只要知道 widget 支持盒子模型 也就是 margin border padding content

    """

    def createItem(self):
        btn1 = QtWidgets.QPushButton("B1B1B1B1B1")
        btn2 = QtWidgets.QPushButton("B2")
        # btn1.setObjectName("btnMenu")
        btn1.clicked.connect(self.__click);
        btn2.clicked.connect(self.__click);

        #sheet 参考网站
        #http://doc.qt.io/qt-4.8/stylesheet-examples.html
        #关于有哪些属性  http://doc.qt.io/qt-4.8/stylesheet-reference.html#border-width-prop
        # btn1.setStyleSheet("QPushButton{margin :100px;padding:20px;border-width:20px;border-radius:25px;"+
        #                    "border-style:solid;border-color:darkblue;color:darkblue;}")

        # print(btn1.getContentsMargins())
        cbw=QtWidgets.QComboBox()
        cbw.addItem("Worker")
        cbw.addItem("Famer")
        cbw.addItem("Doctor")
        cbw.addItem("Lawyer")
        cbw.addItem("Soldier")

        layout = QtWidgets.QHBoxLayout();
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(cbw)
        # 设置边距 默认为10  但是获取的时候不知为什么就为0了  只有设置值得时候才能获取
        #(left,top,right,bottom)
        # layout.setContentsMargins(60,130,60,10)
        # layout.setSpacing(4)#设置控件之间的间隙
        layout.addStretch();
        print(layout.getContentsMargins())

        # layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)

        twobtnWidget = QtWidgets.QWidget();
        twobtnWidget.setLayout(layout);

        listitem = QtWidgets.QListWidgetItem();
        size = twobtnWidget.sizeHint();
        listitem.setSizeHint(QtCore.QSize(size.width(),size.height()))
        return (listitem,twobtnWidget);

    def __click(self):
        #self.sender()可以得到发送信号的对象
        print(self.sender())
    # def getItems(self):
    #     list=[];
    #     print(self.model())
    #     for i in range(self.count()):
    #         list.append(self.item(i));
    #     # print(list)
    #     return list;
    #
    def test(self,index):

        #index 表示被点击的那个控件
        # print(index)
        print(self.indexFromItem(index))
        print("test");

app = QtWidgets.QApplication(sys.argv)
qss = QtCore.QFile("black.qss")
# print(qss.fileName())
qss.open(QtCore.QFile.ReadOnly)
# print(str(qss.readAll()))
app.setStyleSheet(str(qss.readAll()))
tb = MyListWidget()
tb.show()
# print(len(tb.getItems()));
app.exec_()