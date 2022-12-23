#get the enterd numbers bye user
#continue this untill user enter "exit"
#after "exit" inout, show Sum of enterd numbers


print("this code will give you the Sum of inputs till you type 'Exit'")
count = 0
sum = 0
x = 0

while True:
    y = input("please enter the number: ")
    if y == 'Exit':
        print("sum of ", count, "entered number is: ", sum, "and the average is: ", sum/count)
        break
    x = float(y)
    count = count + 1
    sum = sum + x