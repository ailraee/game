'''
class armi
'''
import pygame,time
import pygame.locals as game_globals
import pygame.event as game_events
import Data
def showHealth(health,kind):
    #if health%1==0:
    font=pygame.font.SysFont(None,30)
    s=str(health)
    if '.' in s:
        s=s[:s.index('.')]
    if kind=='f':#fighter
        txt=font.render(s,True,(255,0,0))
    if kind =='d':#defender
        txt=font.render(s,True,(0,0,255))
    return txt
class armi:
    def __init__(self,x,y,name,kind):
        self.x = x
        self.y = y
        self.name=Data.armiData[name]
        self.power=self.name['power']
        if 0<=self.x<=500 and 0<=self.y<=700:
            self.isMove=True
        else:
            self.isMove=False
        self.show=True #bool
        self.kind=kind ##kind of obj is fighter or defender
        self.speed=self.name['speed']
        self.timeHit=0
        self.health=self.name['health']
        self.Image=self.name['image']
    def move(self):
        if self.isMove==True:
            if self.kind=='d':
                self.y-=self.speed
                if self.y<0:
                    self.y=800
            if self.kind=='f':
                self.y+=self.speed
                if self.y>800:
                    self.y=800
    def image(self,surface):
        if self.show==True:
            surface.blit(self.Image,(self.x,self.y-250))
            surface.blit(showHealth(self.health,self.kind), (self.x, self.y - 270))
'''
building class
'''
class building:
    def __init__(self,name):
        self.name=Data.building[name]
        self.x=self.name['x']
        self.y=self.name['y']
        self.Image=self.name['image']
        self.health=self.name['health']
        self.show=True
        self.kind=self.name['kind']
        self.speed=0
        self.power=self.name['power']
        self.board=self.name['board']
    def image(self,surface):
        if self.show==True:
            surface.blit(self.Image,(self.x,self.y-250))
            surface.blit(showHealth(self.health,self.kind),(self.x,self.y-270))
class IMAGE:
    def __init__(self,name,x,y):
        self.x=x
        self.y=y
        self.Image=Data.images[name]
    def image(self,surface):
        surface.blit(self.Image,(self.x,self.y))
def gotoGether(obj1,obj2):
    if distance(obj1,obj2)>65:#obj1.x!=obj2.x or obj1.y!=obj2.y
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
    if distance(obj1,obj2)<100:
        obj1.isMove=False
        obj2.isMove=False

        if obj1.show==obj2.show==True:
            obj1.health-=obj2.power
            pygame.display.update()
            #time.sleep(1)
            obj2.health-=obj1.power
            pygame.display.update()
            checkHealth(obj1)
            checkHealth(obj2)
        elif obj1.show==False:#
            obj2.isMove=True
        elif obj2.show==False:
            obj1.isMove=True
def defend(tower,obj):
    c=True
    if tower.show==obj.show==True:
        if distance(tower,obj)<=tower.board and c==True:
            obj.health-=tower.power
            #time.sleep(1)
            c=False
        elif c==False:
            fight(tower,obj)
            #time.sleep(1)
            c=True

def checkHealth(obj):
    if obj.health<=0:
        obj.show=False
def distance(obj1,obj2):
    return ((obj1.x-obj2.x)**2 + (obj1.y-obj2.y)**2)**0.5
