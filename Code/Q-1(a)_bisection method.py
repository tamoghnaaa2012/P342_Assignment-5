#Question-1(a)
#Bisection Method

from Own_library import *
import math

def f(x):
    return(math.log(x)- math.sin(x))


q1a_1 = open("Q1a_Bisection_method.txt","w+")
ans = bisection_method(f,1.5,2.5,1.0e-07,q1a_1)

print("The solution is:", ans)
print("At root point the f(x)is   ",f(ans),"   which is tends to 0")



"""

Iterations   Absolute error
     1       5.000e-01
     2       2.500e-01
     3       1.250e-01
     4       6.250e-02
     5       3.125e-02
     6       1.562e-02
     7       7.812e-03
     8       3.906e-03
     9       1.953e-03
     10      9.766e-04
     11      4.883e-04
     12      2.441e-04
     13      1.221e-04
     14      6.104e-05
     15      3.052e-05
     16      1.526e-05
     17      7.629e-06
     18      3.815e-06
     19      1.907e-06
     20      9.537e-07
     21      4.768e-07
     22      2.384e-07
     23      1.192e-07
The solution is: 2.2191070318222046
At root point the f(x)is    -1.234698068230955e-07    which is tends to 0

Process finished with exit code 0



"""