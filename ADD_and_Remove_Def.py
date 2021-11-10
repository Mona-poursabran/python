#  Def Add and Remove :

def ADD (key, value) :
    if key not in dictionary:
        dictionary.update({key:value})
        return "Adding is done!"
    else:
        return f"This key ({key}) is in the dictionary!"
   

def REMOVE (key, value) :
    if key in dictionary and dictionary[k] == value:
        dictionary.pop(key)
        return "It's removed successfully!"
    else:
        return "Value is Wrong!"

dictionary = {} # global 

# first Step 
for i in range(1): 
    k, v = input("Enter key  and value : ").lower().split(",")
    print(ADD(k,v))
    
# second step
k, v, A_R = input("Enter a Key and value,choose ADD or REMOVE: ").lower().split(",") 

if A_R == "remove" or A_R ==" remove" :
    print(REMOVE(k,v))
elif A_R == "add" or A_R == " add" :
    print(ADD(k, v))
else:
    print("Invalid Input!")

# print(dictionary)











