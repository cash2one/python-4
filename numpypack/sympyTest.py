from sympy import *;
import numpy as np;
from sympy.polys.polyroots import root_factors;
import pandas as pd;

#定义符号变量
x = symbols("x");
y = symbols("y");
t = 2*x**3 + 2*x + sin(x);
print(t);


# print(type(y));
print("qiu多项式的根");
print(roots(x**2+1,x));

#这个是用来将多项式拆成乘积的方式
print(root_factors(x**2+1,x));

#解微分方程
f = Function("f");
a = dsolve(f(x).diff(x) + f(x)**2 +f(x),f(x));
print("解微分方程")
print(a);
# print(roots(x**2+2*x+1,x));
#{-1:2} 前面是根  后面是根的个数

#求导函数
print("求导函数")
s = diff(t, x,1);#1 次求导
print(s)

#求极限
print("求极限")
print(limit(sin(x),x,0));
# s = t;
# print(str(s));

#求泰勒级数  并且将最后的大O 去掉
print("求泰勒级数  并且将最后的大O 去掉")
t = series(t,x,0,8);
s = t;
s = str(s);
s = s[0:str(s).rfind("+ O",0,len(str(s)))];
print( s[0:str(s).rfind("+ O",0,len(str(s)))]);


#求积分
print("求积分")
s = integrate(exp(-x),(x,0,+oo))#积分 从0 到 正无穷
print(s);
# from numpy import *;
#
# exec("z = lambda x,y:"+str(s));
#
# print(z(2,3));

# t = 2*x**3 + 2*x + sin(x);
# t = series(t,x,0,8);#泰勒展开

#用于将符号表达式函数转换为numpy的数值表达式
print("用于将符号表达式函数转换为numpy的数值表达式")
s = diff(sin(x)+x**2)
t = lambdify(x,s,modules='numpy') #这句会把符号函数转换为数值函数  就不用上面的exec 来转换了
print(t);
print(t(np.array([1,2,3])))

#Converting Strings to SymPy Expressions
print("Converting Strings to SymPy Expressions")
str_expr = "x**2 + 3*x + y - 1/2"
expr = sympify(str_expr);
expr = diff(expr,x,1)
print(expr)


#多项式的拆分与合并
print("多项式的拆分与合并")
expr = apart(2/((x-2)*(x-3)));#拆分多项式
print(expr,x);
print(together(expr, x))#重新合并

#求连续 和  阶乘 以及 解方程组  其中Eq代表等式
print("求连续 和  阶乘 以及 解方程组")
n = symbols('n')
print(summation(x,(x,0,n)))#求极限和
print(factorial(n))#阶乘函数
print(solve([Eq(x + 5*y - 2,0), Eq(-3*x + 6*y - 15,0)], [x, y])) #解方程
# print(0.1**8);
# print(type(z));
# x1 = pd.Series([1,2,3]);
# x2 = pd.Series([1,2,3]);
# print(x1);
# print(z(array([1,2,3]),array([1,2,3])));
# print(cos(2));
# pprint(y);

#简化表达式
print("简化表达式")
print(simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1)))

#简化三角函数表达式
print(trigsimp(sin(x)**2 + cos(x)**2))

#展开三角函数
print(expand_trig(sin(x + y)))

#返回第二个质数
print(prime(2))

#表示分数
print("表示分数")
print(Rational(2,3));

