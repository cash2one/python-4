# coding=UTF-8
import subprocess;
import re;

import fileutil;

class ThePhoneNotExist(Exception):
     def __init__(self, value):
         self.value = value;
     def __str__(self):
        return repr(self.value);

class ThePhonePathIsNotExist(Exception):
     def __init__(self, value):
         self.value = value;
     def __str__(self):
        return repr(self.value);

fileOrDirectoryNotExist = "No such file or directory";#这样以后好改
fileIsNotDirectory = "Not a directory";

class PhoneUtil():

    deviceList=[];
    currentDevice = "";
    def __init__(self):
        self.__updatePhoneList();
        if(self.deviceList!=None and self.deviceList!=""):
            # 默认是操作第一个手机
            self.currentDevice = self.deviceList[0];

    def getDevice(self):
        self.__updatePhoneList();
        return self.deviceList;

    def __updatePhoneList(self):
        cmd = r"D:\adb\adb.exe  "  + " devices"; #这个语句不需要加上-s  因为它本来就是为了获得 现在有哪些设备
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True);
        #一直等到子进程结束 并返回pout与错误信息
        (pout,perr) = p.communicate(timeout=5);
        # print(pout)
        poutstr = str(pout,"utf-8");

        # print(poutstr);
        pattern  = re.compile("([0-9a-fA-F]{1,})\t");
        devicelist = re.findall(pattern,poutstr);
        self.deviceList = devicelist;
        if(p.stdout!=None):
            p.stdout.close();
        if(p.stderr!=None):
            p.stderr.close();

    def setCurrentPhone(self,index):
        self.__updatePhoneList();
        phoneNumber = len(self.deviceList);
        if(index>phoneNumber):
            raise ThePhoneNotExist("序号所指定的手机ID不存在 请调用getPhoneNumber");
        else:
            self.currentDevice = self.deviceList[index];

    def getPhoneNumber(self):
        self.__updatePhoneList();
        return len(self.deviceList);

    def getCurrentPhoneName(self):
        return self.currentDevice;


    def getFileList(self,path):

        #因为手机打开目录 比如说sdcard 他是要在sdcard 后面加上/
        path = path.lstrip('/');
        path = path+'/';

        cmd = r"D:\adb\adb.exe -s "+self.currentDevice+" shell ls "+ path;
        print(cmd);
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True);
        #一直等到子进程结束 并返回pout与错误信息
        try:
            (pout,perr) = p.communicate(timeout=1);
        except subprocess.TimeoutExpired as e:
            print(e);
            return [];
        pout = str(pout,'utf-8').replace("\r\r",'\r');
        if(pout.find(fileOrDirectoryNotExist) != -1):
            raise ThePhonePathIsNotExist("你所指定的路径在手机上不存在");

        pout = pout.strip("\r\n");
        pout = pout.split('\r\n');
        if(p.stdout!=None):
            p.stdout.close();
        if(p.stderr!=None):
            p.stderr.close();
        return pout;

    def joinPhonePath(self,root,path):
        return root+'/'+path;

    def copyFileOrDirectory(self,src,des):
        path = src.lstrip('/');
        path = path+'/';
        if(self.isFile(src)):
            path = path.rstrip('/') ;

        fileutil.makedirs(des);
        des = str(des).replace('\\',"/");
        # print(des);
        cmd = r"D:\adb\adb.exe -s "+self.currentDevice+" pull "+ path +"  "+des;
        # print(cmd);
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True);
        #一直等到子进程结束 并返回pout与错误信息
        try:
            (pout,perr) = p.communicate();
        except subprocess.TimeoutExpired as e:
            print(e);
            return [];

        if(p.stdout!=None):
            p.stdout.close();
        if(p.stderr!=None):
            p.stderr.close();
        print("已经将"+src +" copy到  "+des);

    def isFile(self,src):
        path = src.lstrip('/');
        path = src+'/';
        cmd = r"D:\adb\adb.exe -s  "+self.currentDevice+" shell cd "+ src ;
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True);
        #一直等到子进程结束 并返回pout与错误信息
        try:
            (pout,perr) = p.communicate();
        except subprocess.TimeoutExpired as e:
            print(e);
            return None;

        pout = str(pout,'utf-8').replace("\r\r",'\r');
        if(pout.find(fileOrDirectoryNotExist) != -1):
            raise ThePhonePathIsNotExist("你所指定的路径在手机上不存在");

        if(pout.find(fileIsNotDirectory) != -1):#结果中有Not a directory
            return True;
        return False;

    def isDirectory(self,src):
        src = src.lstrip('/');
        src = src+'/';
        cmd = r"D:\adb\adb.exe -s "+self.currentDevice+" shell cd "+ src ;
        # print(cmd);
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True);
        #一直等到子进程结束 并返回pout与错误信息
        try:
            (pout,perr) = p.communicate();
        except subprocess.TimeoutExpired as e:
            print(e);
            return None;
        pout = str(pout,'utf-8').replace("\r\r",'\r');
        if(pout.find(fileOrDirectoryNotExist) != -1):
            raise ThePhonePathIsNotExist("你所指定的路径在手机上不存在");

        # print(pout.find(fileIsNotDirectory))
        if(pout.find(fileIsNotDirectory) == -1):#没有找到这个路径
            return True;
        return False;

    def fileOrDirectoryExist(self,src):
        src = src.lstrip('/');
        src = src+'/';
        cmd = r"D:\adb\adb.exe -s "+self.currentDevice+" shell cd "+ src ;
        # print(cmd);
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True);
        #一直等到子进程结束 并返回pout与错误信息
        try:
            (pout,perr) = p.communicate();
        except subprocess.TimeoutExpired as e:
            print(e);
            return None;

        pout = str(pout,'utf-8').replace("\r\r",'\r');
        if(pout.find(fileOrDirectoryNotExist) == -1):
            return True;
        return False;

if __name__ == "__main__":
    a = PhoneUtil();
    print(a.getDevice());
    a.copyFileOrDirectory("sdcard/360/permmgr",r"d:\date1");
    print(a.fileOrDirectoryExist("sdcard1"));
    print(a.isDirectory("sdcard"));