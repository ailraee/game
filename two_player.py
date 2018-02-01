import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME


class hero:
    def __init__(self,kind,player,xpos,ypos,health=100,power=0,color=(0,0,0)):
        self.kind = kind
        self.player = player
        self.health = health
        self.power = power
        self.bord = None
        self.x = xpos
        self.y = ypos
        self.image = None
        self.color = color
        if self.kind == 1:
            self.health = 75
            self.power = 13
            self.bord = (self.x - 20,self.y -20,80,90)
            self.color = (255,0,0)
            self.image = pygame.image.load("archer.jpg")
        if self.kind == 2:
            self.health = 65
            self.power = 10
            self.bord = (self.x - 10,self.y - 10,60,70)
            self.color = (0,255,0)
            self.image = pygame.image.load("barbarian.jpg")
        if self.kind == 3:
            self.health = 85
            self.power = 9
            self.bord = (self.x - 14,self.y - 14,68,78)
            self.color = (0,0,255)
            self.image = pygame.image.load("dragon.png")
        if self.kind == 4:
            self.health = 100
            self.power = 12
            self.bord = (self.x - 10,self.y - 10,60,70)
            self.color = (255,255,0)
            self.image = pygame.image.load("giant.png")
        if self.kind == 5:
            self.health = 80
            self.power = 9
            self.bord = (self.x - 20,self.y - 20,80,90)
            self.color = (0,255,255)
            self.image = pygame.image.load("goblin.png")
        if self.kind == 6:
            self.health = 90
            self.power = 10
            self.bord = (self.x - 16,self.y - 16,72,82)
            self.color = (255,0,255)
            self.image = pygame.image.load("prince.jpg")
        if self.kind == 7:
            self.health = 50
            self.power = 6
            self.bord = (self.x - 14,self.y - 14,68,78)
            self.color = (127,127,127)
            self.image = pygame.image.load("skeleton.jpg")
        if self.kind == 8:
            self.helth = 80
            self.power = 10
            self.bord =(self.x - 18,self.y - 18,76,86)
            self.color = (200,200,200)
            self.image = pygame.image.load("wizard.jpg")
        if self.health == 0:
            self.x = -1000
            self.y = -1000
            return None
        pygame.draw.rect(surface,self.color,self.bord)
        surface.blit(self.image,(self.x,self.y))
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def setx(self,x):
        self.x = x
    def sety(self,y):
        self.y = y
class building:
    def __init__(self,x,y,health,bord,power,image,color):
        self.health = health
        self.bord = bord
        self.power = power
        self.x = x
        self.y = y
        self.color = color
        if self.health == 0:
            return
        if color == 1:
            self.color = (100,150,200)
            pygame.draw.rect(surface,self.color,(self.x - self.bord,self.y - self.bord,2*self.bord + 80,2*self.bord + 80))
            surface.blit(image,(x,y))
        if color == 2:
            self.color = (120,230,180)
            pygame.draw.rect(surface,self.color,(self.x - self.bord,self.y - self.bord,2*self.bord + 70,2*self.bord + 70))
            surface.blit(image,(x,y))
    def gethealth(self):
        return self.health
    def sethealth(self,health):
        self.health = health
    def getpower(self):
        return self.power
    

pygame.init()
windowWidth = 800
windowHeight = 600
icon = pygame.image.load('icon.jpg')
flags=GAME_GLOBALS.DOUBLEBUF | GAME_GLOBALS.FULLSCREEN
surface = pygame.display.set_mode((windowWidth,windowHeight),flags)
pygame.display.set_caption("CLASH ROYALE")
pygame.display.set_icon(icon)
backgroundgameImage=pygame.image.load("backgroundgame.jpg")

archerCImage=pygame.image.load("archercard.jpg")
barbarianCImage=pygame.image.load("barbarianCard.jpg")
dragonCImage=pygame.image.load("dragonCard.png")
giantCImage=pygame.image.load("GiantCard.png")
goblinCImage=pygame.image.load("goblinCard.png")
princeCImage=pygame.image.load("princeCard.jpg")
skeletonCImage=pygame.image.load("skeletonCard.jpg")
wizardCImage=pygame.image.load("wizardCard.jpg")
sakhtemanasliImage=pygame.image.load("defenderbuildinghall.png")
sakhtemanfareeImage=pygame.image.load("defenderbuilding.png")
sakhtemanasli2Image=pygame.image.load("fighterbuildinghall.png")
sakhtemanfaree2Image=pygame.image.load("fighterbuilding.png")
scoreplayer1Image=pygame.image.load("scoreplayer1.PNG")
scoreplayer2Image=pygame.image.load("scoreplayer2.PNG")

winplayer1Image = pygame.image.load("winplayer1.jpg")
winplayer2Image = pygame.image.load("winplayer2.jpg")

gamePage = True
winplayer1 = False
winplayer2 = False
wincomputer = False

mousePosition = None
mousePressed = False

vara1 = False
varb1 = False
varc1 = False
vard1 = False
vare1 = False
varf1 = False

a1posx =0
a1posy =0
b1posx =0
b1posy =0
c1posx =0
c1posy =0
d1posx =0
d1posy =0
e1posx =0
e1posy =0
f1posx =0
f1posy =0

a,b,c,d,e,f=1,1,1,1,1,1
ahero1 = hero(a,1,-1000,-1000)
bhero1 = hero(b,1,-1000,-1000)
chero1 = hero(c,1,-1000,-1000)
dhero1 = hero(d,1,-1000,-1000)
ehero1 = hero(e,1,-1000,-1000)
fhero1 = hero(f,1,-1000,-1000)
timer = 0
def firsvar():
    global a,b,c,d,e,f
    a = random.randint(1,8)
    b = random.randint(1,8)
    c = random.randint(1,8)
    if b == a :
        b = random.randint(1,8)
        if b == a :
            b = random.randint(1,8)
    if c == a or c == b :
        c = random.randint(1,8)
        if c == a or c == b :
            c = random.randint(1,8)
            if c == a or c == b :
                c =random.randint(1,8)

    d = random.randint(1,8)
    e = random.randint(1,8)
    f = random.randint(1,8)

    if e == d :
        e = random.randint(1,8)
        if e == d :
            e = random.randint(1,8)
    if f == d or f == e :
        f = random.randint(1,8)
        if f == d or f == e :
            f = random.randint(1,8)
            if f == d or f == e :
                f = random.randint(1,8)
