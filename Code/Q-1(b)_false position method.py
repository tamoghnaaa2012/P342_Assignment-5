#Question-1(b)
#False position method

from Own_library import *
import math
def f(x):
    return(-x-math.cos(x))


q1b_2 = open("Q1b_regula_falsi.txt","w+")
ans= regula_falsi(f,-1,1,1.0e-07,q1b_2)
print("The solution is:",ans)
print("At root point the f(x)is   ",f(ans),"   which is tends to 0")



"""

Iterations   Absolute error
     1       4.597e-01   
     2       1.877e-01   
     3       1.052e-02   
     4       5.302e-04   
     5       2.657e-05   
     6       1.331e-06   
     7       6.666e-08   
The solution is: -0.7390851296998365
At root point the f(x)is    -5.883288745067716e-09    which is tends to 0

Process finished with exit code 0

"""