import cx_Oracle as oracle


def oracleTest(sss):
    # conn=oracle.connect ('chen','chen','192.168.1.130:1531/myorcl');
    # conn=oracle.connect ('scott','chen','192.168.1.11:1541/orcl');
    conn=oracle.connect ('Scott','chenyang','localhost:1521/orcl');#连接数据库
    curs=conn.cursor();  #创建一个cursor 用于存放返回数据
    # sql="update emp set ename = 'chen' where ename = '%s'" % ('chen',); #这里写sql语句
    sql = "select name,IdNuber,PhoneNumber from BiShe WHERE IDCard like :bianliang";
    print(sss);
    print("&&&&&&&&&&&&&&&&&&&&&&&&&7")
    rr=curs.execute(sql,bianliang="%"+sss+"%"); #执行sql 语句 这里暂时没有发现执行更新时 删除时 是不是像java一样 能够返回跟新的行数
    list = []
    row=curs.fetchone(); #得到一行
    print(row)
    while(row):
        row = curs.fetchone();
        print(row);
        list.append(row)
    print(row);

    try:
        conn.commit();#  如果是插入删除 更新最后要提交   选择不用更新
    except:
        print("rollback");
        conn.rollback();
    finally:
        curs.close();#资源关闭
        conn.close();
    # c.callproc('p_demo',[str1,str2])调用存储过程
    # print(row)



if (__name__=="__main__"):
    oracleTest("20562461051798409899100101102103104105")