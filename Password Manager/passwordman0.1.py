'''
Password Manager version 0.1
Hii this might be my first program/project in python
This program is to save my passwords in a secure file so that I can use it
any time I want.
->Passwords should not be recyled.<-

Changelog:
->User ability to add new passwords
->Ability to add passwords from clipboard

'''

import sys,pyperclip as pc,json

def pswdcopy(x):
    pc.copy(pswds[x])
    print('Password copied to clipboard')
def pswdpaste(ac):
    print('Do you want to add a new password.y/n?')
    inp=input()
    if inp[0]=='y' or inp[0]=='Y':
        print('Do you want to copy the password from clipboard.y/n?')
        inp=input()
        if inp[0]=='y' or inp[0]=='Y':
            cpswd=pc.paste()
            print(f'This is the copied pswd {cpswd}')
            pswds[ac]=cpswd
            
        else:
            print(f'Enter the password for {ac}')
            inp=input()
            pswds[ac]=inp
        f=open('pswdata.txt','w')
        json.dump(pswds,f)
        f.close()
    

if (len(sys.argv)<2):
    print('Usage: python passwordman<version>.py <account domain> ')
    sys.exit()
acc_domain=sys.argv[1]
f=open('pswdata.txt','r')
pswds=json.load(f)
f.close()

if acc_domain in pswds:
    pswdcopy(acc_domain)
else:
    pswdpaste(acc_domain)
sys.exit()
    
