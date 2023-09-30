from random import randint
from art import *
print(logo)
print(f"Welcome to the Number Guessing Game! ")
print(f"I am thinking of a number between 1 to 100")






def guess():
    loop=True
    answer=randint(1,100)
    if(input(f"Choose a difficulty {'Easy'} or {'Hard'}: ")=='Easy'):
        i=10
    else:
        i=5
    

    while i>0 and loop:
        print(f"You have {i} attempts")
        n=int(input(f"Make a guess: "))
        if n>answer:
            print(f"Too high")
            i-=1
            if(i>0):
                print(f"Guess again")
            if(i==0):
                print(f"You failed")
                loop=False
            
            
        elif n<answer:
            print(f"Too low")
            i-=1
            if(i>0):
                print(f"Guess again")
            if(i==0):
                print(f"You failed")
                loop=False
           
            
        else:
            print(f"You got it,the answer is {answer}")
            loop=False

guess()