# with for  loop and elif

n = input("Enter 5 letters (G or Y or R): ")

G = 0
R = 0
Y = 0

for ch in n :
    if ch.count("g") or  ch.count("G"):
        G+= 1
    elif ch.count("r") or ch.count("R"):
        R+= 1
    elif ch.count("y") or ch.count("Y"):
        Y+= 1


if len(n)!= 5:
    print("You've entered more or few characters.")
elif R == len(n) or Y == len(n)  or R >= 2 or Y >=2 :
    print("Nakhor Lite! :(")
else:
    print("Rahat Bash Lite :)")
