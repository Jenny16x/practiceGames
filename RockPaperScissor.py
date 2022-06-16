import random

user_score = 0
comp_score = 0


while user_score <5 and comp_score<5:
    mylist = [1, 2, 3]
    comp_output = random.choice(mylist)

    isval= False
    while isval==False:
        user_input = int(input("type your choice here..enter 1 for rock, 2 for paper, 3 for scissor:")) 
        if (user_input in mylist):
            break
        print("Oops! invalid input.. ")
    print("let's play..")

    if user_input == 1 :
        print(" You throw out a rock")
    if user_input == 2 :
        print(" You throw out a paper")
    if user_input == 3 :
        print(" You throw out a scissor")
    if comp_output == 1:
        print(" I throw out a rock")
    if comp_output == 2: 
        print(" I throw out a paper")
    if comp_output == 3:
        print(" I throw out a scissor")


    if user_input == comp_output : 
        print ("Its a tie") 
    if user_input == 1 and comp_output == 2 :
        comp_score +=1
        print ("I win!") 
    if user_input == 1 and comp_output == 3 :
        user_score +=1
        print ("You win!") 
    if user_input == 2 and comp_output == 1 :
        user_score +=1
        print ("You win!") 
    if user_input == 2 and comp_output == 3 :
        comp_score +=1
        print ("I win!") 
    if user_input == 3 and comp_output == 1 :
        comp_score +=1
        print ("I win!") 
    if user_input == 3 and comp_output == 2 :
        user_score +=1
        print ("You win!")
    print("Your score is  " , user_score)
    print("My score is " , comp_score)

print("Your final score is  " , user_score)
print("My final score is " , comp_score)



    