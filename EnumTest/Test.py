
class A():
    __slots__ = ('name', 'age')
    def set_score(self, score):
        self.score = score

a = A();
# print(a.__dict__)
print(hasattr(A,"name"))
print(type(A.set_score))
