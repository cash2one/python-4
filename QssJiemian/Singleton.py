# coding = utf-8
from PyQt5 import QtWidgets,QtCore


class MoFang(QtWidgets.QWidget):
    def __init__(self):
        super(MoFang,self).__init__();
        self.resize(663, 543)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout");

        self.widget_title = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_title.sizePolicy().hasHeightForWidth())
        self.widget_title.setSizePolicy(sizePolicy)
        self.widget_title.setMinimumSize(QtCore.QSize(100, 28))
        self.widget_title.setObjectName("widget_title")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_title)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
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

        self.widget_menu = QtWidgets.QWidget(self.widget_title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_menu.sizePolicy().hasHeightForWidth())
        self.widget_menu.setSizePolicy(sizePolicy)
        self.widget_menu.setObjectName("widget_menu")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_menu)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

if __name__=="__main__":
    import sys  
    app=QtWidgets.QApplication(sys.argv)  
    widget=MoFang();

    widget.show()  
    app.exec_()