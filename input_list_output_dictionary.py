lst = eval(input("Enter a list by using bracket [ ]: "))

print(lst)

empty_dict = {}
new_dict = empty_dict

for item in lst:   # return each item in a list 
    empty_dict[item] = {}   # key = 1 : value = {} => {1:{}}
    empty_dict = empty_dict[item]

print(new_dict)

print(empty_dict)

