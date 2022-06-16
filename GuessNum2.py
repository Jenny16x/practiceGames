
# Create function
# Generate random number
# Ask for user input
# If user input number = generated number then user win, display do you want to play again y/n
# If user input number not = to generated number then user lose
# If user input is < than than generated number then display “too low”
# If user input is > than than generated number then display “too high”

import random

# def game():

# while user_input == comp_output:
#     comp_output = random. randint(0,50)
# # print (comp_output)
#     user_input = int(input("Guess my number .. between 1-50:")) 
#     isval= False
#     while isval == False:
#         user_input = int(input("Guess my number .. between 1-50:")) 
#         if (user_input in comp_output):
#             break
#         print("Oops! invalid input.. ")
#     print("let's play..")

comp_output = random. randint(0,50)
print (comp_output)
user_input = int(input("Guess my number .. between 1-50:")) 

#while user_input == comp_output:
if user_input == comp_output : 
    print ("You Win!") 
isval= False
while isval==False:
    user_input = int(input("Guess my num .. between 1-50:")) 
    if (user_input < comp_output) : 
        break
    print ("Too low!")
    user_input = int(input("Try again .. my number is in between 1-50:")) 
    if (user_input > comp_output) :
        break
    print ("Too high try again!")
    user_input = int(input("Try again .. my number is in between 1-50:"))
print("Wanna guess my number?")


