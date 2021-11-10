# with elif
n = input("Enter 5 letters (G or Y or R): ").upper()

G = n.count('G')
R = n.count ('R')
Y = n.count('Y')

if len(n) != 5:
    print("You've entered more or few characters")
elif R == len(n) or Y == len(n)  or R >= 2 or Y >=2 :
    print("Nakhor Lite! :(")
else:
    print("Rahat Bash Lite :)")