# coding = utf-8
import sys
from PyQt5 import Qt,QtWidgets,QtCore,QtGui


"""
测试布局里面再嵌入布局应该怎么用
"""
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv);
    widget = QtWidgets.QWidget();
    label = QtWidgets.QLabel();
    label.setText("及亚欧");
    btn1 = QtWidgets.QPushButton(widget);
    btn1.setText("click")

    layout = QtWidgets.QVBoxLayout();
    layout.addWidget(label);
    layout.addWidget(btn1);

    label2 = QtWidgets.QLabel(widget);
    label2.setText("及亚欧");
    btn2 = QtWidgets.QPushButton(widget);
    btn2.setText("click")

    layout1 = QtWidgets.QVBoxLayout();
    layout1.addWidget(label2);
    layout1.addWidget(btn2);
    
    layout.addItem(layout1)
    print(label.parent())
    print(layout.parent())
    widget.setLayout(layout);
    # help(QtWidgets.QWidget().setAutoFillBackground)
    # qpale = QtGui.QPalette
    # label.setPalette()
    widget.show();
    app.exec_()


