# define function // second degree equation

# a*x**2 + b*x + c = 0

# delta = b**2 - 4*a*c

# x1 = -b + sqrt(delta) / 2*a
# x1 = -b - sqrt(delta) / 2*a

import math

print("second degree equation's format is a*x**2 + b*x + c = 0")

def second_degree_equation1():
    a=int(input("Please enter a: "))
    b=int(input("Please enter b: "))
    c=int(input("Please enter c: "))

    delta = b**2 - 4*a*c

    if delta == 0 :
        x = -b + math.sqrt(delta)
        print("The equation has a single routs. \n X= ",x)

    elif delta < 0:
        print("The equation has no answers in R")

    else :    
        x1=(-b + math.sqrt(delta)) / (2*a)
        x2=(-b - math.sqrt(delta))/(2*a)
        print("The equation has 2 answers in R.\n X1= ",x1, "\n X2= " , x2)

second_degree_equation1()

# by: Jafar.Khooshebast