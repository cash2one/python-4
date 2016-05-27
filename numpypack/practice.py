import numpy as np;
from sympy.utilities.lambdify import lambdify;




if(__name__=="__main__"):
    a = [[1,2,3],[4,5,6]];
    a = np.array(a);

    for i in a:
        print(i)