def tatbigh():
    global a,b,c,d,e,f
    if a == 1:
        surface.blit(archerCImage,(windowWidth-100,windowHeight-100))
    if a == 2:
        surface.blit(barbarianCImage,(windowWidth-100,windowHeight-100))
    if a == 3:
        surface.blit(dragonCImage,(windowWidth-100,windowHeight-100))
    if a == 4:
        surface.blit(giantCImage,(windowWidth-100,windowHeight-100))
    if a == 5:
        surface.blit(goblinCImage,(windowWidth-100,windowHeight-100))
    if a == 6:
        surface.blit(princeCImage,(windowWidth-100,windowHeight-100))
    if a == 7:
        surface.blit(skeletonCImage,(windowWidth-100,windowHeight-100))
    if a == 8:
        surface.blit(wizardCImage,(windowWidth-100,windowHeight-100))
    if b == 1:
        surface.blit(archerCImage,(windowWidth-200,windowHeight-100))
    if b == 2:
        surface.blit(barbarianCImage,(windowWidth-200,windowHeight-100))
    if b == 3:
        surface.blit(dragonCImage,(windowWidth-200,windowHeight-100))
    if b == 4:
        surface.blit(giantCImage,(windowWidth-200,windowHeight-100))
    if b == 5:
        surface.blit(goblinCImage,(windowWidth-200,windowHeight-100))
    if b == 6:
        surface.blit(princeCImage,(windowWidth-200,windowHeight-100))
    if b == 7:
        surface.blit(skeletonCImage,(windowWidth-200,windowHeight-100))
    if b == 8:
        surface.blit(wizardCImage,(windowWidth-200,windowHeight-100))
    if c == 1:
        surface.blit(archerCImage,(windowWidth-150,windowHeight-200))
    if c == 2:
        surface.blit(barbarianCImage,(windowWidth-150,windowHeight-200))
    if c == 3:
        surface.blit(dragonCImage,(windowWidth-150,windowHeight-200))
    if c == 4:
        surface.blit(giantCImage,(windowWidth-150,windowHeight-200))
    if c == 5:
        surface.blit(goblinCImage,(windowWidth-150,windowHeight-200))
    if c == 6:
        surface.blit(princeCImage,(windowWidth-150,windowHeight-200))
    if c == 7:
        surface.blit(skeletonCImage,(windowWidth-150,windowHeight-200))
    if c == 8:
        surface.blit(wizardCImage,(windowWidth-150,windowHeight-200))
    if d == 1:
        surface.blit(archerCImage,(windowWidth-100,0))
    if d == 2:
        surface.blit(barbarianCImage,(windowWidth-100,0))
    if d == 3:
        surface.blit(dragonCImage,(windowWidth-100,0))
    if d == 4:
        surface.blit(giantCImage,(windowWidth-100,0))
    if d == 5:
        surface.blit(goblinCImage,(windowWidth-100,0))
    if d == 6:
        surface.blit(princeCImage,(windowWidth-100,0))
    if d == 7:
        surface.blit(skeletonCImage,(windowWidth-100,0))
    if d == 8:
        surface.blit(wizardCImage,(windowWidth-100,0))
    if e == 1:
        surface.blit(archerCImage,(windowWidth-200,0))
    if e == 2:
        surface.blit(barbarianCImage,(windowWidth-200,0))
    if e == 3:
        surface.blit(dragonCImage,(windowWidth-200,0))
    if e == 4:
        surface.blit(giantCImage,(windowWidth-200,0))
    if e == 5:
        surface.blit(goblinCImage,(windowWidth-200,0))
    if e == 6:
        surface.blit(princeCImage,(windowWidth-200,0))
    if e == 7:
        surface.blit(skeletonCImage,(windowWidth-200,0))
    if e == 8:
        surface.blit(wizardCImage,(windowWidth-200,0))
    if f == 1:
        surface.blit(archerCImage,(windowWidth-150,100))
    if f == 2:
        surface.blit(barbarianCImage,(windowWidth-150,100))
    if f == 3:
        surface.blit(dragonCImage,(windowWidth-150,100))
    if f == 4:
        surface.blit(giantCImage,(windowWidth-150,100))
    if f == 5:
        surface.blit(goblinCImage,(windowWidth-150,100))
    if f == 6:
        surface.blit(princeCImage,(windowWidth-150,100))
    if f == 7:
        surface.blit(skeletonCImage,(windowWidth-150,100))
    if f == 8:
        surface.blit(wizardCImage,(windowWidth-150,100))
def checkbox(xpos1,xpos2,ypos1,ypos2):
    if mousePosition[0] > xpos1 and mousePosition[0] < xpos2:
        if mousePosition[1] > ypos1 and mousePosition[1]< ypos2:
            return True
    return False
def clickdown():
    global vara1,varb1,varc1,vard1,vare1,varf1
    if checkbox(windowWidth-100,windowWidth,windowHeight-100,windowHeight):
        ahero1 = hero(a,1,mousePosition[0],mousePosition[1])
        vara1 = True
    if checkbox(windowWidth-200,windowWidth-100,windowHeight-100,windowHeight):
        bhero1 = hero(b,1,mousePosition[0],mousePosition[1])
        varb1 = True
    if checkbox(windowWidth-150,windowWidth-50,windowHeight-200,windowHeight-100):
        chero1 = hero(c,1,mousePosition[0],mousePosition[1])
        varc1 = True
    if checkbox(windowWidth-100,windowWidth,0,100):
        dhero1 = hero(d,1,mousePosition[0],mousePosition[1])
        vard1 = True
    if checkbox(windowWidth-200,windowWidth-100,0,100):
        ehero1 = hero(e,1,mousePosition[0],mousePosition[1])
        vare1 = True
    if checkbox(windowWidth-150,windowWidth-50,100,200):
        fhero1 = hero(f,1,mousePosition[0],mousePosition[1])
        varf1 = True
