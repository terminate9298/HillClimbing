import math 


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
    
    delta_x =  -47 * sin(sqrt(sqrt((x[0]/2 + x[1] + 47)**2))) - x[0]*sin(sqrt(sqrt((x[0]-x[1]-47)**2)) - x[1]*sin(sqrt(sqrt((x[0]/2 + x[1] + 47)**2))))
    return x[0] -  (scalar*delta_x), x[1] - (scalar*delta_x)

# Definition of  the first function 
def f_1(x):
    """ Function => f(x) = -(x2 + 47)sin(sqrt(|x2+(x1/2)+47|)) - x1*sin(sqrt(|x1-(x2+47)|)) """
    return -((x[1] + 47)* sin(sqrt(abs(x[1]+(x[0]/2)+47)))) - (x[0]*sin(sqrt(abs(x[0]-(x[1]+47)))))
    # return -((x + 47)* sin(sqrt(abs(x+(x/2)+47)))) - (x*sin(sqrt(abs(x-(x+47)))))


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
    x_init = []
    x_init.append(float(input("Please Enter number one for first element starting point : ")))
    x_init.append(float(input("Please Enter number Two for second element starting point : ")))    
    hill_climb(f_1 ,x_init,gradient_descent) 
