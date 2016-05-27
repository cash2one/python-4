# coding = utf-8
import sys
from PyQt5 import Qt,QtWidgets,QtCore,QtGui



if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    #这里不要使用命名参数  可能是底部调用c的原因
    """
    第一个参数parent，用于指定父组件。注意，很多Qt组件的构造函数都会有这么一个parent参数，并提供一个默认值0；
    第二个参数caption，是对话框的标题；
    第三个参数dir，是对话框显示时默认打开的目录，"." 代表程序运行目录，"/" 代表当前盘符的根目录(Windows，Linux下/就是根目录了)，
    也可以是平台相关的，比如"C:\\"等；
    第四个参数filter，是对话框的后缀名过滤器；
    多个文件使用空格分隔：比如我们使用"Image Files(*.jpg *.png)"就让它只能显示后缀名是jpg或者png的文件。
    多个过滤使用两个分号分隔：如果需要使用多个过滤器，使用";;"分割，比如"JPEG Files(*.jpg);;PNG Files(*.png)"；
    """
    # return ('D:/data/python/demo/QTTest/QTFileDialog.py', 'ALL FIle(*)')
    openFileName = QtWidgets.QFileDialog.getOpenFileName(None,"ceshi",".","ALL FIle(*);;JPEG Files(*.jpg);;pythonFile(*.py)");

    # return (['D:/data/python/demo/QTTest/PyQtTableTest.py', 'D:/data/python/demo/QTTest/QTFileDialog.py'], 'ALL FIle(*)')
    openFIleNames = QtWidgets.QFileDialog.getOpenFileNames(None,"ceshi",".","ALL FIle(*);;JPEG Files(*.jpg);;pythonFile(*.py)")

    # return ('D:/data/python/demo/QTTest/1.py', 'pythonFile(*.py)')
    saveFileName = QtWidgets.QFileDialog.getSaveFileName(None,"baocun",".","pythonFile(*.py)");

    app.exec_();