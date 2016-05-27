import numpy as np;
from sympy.utilities.lambdify import lambdify;

from sympy import *;
import matplotlib as matplot;
from matplotlib import pyplot as plt;
a = np.random.randn(2,3)+np.random.randint(1,100,(2,3));
b = np.random.randint(1,100,(2,3));
c = np.modf(a);
print(np.hstack((a,b)));
xBian = symbols("x");
yBian = symbols("y");
print(c)
x = np.linspace(0,2*np.pi,200);
figure = plt.figure();
ax = figure.add_subplot(1,1,1);


ax.axis([ 0, 10, 0, 5 ])
ax.set_xlabel("x")
ax.set_ylabel("y")
pt, = ax.plot(x,np.sin(x));#因为会返回来很多值
ax.legend([pt], [ 'nope'],loc='upper right')


# plt.plot(x,np.cos(x),hold = false); #hold = false  意味着不保存之前画的图像


plt.show();
# a = np.arange(0,60,10).reshape(-1,1) + np.arange(0,6,1);
# print(a)
# print(np.arange(0,60,10).reshape(-1,1).shape)
# print(b.T)
