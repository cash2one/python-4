import pickle;
import copy;
from sympy.functions.special.gamma_functions import uppergamma


class Test(object):
    name = "jia";
    __slots__=('a', 'b');
    # print("asdfasdf");

    @property
    def name(self):
        self.a = 0;
        print(self.a);
        return self.a;

    @name.setter
    def name(self,va):
        self.a = 2;
        print("asdfas");
        print(self.a);

    def __init__(self):
        self.a,self.b = 0,1;

    def __iter__(self):
        return self;

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 2: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值
    def __getattr__(self, attr):
        pass

    def __str__(self):
        return "test";
    __repr__=__str__

    def test(self):
        pass;

    def __deepcopy__(self,visit):
        a = Test();
        a.a = copy.deepcopy(self.a);
        a.b = copy.deepcopy(self.b);
        return a;

def Testfun(*a,**kw):
    print(a);
    for i,y in kw.items():
        print(i)
        print(y)

def bina(a):
    a+=(1,2);
    return a;

count = 1;
def f(cls,a):
    print(cls)
    print(a);
    return a;

class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        # print("asdfdsaj");
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        # print(name);
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        uppercase_attr['jiayou'] = [1,3,4];
        uppercase_attr['ce'] = f;
        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)


class newTest(metaclass=UpperAttrMetaclass):

    def __init__(self,pa):
        self.a = 1;

    def ceshi(self):
        print("cesjo");
if (__name__=="__main__"):

    a = newTest();
    a.CESHI();
    print(newTest.jiayou);
    a.ce('asdf');
    print(a.jiayou);
    print(a)
    print(type(a))
    
    # a = Test();
    # print(a.__dict__);
    # f = open('D:\dump.txt', 'wb');
    # pickle.dump([1,2,3,[1,2,3]], f);
    # # a.ceshi = 1;
    # print(a.name);
    # a.name = 12;
    # print(a)
    # print(type(a));
    # for i in a:
    #     print(i);

    # Testfun(1,2,3,q=1,e=2);
    # a = (1,2)*3;
    # a[0] = 10;
    # print(a)