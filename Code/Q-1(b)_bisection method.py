#Question-1(b)
#Bisection method

from Own_library import *
import math

def f(x):
    return(-x- math.cos(x))


q1b_1 = open("Q1b_Bisection_method.txt","w+")
ans = bisection_method(f,-1,1,1.0e-07,q1b_1)

print("The solution is:", ans)
print("At root point the f(x)is   ",f(ans),"   which is tends to 0")




"""
Iterations   Absolute error
     1       1.000e+00   
     2       5.000e-01   
     3       2.500e-01   
     4       1.250e-01   
     5       6.250e-02   
     6       3.125e-02   
     7       1.562e-02   
     8       7.812e-03   
     9       3.906e-03   
     10      1.953e-03   
     11      9.766e-04   
     12      4.883e-04   
     13      2.441e-04   
     14      1.221e-04   
     15      6.104e-05   
     16      3.052e-05   
     17      1.526e-05   
     18      7.629e-06   
     19      3.815e-06   
     20      1.907e-06   
     21      9.537e-07   
     22      4.768e-07   
     23      2.384e-07   
     24      1.192e-07   
The solution is: -0.7390850782394409
At root point the f(x)is    -9.200802475461956e-08    which is tends to 0

Process finished with exit code 0


"""


