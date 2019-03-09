import math 
import numpy as np 

fabs = math.fabs
sin = math.sin
cos = math.cos
exp = math.exp
pi = math.pi
sqrt = math.sqrt

#scalar multiple for grad-ascent
scalar=0.005


# dar inja shibe khat mohasebeh mishavad.
def gradient_descent(x):
    d = 5
    delta = [] 
    for i in range(len(x)):
        delta.append(x[i] * sin(sqrt(abs(x[i])))) 
    delta_x =  418.9829*d - sum(delta)
    return x[0] +  (scalar*delta_x), x[1] + (scalar*delta_x), x[2] +  (scalar*delta_x), x[3] + (scalar*delta_x),x[4] +  (scalar*delta_x),

# Definition of the second function 
def f_2(x):
    """ Function => f(x) = 418.9829d - sigma(xi*sin(sqrt(|xi|))) """ 
    d = 5
    delta = [] 
    for i in range(len(x)):
        delta.append(x[i] * sin(sqrt(abs(x[i]))))
    return 418.9829*d - sum(delta)

#Definition of the simple hill climbing search
def hill_climb(objfunc,x,next_move):
    current = x
    with open("result.txt","w") as result:
        while True:
            current_val=objfunc(current)
            next = next_move(current)
            if objfunc(next) < current_val:
                current = next
                print (current,current_val)
                result.write(f"The points is : {current} and the current result value is : {current_val} ")
            else:
                break
    
if __name__=='__main__':
    x_init = [ float(input("Please enter the start point : ")) for i in range(5)]
    # x_init.append(float(input("Please Enter number one for first element starting point : ")))
    # x_init.append(float(input("Please Enter number Two for second element starting point : ")))    
    # x_init.append(float(input("Please Enter number one for third element starting point : ")))
    # x_init.append(float(input("Please Enter number one for fourth element starting point : ")))
    # x_init.append(float(input("Please Enter number one for fifth element starting point : ")))
    hill_climb(f_2 ,x_init,gradient_descent) 
