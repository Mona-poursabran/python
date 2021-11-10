# if letter in string:
#     print(string.count(letter))
# else :
#     print(string.find(letter))
#### Do top code with a for loop :)

string = input(" Enter sth: ").lower()
letter = input ("Enter one letter: ").lower()

l = string.count(letter)
if l:
    print(l)
else:
    print("-1")

# counter = 0
# for i in string:
#     if i in letter:
#         counter += 1
# if counter == 0:
#     print(-1)
# else: 
#     print(counter)
    
