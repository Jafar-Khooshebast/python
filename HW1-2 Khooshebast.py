# inputs are 3 number for dimaesion of the triangle's sides
# in output we will tell you can we draw this triangle with these dimensions?
print("please enter dimensions of 3 sides of triangle")

a = float(input("\nplease enter first dimension: "))
b = float(input("please enter second dimension: "))
c = float(input("please enter third dimension: "))

if a < b + c  and  b < a + c  and  c < a + b :
    print("\n** These are (Valid) dimensions for drawing Triangle **")

else :
    print("\n** These are (Invalid) dimensions for drawing Triangle **")