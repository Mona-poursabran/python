# import csv
# import random 

# class Quiz :

#     questions =["What is the past form of go?", "What is the synonym of vital?",
#                 "What is the verb of beautiful?", "what is the past participle of take?",
#                 "what is the part speech of friendly?", "Iran is The biggest country in Asia.\nTrue\nFalse",
#                 "sky is red.\nTrue\nFalse","The word 'education' is uncountable noun.\nTrue\nFalse",
#                 "Farm animal's author is charles dickens.\nTrue\nFalse",
#                 "what does the word 'insomnia' mean?\nA)unable to sleep \tB)unable to think \tc)unable to eat \tD)unable to concentrate",
#                 "what does the word 'essential' mean?\nA)hard \tB)difficult \tC)necessary \tD) awful",
#                 "what does the word 'hoard' mean?\nA)happy \tB)store \tC)sad \tD)confusing",
#                 "what does the word 'umpire' maen?\nA)stingy \tB)unhappy \tC)referee \tD)tough"]

#     answers =["went", "important", "beautify", "taken", "adverb",
#              "False", "False", "True", "False",
#              "a","c","b","c"]

#     def __init__ (self):
#         self.score = 0


#     def check_answer (self, responce):
#         for i in range(len(self.answers)):
#             if responce == self.answers[i]:
#                 return True
#             else:
#                 return False


#     def __str__(self):
#         for i in range(len(self.questions)):
#             return f"{self.questions[i]}"


# class TrueFalse (Quiz):
#     questions = Quiz.questions[5:9]
#     answers = Quiz.answers[5:9]

#     def check_answer(self, responce):
#         return super().check_answer(responce)



# class ShortQuestion(Quiz):
#     questions = Quiz.questions[:5]
#     answers = Quiz.answers[:5]

#     def check_answer(self, responce):
#         return super().check_answer(responce)
    
# class MultipleChoice(Quiz):
#     questions = Quiz.questions[9:]
#     answers = Quiz.answers[9:]

#     def check_answer(self, responce):
#         return super().check_answer(responce)


# t = TrueFalse()
# # print(t.questions)
# # print(t.answers)
# # print()
# s = ShortQuestion()
# # print(s.questions)
# # print(s.answers)
# # print()
# m = MultipleChoice()
# # print(m.questions)
# # print(m.answers)

# n = 0
# score = 0
# while n != 5 :
#     print("Quesion_1.",t.questions[0])
#     answer = input("Answer: ").capitalize()
#     t.check_answer(answer)
#     if answer == t.answers[0]:
#         score +=10 
#     else:
#         score -= 3 
#     n +=1
#     print("Quesion_2.",s.questions[0])
#     answer = input("Answer: ").lower()
#     if answer == s.answers[0]:
#         score +=10
#     else:
#         score -= 3
#     n +=1
#     print("Quesion_3.",m.questions[0])
#     answer = input("Answer: ").lower()
#     if answer == m.answers[0]:
#         score +=10
#     else:
#         score -= 3
#     n +=1
#     print("Quesion_4.",t.questions[1])
#     answer = input("Answer: ").capitalize()
#     if answer == t.answers[1]:
#         score +=10
#     else:
#         score -= 3
#     n +=1
#     print("Quesion_5.",m.questions[1])
#     answer = input("Answer: ").lower()
#     if answer == m.answers[1]:
#         score +=10
#     else:
#         score -= 3
#     n +=1

# if score > 40 :
#     print("Winner")
# else:
#     print("Loser")

# print(score)

