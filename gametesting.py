
import pygame,sys,time
import pygame.locals as game_globals
import pygame.event as game_events
from barbarian import *
pygame.init()
width=800
height=600
w=pygame.display.set_mode((width,height))
#background=pygame.image.load()
pygame.display.set_caption('clashRoyal')
b=barbar(100,799,'f',0.5)
b1=barbar(200,100,'d',0.5)
def exit():
    pygame.quit()
    sys.exit()
def checkHealth(obj):
    if obj.health<0:
        obj.show=False
def fight(obj1,obj2):
    if (obj1.x-obj2.x<=100 or obj2.x-obj1.x<=100) and (obj1.y-obj2.y<=100 or obj2.y-obj1.y<=100):
        obj1.isMove=False
        obj2.isMove=False
        obj1.health-=obj2.power
        obj2.health-=obj1.power
        checkHealth(obj1)
        checkHealth(obj2)

def show_score(score):
    #if score%1==0:
        font=pygame.font.SysFont(None,40)
        s='SCORE:'+str(score)[:-2]
        txt=font.render(s,True,(255,60,100))
        w.blit(txt,(0,0))
        pygame.display.update()
def showGameOver():
    font=pygame.font.SysFont(None,100)
    txt=font.render('GAME OVER',True,(0,255,100))
    w.blit(txt,(200,200))
def isExit():
    font=pygame.font.SysFont(None,50)
    txt=font.render("do you want to Exit? ",True,(255,200,200))
    w.blit(txt,(width/2-150,height/2))
c=0
while True:
    w.fill((0,0,0))

    fight(b,b1)
    #showGameOver()
    b.image(w)
    b1.image(w)
    #pygame.key.set_repeat(10)
    b.move()
    b1.move()
    c+=1
    '''if b1.y<=250 or b.y<=250:
        showGameOver()
        isExit()
        pygame.display.update()
        time.sleep(1)
        exit()'''
    for event in game_events.get():
        if event.type==game_globals.QUIT:
            exit()
    show_score(c)
    #pygame.key.get_repeat()
    pygame.display.update()
