# inputs are name, family, 3 scores for 3 lessons
# in output we will show the statue of this student

print("please Fill the bellow form out: ")

name = input("please enter your name: ")
family = input("please enter your family: ")

a = float(input("please enter your Math score: "))
b = float(input("please enter your Physics score: "))
c = float(input("please enter your Programming score: "))

avg = (a + b + c) / 3

if avg >= 17 :
    print(name, family, "'s statue is (Graet)")

if 12 <= avg < 17 :
    print(name, family, "'s statue is (Normal)")

if avg < 12 :
    print(name, family, "'s statue is (Fail)")
