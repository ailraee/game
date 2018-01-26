import pygame,sys
import pygame.locals as game_globals
import pygame.event as game_events
from barbarian import *
import time,random
pygame.init()
height=600
widtht=800
w=pygame.display.set_mode((widtht,height))
background=pygame.image.load('backgroundgame.jpg')
icon=pygame.image.load('icon.jpg')
#background=pygame.image.load()
pygame.display.set_icon(icon)
pygame.display.set_caption('clashRoyal')
b=barbar(0,800,'f',0.5)
b1=barbar(200,270,'d',0.5)
x=100
y=100
def checkHealth(obj):
    if obj.health<0:
        obj.show=False
def distance(obj1,obj2):
    return ((obj1.x-obj2.x)**2 + (obj1.y-obj2.y)**2)**0.5
def gotoGether(obj1,obj2):
    if distance(obj1,obj2)>60:#obj1.x!=obj2.x or obj1.y!=obj2.y
        if obj1.x-obj2.x>0:
            obj1.x-=obj1.speed
            obj2.x+=obj2.speed
        else:
            obj1.x += obj1.speed
            obj2.x -= obj2.speed
        if obj1.y - obj2.y > 0:
            obj1.y -= obj1.speed
            obj2.y += obj2.speed
        else:
            obj1.y += obj1.speed
            obj2.y -= obj2.speed
def fight(obj1,obj2):
    if distance(obj1,obj2)<60:
        obj1.isMove=False
        obj2.isMove=False

        if obj1.show==obj2.show==True:
            obj1.health-=obj2.power
            time.sleep(0.1)
            obj2.health-=obj1.power
            checkHealth(obj1)
            checkHealth(obj2)
        elif obj1.show==True:#
            obj1.isMove=True
        elif obj2.show==True:
            obj2.isMove=True
def showGameOver():
    font=pygame.font.SysFont(None,100)
    txt=font.render('GAME OVER',True,(0,255,100))
    w.blit(txt,(200,200))
def isExit():
    font=pygame.font.SysFont(None,50)
    txt=font.render("do you want to Exit? ",True,(255,200,200))
    w.blit(txt,(width/2-150,height/2))

def exit():
    pygame.quit()
    sys.exit()
def show_score(score):
    font=pygame.font.SysFont(None,40)
    txt=font.render('SCORE:'+str(score),True,(255,0,100))
    w.blit(txt,(0,0))

c=0
showCard=True
while True:
    w.blit(background,(0,0))
    b.image(w)
    b1.image(w)
    show_score(c)
    c+=1
    #pygame.key.set_repeat(10)
    b.move()
    b1.move()
    fight(b,b1)
    gotoGether(b, b1)
    for event in game_events.get():
        if event.type==game_globals.QUIT:
            exit()
    #pygame.key.get_repeat()
    pygame.display.update()
