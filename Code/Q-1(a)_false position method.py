#Question-1(a)
#False position method

from Own_library import *
import math
def f(x):
    return(math.log(x)-math.sin(x))


q1a_2 = open("Q1a_regula_falsi.txt","w+")
ans= regula_falsi(f,1.5,2.5,1.0e-07,q1a_2)
print("The solution is:",ans)
print("At root point the f(x)is  ",f(ans),"   which is tends to 0")





"""
Iterations   Absolute error
     1       6.507e-01   
     2       6.359e-02   
     3       4.499e-03   
     4       3.070e-04   
     5       2.089e-05   
     6       1.421e-06   
     7       9.672e-08   
The solution is: 2.2191071418525734
At root point the f(x)is   -7.445812411077668e-09    which is tends to 0

Process finished with exit code 0


"""