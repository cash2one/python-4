# coding = utf-8
from PyQt5 import Qt,QtWidgets,QtCore,QtGui
from MySerial.BiShe import Ui_frmMain;
import ctypes.wintypes
import threading;
import serial
from threading import Timer
import threading
import cx_Oracle as oracle
import time
class mythread(threading.Thread):
    def __init__(self,stopevt = None,name = 'subthread',t = None,xianshi = None):
        threading.Thread.__init__(self)
        self.stopevt = stopevt
        self.name = name
        self.t = t;
        self.ui = xianshi;

    def Eventrun(self):
        st = '';
        while not self.stopevt.isSet():
            # print(self.name +' alive\n')
            # t = serial.Serial('COM3',115200)
            c = self.t.read(1);
            if(c!=b'\n'):
                st+=c.decode();
            else:
                if(len(st)>10):
                    sssss='';
                    for i in st:
                        if i!=' ' and ord(i)!=13:
                            sssss+=i;
                    st = connectOracle(sssss);
                    string = "";
                    for i in st:
                        if(i):
                           string+= str(i);
                    if( not string.rstrip()==""):
                        self.ui.append(string);
                st = '';
    def run(self):
        self.Eventrun()

def connectOracle(sss):

    conn=oracle.connect ('Scott','chenyang','localhost:1521/orcl');#连接数据库
    curs=conn.cursor();  #创建一个cursor 用于存放返回数据
    # sql="update emp set ename = 'chen' where ename = '%s'" % ('chen',); #这里写sql语句
    sql = "select name,IdNuber,PhoneNumber from BiShe WHERE IDCard like :bianliang";
    print(sss);
    print("&&&&&&&&&&&&&&&&&&&&&&&&&7")
    rr=curs.execute(sql,bianliang="%"+sss+"%"); #执行sql 语句 这里暂时没有发现执行更新时 删除时 是不是像java一样 能够返回跟新的行数
    list = []
    row=curs.fetchone(); #得到一行
    list.append(row);
    while(row):
        row = curs.fetchone();
        print(row);
        if(row):
            list.append(row)
    return list


    # c.callproc('p_demo',[str1,str2])调用存储过程
    # print(row)


