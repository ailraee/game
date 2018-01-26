'''
class barbarian
'''
import pygame
import pygame.locals as game_globals
import pygame.event as game_events
def showHealth(health,kind):
    font=pygame.font.SysFont(None,30)
    if kind=='f':#fighter
        txt=font.render(str(health),True,(255,0,0))
    if kind =='d':#defender
        txt=font.render(str(health),True,(0,0,255))
    return txt
class barbar:
    def __init__(self,x,y,kind,power):
        self.power=power
        self.isMove=True
        self.show=True #bool
        self.kind=kind ##kind of obj is fighter or defender
        self.x=x
        self.y=y
        self.speed=0.6
        self.timeHit=0
        self.health=100
        self.Image=None
    def move(self):
        if self.isMove==True:
            if self.kind=='f':
                self.y-=self.speed
                if self.y<0:
                    self.y=800
            if self.kind=='d':
                self.y+=self.speed
                if self.y>800:
                    self.y=800
    def image(self,surface):
        if self.show==True:
            self.Image=pygame.image.load('barbarian.jpg')
            surface.blit(self.Image,(self.x,self.y-250))
            surface.blit(showHealth(self.health,self.kind), (self.x, self.y - 270))