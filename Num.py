import random
num = random.randint(0,10)
attempts = 0
print("Can you crack the mysterious digit!?")
while attempts < 3:
    guess1 = input("Pick a number between 1 and 10:")
    try:
        guess = int(guess1)
        attempts += 1
        print("You have ", 3 - attempts, " tries left")
        if(guess < num):
            print("It is too small!")
        
        elif(guess > num):
            print("The number is too large!")
        else:
            print("Congratulations! You unlocked the mysterious number")
            break
    except:
         print("Invalid input.\n Please try again")
         
if (num != guess):
       print("Sorry bud, until next time!") 
 
