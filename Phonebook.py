## Phonebook:
def Add_user_info (name, last_name, cell, birth, email) :
    if (name=="" or  last_name == "" or cell == "") :
        print("fill * parts !")
    else:   
        dict_info.update({"name":name, "last name":last_name, 
                            "cell": cell, "birthday":birth, "email":email})
        print("Information saved...")
    list_info.append(dict_info.copy())
    return list_info


def search (item) : 
    for i in range(len(list_info)):  
        for j in list_info[i]:
            if list_info[i][j] == item:
                print("User's info is found: ")
                for k , v in list_info[i].items():
                    print(f"{k}: {v}")
            
            
def view_all_info ():
    for i in range(len(list_info)):
        for k, v in list_info[i].items():
            print(k,":",v)
        print("***************")


def menu ():
    print("Menu: ")
    print("1.Add a new user")
    print("2.Search")
    print("3.View all info")
    print("4.Exit ")
    print()

dict_info = {}
list_info = []

# First step : save at least one user's info 
for i in range(1):
    print("Enter new user's information:(filling * is necessary)")
    name = input("* Name: ").capitalize().strip()
    last_name = input("* Last_name: ").capitalize().strip()
    cell = input("* Phone number: ").strip()
    birth = input("Birthday:(yyyy/mm/dd)=>1371/06/11:  ")
    email = input("Email: ")
    Add_user_info(name, last_name, cell, birth, email)

print("---------"*5)
num_menu = 0
while num_menu != 4:
    menu()
    num_menu =int(input("Enter a number from the menu: "))

    if num_menu == 1 :
        print("Enter new user's information:(filling * is necessary)")
        name = input("* Name: ").capitalize().strip()
        last_name = input("* Last_name: ").capitalize().strip()
        cell = input("* Phone number: ").strip()
        birth = input("Birthday:(yyyy/mm/dd)=>1371/06/11:  ")
        email = input("Email: ")
        Add_user_info(name, last_name, cell, birth, email)
        print("---------"*5)
    elif num_menu == 2 :
        item = input("Enter a Name or phone number :").capitalize().strip()
        search(item)
        print("---------"*5)
    elif num_menu == 3 :
        view_all_info()
        
