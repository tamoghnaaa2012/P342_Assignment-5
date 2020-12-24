#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

def bisection_method(f,a,b,tol,file):
    step = 0                                   #iteration counter
    
    for i in range(1,200):
        if f(a)*f(b)<0:
            continue
        else:
            if (abs(f(a)) < abs(f(b))):
                a=a - 0.5*(b-a)
            else:
                b=b + 0.5*(b-a)                #upto this portion we are bracketing
            
            
            
    print("{:<12} {:<12}".format("Iterations", "Absolute error"))       #This is used to tabulate the output                  
    while(b-a)/2.0 >tol and step<200:
            mid_point = (a+b)/2.0
            #print("Iteration-%d ,mid_point= %f ,f(mid_point) =%f)" %(step,mid_point,f(mid_point)))
            #print('Iteration-%d,')
            if f(mid_point)==0:
                return(mid_point) #The midpoint is the root;
            elif f(a)*f(mid_point) < 0:
                b = mid_point
                
            else:
                a= mid_point
               
            step = step+1
            #print(f(a))
            #print(a)
            #print(f(b))
            #print(b)
            #print(f(a)*f(b))
            error=abs(b-a)
            file.write("{:^12} {:<12.3e}\n".format(step, error))
            print("{:^12} {:<12.3e}".format(step, error))
    file.close()            
    return(mid_point)




def regula_falsi(f,a,b,tol,file):
    step=0
    
                                                ## a,b is initial guess
        
    for i in range(1,200):
        if f(a)*f(b)<0:
            continue
        else:
            if (abs(f(a)) < abs(f(b))):
                a=a - 0.5*(b-a)
            else:
                b=b + 0.5*(b-a)                 ## Upto this portion we are bracketing.
    
    
    
    
    last_c=a 
    c=a+1*tol
    condition = True
    print("{:<12} {:<12}".format("Iterations", "Absolute error"))     #This is used to tabulate the output
    while condition and step<200:
        last_c=c
        c = b - ((b-a)*f(b))/(f(b)-f(a))
        #print(c)
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
        step =step+1
        error =abs(c-last_c)
        #print(error)
        condition = abs(f(c))>tol
        file.write("{:^12} {:<12.3e}\n".format(step, error))
        print("{:^12} {:<12.3e}".format(step, error))
        
    file.close()    
    return (c)



def N_raphson(f,derivative, x0, tol,file):
    step=0
    last_X = x0
    next_X = last_X + 1* tol                          # "different than lastX so loop starts OK
    print("{:<12} {:<12}".format("Iterations", "Absolute error"))
    while (abs(next_X - last_X) >= tol) and step<200:              # this is how you terminate the loop - note use of abs()
        new_Y = f(next_X)                     
        step =step+1
        last_X = next_X
        next_X = last_X - new_Y / derivative(f, last_X, tol)  # update estimate using N-R
        error = abs(next_X-last_X)
        
        file.write("{:^12} {:<12.3e}\n".format(step, error))
        print("{:^12} {:<12.3e}".format(step, error))
        
    file.close()    
    return next_X

def laguerre(f,f_derivative,s_derivative,alpha,n,tol,file):
    if f(alpha)== 0:
        print("The root is",alpha)
    else:
        alpha1=alpha+ 1*tol              # "different than lastX so loop starts OK
        step=0
        print("{:<12} {:<12}".format("Iterations", "Absolute error"))
        while abs(alpha1-alpha)>tol and step<200:
            step = step+1
           
            G = f_derivative(alpha,0.4,f)/f(alpha)
            H = G*G-(s_derivative(alpha,0.4)/f(alpha))
            F =math.sqrt((n-1)*(n*H-(G*G)))
           
            if abs(G+F)<abs(G-F):
                a = n/(G-F)
            else:
                a = n/(G+F)
            alpha1=alpha    
            alpha = alpha -a
            error= (alpha1-alpha)
            file.write("{:^12} {:<12.3e}\n".format(step, error))
            print("{:^12} {:<12.3e}".format(step, error))
       
            #print(step,error)
            print()
        file.write("{:^12} {:<12}\n".format("Iter number", "error"))    
        print("The root is",alpha)
       
    return (alpha)



def synthetic_div(coeff,alpha):
    while abs(coeff[0])!=1:
        for k in range(len(coeff)):
            coeff[k]=coeff[k]/coeff[0]

    for l in range(1,len(coeff)):
        coeff[l]=coeff[l]+alpha*coeff[l-1]
    #print("Coeff",coeff)
    return (coeff)


