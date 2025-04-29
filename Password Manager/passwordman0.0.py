'''
Hii this might be my first program/project in python
This program is to save my passwords in a secure file so that I can use it
any time I want.
->Passwords should not be recyled.<-
'''

import sys,pyperclip as pc

def pswdcopy(x):
    pc.copy(pswds[x])
    print('Password copied to clipboard')

if (len(sys.argv)<2):
    print('Usage: python passwordman.py <account domain> ')
    sys.exit()
acc_domain=sys.argv[1]
pswds={'mcl':12345,'examly':4321,'zoom':6768}
if acc_domain in pswds:
    pswdcopy(acc_domain)
    
