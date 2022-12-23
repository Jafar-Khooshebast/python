m =int(input("please set the row number:"))
n =int(input("please set the colomn number:"))

import numpy as np
 
# function to print Checkerboard pattern
def printcheckboard(m,n):
     
    # create a m * n matrix
    x = np.full((m,n), "*")
 
    # fill with # the alternate rows and columns
    x[1::2, ::2] = "#"
    x[::2, 1::2] = "#"

    # print the pattern
    for i in range(m):
        for j in range(n):
            print(x[i][j], end =" ")
        print()
 
 
printcheckboard(m,n)

# by: Jafar.Khooshebast