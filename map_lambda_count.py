
## Using for loop
lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
c = 0
for i in lst1:
    for j in i:
        if j.count('A') or j.count('a'):
            c += 1
# print("Using for loop: ",c)


## Using list comprehension:
a = [j for i in lst1 for j in i if j.count('A') or j.count('a')]
# print("Comprehension: ",a.count('A') + a.count('a'))


## Using map and lambda :
print(sum( list(map(lambda lst: lst[:].count('A') + lst[:].count('a') , lst1))))

