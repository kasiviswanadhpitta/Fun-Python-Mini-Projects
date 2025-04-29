'''
Hii this is my second mini project to play
"rock paper scissors with the computer"
Version 0.0
'''
from random import randint
from time import sleep
def intro():
    #introduction
    print('Hii this is Rock Paper Scissors game\n')
    print('In this game -\n "0" means Rock\n "1" means Paper\n "2" means Scissors')
    print('Well, you know the rules? y or n  ',end='')
    if (input()=='n'):
        print('Rules:\nScissors defeats Paper\nRock defeats Scissors\nPaper defeats Rock')
    print("Let's Play")

def cpu():
    #computer output
    return randint(0,2)
def fight(a,b):
    #comparing the two inputs
    print(f'{options[a]} fights {options[b]}')
    '''Return values
        0 means Tie
        1 means a won
        2 means b won'''
    if a==b:
        return 0
    elif a<b and a!=0:
        return 2
    else:
        return 1
def output(q):
    print()
    if q==0:
        print('It\'s a tie')
    elif q==1:
        print('You won')
    else:
        print('You lost')
    
    
def userinput():
    inp=int(input())
    return inp%3
options=['Rock','Paper','Scissors']
intro()
output_value=fight(userinput(),cpu())
output(output_value)
sleep(3)
