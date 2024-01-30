print("="*20)
print("     Quiz Game")
print("="*20)
print("Do U want to play the quiz ?\n ")
press=input("Press 'Y' to play Quiz Or 'N' to exit the game. ")
if press.lower() == 'y':
    print("Welcome to the Quiz Game :) ")
elif press.lower() == 'n':
    print("Bye Bye!!!")
    exit()    
else:
    print("Invalid Input. ")
    exit()   
score=0

#1
press=input("What does 'CPU' stands for ? ")
if press.lower() == 'central processing unit':
    print("Correct Answer :) ")
    score+=1     
else:
    print("Wrong Answer :(\n ")

#2    
press=input("What does 'ATM' stands for ? ")
if press.lower() == 'automated teller machine':
    print("Correct Answer :) ")
    score+=1     
else:
    print("Wrong Answer :(\n ")
    
#3    
press=input("What does 'WHO' stands for ? ")
if press.lower() == 'world health organization':
    print("Correct Answer :) ")
    score+=1     
else:
    print("Wrong Answer :(\n ")    

#4   
press=input("What does 'LPG' stands for ? ")
if press.lower() == 'liquified petroleum gas':
    print("Correct Answer :)")
    score+=1     
else:
    print("Wrong Answer :(\n ") 
    
#5    
press=input("What does 'SIM' stands for ? ")
if press.lower() == 'subscriber identity module':
    print("Correct Answer :) ")
    score+=1     
else:
    print("Wrong Answer :(\n ")    

print("You've Scored " +str(score)+ " Points ") 
if score == 5:
    print("Excellent Score :) ")
else:
    print("better luck next time :(\n ")
    exit()  