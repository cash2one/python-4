# coding = utf-8
from PyQt5 import Qt,QtWidgets,QtCore,QtGui
from QTTest.frmmain import Ui_frmMain;
import ctypes.wintypes

class Test(QtWidgets.QDialog):
    def __init__(self,app):
        super(Test, self).__init__();
        self.mymaxinum = False;
        self.mousePressed = False;
        self.location = self.geometry();
        self.ui = Ui_frmMain();
        self.ui.setupUi(self);

        # 设置无边框  一定要加上Qt.Qt.Dialog  否则无法实现伸缩功能
        self.setWindowFlags(Qt.Qt.FramelessWindowHint | Qt.Qt.Dialog)
        self.ui.btnMenu_Close.clicked.connect(self.close)
        self.ui.btnMenu_Min.clicked.connect(self.showMinimized)
        self.ui.btnMenu_Max.clicked.connect(self.showMaximized)
        self.ui.btnMenu_Max.clicked.connect(self.on_btnMenu_Max_clicked)
        self.menu = QtWidgets.QMenu();

        action1 = self.menu.addAction("action1");

        menu2 = self.menu.addMenu("childMenu");

        action2 = menu2.addAction("action2");

        action3 = menu2.addAction("action3");

        action4 = self.menu.addAction("action4");

        self.ui.btnMenuMain.clicked.connect(self.popmenu);


        # self.ui.btnMenu_Max.click.connect(self.showNormal)
        # 这个非常重要  设置代理
        self.ui.lab_Title.installEventFilter(self)
        # self.installEventFilter(self)

    def popmenu(self):
        pos = self.ui.btnMenuMain.pos()
        # QtCore.QMargins
        pos.setY(pos.y()+self.ui.btnMenuMain.sizeHint().height())
        self.menu.exec_(self.mapToGlobal(pos));

    def on_btnMenu_Max_clicked(self):
        if (self.mymaxinum):
            self.setGeometry(self.location);
            self.ui.btnMenu_Max.setToolTip("最大化");
        else:
            self.location = self.geometry();
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