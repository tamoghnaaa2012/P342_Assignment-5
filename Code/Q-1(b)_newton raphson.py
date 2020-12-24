#Question-1(b)
#Newton Raphson method


from Own_library import *

import math
def derivative(f, x, h):
      return (f(x+h) - f(x-h)) / (2.0*h)  # might want to return a small non-zero if ==0

def f(x):
    return (-x- math.cos(x))    # just a function to show it works

q1b_3 = open("Q1b_Newton_raphson.txt","w+")
ans = N_raphson(f,derivative, 3, 1.0e-04,q1b_3)    # call the solver
print("The solution is:",ans)
print("At root point the f(x)is   ",f(ans),"   which is tends to 0")




"""
Iterations   Absolute error
     1       2.340e+00   
     2       3.748e+00   
     3       3.878e+00   
     4       5.164e+00   
     5       8.264e+01   
     6       1.062e+02   
     7       2.134e+01   
     8       4.354e+00   
     9       1.579e+00   
     10      9.560e-02   
     11      2.125e-03   
     12      9.958e-07   
The solution is: -0.7390851332153789
At root point the f(x)is    3.65374397404139e-13    which is tends to 0

Process finished with exit code 0


"""