class Test(QtWidgets.QDialog):

    def __init__(self,app):
        super(Test, self).__init__();
        self.flag = False;
        self.th = None
        self.mymaxinum = False;
        self.mousePressed = False;
        self.location = self.geometry();
        self.ui = Ui_frmMain();
        self.ui.setupUi(self);

        self.timer_interval=5

        for i in range(20):
            try:
                self.serial = serial.Serial("COM"+str(i),int(self.ui.comboBox.currentText()));
                self.ui.cboxStyle.addItem("COM"+str(i));
            except serial.serialutil.SerialException as  e:
                pass;
        self.stopevt = threading.Event()
        self.serial = None;
        # 设置无边框  一定要加上Qt.Qt.Dialog  否则无法实现伸缩功能
        self.setWindowFlags(Qt.Qt.FramelessWindowHint | Qt.Qt.Dialog)
        self.ui.btnMenu_Close.clicked.connect(self.close)
        self.ui.btnChangeStyle.clicked.connect(self.clickBtnChangeStyle)
        self.ui.btnMenu_Min.clicked.connect(self.showMinimized)
        # self.ui.btnMenu_Max.clicked.connect(self.showMaximized)
        self.ui.btnMenu_Max.clicked.connect(self.on_btnMenu_Max_clicked)
        self.menu = QtWidgets.QMenu();

        # self.ui.btnMenu_Max.click.connect(self.showNormal)
        # 这个非常重要  设置代理
        self.ui.lab_Title.installEventFilter(self)

        # self.installEventFilter(self)


    def clickBtnChangeStyle(self):
        if(self.flag == False):
            self.stopevt.clear();

            # print(self.ui.cboxStyle.currentText())
            try:
                self.serial = serial.Serial(self.ui.cboxStyle.currentText(),int(self.ui.comboBox.currentText()));
                self.ui.btnChangeStyle.setText("close")
                print("asdfa")
                self.flag = not self.flag;
                self.th = mythread(self.stopevt,'subthread',self.serial,self.ui.textEdit);
                self.th.start();
            except serial.serialutil.SerialException as  e:

                reply = QtWidgets.QMessageBox.question(self, '串口开启出错',
                "Are you sure to quit?", QtWidgets.QMessageBox.Ok , QtWidgets.QMessageBox.Ok)

                if reply == QtWidgets.QMessageBox.Ok:
                    print('yes')
                    # event.accept()
                else:
                    print ('no')
                    # event.ignore()
                print(e.__class__)
        else:
            self.ui.btnChangeStyle.setText("open")
            self.stopevt.set();
            self.serial.close();
            self.flag = not self.flag;

    def on_btnMenu_Max_clicked(self):
        if (self.mymaxinum):
            self.setGeometry(self.location);
            self.ui.btnMenu_Max.setToolTip("最大化");
        else:

            self.location = self.geometry();
            print(self.location)
            self.setGeometry(app.desktop().availableGeometry());
            self.ui.btnMenu_Max.setToolTip("还原");

        self.mymaxinum = not self.mymaxinum;

    #实现双击最大化  以及窗口移动
    def eventFilter(self,w, event):
        if event.type() == QtCore.QEvent.MouseButtonDblClick:
            self.on_btnMenu_Max_clicked();
            # self.showMaximized();
            return True;
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if (event.button() == Qt.Qt.LeftButton):
                self.mousePressed = True;
                self.mousePoint = event.globalPos() - self.pos();
                return True;
        elif (event.type() == QtCore.QEvent.MouseButtonRelease):
            self.mousePressed = False;
            return True;
        elif (event.type() == QtCore.QEvent.MouseMove):
            if self.mousePressed and (event.buttons() and Qt.Qt.LeftButton):
                self.move(event.globalPos() - self.mousePoint);
                return True;
        # elif (event.type() == QtCore.QEvent)
        return super(Test,self).eventFilter(w, event);

    def nativeEvent(self, type, msg,*arg):
        # print("rrrrrrrrrrrrrrrrrrrrr")

        msg = ctypes.wintypes.MSG.from_address(msg.__int__())
        # print(msg.message)

        # a = self.mapFromGlobal(QtGui.QCursor.pos());
        # print(a.x())
        # print(self.width())
        # print(self.height())
        if(msg.message == 0x84):
            captionHeight = 25;
            frameWidth = 6;
            HTNOWHERE = 0
            HTCAPTION = 2
            HTLEFT = 10
            HTRIGHT = 11
            HTTOP = 12
            HTTOPLEFT = 13
            HTTOPRIGHT = 14
            HTBOTTOM = 15
            HTBOTTOMLEFT = 0x10
            HTBOTTOMRIGHT = 17
            HTCLIENT = 1
            result = 1;
            # print(self.GET_X_LPARAM(msg.lParam))
            # print(self.GET_Y_LPARAM(msg.lParam))
            # xPos = self.GET_X_LPARAM(msg.lParam) - self.frameGeometry().x();
            # yPos = self.GET_Y_LPARAM(msg.lParam) - self.frameGeometry().y();
            pos = self.mapFromGlobal(QtGui.QCursor.pos());
            xPos = pos.x()
            yPos = pos.y()
            # if(self.childAt(xPos,yPos) == 0):
            #     print("HTCAPTION")
            #     result = HTCAPTION;
            # else:
            #     return super(Test, self).nativeEvent(type, msg,*arg);

            # if(xPos < 10):
            #     print("HTLEFT")
            #     result = HTLEFT;
            # if(xPos > (self.width() - 10) ):
            #     print("HTRIGHT")
            #     result = HTRIGHT;
            # if(yPos < 18):
            #     print("HTTOP")
            #     result = HTTOP;
            # if(yPos > (self.height() - 22) ):
            #     print("HTBOTTOM")
            #     result = HTBOTTOM;
            # if(xPos <18 and yPos <18):
            #     print("HTTOPLEFT")
            #     result = HTTOPLEFT;
            # if(xPos > (self.width() - 22)  and yPos > 18):
            #     print("HTTOPRIGHT")
            #     result = HTTOPRIGHT;
            # if(xPos <18 and yPos > (self.height() - 22)):
            #     print("HTBOTTOMLEFT")
            #     result = HTBOTTOMLEFT;
            if(xPos > (self.width() - 15) and yPos > (self.height() - 15) ):
                # print("HTBOTTOMRIGHT")
                result = HTBOTTOMRIGHT;

            return (True,result);
        else:
            return super(Test, self).nativeEvent(type, msg,*arg);


    def GET_X_LPARAM(self, param):
        #define LOWORD(l)           ((WORD)((DWORD_PTR)(l) & 0xffff))
        #define HIWORD(l)           ((WORD)((DWORD_PTR)(l) >> 16))
        #define GET_X_LPARAM(lp)                        ((int)(short)LOWORD(lp))
        #define GET_Y_LPARAM(lp)                        ((int)(short)HIWORD(lp))
        return param & 0xffff

    def GET_Y_LPARAM(self, param):
        return param >> 16

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=Test(app)

    # ui.btnMenu_Max.clicked.connect(widget.showMaximized)
    widget.show()

    qss = QtCore.QFile("black.qss")
    qss.open(QtCore.QFile.ReadOnly)
    app.setStyleSheet(str(qss.readAll(),"utf-8"))
    # app.setStyleSheet("QLabel#label{border:1px solid};")
    widget.show()
    app.exec_()

