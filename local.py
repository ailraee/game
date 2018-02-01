import pygame,sys
import pygame.locals as game_globals
import pygame.event as game_events
from barbarian import *
from Data import *
from ai import *
import time,random

pygame.init()
height=800
width=800
flags=game_globals.DOUBLEBUF
w=pygame.display.set_mode((height,width),flags)
background=pygame.image.load('backgroundgame.jpg')
icon=pygame.image.load('icon.jpg')
Fscore=pygame.image.load('fighterscore.PNG')
Dscore = pygame.image.load('defenderscore.PNG')
#background=pygame.image.load()
pygame.display.set_icon(icon)
pygame.display.set_caption('clashRoyal')
winplayer1Image = pygame.image.load("winplayer1.jpg")
winplayer2Image = pygame.image.load("winplayer2.jpg")
print('player 1 please enter the 4 point for init your army')
print('notice: 0=<x<=500 & 0<=y<=700')
'''poslist1=[]
for i in range(4):
    s=input(str(i+1)+')'+'x,y:')
    s=s.split(sep=',')
    s[0]=int(s[0])
    s[1]=int(s[1])
    p=(s[0],s[1])
    poslist1.append(p)
print('player 2 please enter the 4 point for init your army')
print('notice: 0=<x<=500 & 0<=y<=700')
poslist2=[]
for i in range(4):
    s=input(str(i+1)+')'+'x,y:')
    s=s.split(sep=',')
    s[0]=int(s[0])
    s[1]=int(s[1])
    p=(s[0],s[1])
    poslist2.append(p)'''
player1=player('f')
player2=player('d')
def setCard():
    taghche=[]
    try:
        taghche+=[IMAGE(player1.playernamelist[0],600,100)]
        taghche+=[IMAGE(player1.playernamelist[1],700,100)]
        taghche+=[IMAGE(player1.playernamelist[2],600,200)]
        taghche+=[IMAGE(player1.playernamelist[3],700,200)]
        taghche+=[IMAGE(player2.playernamelist[0],600,400)]
        taghche+=[IMAGE(player2.playernamelist[1],700,400)]
        taghche+=[IMAGE(player2.playernamelist[2],600,500)]
        taghche+=[IMAGE(player2.playernamelist[3],700,500)]
    except:
        pass

    return taghche

def initImage():
    for i in player1.playerbuildings+player2.playerbuildings+player1.playerlist+player2.playerlist:
        i.image(w)
def inittaghche():
    for i in setCard():
        i.image(w)
def initMove(player):
    for i in player.playerlist:
        i.move()
#----------------------------------------------------------------------------------------------------------------------
def showTime():
    font=pygame.font.SysFont(None,30)
    txt=font.render("")
def showGameOver():
    font=pygame.font.SysFont(None,100)
    txt=font.render('GAME OVER',True,(0,255,100))
    w.blit(txt,(200,200))
def goback():
    for event in game_events.get():
        if event.type==game_globals.KEYDOWN:
            if event.key==game_globals.K_SPACE:
                import project

def isExit(bool):
    global showGamePage
    if bool==False:
        if pass_score('f')==3:
            showGamePage = False
            w.blit(winplayer1Image,(0,0))
            goback()
            pygame.display.flip()
        elif pass_score('d')==3:
            showGamePage = False
            w.blit(winplayer2Image,(0,0))
            goback()
            pygame.display.flip()
    else:
        showGamePage = False
        if pass_score('f')>pass_score('d'):
            w.blit(winplayer1Image, (0, 0))
            goback()
            pygame.display.flip()
        elif pass_score('f')<pass_score('d'):
            w.blit(winplayer2Image, (0, 0))
            goback()
            pygame.display.flip()
        else:
            if player1.playerbuildings[0].health>player2.playerbuildings[0].health:
                w.blit(winplayer1Image, (0, 0))
                goback()
                pygame.display.flip()
            else:
                w.blit(winplayer2Image, (0, 0))
                goback()
                pygame.display.flip()
