# Using Loop
n, m =(input("Enter two nums: ")).split(" ")

count = 0

for i in range (0, int(n)): 
    a = input ("")
    for j in range (0, int(m)): 
        if a[j].count("*"):
            count += 1

if count == 1:
    print (f"There is {count} star.")
else:
    print(f"There are {count} stars.")