def clickup():
    global a1posx,a1posy,vara1,varb1,b1posx,b1posy,varc1,c1posx,c1posy,vard1,vare1,varf1,d1posx,d1posy,e1posx,e1posy,f1posx,f1posy
    if mousePosition[0] < 600 and mousePosition[1] < 600:
        if vara1 == True:
            a1posx = mousePosition[0]
            a1posy = mousePosition[1]
            ahero1.setx(a1posx)
            ahero1.sety(a1posy)
            vara1 = False
        if varb1 == True:
            b1posx = mousePosition[0]
            b1posy = mousePosition[1]
            bhero1.setx(b1posx)
            bhero1.sety(b1posy)
            varb1 = False
        if varc1 == True:
            c1posx = mousePosition[0]
            c1posy = mousePosition[1]
            chero1.setx(c1posx)
            chero1.sety(c1posy)
            varc1 = False
        if vard1 == True:
            d1posx = mousePosition[0]
            d1posy = mousePosition[1]
            dhero1.setx(d1posx)
            dhero1.sety(d1posy)
            vard1 = False
        if vare1 == True:
            e1posx = mousePosition[0]
            e1posy = mousePosition[1]
            ehero1.setx(e1posx)
            ehero1.sety(e1posy)
            vare1 = False
        if varf1 == True:
            f1posx = mousePosition[0]
            f1posy = mousePosition[1]
            fhero1.setx(f1posx)
            fhero1.sety(f1posy)
            varf1 = False