def chekHero(player):
    for i in player.playerlist:
        if i.show==True:
            return False
    return True
def turnhero(player,k):
    if chekHero(player)==True:
        player.resetPlayerList(k)

def exit():
    pygame.quit()
    sys.exit()
def show_score(score,kind):
    if kind=='f':
        #if score%1==0:
            font=pygame.font.SysFont(None,30,True)
            txt=font.render(str(score),True,(255,0,0))
            w.blit(txt,(570,305))
    else:
        #if score%1==0:
            font = pygame.font.SysFont(None, 30, True)
            txt = font.render(str(score), True, (0, 0, 255))
            w.blit(txt, (570, 378))
FscoreList=[0,0,0]
DscoreList=[0,0,0]
def pass_score(kind):
    global FscoreList,DscoreList

    if kind=='f':
        if player2.playerbuildings[0].show==False:
            for i in player2.playerbuildings+player2.playerlist:
                i.show=False
            return 3
        for i in range(len(player1.playerbuildings)):
            if player1.playerbuildings[i].show==False:
                DscoreList[i]=1
        c = 0
        if player1.playerbuildings[0].show==False:
            for i in player1.playerbuildings+player1.playerlist:
                i.show=False
            return 3
        for i in DscoreList:
            if i == 1:
                c += 1
        return c
    else:

        for i in range(len(player2.playerbuildings)):
            if player2.playerbuildings[i].show==False:
                FscoreList[i]=1
        c=0
        for i in FscoreList:
            if i==1:
                c+=1
        return c
