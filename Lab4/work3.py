# import random
# r = ["scissor","rock","paper"]
# computer = print(random.choice(r))
# user = input("scissor(0),rock(1),paper(2)")
# if user ==1 and computer == "scissor":
#    print("The computer is scissor. You are rock. you won")


import random

r = ["scissor", "rock", "paper"]
computer = random.choice(r)

user = input("Choose: scissor(0), rock(1), paper(2):")

if user == "0":
    user_choice = "scissor"
elif user == "1":
    user_choice = "rock"
elif user == "2":
    user_choice = "paper"
else:
    print("Invalid input")
    exit()


if user_choice == computer:
    print("The same")
elif (user_choice == "rock" and computer == "scissor") or \
     (user_choice == "scissor" and computer == "paper") or \
     (user_choice == "paper" and computer == "rock"):
    print("The computer is",computer ,"You are",user_choice,"You won!")
else:
    print("The computer is",computer ,"You are",user_choice,"Computer won!")