# you will say how many array you want in output
# in output will show a list with random array amount
#numpy library used in this code

import numpy as np

n = int(input("type your array range: "))

randnums= np.random.randint(1,101,n)

randnums