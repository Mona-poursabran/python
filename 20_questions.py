import random

words = ["apple", "snake", "pen", "cinema", "shark"]

random_word = random.choice(words) 
# print(random_word)

questions =[[{"1.Is it edible?":"Yes"}, {"2.Is it alive?":"No"},{"3.Is it used in food?": "No"},
            {"4.Is it a fruit?":"Yes"},{"5.Is it round?":"Yes"},{"6.Is it sweet?":"Yes"},
            {"7.Can you have it just in winter?":"No"},{"8.Have i eaten it yet?":"Yes"}, 
            {"9.Is it meat?":"No"}, {"10.Does it live in a jungle?":"No"}], 
           
            [{"1.Is it an animal?":"Yes"},{"2.Is it alive":"Yes"},
            {"3.Does it eat meat?":"Yes"}, {"4.Is it a common pet?":"No"},
            {"5.Is it a mammal?":"No"},{"6.Can it fly?":"No"},{"7.Does it live in jungle?":"Yes"},
            {"8.Is it a reptile?":"Yes"}, {"9.Is it small?":"No"}, {"10.Do a lot of people love it?":"No"}],

            [{"1.Is it edible?":"No"}, {"2.Is it alive?":"No"}, {"3.Is it light enough to pick up?":"Yes"},
            {"4.Can it fly?":"No"},{"5.Would it be expensive to buy?":"No"},{"6.Is it used more for work?":"Yes"},
            {"7.Do some people have it?":"Yes"},{"8.Can it fly?":"No"},{"9.Is it big?":"No"},{"10.Is it useful?":"Yes"}],

            [{"1.Is it edible?": "No"},{"2.Is it alive?": "No"},{"3.Is it a place?":"Yes"},{"4.Is it famous?":"Yes"},
            {"5.Is it often crowded?":"Yes"},{"6.Would I need a plane to reach it?":"No"},{"7.Is it cold?":"No"},
            {"8.Do some people like it?":"Yes"},{"9.Can we visit each other there?":"Yes"},{"10.Is it small?":"No"}],

            [{"1.Is it edible?": "No"},{"2.Is it alive": "Yes"},{"3.Does it eat meat?":"Yes"},{"4.Can it fly?":"No"},
            {"5.Does it live in the ocean?":"Yes"},{"6.Is it a mammal?":"Yes"},{"7.Is it a common pet?":"No"},
            {"7.Do I have it?": "No"},{"8.Is it beautiful?":"No"},{"Is it big?":"Yes"}]]

ind = words.index(random_word)
# print(ind)

score = 100
quess_num = 3
guess_list = {}
counter = 1

while quess_num != 0 and score > 0 :
    print()
    for d in questions[ind] :
        print(list(d.keys())[0])
    print()
    num = int(input("choose a num or enter 0 to guess: "))

    if num == 0:

        guess = input("Guess: ").strip()
        # guess = ''.join(char for char in guess if char.isalpha()).lower()
        guess_list[counter] = guess
        counter += 1
        if guess == random_word:
            score += 20
            print("You are winner :)","\n", f"Score: {score}")
            break
        else :
            score -= 10
            print("Wrong guess!")
    else:
        question= list(questions[ind][num-1].keys())[0]
        answer = list(questions[ind][num-1].values())[0]
        print(question, answer)
        score -= 5
        quess_num -= 1

    print("score", score)
    print("*******"*5)

     
if quess_num == 0 or score == 0 :
    print("You are loser :(")

print("Your Guesses:", guess_list, "\n", "Answer: ", random_word)




   




