# coding=UTF-8
import os;
import shutil;
import  re;
#不管目标目录存不存在都可以  不管是文件复制 还是文件夹复制都可以 但是des 必须是文件夹 不能是文件 否则会抛出异常
def copy(src,des):
    if(os.path.exists(src)):
        __copy_src_exist(src,des);
    else:
        raise FileIsNotExist(src+" 不存在 ")

#不管是文件移动 还是文件夹移动都可以  des必须是目录 但是可以不存在 程序自动创建
def move(src,des):
    if(os.path.exists(src)):
        if(os.path.exists(des)):
            if(__pin_jie_name(src,des).strip() != str(src).strip()):
                des = __copy_rename(src,des);
                shutil.move(src,des);
        else:
            os.makedirs(des);
            shutil.move(src,des);

#它会完成多级目录创建
def makedirs(path):
    if(os.path.exists(path)==False):
        os.makedirs(path);
    else:
        print(path+"  已经存在");

#newname 可以加后缀也可以不加后缀 可以加路径  也可以不加  加了会忽略
def rename(oldname,newname):
    if(os.path.exists(oldname)):
        newlujing,newwenjian = os.path.split(newname);
        newwenjian,newhouzhui = os.path.splitext(newwenjian);
        
        oldlujing,oldwenjian = os.path.split(oldname);
        oldwenjian,oldhouzhui = os.path.splitext(oldwenjian);
        if newhouzhui == "":
            newname = newwenjian+oldhouzhui;
        else:
            newname = newwenjian+newhouzhui;
        newname = os.path.join(oldlujing,newname);

        newnamebeifen = __avoid_chong_ming(newname);
        if(newnamebeifen.strip() != newname.strip() ):
            print("rename "+ newname +"已经存在 函数将重新命名为" + newnamebeifen)
        os.rename(oldname,newnamebeifen);
        print(oldname+"  已经成功被命名为 "+newnamebeifen);
    else:
        raise FileIsNotExist(oldname+" 不存在 ");

def delete(path):
    if(os.path.exists(path)):
        if os.path.isfile(path):  
            os.remove(path)  
            print (path+" removed!")  
        elif os.path.isdir(path):  
            shutil.rmtree(path,True)  
            print ("dir "+path+" removed!")
    else:
        raise FileIsNotExist(path+" 不存在 ");

def isDirectory(path):
    if not os.path.exists(path):
        return None;
    return os.path.isdir(path);

def isFile(path):
    if not os.path.exists(path):
        return None;
    return os.path.isfile(path);

def getSeparator():
    return os.path.sep;
#~ #----------------------------------------------------------------------
def GetFileList(FindPath,FlagStr=None):
    '''
    #获取目录中指定的文件名
    #>>>FlagStr=['F','EMS','txt'] #要求文件名称中包含这些字符
    #>>>FileList=GetFileList(FindPath,FlagStr) #
    '''
    import os
    FileList=[];
    FileNames=os.listdir(FindPath)
    if (len(FileNames)>0):
       for fn in FileNames:
           if (FlagStr!=None and len(FlagStr)>0):
               #返回指定类型的文件名
               if (__IsSubString(FlagStr,fn)):
                   fullfilename=os.path.join(FindPath,fn)
                   FileList.append(fullfilename)
           else:
               #默认直接返回所有文件名
               fullfilename=os.path.join(FindPath,fn)
               FileList.append(fullfilename)

    #对文件名排序
    # if (len(FileList)>0):
    #     FileList.sort()
    return FileList



#内部调用
#path表示经过拼凑后的一个路径，是否存在了  与copy_rename的区别，他已经拼凑好了，
#copy_rename没有拼凑
def __avoid_chong_ming(path):
    num = 1;
    houzhui = "";
    while(os.path.exists(path)):
       lujing,wenjian =  os.path.split(path);
       if(os.path.isfile(path)):
           wenjian,houzhui = os.path.splitext(wenjian);
       wenjian+="("+str(num)+")";
       wenjian += houzhui;
       path = os.path.join(lujing,wenjian);
       num+=1;
    return path;



def __IsSubString(SubStrList,Str):
    '''''
    #判断字符串Str是否符合SubStrList正则表达式
    #>>>SubStrList=['F','EMS','txt']
    #>>>Str='F06925EMS91.txt'
    #>>>__IsSubString(SubStrList,Str)#return True (or False)
    '''
    flag=True
    for substr in SubStrList:
        if not re.search(substr, Str):
            flag=False

    return flag


#内部调用
def __copy_src_exist(src,des):
    if(os.path.exists(des) and os.path.isdir(des)):
        if(os.path.isfile(src)):
            desbeifen = __copy_rename(src,des);
            if(desbeifen.strip() == str(des).strip()):
                print(des +"  已经存在 重新命名为 "+ desbeifen )
            shutil.copy(src,desbeifen);
        if(os.path.isdir(src)):
            desbeifen = __copy_rename(src,des);
            if(desbeifen.strip() == str(des).strip()):
                print(des +"  已经存在 重新命名为 "+ desbeifen )
            shutil.copytree(src,desbeifen);
    if(os.path.exists(des)==False):
        os.makedirs(des);
        if(os.path.isfile(src)):
            shutil.copy(src,des);
        if(os.path.isdir(src)):
            des = __copy_rename(src,des);
            shutil.copytree(src,des);

#内部调用
#des只能是文件夹  如果是文件  则会抛出异常
#表示path的这个路径下最后一层  是否在des这个路径下存在
def __copy_rename(path,des):
    num = 1;
    houzhui = "";
    qian,hou = os.path.split(path);
    if(os.path.isfile(des)):
        raise FilePathIsNotDirectory(path + "  不是目录而是文件 ");
    path = os.path.join(des,hou);

    lujing,wenjian =  os.path.split(path);
    if(os.path.isfile(path)):
        wenjian,houzhui = os.path.splitext(wenjian);
    
    while(os.path.exists(path)):
       wenjianbei =wenjian +"("+str(num)+")";
       wenjianbei += houzhui;
       path = os.path.join(lujing,wenjianbei);
       num+=1;
    return path;

#内部调用 用来拼接路径
def __pin_jie_name(path,des):
    qian,hou = os.path.split(path);
    if(os.path.isfile(des)):
        raise FilePathIsNotDirectory(path + "  不是目录而是文件 ");
    path = os.path.join(des,hou);
    return path;

class FilePathIsNotDirectory(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
        return repr(self.value)

class FileIsNotExist(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
        return repr(self.value)


if(__name__ == "__main__"):
    a = r"D:\softdata\thunder_xiazai\ADMSetup_v2.0.1.exe";
    b = r"D:\ADMSetup_v2.0.1.exe";
    c = r"D:\ceshi.pdf";
    d = r"d:\jiayou\ceshi1.pdf";
    makedirs(d);
    a = GetFileList(r"d:"+getSeparator())
    for i in a:
        if isDirectory(i):
            print(i)


                
