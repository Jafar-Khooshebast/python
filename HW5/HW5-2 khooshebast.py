class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

# show function
    def show(self):
        print(self.h, ":", self.m, ":", self.s)

# Sum function
    def sum(self, t2):
        result = Time(None, None, None)
        result.h = self.h + t2.h
        result.m = self.m + t2.m
        result.s = self.s + t2.s

        if result.s >= 60:
            result.s -= 60
            result.m += 1

        if result.m >= 60:
            result.m -= 60
            result.h += 1

        return result

# Subtraction function
    def minus(self, t2):
        result = Time(None, None, None)
        result.h = self.h - t2.h
        result.m = self.m - t2.m
        result.s = self.s - t2.s
        
        if result.s < 0:
            result.s += 60
            result.m -= 1

        if result.m < 60:
            result.m += 60
            result.h -= 1

        return result

# Convert time to second
    def TtoS(self):
        convert1 = 3600 * self.h + 60 * self.m + self.s
        return convert1


def StoT(self):
    hour = int(self/3600)
    minute = int((self-hour*3600)/60)
    second1 = int(self - hour*3600 - minute*60)
    return [hour, minute, second1]

time1 = Time(10, 20, 25)
time2 = Time(8, 30, 40)
sanie = 7393

print("time1 is: ")
time1.show()

print("time2 is: ")
time2.show()

s = time1.sum(time2)
print("time1 + time2 is equal to: ")
s.show()

m = time1.minus(time2)
print("time1 - time2 is equal to: ")
m.show()

second = time1.TtoS()
print("time1 convert to second:\n" ,second)

time = StoT(sanie)
print ("second convert to Time:\n", time[0], ":", time[1], ":", time[2])



# By: Jafar.Khooshebast

