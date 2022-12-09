#calculator with bellow operation

 
import math

#operations for 2 inputs: +, -, *, /
#operations for single input: radical, sin, cos, tan, factorial

type = int(input("which operations do you need? 2 inputs or 1 input? "))


if type == 1 :

    a = float(input("plz enter number: "))
    print("operations are sqrt, sin, cos, tan, cot, factorial")
    op = input("please enter operation: ")
    
    if op == "sqrt" :
        result =  math. sqrt(a)
    
    if op == "sin" :
        result = math.sin(a)

    if op == "cos" :
        result = math.cos(a)        

    if op == "tan" :
        result = math.tan(a)

    if op == "cot" :
        result = math.cot(a)

    if op == "factorial" :
        result = math.factorial(a)


if type == 2 :
    
    b = float(input("plz enter first number: "))
    c = float(input("plz enter second number: "))
    op = input("please enter operation: ")

    if op == "+":
        result = b + c

    if op == "-":
        result = b - c

    if op == "*":
        result = b * c

    if op == "/":
        result = b / c


print(result)