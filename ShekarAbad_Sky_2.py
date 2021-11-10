
# without using loop :

n, m =(input("Enter two nums: ")).split(" ")

s = int(n) * int(m)

star = input(f"{s} characters: ")

if len(star)> s or len(star) < s :
    print('Wrong! more or few characters are entered')
else:
    print("Stars: {}".format(star.count("*")))
    