'''def setPos():
    global poslist2,poslist1,mousePressed,pos0,pos1,pos2,pos3,pos4,pos5,pos6,pos7
    t = setCard()

    if pygame.mouse.get_pressed()[0] and t[0].x<=pygame.mouse.get_pos()[0]<=t[0].x+100 and t[0].y<=pygame.mouse.get_pos()[1]<=t[0].y+100:
        mousePressed=True
    if not pygame.mouse.get_pressed()[0]:
        mousePressed=False
    if mousePressed:

        t[0].x=pygame.mouse.get_pos()[0]
        t[0].y=pygame.mouse.get_pos()[1]
        pos0 = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    if not mousePressed:
        poslist1[0]=pos0
    if pygame.mouse.get_pressed()[0] and t[1].x<=pygame.mouse.get_pos()[0]<=t[1].x+100 and t[1].y<=pygame.mouse.get_pos()[1]<=t[1].y+100:
        mousePressed=True
    if not pygame.mouse.get_pressed()[0]:
        mousePressed=False
    if mousePressed:
        t[1].x=pygame.mouse.get_pos()[0]
        t[1].y=pygame.mouse.get_pos()[1]
        pos1 = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    if not mousePressed:
        poslist1[1]=pos1
    if pygame.mouse.get_pressed()[0] and t[2].x<=pygame.mouse.get_pos()[0]<=t[2].x+100 and t[2].y<=pygame.mouse.get_pos()[1]<=t[2].y+100:
        mousePressed=True
    if not pygame.mouse.get_pressed()[0]:
        mousePressed=False
    if mousePressed:
        t[2].x=pygame.mouse.get_pos()[0]
        t[2].y=pygame.mouse.get_pos()[1]
        pos2 = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    if not mousePressed:
        poslist1[2]=pos2
    if pygame.mouse.get_pressed()[0] and t[3].x<=pygame.mouse.get_pos()[0]<=t[3].x+100 and t[3].y<=pygame.mouse.get_pos()[1]<=t[3].y+100:
        mousePressed=True
    if not pygame.mouse.get_pressed()[0]:
        mousePressed=False
    if mousePressed:
        t[3].x=pygame.mouse.get_pos()[0]
        t[3].y=pygame.mouse.get_pos()[1]
        pos3 = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    if not mousePressed:
        poslist1[3]=pos3
    if pygame.mouse.get_pressed()[0] and t[4].x<=pygame.mouse.get_pos()[0]<=t[4].x+100 and t[4].y<=pygame.mouse.get_pos()[1]<=t[4].y+100:
        mousePressed=True
    if not pygame.mouse.get_pressed()[0]:
        mousePressed=False
    if mousePressed:
        t[4].x=pygame.mouse.get_pos()[0]
        t[4].y=pygame.mouse.get_pos()[1]
        pos4 = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    if not mousePressed:
        poslist2[0]=pos4
    if pygame.mouse.get_pressed()[0] and t[5].x<=pygame.mouse.get_pos()[0]<=t[5].x+100 and t[5].y<=pygame.mouse.get_pos()[1]<=t[5].y+100:
        mousePressed=True
    if not pygame.mouse.get_pressed()[0]:
        mousePressed=False
    if mousePressed:
        t[5].x=pygame.mouse.get_pos()[0]
        t[5].y=pygame.mouse.get_pos()[1]
        pos5 = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    if not mousePressed:
        poslist2[1]=pos5
    if pygame.mouse.get_pressed()[0] and t[6].x<=pygame.mouse.get_pos()[0]<=t[6].x+100 and t[6].y<=pygame.mouse.get_pos()[1]<=t[6].y+100:
        mousePressed=True
    if not pygame.mouse.get_pressed()[0]:
        mousePressed=False
    if mousePressed:
        t[6].x=pygame.mouse.get_pos()[0]
        t[6].y=pygame.mouse.get_pos()[1]
        pos6 = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    if not mousePressed:
        poslist2[2]=pos6
    if pygame.mouse.get_pressed()[0] and t[7].x<=pygame.mouse.get_pos()[0]<=t[7].x+100 and t[7].y<=pygame.mouse.get_pos()[1]<=t[7].y+100:
        mousePressed=True
    if not pygame.mouse.get_pressed()[0]:
        mousePressed=False
    if mousePressed:
        t[7].x=pygame.mouse.get_pos()[0]
        t[7].y=pygame.mouse.get_pos()[1]
        pos7 = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    if not mousePressed:
        poslist2[3]=pos7
    player1.SetPoslist(poslist1)
    player2.SetPoslist(poslist2)
'''
showGamePage=True
k=4 #tedad armi
j=4
mousePressed=False
aliMod=False
aliMod2=False
while True:
    isExit(False)
    if showGamePage:
        setCard()
        #setPos()
        if mousePressed==True:
            print(poslist1,poslist2)
        w.blit(background, (0, 0))
        w.blit(Fscore, (560, 300))
        w.blit(Dscore,(560,350))
        show_score(pass_score('d'), 'f')
        show_score(pass_score('f'), 'd')
        initImage()
        inittaghche()
        initMove(player1)
        initMove(player2)
        for i in player1.playerlist+player1.playerbuildings+player2.playerlist+player2.playerbuildings:
            checkHealth(i)
        for i in player1.playerlist+player1.playerbuildings:
            fighting(i,player2)
        for i in player2.playerlist+player2.playerbuildings:
            fighting(i,player1)
        for i in player1.playerbuildings:
            defending(i,player2)
        for i in player2.playerbuildings:
            defending(i,player1)
        if chekHero(player1)==True:
            k-=1
            turnhero(player1,k)
        if chekHero(player2)==True:
            j-=1
            turnhero(player2,j)
        if k==0 or j==0:
            isExit(True)
        if aliMod==True:
            for i in player2.playerbuildings:
                i.health+=100
        if aliMod2==True:
            player2.playerlist+=randomSelect(player2.kind,1)[0]
        for event in game_events.get():
            if event.type==game_globals.KEYDOWN:
                if event.key==game_globals.K_b:
                    aliMod2=True
                if event.key==game_globals.K_a:
                    aliMod=True
            if event.type==game_globals.KEYUP:
                if event.key==game_globals.K_b:
                    aliMod2=False
                if event.key==game_globals.K_a:
                    aliMod=False
            if event.type==game_globals.QUIT:
                exit()
        pygame.display.flip()