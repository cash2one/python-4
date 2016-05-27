# coding = utf-8
import socket
import threading
#下面这两段是用公司电脑测试的

def client():

    # 获得域名的ip地址
    # host = 'www.google.com'
    # port = 80
    #
    # try:
    # remote_ip = socket.gethostbyname( host )

    HOST='192.168.1.11'
    PORT=80
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
    s.connect((HOST,PORT))       #要连接的IP与端口
    while 1:
        cmd=input("Please input cmd:")       #与人交互，输入命令
        s.sendall(cmd.encode())      #把命令发送给对端  因为sendall  只接受byte  所以要将string 转嘛
        data=s.recv(1024).decode();     #把接收的数据定义为变量
        print(data)         #输出变量
    s.close()   #关闭连接

def server(): #这个只能接受一个client的连接
    HOST='192.168.1.11'
    PORT=50007
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #定义socket类型，网络通信，TCP
    s.bind((HOST,PORT))   #套接字绑定的IP与端口
    s.listen(1)         #开始TCP监听
    print("begin");
    while 1:
           conn,addr=s.accept()   #接受TCP连接，并返回新的套接字与IP地址
           print('Connected by',addr)    #输出客户端的IP地址
           while 1:
                data=conn.recv(1024).decode()    #把接收的数据实例化
                print(data)
                # cmd_status,cmd_result=commands.getstatusoutput(data)   #commands.getstatusoutput执行系统命令（即shell命令），返回两个结果，第一个是状态，成功则为0，第二个是执行成功或失败的输出信息
                if len(data.strip()) >=0:   #如果输出结果长度为0，则告诉客户端完成。此用法针对于创建文件或目录，创建成功不会有输出信息
                    conn.sendall('Done.'.encode())
                else:
                    conn.sendall(data)   #否则就把结果发给对端（即客户端）
    conn.close()     #关闭连接

def servers():

    # import commands   #执行系统命令模块
    HOST='192.168.1.11'
    PORT=50007
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #定义socket类型，网络通信，TCP
    s.bind((HOST,PORT))   #套接字绑定的IP与端口
    s.listen(1)         #开始TCP监听
    print("begin");

    def clientthread(conn):
        #Sending message to connected client
        print("clientthread begin")
        # conn.send('Welcome to the server. Type something and hit enter\n'.encode()) #send only takes string
        print("clientthread welcome")
        #infinite loop so that function do not terminate and thread do not end.
        while True:
            #Receiving from client
            print("wait")
            data = conn.recv(1024).decode();
            reply = 'OK...' + data

            conn.sendall(reply.encode())

        #came out of loop
        conn.close()

    while 1:
        conn, addr = s.accept()
        print( 'Connected with ' + addr[0] + ':' + str(addr[1]))
        t = threading.Thread(target = clientthread ,args = (conn,))
        t.start();
    conn.close()     #关闭连接

if __name__ == "__main__":
    client();