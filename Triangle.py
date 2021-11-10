n = int(input(" Num: "))

for i in range(n, 0, -1):
    if  i == n or i == 1:
       print( "*" * (i))
    else:
        s = "*" + " " * (i-2) + "*"
        print(s)

