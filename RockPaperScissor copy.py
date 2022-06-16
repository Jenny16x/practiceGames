# Rock > scissors

# Scissors > paper

# Paper > rock 





# Generate random choice (random library)
# # afrom msilib.schema import Error
# import random

# mylist = ["rock", "paper", "scissor"]

# # print(random.choice(mylist))

# # Take in user choice user_input = input(“What is your choice? \n“)
# # user_input = input("type your choice here..")
# # print(" You throw out a " + user_input)
# # # Handle user errors

# comp_input = random.choice(mylist)
# user_input = input("type your choice here..")

# # mylist[1] or user_input ==  mylist[2] or user_input ==  mylist[3]:

# import sys

# # for entry in user_input:
# #     try:
# #         if user_input ==  mylist[0] or user_input ==  mylist[1] or user_input ==  mylist[2]:
# #             print(" You throw out a " + user_input)
# #             # print(" I throw out a " + comp_input)
# #             break
# #     except IndexError:
# #             print("Oops! Please check your spelling! Use all lower case!")
# #             # user_input = input("type your choice here..")

# for entry in user_input:
#     try:
#         if user_input ==  mylist[0] or user_input ==  mylist[1] or user_input ==  mylist[2]:
#             print(" You throw out a " + user_input)
#             # print(" I throw out a " + comp_input)
#             break
#     except IndexError:
#             print("Oops! Please check your spelling! Use all lower case!")
#             # user_input = input("type your choice here..")



# Output random choice & user choice (respectively - sanity check) 
# Determine winner option between random_choice & user_choice (switch case)
# Output winner (computer or user)
# BONUS: Keep score?
# Create score (starting at 0)
# After each game 
# Update score
# Ask user if they want to (1) play again or (2)start over or (3) quit game & close app




# If rock and rock: 

# Print (TIE) 



# If user = rock and computer = scissors:

# print(YOU WIN)+1 to user score


import random
import sys


mylist = ["rock", "paper", "scissor"]
comp_input = random.choice(mylist)
user_input = input("type your choice here..")

for entry in user_input:
    try:
        if user_input ==  mylist[0] or user_input ==  mylist[1] or user_input ==  mylist[2]:
            print(" You throw out a " + user_input)
            # print(" I throw out a " + comp_input)
            break
    except IndexError:
            print("Oops! Please check your spelling! Use all lower case!")