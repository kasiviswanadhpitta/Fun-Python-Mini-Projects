'''
Password Manager version 0.2
Hii this might be my first program/project in python
This program is to save my passwords in a secure file so that I can use it
any time I want.
->Passwords should not be recyled.<-

Changelog:
->Added new master password to see the passwords
->Ability to delete a password
->Ability to view all passwords
->Ability to update a password
'''

import sys,pyperclip as pc,json

def pswdcopy(x):
    pc.copy(pswds[x])
    print('Password copied to clipboard')

def pswdadd(ac):
    print('Do you want to add a new password.y/n?')
    inp=input()
    if inp[0]=='y' or inp[0]=='Y':
        print('Do you want to copy the password from clipboard.y/n?')
        inp=input()
        if inp[0]=='y' or inp[0]=='Y':
            cpswd=pc.paste()
            print(f'This is the copied pswd {cpswd}')
            print('Do you want to use it,y/n?')
            inp=input()
            if inp[0]=='y' or inp[0]=='Y':
                pswds[ac]=cpswd
            
        else:
            print(f'Enter the password for {ac}')
            pass_inp=input()
            pswds[ac]=pass_inp
        print(f'Password added for {ac}')
        

def pswddel(ac):
    print(f'Do you want to delete {ac} password.y/n?')
    inp=input()
    if inp[0]=='y' or inp[0]=='Y':
        del(pswds[ac])
        print(f'Password deleted for {ac}')

def pswdupd(ac):
    print(f'Do you want to update {ac} password.y/n?')
    inp=input()
    if inp[0]=='y' or inp[0]=='Y':
        print(f'The original password is {pswds[ac]}')
        print('Do you want to copy the password from clipboard.y/n?')
        inp=input()
        if inp[0]=='y' or inp[0]=='Y':
            cpswd=pc.paste()
            print(f'This is the copied pswd {cpswd}')
            print('Do you want to use it,y/n?')
            inp=input()
            if inp[0]=='y' or inp[0]=='Y':
                pswds[ac]=cpswd
            else:
                return
        else:
            print(f'Enter the password for {ac}')
            inp=input()
            pswds[ac]=inp
        print(f'Password updated for {ac}')
def pswdshow():
    print('Domains     Passwords')
    for i in pswds:
        print(f" {i}  <-> {pswds[i]}")

if (len(sys.argv)<3 or sys.argv[2] not in 'cudla'):
    print('''Errror Not enough arguments or wrong ones.
Usage: python passwordman<version>.py <account domain> <argument>
The arguments are "c" to copy the password
                  "a" to add a new password
                  "u" to update the password
                  "l" to list all the passwords
                  "d" to delete the password
''')
    sys.exit()
if input('Enter master password\n')!='asdf':
    print('Wrong Password')
    sys.exit()
acc_domain=sys.argv[1]
argument=sys.argv[2]
f=open('pswdata.txt','r')
pswds=json.load(f)
f.close()
if argument=='c':
    pswdcopy(acc_domain)
elif argument=='a':
    if acc_domain in pswds:
        print("Password Already exits")
    else:
        pswdadd(acc_domain)
elif argument=='d':
    pswddel(acc_domain)
elif argument=='u':
    pswdupd(acc_domain)
else:
    pswdshow()
if argument!='l':
    f=open('pswdata.txt','w')
    json.dump(pswds,f)
    f.close()
print('\nPassword Manager Exited')
sys.exit()
    
