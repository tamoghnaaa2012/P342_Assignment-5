#Question-2
#Laguerre's method and synthetic division method

import math
from Own_library import *




def polyfunc(x,n,coeff):
    result=0
    for i in (range(1,n+1)):
        if i==n:
            result=result+coeff[i-1]
        else:
            result=result+coeff[i-1]*x**(n-i)
    return (result)

def f(x):
    return polyfunc(x,n,coeff)

def f_derivative(x,h,f):
    s = (f(x+h)-f(x-h))/(2*h)
    return s
def s_derivative(x,h):
    s = (f(x+h)+f(x-h)-2*f(x))/(2*h*h)
    return s
file = open("Q2_polynomial.txt","w+")
coeff = [1,-3,-7,27,-18]
n=5
tol=1.0e-06
alpha=float(input("Enter your first guess"))
while n>1:
    coefficients = synthetic_div(coeff,laguerre(f,f_derivative,s_derivative,alpha,n,tol,file))
    n= n-1
    print(coefficients)
    print()



"""

Enter your first guess2.5
Iterations   Absolute error
     1       5.385e-01   

     2       -4.592e-02  

     3       8.785e-03   

     4       -1.673e-03  

     5       3.187e-04   

     6       -6.071e-05  

     7       1.156e-05   

     8       -2.203e-06  

     9       4.195e-07   

The root is 1.999999932873082
[1, -1.000000067126918, -9.000000067126914, 9.000000469888437, 3.356345814609085e-07]

Iterations   Absolute error
     1       -5.868e-01  

     2       8.330e-02   

     3       3.414e-03   

     4       4.875e-05   

     5       6.422e-07   

The root is 3.000000036532766
[1, 1.9999999694058481, -3.0000000858438387, 1.0275861939135211e-07, 6.439104433890214e-07]

Iterations   Absolute error
     1       1.296e+00   

     2       1.994e-01   

     3       4.991e-03   

     4       3.115e-06   

     5       1.213e-12   

The root is 1.0000000291094977
[1, 2.999999998515346, 0.0, 1.0275861939135211e-07, 7.466690657716253e-07]

Iterations   Absolute error
     1       5.500e+00   

     2       4.441e-15   

The root is -2.999999998515346
[1, 0.0, 0.0, 1.0275861939135211e-07, 4.3839320775013e-07]


Process finished with exit code 0

"""