# set syntax can't store duplicate array in itself.
# we can use **set** in order to delete duplicated array in a list
# than make a list from that set
# the new list will be without duplicated array.

def delete_duplicate(x):
    return list(set(x))

mylist = delete_duplicate([1, 2, 3, 3, 4, 5, 5, 6, 2, 7, 8, 9, 10, 10, 6])

print(mylist)

# by: Jafar.Khooshebast