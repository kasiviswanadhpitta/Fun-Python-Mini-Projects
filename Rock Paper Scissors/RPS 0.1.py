'''
Hii this is my second mini project to play
"rock paper scissors with the computer"
Version 0.1

Change log:
-> Added the ability to play again
-> Input will be asked again if the input is invalid
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
    flag=1
    while(flag):
        inp=input()
        if int(inp) in range(0,3):
            flag=0
        else:
            print('Please enter valid input')
    return int(inp)
options=['Rock','Paper','Scissors']
intro()
repititive=True
while(repititive):
    inp=userinput()
    output_value=fight(inp,cpu())
    output(output_value)
    sleep(1)
    print('Do you want to play again  y or n ',end='')
    if input()=='n':
        repititive=False
    else:
        print('\nLet\'s Play')
