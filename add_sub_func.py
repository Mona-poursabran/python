# Using map function for adding and subtracting :)
def my_lists(x, y):
    return x + y, x - y


x = list(map(int, input("list1:E.g(1, 25, ...) ").split(",")))
y = list(map(int, input("list2:E.g(1, 25, ...) ").split(",")))

result = list(map(my_lists, x, y))

print("Result: ", result)


# app_lst = []

# for i in range(len(result)) :
#     # print(result[i], end=", ")
#     app_lst.append(result[i])

# print("\n", app_lst)



















