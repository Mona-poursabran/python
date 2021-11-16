import csv
import os
import random 

class Score:
    def __init__(self) :
        self.score = 0
        self.result = ""
        self.remaining = 5
        self.q = 0  # Number of questions
        self.wrong = 0
        self.correct = 0

    def check_score (self, answer, correct_answer) :
        if  answer == correct_answer :
            self.score += 10
            self.correct += 1
        elif answer not in  correct_answer:
            self.score -= 3 
            self.wrong +=1
        else:
            self.score += 0
        self.remaining -= 1
        self.q += 1

    def check_winner (self):
        if self.score >= 40:
            self.result = "Congratulations!You are Winner."
            return self.result
        else :
            self.result = "Oops! Your are Loser."
            return self.result
            

    
    def __str__(self):  
        return f"Q\tCorrect\t\tWrong\t\tScore\t\tremaining:\n{self.q}\t  {self.correct}\t\t  {self.wrong}\t\t  {self.score}\t\t    {self.remaining}"

   


class Quiz :
    lst=[]  # it is used to save result 
    score = Score() # making an instance from class Score 

    def __init__(self, questions, answer):
        self.questions =questions
        self.answer = answer
        self.response = None
        self.__dict__


    def checking (self, response):  # check the response and correct answer + Using class Score 
            if response == self.answer:
                self.response = response
                print("Correct answer!")
            else:
                self.response = response
                print( "Wrong answer!")
            Quiz.score.check_score(response, self.answer)
            print(Quiz.score)
            
    def winner (self):
        print(f"You've got {Quiz.score.score} score.",Quiz.score.check_winner())
            

    def saving (self):   # save questios and user's answer
        with open ('save.txt', 'w') as save:
            write = csv.writer(save)
            self.lst.append(self.__dict__)
            write.writerows([self.lst])

    # def reading(self): # read saved file 
    #     with open ('save.txt', 'r') as read_ing:
    #         read = csv.reader(read_ing, delimiter= ",")
    #         for row in read:
    #             print(row)

    def __str__(self) :
        return f"Question: {self.questions}"


class TrueFalse (Quiz): 
    def __init__(self, questions, answer, selection): 
        super().__init__(questions, answer)
        self.selection = selection

    def checking(self, response): # override checking method 
        return super().checking(str(response).strip().capitalize()) 


class ShortAnswer(Quiz):
    def __init__(self, questions, answer, selection=[]): 
        super().__init__(questions, answer)
        self.selection = selection
    

    def checking(self, response): # override checking method 
        return super().checking(str(response).strip().lower()) 

    
class Multiplechoice (Quiz): 
    def __init__(self, questions, answer,selection):  
        super().__init__(questions, answer)
        random.shuffle(selection)   ## shuffle the choices 
        self.selection = selection


    def checking(self, response): # override checking method 
        return super().checking(str(response).strip().lower())
    

###################################################################
# main: 
All_Questions = []

with open ('questions.txt', 'r') as all_questions :
    reader = csv.reader(all_questions, delimiter=',')
    for i, row in enumerate(reader) :
        if i < 5 :
            All_Questions.append(TrueFalse(row[0], row[1], ["1.True", "2.False"]))  # append questions and correct answers + selections
        elif i < 10 :
            All_Questions.append(ShortAnswer(row[0], row[1]))
        else :
            All_Questions.append(Multiplechoice(row[0], row[1],row[1:]))  


questions_random = random.sample(range(0, 14), 5)  # return random numbers
# print(questions_random)



for i in questions_random:
    print(All_Questions[i])
    for item in All_Questions[i].selection:
        print(item)
    answer = input(">>>")
    All_Questions[i].checking(answer)
    print()
    All_Questions[i].saving()
os.system('cls')
All_Questions[i].winner()


        
        

    



