
# coding = utf-8

class A(type):
    def __new__(cls, *args, **kwargs):
        print(cls)
        print(id(cls))
        return super(A,cls).__new__(cls,*args)
    def __call__(cls, *args, **kwargs):
        print(cls)
        print("A call")

class B(metaclass=A):

    def __init__(self):
        print("B init")
    def __call__(cls, *args, **kwargs):
        print("B call")
if(__name__=="__main__"):
    a = B();

