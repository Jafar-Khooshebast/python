products = []
def read_file():
    f = open("E:\Jafar\pyhton course\projects\Homeworks\HW4\productsdata.txt", "r")
    for line in f:
        result = line.split(",")
        my_dic = {"id":result[0],"name":result[1],"price":result[2],"count":result[3]}
        products.append(my_dic)
        print(result)
       

# Show_menu Function
def show_menu():
    print("1- add")
    print("2- remove")    
    print("3- search")
    print("4- edit")
    print("5- show_list")
    print("6- buy")
    print("7- exit")

# Add product Function 
def add():
    id = input("id: ")
    name = input("name: ")
    price = input("price: ")
    count = input("count: ")  

    new_dic = {"id":id,"name":name,"price":price,"count":count}
    products.append(new_dic)
    print(products)

# Remove product Function
def remove():
    key = input("Enter your key: ")
    for product in products:
        if product["id"] == key or product["name"] == key:
            products.remove(product)
            print(products)
            show_list()
            break

# Search Function
def search():
    key = input("Enter your Key: ")
    for product in products:
        if product["id"] == key or product["name"] == key:
            print(product)
            break
    else:
        print("NOT FOUND")    

# Show_list Function
def show_list():
    print("id\tname\tprice\tcount")
    for product in products:
        print(product["id"],product["name"],product["price"],product["count"] )

# Buy Function
def buy():
    read_file()
    buy_list = []
    key = input("Enter ID or name of product: ")
    for product in products:
        if product["id"] == key or product["name"] == key:
            print(product)
            number = int(input("How many did you need? "))
            count = int(product["count"])
            price = int(product["price"])
            print(price)
            print(count)
            if count == 0:
                price("ERROR")
                break
            if number > count:
                print("Product shortage")
                break
            else:
                print("Available")
                
                b = input("Are you sure for your purchase?\n Yes=Y    No=N ")
                if b == "Y":
                    payable = number * price
                    print("Total price is: ", payable)
                    buy_list.append(product["name"])
                    buy_list.append(count)
                    buy_list.append(payable)
                    print(buy_list)
                    show_list()
                    break
            
# Save Function
def save():
    sv = input("Sure to Save?\n Yes=Y    No=N ")
    if sv == "Y":
        sv = open("database.txt", "a")
        for product in products:
            sv.write(str(product))
            sv.write("")
        print(product)
    else:
        print("did'nt save")


read_file()

while True:
    show_menu()

    user_choice = int(input("Enter you choice: "))

    if user_choice == 1:
        add()
    elif  user_choice == 2: 
        remove()
    elif  user_choice == 3:
        search()
    # elif  user_choice == 4:
    #     edit() 
    elif  user_choice == 5: 
        show_list() 
    elif  user_choice == 6:
        buy()
    elif  user_choice == 7:
        save()
        exit(0)  

    else:
        print("not in choise")   