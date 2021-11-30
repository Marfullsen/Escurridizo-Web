#!/usr/bin/env python
#-*- coding: utf-8 -*-
#import os # os.system('cls') # on windows
from random import randint,shuffle
lab = [[0 for i in range(11)]for i in range(11)]
prs = 'O' #Personaje: Letra que se escojerá para usar en el laberinto
box = [1,2,3,4]
cheese=[]
for i in range(11): 
    for j in range(11):
        if i%2==0:
            print(j,end='')
            if i>4: cheese.append([i,j])
        else:
            if j%2==1:
                print('X',end='')
                lab[i][j]=1
                shuffle(box)
                if box[0]==1: lab[i+1][j]=1
                if box[0]==2: lab[i-1][j]=1
                if box[0]==3: lab[i][j+1]=1
                if box[0]==4: lab[i][j-1]=1
            else: print(j,end='')
    print('')
print(cheese)

def mapa():
    import os
    os.system('cls')  # on windows
    for i in lab:
        for j in i:
            if j==0:
                print(' ',end='')
            elif j==2: print(prs[0],end='')
            else: print('X',end='')
        print()
    
def move():
    global YR,XR,YS,XS    
    print('you are in ',YR,XR, ', The exit is in ',YS,XS)
    key=str(input('Keys: [W]->UP [A]->LEFT [S]->DOWN [D]->RIGHT:\n')).upper()
    lab[YR][XR]=0
    for i in range(len(key)):
        if key[i]=='W': YR-=1
        if key[i]=='A': XR-=1
        if key[i]=='S': YR+=1
        if key[i]=='D': XR+=1
    lab[YR][XR]=2
    mapa()
    if not((YR==YS) and (XR==XS)): move()

if __name__=='__main__':
    YR=0;XR=0;
    lab[YR][XR]=2
    mapa()
    prs = str(input('Eliga una letra o símbolo y presione enter: '))
    #for i in [i for i in range(11+1)]:
    #    print(i)
    input('Checkpoint')
    YS=0;XS=0;
    while (YS<5) or (XS<5):
        YS=randint(0,11)
        XS=randint(0,11)
    input('Checkpoint')
    move()
    print('You Win!')