def move ():
    global a,b,c,d,e,f,a1posx,a1posy,b1posx,b1posy,c1posx,c1posy,d1posx,d1posy,e1posx,e1posy,f1posx,f1posy
    if  0<a1posx<115 :
        if a ==1:
            a1posx += 0.1
            a1posy -= 0.1
        if a ==2:
            a1posx += 0.1
            a1posy -= 0.1
        if a ==3:
            a1posx += 0.1
            a1posy -= 0.1
        if a ==4:
            a1posx += 0.1
            a1posy -= 0.1
        if a ==5:
            a1posx += 0.1
            a1posy -= 0.1
        if a ==6:
            a1posx += 0.1
            a1posy -= 0.1
        if a ==7:
            a1posx += 0.1
            a1posy -= 0.1
        if a ==8:
            a1posx += 0.1
            a1posy -= 0.1
    if a1posx == 115 :
        if a==1:
            if a1posy >=150:
                a1posy -= 0.1
        if a==2:
            if a1posy >= 150:
                a1posy -= 0.1
        if a==3:
            if a1posy >= 150:
                a1posy -= 0.1
        if a==4:
            if a1posy >= 150:
                a1posy -= 0.1
        if a==5:
            if a1posy >= 150:
                a1posy -= 0.1
        if a==6:
            if a1posy >=150:
                a1posy -= 0.1
        if a==7:
            if a1posy >= 150:
                a1posy -= 0.1
        if a==8:
            if a1posy >= 150:
                a1posy -= 0.1
    if 115<a1posx<173:
        if a==1:
            a1posx-=0.1
            a1posy-=0.1
        if a==2:
            a1posx-=0.1
            a1posy-=0.1
        if a==3:
            a1posx-=0.1
            a1posy-=0.1
        if a==4:
            a1posx-=0.1
            a1posy-=0.1
        if a==5:
            a1posx-=0.1
            a1posy-=0.1
        if a==6:
            a1posx-=0.1
            a1posy-=0.1
        if a==7:
            a1posx-=0.1
            a1posy-=0.1
        if a==8:
            a1posx-=0.1
            a1posy-=0.1
    if 173<a1posx<300:
        if a==1:
            a1posx+=0.1
            a1posy-=0.1
        if a==2:
            a1posx+=0.1
            a1posy-=0.1
        if a==3:
            a1posx+=0.1
            a1posy-=0.1
        if a==4:
            a1posx+=0.1
            a1posy-=0.1
        if a==5:
            a1posx+=0.1
            a1posy-=0.1
        if a==6:
            a1posx+=0.1
            a1posy-=0.1
        if a==7:
            a1posx+=0.1
            a1posy-=0.1
        if a==8:
            a1posx+=0.1
            a1posy-=0.1
    if a1posx == 300 :
        if a==1:
            if a1posy >=110:
                a1posy -= 0.1
        if a==2:
            if a1posy >= 110:
                a1posy -= 0.1
        if a==3:
            if a1posy >= 110:
                a1posy -= 0.1
        if a==4:
            if a1posy >= 110:
                a1posy -= 0.1
        if a==5:
            if a1posy >= 110:
                a1posy -= 0.1
        if a==6:
            if a1posy >= 110:
                a1posy -= 0.1
        if a==7:
            if a1posy >= 110:
                a1posy -= 0.1
        if a==8:
            if a1posy >= 110:
                a1posy -= 0.1
    if 300<a1posx<427:
        if a==1:
            a1posx-=0.1
            a1posy-=0.1
        if a==2:
            a1posx-=0.1
            a1posy-=0.1
        if a==3:
            a1posx-=0.1
            a1posy-=0.1
        if a==4:
            a1posx-=0.1
            a1posy-=0.1
        if a==5:
            a1posx-=0.1
            a1posy-=0.1
        if a==6:
            a1posx-=0.1
            a1posy-=0.1
        if a==7:
            a1posx-=0.1
            a1posy-=0.1
        if a==8:
            a1posx-=0.1
            a1posy-=0.1
    if 427<a1posx<485:
        if a==1:
            a1posx+=0.1
            a1posy-=0.1
        if a==2:
            a1posx+=0.1
            a1posy-=0.1
        if a==3:
            a1posx+=0.1
            a1posy-=0.1
        if a==4:
            a1posx+=0.1
            a1posy-=0.1
        if a==5:
            a1posx+=0.1
            a1posy-=0.1
        if a==6:
            a1posx+=0.1
            a1posy-=0.1
        if a==7:
            a1posx+=0.1
            a1posy-=0.1
        if a==8:
            a1posx+=0.1
            a1posy-=0.1
    if a1posx == 485 :
        if a==1:
            if a1posy >=150:
                a1posy -= 0.1
        if a==2:
            if a1posy >= 150:
                a1posy -= 0.1
        if a==3:
            if a1posy >= 150:
                a1posy -= 0.1
        if a==4:
            if a1posy >= 150:
                a1posy -= 0.1
        if a==5:
            if a1posy >= 150:
                a1posy -= 0.1
        if a==6:
            if a1posy >=150:
                a1posy -= 0.1
        if a==7:
            if a1posy >= 150:
                a1posy -= 0.1
        if a==8:
            if a1posy >= 150:
                a1posy -= 0.1
    if 485<a1posx<600:
        if a==1:
            a1posx-=0.1
            a1posy-=0.1
        if a==2:
            a1posx-=0.1
            a1posy-=0.1
        if a==3:
            a1posx-=0.1
            a1posy-=0.1
        if a==4:
            a1posx-=0.1
            a1posy-=0.1
        if a==5:
            a1posx-=0.1
            a1posy-=0.1
        if a==6:
            a1posx-=0.1
            a1posy-=0.1
        if a==7:
            a1posx-=0.1
            a1posy-=0.1
        if a==8:
            a1posx-=0.1
            a1posy-=0.1
            


    if  0 < b1posx < 115 :
        if b ==1:
            b1posx += 0.1
            b1posy -= 0.1
        if b ==2:
            b1posx += 0.1
            b1posy -= 0.1
        if b ==3:
            b1posx += 0.1
            b1posy -= 0.1
        if b ==4:
            b1posx += 0.1
            b1posy -= 0.1
        if b ==5:
            b1posx += 0.1
            b1posy -= 0.1
        if b ==6:
            b1posx += 0.1
            b1posy -= 0.1
        if b ==7:
            b1posx += 0.1
            b1posy -= 0.1
        if b ==8:
            b1posx += 0.1
            b1posy -= 0.1
    if b1posx == 115 :
        if b==1:
            if b1posy >=150:
                b1posy -= 0.1
        if b==2:
            if b1posy >= 150:
                b1posy -= 0.1
        if b==3:
            if b1posy >= 150:
                b1posy -= 0.1
        if b==4:
            if b1posy >= 150:
                b1posy -= 0.1
        if b==5:
            if b1posy >= 150:
                b1posy -= 0.1
        if b==6:
            if b1posy >=150:
                b1posy -= 0.1
        if b==7:
            if b1posy >= 150:
                b1posy -= 0.1
        if b==8:
            if b1posy >= 150:
                b1posy -= 0.1
    if 115<b1posx<173:
        if b==1:
            b1posx-=0.1
            b1posy-=0.1
        if b==2:
            b1posx-=0.1
            b1posy-=0.1
        if b==3:
            b1posx-=0.1
            b1posy-=0.1
        if b==4:
            b1posx-=0.1
            b1posy-=0.1
        if b==5:
            b1posx-=0.1
            b1posy-=0.1
        if b==6:
            b1posx-=0.1
            b1posy-=0.1
        if b==7:
            b1posx-=0.1
            b1posy-=0.1
        if b==8:
            b1posx-=0.1
            b1posy-=0.1
    if 173<b1posx<300:
        if b==1:
            b1posx+=0.1
            b1posy-=0.1
        if b==2:
            b1posx+=0.1
            b1posy-=0.1
        if b==3:
            b1posx+=0.1
            b1posy-=0.1
        if b==4:
            b1posx+=0.1
            b1posy-=0.1
        if b==5:
            b1posx+=0.1
            b1posy-=0.1
        if b==6:
            b1posx+=0.1
            b1posy-=0.1
        if b==7:
            b1posx+=0.1
            b1posy-=0.1
        if b==8:
            b1posx+=0.1
            b1posy-=0.1
    if b1posx == 300 :
        if b==1:
            if b1posy >=110:
                b1posy -= 0.1
        if b==2:
            if b1posy >= 110:
                b1posy -= 0.1
        if b==3:
            if b1posy >= 110:
                b1posy -= 0.1
        if b==4:
            if b1posy >= 110:
                b1posy -= 0.1
        if b==5:
            if b1posy >= 110:
                b1posy -= 0.1
        if b==6:
            if b1posy >=110:
                b1posy -= 0.1
        if b==7:
            if b1posy >= 110:
                b1posy -= 0.1
        if b==8:
            if b1posy >= 110:
                b1posy -= 0.1
    if 300<b1posx<427:
        if b==1:
            b1posx-=0.1
            b1posy-=0.1
        if b==2:
            b1posx-=0.1
            b1posy-=0.1
        if b==3:
            b1posx-=0.1
            b1posy-=0.1
        if b==4:
            b1posx-=0.1
            b1posy-=0.1
        if b==5:
            b1posx-=0.1
            b1posy-=0.1
        if b==6:
            b1posx-=0.1
            b1posy-=0.1
        if b==7:
            b1posx-=0.1
            b1posy-=0.1
        if b==8:
            b1posx-=0.1
            b1posy-=0.1
    if 427<b1posx<485:
        if b==1:
            b1posx+=0.1
            b1posy-=0.1
        if b==2:
            b1posx+=0.1
            b1posy-=0.1
        if b==3:
            b1posx+=0.1
            b1posy-=0.1
        if b==4:
            b1posx+=0.1
            b1posy-=0.1
        if b==5:
            b1posx+=0.1
            b1posy-=0.1
        if b==6:
            b1posx+=0.1
            b1posy-=0.1
        if b==7:
            b1posx+=0.1
            b1posy-=0.1
        if b==8:
            b1posx+=0.1
            b1posy-=0.1
    if b1posx == 485 :
        if b==1:
            if b1posy >=150:
                b1posy -= 0.1
        if b==2:
            if b1posy >= 150:
                b1posy -= 0.1
        if b==3:
            if b1posy >= 150:
                b1posy -= 0.1
        if b==4:
            if b1posy >= 150:
                b1posy -= 0.1
        if b==5:
            if b1posy >= 150:
                b1posy -= 0.1
        if b==6:
            if b1posy >=150:
                b1posy -= 0.1
        if b==7:
            if b1posy >= 150:
                b1posy -= 0.1
        if b==8:
            if b1posy >= 150:
                b1posy -= 0.1
    if 485<b1posx<600:
        if b==1:
            b1posx-=0.1
            b1posy-=0.1
        if b==2:
            b1posx-=0.1
            b1posy-=0.1
        if b==3:
            b1posx-=0.1
            b1posy-=0.1
        if b==4:
            b1posx-=0.1
            b1posy-=0.1
        if b==5:
            b1posx-=0.1
            b1posy-=0.1
        if b==6:
            b1posx-=0.1
            b1posy-=0.1
        if b==7:
            b1posx-=0.1
            b1posy-=0.1
        if b==8:
            b1posx-=0.1
            b1posy-=0.1



    if  0 < c1posx < 115 :
        if c ==1:
            c1posx += 0.1
            c1posy -= 0.1
        if c ==2:
            c1posx += 0.1
            c1posy -= 0.1
        if c ==3:
            c1posx += 0.1
            c1posy -= 0.1
        if c ==4:
            c1posx += 0.1
            c1posy -= 0.1
        if c ==5:
            c1posx += 0.1
            c1posy -= 0.1
        if c ==6:
            c1posx += 0.1
            c1posy -= 0.1
        if c ==7:
            c1posx += 0.1
            c1posy -= 0.1
        if c ==8:
            c1posx += 0.1
            c1posy -= 0.1
    if c1posx == 115 :
        if c==1:
            if c1posy >=150:
                c1posy -= 0.1
        if c==2:
            if c1posy >= 150:
                c1posy -= 0.1
        if c==3:
            if c1posy >= 150:
                c1posy -= 0.1
        if c==4:
            if c1posy >= 150:
                c1posy -= 0.1
        if c==5:
            if c1posy >= 150:
                c1posy -= 0.1
        if c==6:
            if c1posy >=150:
                c1posy -= 0.1
        if c==7:
            if c1posy >= 150:
                c1posy -= 0.1
        if c==8:
            if c1posy >= 150:
                c1posy -= 0.1
    if 115<c1posx<173:
        if c==1:
            c1posx-=0.1
            c1posy-=0.1
        if c==2:
            c1posx-=0.1
            c1posy-=0.1
        if c==3:
            c1posx-=0.1
            c1posy-=0.1
        if c==4:
            c1posx-=0.1
            c1posy-=0.1
        if c==5:
            c1posx-=0.1
            c1posy-=0.1
        if c==6:
            c1posx-=0.1
            c1posy-=0.1
        if c==7:
            c1posx-=0.1
            c1posy-=0.1
        if c==8:
            c1posx-=0.1
            c1posy-=0.1
    if 173<c1posx<300:
        if c==1:
            c1posx+=0.1
            c1posy-=0.1
        if c==2:
            c1posx+=0.1
            c1posy-=0.1
        if c==3:
            c1posx+=0.1
            c1posy-=0.1
        if c==4:
            c1posx+=0.1
            c1posy-=0.1
        if c==5:
            c1posx+=0.1
            c1posy-=0.1
        if c==6:
            c1posx+=0.1
            c1posy-=0.1
        if c==7:
            c1posx+=0.1
            c1posy-=0.1
        if c==8:
            c1posx+=0.1
            c1posy-=0.1
    if c1posx == 300 :
        if c==1:
            if c1posy >=110:
                c1posy -= 0.1
        if c==2:
            if c1posy >= 110:
                c1posy -= 0.1
        if c==3:
            if c1posy >= 110:
                c1posy -= 0.1
        if c==4:
            if c1posy >= 110:
                c1posy -= 0.1
        if c==5:
            if c1posy >= 110:
                c1posy -= 0.1
        if c==6:
            if c1posy >= 110:
                c1posy -= 0.1
        if c==7:
            if c1posy >= 110:
                c1posy -= 0.1
        if c==8:
            if c1posy >= 110:
                c1posy -= 0.1
    if 300<c1posx<427:
        if c==1:
            c1posx-=0.1
            c1posy-=0.1
        if c==2:
            c1posx-=0.1
            c1posy-=0.1
        if c==3:
            c1posx-=0.1
            c1posy-=0.1
        if c==4:
            c1posx-=0.1
            c1posy-=0.1
        if c==5:
            c1posx-=0.1
            c1posy-=0.1
        if c==6:
            c1posx-=0.1
            c1posy-=0.1
        if c==7:
            c1posx-=0.1
            c1posy-=0.1
        if c==8:
            c1posx-=0.1
            c1posy-=0.1
    if 427<c1posx<485:
        if c==1:
            c1posx+=0.1
            c1posy-=0.1
        if c==2:
            c1posx+=0.1
            c1posy-=0.1
        if c==3:
            c1posx+=0.1
            c1posy-=0.1
        if c==4:
            c1posx+=0.1
            c1posy-=0.1
        if c==5:
            c1posx+=0.1
            c1posy-=0.1
        if c==6:
            c1posx+=0.1
            c1posy-=0.1
        if c==7:
            c1posx+=0.1
            c1posy-=0.1
        if c==8:
            c1posx+=0.1
            c1posy-=0.1
    if c1posx == 485 :
        if c==1:
            if c1posy >=150:
                c1posy -= 0.1
        if c==2:
            if c1posy >= 150:
                c1posy -= 0.1
        if c==3:
            if c1posy >= 150:
                c1posy -= 0.1
        if c==4:
            if c1posy >= 150:
                c1posy -= 0.1
        if c==5:
            if c1posy >= 150:
                c1posy -= 0.1
        if c==6:
            if c1posy >=150:
                c1posy -= 0.1
        if c==7:
            if c1posy >= 150:
                c1posy -= 0.1
        if c==8:
            if c1posy >= 150:
                c1posy -= 0.1
    if 485<c1posx<600:
        if c==1:
            c1posx-=0.1
            c1posy-=0.1
        if c==2:
            c1posx-=0.1
            c1posy-=0.1
        if c==3:
            c1posx-=0.1
            c1posy-=0.1
        if c==4:
            c1posx-=0.1
            c1posy-=0.1
        if c==5:
            c1posx-=0.1
            c1posy-=0.1
        if c==6:
            c1posx-=0.1
            c1posy-=0.1
        if c==7:
            c1posx-=0.1
            c1posy-=0.1
        if c==8:
            c1posx-=0.1
            c1posy-=0.1




    if  0 < d1posx < 115 :
        if d ==1:
            d1posx += 0.1
            d1posy += 0.1
        if d ==2:
            d1posx += 0.1
            d1posy += 0.1
        if d ==3:
            d1posx += 0.1
            d1posy += 0.1
        if d ==4:
            d1posx += 0.1
            d1posy += 0.1
        if d ==5:
            d1posx += 0.1
            d1posy += 0.1
        if d ==6:
            d1posx += 0.1
            d1posy += 0.1
        if d ==7:
            d1posx += 0.1
            d1posy += 0.1
        if d ==8:
            d1posx += 0.1
            d1posy += 0.1
    if d1posx == 115 :
        if d==1:
            if d1posy <= 400 :
                d1posy += 0.1
        if d==2:
            if d1posy <= 400:
                d1posy += 0.1
        if d==3:
            if d1posy <= 400:
                d1posy += 0.1
        if d==4:
            if d1posy <= 400:
                d1posy += 0.1
        if d==5:
            if d1posy <= 400:
                d1posy += 0.1
        if d==6:
            if d1posy <= 400:
                d1posy += 0.1
        if d==7:
            if d1posy <= 400:
                d1posy += 0.1
        if d==8:
            if d1posy <= 400:
                d1posy += 0.1
    if 115<d1posx<173:
        if d==1:
            d1posx-=0.1
            d1posy+=0.1
        if d==2:
            d1posx-=0.1
            d1posy+=0.1
        if d==3:
            d1posx-=0.1
            d1posy+=0.1
        if d==4:
            d1posx-=0.1
            d1posy+=0.1
        if d==5:
            d1posx-=0.1
            d1posy+=0.1
        if d==6:
            d1posx-=0.1
            d1posy+=0.1
        if d==7:
            d1posx-=0.1
            d1posy+=0.1
        if d==8:
            d1posx-=0.1
            d1posy+=0.1
    if 173<d1posx<300:
        if d==1:
            d1posx+=0.1
            d1posy+=0.1
        if d==2:
            d1posx+=0.1
            d1posy+=0.1
        if d==3:
            d1posx+=0.1
            d1posy+=0.1
        if d==4:
            d1posx+=0.1
            d1posy+=0.1
        if d==5:
            d1posx+=0.1
            d1posy+=0.1
        if d==6:
            d1posx+=0.1
            d1posy+=0.1
        if d==7:
            d1posx+=0.1
            d1posy+=0.1
        if d==8:
            d1posx+=0.1
            d1posy+=0.1
    if d1posx == 300 :
        if d==1:
            if d1posy <= 440 :
                d1posy += 0.1
        if d==2:
            if d1posy <= 440:
                d1posy += 0.1
        if d==3:
            if d1posy <= 440:
                d1posy += 0.1
        if d==4:
            if d1posy <= 440:
                d1posy += 0.1
        if d==5:
            if d1posy <= 440:
                d1posy += 0.1
        if d==6:
            if d1posy <= 440:
                d1posy += 0.1
        if d==7:
            if d1posy <= 440:
                d1posy += 0.1
        if d==8:
            if d1posy <= 440:
                d1posy += 0.1
    if 300<d1posx<427:
        if d==1:
            d1posx-=0.1
            d1posy+=0.1
        if d==2:
            d1posx-=0.1
            d1posy+=0.1
        if d==3:
            d1posx-=0.1
            d1posy+=0.1
        if d==4:
            d1posx-=0.1
            d1posy+=0.1
        if d==5:
            d1posx-=0.1
            d1posy+=0.1
        if d==6:
            d1posx-=0.1
            d1posy+=0.1
        if d==7:
            d1posx-=0.1
            d1posy+=0.1
        if d==8:
            d1posx-=0.1
            d1posy+=0.1
    if 427<d1posx<485:
        if d==1:
            d1posx+=0.1
            d1posy+=0.1
        if d==2:
            d1posx+=0.1
            d1posy+=0.1
        if d==3:
            d1posx+=0.1
            d1posy+=0.1
        if d==4:
            d1posx+=0.1
            d1posy+=0.1
        if d==5:
            d1posx+=0.1
            d1posy+=0.1
        if d==6:
            d1posx+=0.1
            d1posy+=0.1
        if d==7:
            d1posx+=0.1
            d1posy+=0.1
        if d==8:
            d1posx+=0.1
            d1posy+=0.1
    if d1posx == 485 :
        if d==1:
            if d1posy <= 400 :
                d1posy += 0.1
        if d==2:
            if d1posy <= 400:
                d1posy += 0.1
        if d==3:
            if d1posy <= 400:
                d1posy += 0.1
        if d==4:
            if d1posy <= 400:
                d1posy += 0.1
        if d==5:
            if d1posy <= 400:
                d1posy += 0.1
        if d==6:
            if d1posy <= 400:
                d1posy += 0.1
        if d==7:
            if d1posy <= 400:
                d1posy += 0.1
        if d==8:
            if d1posy <= 400:
                d1posy += 0.1
    if 485<d1posx<600:
        if d==1:
            d1posx-=0.1
            d1posy+=0.1
        if d==2:
            d1posx-=0.1
            d1posy+=0.1
        if d==3:
            d1posx-=0.1
            d1posy+=0.1
        if d==4:
            d1posx-=0.1
            d1posy+=0.1
        if d==5:
            d1posx-=0.1
            d1posy+=0.1
        if d==6:
            d1posx-=0.1
            d1posy+=0.1
        if d==7:
            d1posx-=0.1
            d1posy+=0.1
        if d==8:
            d1posx-=0.1
            d1posy+=0.1
    if  0 < e1posx < 115 :
        if e ==1:
            e1posx += 0.1
            e1posy += 0.1
        if e ==2:
            e1posx += 0.1
            e1posy += 0.1
        if e ==3:
            e1posx += 0.1
            e1posy += 0.1
        if e ==4:
            e1posx += 0.1
            e1posy += 0.1
        if e ==5:
            e1posx += 0.1
            e1posy += 0.1
        if e ==6:
            e1posx += 0.1
            e1posy += 0.1
        if e ==7:
            e1posx += 0.1
            e1posy += 0.1
        if e ==8:
            e1posx += 0.1
            e1posy += 0.1
    if e1posx == 115 :
        if e==1:
            if e1posy <= 400 :
                e1posy += 0.1
        if e==2:
            if e1posy <= 400:
                e1posy += 0.1
        if e==3:
            if e1posy <= 400:
                e1posy += 0.1
        if e==4:
            if e1posy <= 400:
                e1posy += 0.1
        if e==5:
            if e1posy <= 400:
                e1posy += 0.1
        if e==6:
            if e1posy <= 400:
                e1posy += 0.1
        if e==7:
            if e1posy <= 400:
                e1posy += 0.1
        if e==8:
            if e1posy <= 400:
                e1posy += 0.1
    if 115<e1posx<173:
        if e==1:
            e1posx-=0.1
            e1posy+=0.1
        if e==2:
            e1posx-=0.1
            e1posy+=0.1
        if e==3:
            e1posx-=0.1
            e1posy+=0.1
        if e==4:
            e1posx-=0.1
            e1posy+=0.1
        if e==5:
            e1posx-=0.1
            e1posy+=0.1
        if e==6:
            e1posx-=0.1
            e1posy+=0.1
        if e==7:
            e1posx-=0.1
            e1posy+=0.1
        if e==8:
            e1posx-=0.1
            e1posy+=0.1
    if 173<e1posx<300:
        if e==1:
            e1posx+=0.1
            e1posy+=0.1
        if e==2:
            e1posx+=0.1
            e1posy+=0.1
        if e==3:
            e1posx+=0.1
            e1posy+=0.1
        if e==4:
            e1posx+=0.1
            e1posy+=0.1
        if e==5:
            e1posx+=0.1
            e1posy+=0.1
        if e==6:
            e1posx+=0.1
            e1posy+=0.1
        if e==7:
            e1posx+=0.1
            e1posy+=0.1
        if e==8:
            e1posx+=0.1
            e1posy+=0.1
    if e1posx == 300 :
        if e==1:
            if e1posy <= 440 :
                e1posy += 0.1
        if e==2:
            if e1posy <= 440:
                e1posy += 0.1
        if e==3:
            if e1posy <= 440:
                e1posy += 0.1
        if e==4:
            if e1posy <= 440:
                e1posy += 0.1
        if e==5:
            if e1posy <= 440:
                e1posy += 0.1
        if e==6:
            if e1posy <= 440:
                e1posy += 0.1
        if e==7:
            if e1posy <= 440:
                e1posy += 0.1
        if e==8:
            if e1posy <= 440:
                e1posy += 0.1
    if 300<e1posx<427:
        if e==1:
            e1posx-=0.1
            e1posy+=0.1
        if e==2:
            e1posx-=0.1
            e1posy+=0.1
        if e==3:
            e1posx-=0.1
            e1posy+=0.1
        if e==4:
            e1posx-=0.1
            e1posy+=0.1
        if e==5:
            e1posx-=0.1
            e1posy+=0.1
        if e==6:
            e1posx-=0.1
            e1posy+=0.1
        if e==7:
            e1posx-=0.1
            e1posy+=0.1
        if e==8:
            e1posx-=0.1
            e1posy+=0.1
    if 427<e1posx<485:
        if e==1:
            e1posx+=0.1
            e1posy+=0.1
        if e==2:
            e1posx+=0.1
            e1posy+=0.1
        if e==3:
            e1posx+=0.1
            e1posy+=0.1
        if e==4:
            e1posx+=0.1
            e1posy+=0.1
        if e==5:
            e1posx+=0.1
            e1posy+=0.1
        if e==6:
            e1posx+=0.1
            e1posy+=0.1
        if e==7:
            e1posx+=0.1
            e1posy+=0.1
        if e==8:
            e1posx+=0.1
            e1posy+=0.1
    if e1posx == 485 :
        if e==1:
            if e1posy <= 400 :
                e1posy += 0.1
        if e==2:
            if e1posy <= 400:
                e1posy += 0.1
        if e==3:
            if e1posy <= 400:
                e1posy += 0.1
        if e==4:
            if e1posy <= 400:
                e1posy += 0.1
        if e==5:
            if e1posy <= 400:
                e1posy += 0.1
        if e==6:
            if e1posy <= 400:
                e1posy += 0.1
        if e==7:
            if e1posy <= 400:
                e1posy += 0.1
        if e==8:
            if e1posy <= 400:
                e1posy += 0.1
    if 485<e1posx<600:
        if e==1:
            e1posx-=0.1
            e1posy+=0.1
        if e==2:
            e1posx-=0.1
            e1posy+=0.1
        if e==3:
            e1posx-=0.1
            e1posy+=0.1
        if e==4:
            e1posx-=0.1
            e1posy+=0.1
        if e==5:
            e1posx-=0.1
            e1posy+=0.1
        if e==6:
            e1posx-=0.1
            e1posy+=0.1
        if e==7:
            e1posx-=0.1
            e1posy+=0.1
        if e==8:
            e1posx-=0.1
            e1posy+=0.1
    if  0 < f1posx < 115 :
        if f ==1:
            f1posx += 0.1
            f1posy += 0.1
        if f ==2:
            f1posx += 0.1
            f1posy += 0.1
        if f ==3:
            f1posx += 0.1
            f1posy += 0.1
        if f ==4:
            f1posx += 0.1
            f1posy += 0.1
        if f ==5:
            f1posx += 0.1
            f1posy += 0.1
        if f ==6:
            f1posx += 0.1
            f1posy += 0.1
        if f ==7:
            f1posx += 0.1
            f1posy += 0.1
        if f ==8:
            f1posx += 0.1
            f1posy += 0.1
    if f1posx == 115 :
        if f==1:
            if f1posy <= 400 :
                f1posy += 0.1
        if f==2:
            if f1posy <= 400:
                f1posy += 0.1
        if f==3:
            if f1posy <= 400:
                f1posy += 0.1
        if f==4:
            if f1posy <= 400:
                f1posy += 0.1
        if f==5:
            if f1posy <= 400:
                f1posy += 0.1
        if f==6:
            if f1posy <= 400:
                f1posy += 0.1
        if f==7:
            if f1posy <= 400:
                f1posy += 0.1
        if f==8:
            if f1posy <= 400:
                f1posy += 0.1
    if 115<f1posx<173:
        if f==1:
            f1posx-=0.1
            f1posy+=0.1
        if f==2:
            f1posx-=0.1
            f1posy+=0.1
        if f==3:
            f1posx-=0.1
            f1posy+=0.1
        if f==4:
            f1posx-=0.1
            f1posy+=0.1
        if f==5:
            f1posx-=0.1
            f1posy+=0.1
        if f==6:
            f1posx-=0.1
            f1posy+=0.1
        if f==7:
            f1posx-=0.1
            f1posy+=0.1
        if f==8:
            f1posx-=0.1
            f1posy+=0.1
    if 173<f1posx<300:
        if f==1:
            f1posx+=0.1
            f1posy+=0.1
        if f==2:
            f1posx+=0.1
            f1posy+=0.1
        if f==3:
            f1posx+=0.1
            f1posy+=0.1
        if f==4:
            f1posx+=0.1
            f1posy+=0.1
        if f==5:
            f1posx+=0.1
            f1posy+=0.1
        if f==6:
            f1posx+=0.1
            f1posy+=0.1
        if f==7:
            f1posx+=0.1
            f1posy+=0.1
        if f==8:
            f1posx+=0.1
            f1posy+=0.1
    if f1posx == 300 :
        if f==1:
            if f1posy <= 440 :
                f1posy += 0.1
        if f==2:
            if f1posy <= 440:
                f1posy += 0.1
        if f==3:
            if f1posy <= 440:
                f1posy += 0.1
        if f==4:
            if f1posy <= 440:
                f1posy += 0.1
        if f==5:
            if f1posy <= 440:
                f1posy += 0.1
        if f==6:
            if f1posy <= 440:
                f1posy += 0.1
        if f==7:
            if f1posy <= 440:
                f1posy += 0.1
        if f==8:
            if f1posy <= 440:
                f1posy += 0.1
    if 300<f1posx<427:
        if f==1:
            f1posx-=0.1
            f1posy+=0.1
        if f==2:
            f1posx-=0.1
            f1posy+=0.1
        if f==3:
            f1posx-=0.1
            f1posy+=0.1
        if f==4:
            f1posx-=0.1
            f1posy+=0.1
        if f==5:
            f1posx-=0.1
            f1posy+=0.1
        if f==6:
            f1posx-=0.1
            f1posy+=0.1
        if f==7:
            f1posx-=0.1
            f1posy+=0.1
        if f==8:
            f1posx-=0.1
            f1posy+=0.1
    if 427<f1posx<485:
        if f==1:
            f1posx+=0.1
            f1posy+=0.1
        if f==2:
            f1posx+=0.1
            f1posy+=0.1
        if f==3:
            f1posx+=0.1
            f1posy+=0.1
        if f==4:
            f1posx+=0.1
            f1posy+=0.1
        if f==5:
            f1posx+=0.1
            f1posy+=0.1
        if f==6:
            f1posx+=0.1
            f1posy+=0.1
        if f==7:
            f1posx+=0.1
            f1posy+=0.1
        if f==8:
            f1posx+=0.1
            f1posy+=0.1
    if f1posx == 485 :
        if f==1:
            if f1posy <= 400 :
                f1posy += 0.1
        if f==2:
            if f1posy <= 400:
                f1posy += 0.1
        if f==3:
            if f1posy <= 400:
                f1posy += 0.1
        if f==4:
            if f1posy <= 400:
                f1posy += 0.1
        if f==5:
            if f1posy <= 400:
                f1posy += 0.1
        if f==6:
            if f1posy <= 400:
                f1posy += 0.1
        if f==7:
            if f1posy <= 400:
                f1posy += 0.1
        if f==8:
            if f1posy <= 400:
                f1posy += 0.1
    if 485<f1posx<600:
        if f==1:
            f1posx-=0.1
            f1posy+=0.1
        if f==2:
            f1posx-=0.1
            f1posy+=0.1
        if f==3:
            f1posx-=0.1
            f1posy+=0.1
        if f==4:
            f1posx-=0.1
            f1posy+=0.1
        if f==5:
            f1posx-=0.1
            f1posy+=0.1
        if f==6:
            f1posx-=0.1
            f1posy+=0.1
        if f==7:
            f1posx-=0.1
            f1posy+=0.1
        if f==8:
            f1posx-=0.1
            f1posy+=0.1

