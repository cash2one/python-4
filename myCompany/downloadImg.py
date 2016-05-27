from urllib import request
import  fileutil

def downjpg( filepath,FileName ="default.jpg" ):
    try:
        web = request.urlopen( filepath)
        print("访问网络文件"+filepath+"\n")
        jpg = web.read()

        DstDir="E:\\image\\"
        fileutil.makedirs(DstDir);
        print("保存文件"+DstDir+FileName+"\n")
        with open( DstDir+FileName,"wb" ) as File:
            try:

                File.write( jpg)
                File.close()
                return
            except IOError:
                print("error\n")
                return
    except Exception:
        print("error\n")
        return
if(__name__=="__main__"):
    url = "https://pin.aliyun.com/omeoclickimg?imgid=d9798f7693cd2b8991bb43eb1342ae14&t=1451312057515299";
    downjpg(url);
