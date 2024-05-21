import random
count=0
x=random.randint(2, 100)  
while(True):
    
    
    y=int(input("Guess a number from 2 to 100"))
    if y>x:
            print ("Your guessed number is high")
    elif y<x:
            print("Your guessed number is less")
    else :
            print("Your guessed number is correct")
            break
    count +=1


print(f'you have guessed {count} times')