def quitGame():
    pygame.quit()
    sys.exit()
def lastpage():
    global winplayer1,winplayer2,timer
    if winplayer1 == True:
        surface.blit(winplayer1Image,(0,0))
    if winplayer2 == True:
        surface.blit(winplayer2Image,(0,0))
    for event in GAME_EVENTS.get():
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if winplayer1==True:
                    winplayer1=False
                    timer = 0
                    import project
                if winplayer2==True:
                    winplayer2=False
                    timer = 0
                    import project
firsvar()
if gamePage==True:
    while gamePage:
        #timer = GAME_TIME.get_ticks()
        surface.fill((0,0,0))
        surface.blit(backgroundgameImage,(0,0))
        tatbigh()
        mousePosition= pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] == True :
            mousePressed = True
        else:
            mousePressed = False

        sakhteman1_1 = building(300 - 40,windowHeight-80,200,27,20,sakhtemanasliImage,1)
        sakhteman2_1 = building(300 - 40,0,200,27,20,sakhtemanasli2Image,1)
        sakhteman1_2 = building(150-70,windowHeight-120,150,23,18,sakhtemanfareeImage,2)
        sakhteman1_3 = building(600-150,windowHeight-120,150,23,18,sakhtemanfareeImage,2)
        sakhteman2_2 = building(150-70,50,150,23,18,sakhtemanfaree2Image,2)
        sakhteman2_3 = building(600-150,50,150,23,18,sakhtemanfaree2Image,2)
        pygame.draw.rect(surface,(0,0,255),(0,275,600,50))
        pygame.draw.rect(surface,(210,105,30),(57,275,116,50))
        pygame.draw.rect(surface,(210,105,30),(233,275,134,50))
        pygame.draw.rect(surface,(210,105,30),(427,275,116,50))
        for event in GAME_EVENTS.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quitGame()
            if event.type == GAME_GLOBALS.QUIT:
                quitGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clickdown()
            if event.type == pygame.MOUSEBUTTONUP:
                clickup()
        if a1posx !=0 or a1posy !=0:
            if ahero1.getx() !=-1000 and ahero1.gety() != -1000:
                ahero1 = hero(a,1,a1posx,a1posy)
                move()
        if b1posx !=0 or b1posy !=0:
            if bhero1.getx() !=-1000 and bhero1.gety() != -1000:
                bhero1 = hero(b,1,b1posx,b1posy)
                move()
        if c1posx !=0 or c1posy !=0:
            if chero1.getx() !=-1000 and chero1.gety() != -1000:
                chero1 = hero(c,1,c1posx,c1posy)
                move()
        if d1posx !=0 or d1posy !=0:
            if dhero1.getx() !=-1000 and dhero1.gety() != -1000:
                dhero1 = hero(d,1,d1posx,d1posy)
                move()
        if e1posx !=0 or e1posy !=0:
            if ehero1.getx() !=-1000 and ehero1.gety() != -1000:
                ehero1 = hero(e,1,e1posx,e1posy)
                move()
        if f1posx !=0 or f1posy !=0:
            if fhero1.getx() !=-1000 and fhero1.gety() != -1000:
                fhero1 = hero(f,1,f1posx,f1posy)
                move()
        if 10100 > timer > 10000:
            if sakhteman1_1.gethealth() + sakhteman1_2.gethealth() + sakhteman1_3.gethealth() > sakhteman2_1.gethealth() + sakhteman2_2.gethealth() + sakhteman2_3.gethealth():
                winplayer1 = True
                gamePage = False
            if sakhteman1_1.gethealth() + sakhteman1_2.gethealth() + sakhteman1_3.gethealth() <= sakhteman2_1.gethealth() + sakhteman2_2.gethealth() + sakhteman2_3.gethealth():
                winplayer2 = True
                gamePage = False
        print(timer)
        pygame.display.update()
if gamePage == False:
    while True:
        if winplayer1 == True:
            surface.blit(winplayer1Image,(0,0))
            pygame.display.update()
        if winplayer2 == True:
            surface.blit(winplayer2Image,(0,0))
            pygame.display.update()
        for event in GAME_EVENTS.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if winplayer1==True:
                        winplayer1=False
                        timer = 0
                        import project
                    if winplayer2==True:
                        winplayer2=False
                        timer = 0
                        import project
