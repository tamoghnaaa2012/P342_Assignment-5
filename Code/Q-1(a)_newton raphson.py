#Question-1(a)
#Newton Raphson method


from Own_library import *

import math
def derivative(f, x, h):
      return (f(x+h) - f(x-h)) / (2.0*h)  # might want to return a small non-zero if ==0

def f(x):
    return (math.log(x)- math.sin(x))    # just a function to show it works

q1a_3 = open("Q1a_Newton_raphson.txt","w+")
ans = N_raphson(f,derivative, 3, 1.0e-06,q1a_3)    # call the solver
print("The solution is:",ans)
print("At root point the f(x)is   ",f(ans),"   which is tends to 0")






"""
Iterations   Absolute error
     1       7.236e-01   
     2       5.647e-02   
     3       8.720e-04   
     4       2.141e-07   
The solution is: 2.219107148913759
At root point the f(x)is    1.3433698597964394e-14    which is tends to 0

Process finished with exit code 0

"""