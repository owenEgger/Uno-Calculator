'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import os
import itertools

cardList = []
unknown = 112

colorDict = {
    0:'red',
    1:'yellow',
    2:'blue',
    3:'green',
    4:'black'
}

invColorDict = {x:y for y, x in colorDict.items()}

numDict = {
    10:'skip',
    11:'revs',
    12:'plu2',
    13:'wild',
    14:'plu4'
}

for i in range(0, 10):
    numDict.update({i:str(i)})
    
invNumDict = {x:y for y, x in numDict.items()}

def setCards():
    cardList.clear()
    for i in range(0, 5):
        cardList.append([])
        if i < 4:
            for j in range(13):
                cardList[i].append([colorDict[i], numDict[j], '1' if j == 0 else '2'])
            
        else:
            cardList[i].append([colorDict[i], numDict[13], '4'])
            cardList[i].append([colorDict[i], numDict[14], '4'])
        

def printCards(cardList):
    line = '      |'
    line2 = '------+'
    for i in range(0, 15):
        line += F'{numDict[i]:>4}|'
        line2 += '----+'
    line2 += '------'
    print(line)
    print(line2)
    for i in cardList:
        chance = 0
        line = F'{i[0][0]:>6}|'
        if cardList.index(i) < 4:
            for j in range(0, len(i)):
                line += F'{i[j][2]:>4}|'
                chance += int(i[j][2])
                
            for j in range(2):
                line += ' N/a|'
                
            line += F' {100 * chance / unknown:4.2f}%'
            
        elif cardList.index(i) == 4:
            for j in range(13):
                line += ' N/a|'
                
            for j in range(0, len(i)):
                line += F'{i[j][2]:>4}|'
                chance += int(i[j][2])
                
            line += F' {100 * chance / unknown:4.2f}%'
            
        else:
            pass
        
        print(line)
    line2 = '------+'
    for i in range(0, 15):
        line2 += '----+'
    line2 += '------'
    print(line2)
    chanceStr = '      |'
    for i in range(0, len(numDict)):
        chance = 0
        if i < 13:
            for j in range(0,4):
                chance += int(cardList[j][i][2])
        else:
            chance += int(cardList[4][i - 13][2])
        chanceStr += F'{100 * chance / unknown:3.2}%|'
    print(chanceStr)

def coms(unknown):
    com = input('\n')
    if (com == 'd'):
       return drawCard(unknown)
    
    elif (com == 'od'):
        pass
    
    elif (com == 'reset'):
        setCards()
        return 0
    
    else:
        print('sorry, but that is not a known command')
        return 0
        
def drawCard(unknown):
    card = input('What card did you draw? (color;number/effect)\n')
    dets = card.split(';')
    if len(dets) == 2 and dets[0] in invColorDict and dets[1] in invNumDict:
        dets[0] = invColorDict[dets[0]]
        dets[1] = invNumDict[dets[1]]%12
        if cardList[dets[0]][dets[1]][2] != '0':
            
            cardList[dets[0]][dets[1]][2] = str(int(cardList[dets[0]][dets[1]][2]) - 1)
            return -1
            input('done')
        else:
            input('card dose not exist')
            return 0
        
setCards()
while True:
    os.system('clear')
    printCards(cardList)
    print('______________________________________________________________________________________________________________________________')
    print("\nType 'od' to let an oponent draw a card\nType 'd' to draw a card\nType 'reset' to reset the deck")
    unknown = unknown - coms(unknown)
    