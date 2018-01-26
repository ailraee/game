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
            self.bord = (xpos - 20,ypos -20,80,90)
            self.color = (255,0,0)
            if self.player == 1:
                self.image = pygame.image.load("archer.jpg")
            if self.player == 2:
                self.image = pygame.image.load("archer2.jpg")
        if self.kind == 2:
            self.health = 65
            self.power = 10
            self.bord = (xpos - 10,ypos - 10,60,70)
            self.color = (0,255,0)
            if self.player == 1:
                self.image = pygame.image.load("barbarian.jpg")
            if self.player == 2:
                self.image = pygame.image.load("barbarian2.jpg")
        if self.kind == 3:
            self.health = 85
            self.power = 9
            self.bord = (self.x - 14,self.y - 14,68,78)
            self.color = (0,0,255)
            if self.player == 1:
                self.image = pygame.image.load("dragon.png")
            if self.player == 2:
                self.image = pygame.image.load("dragon2.png")
        if self.kind == 4:
            self.health = 100
            self.power = 12
            self.bord = (xpos - 10,ypos - 10,60,70)
            self.color = (255,255,0)
            if self.player == 1:
                self.image = pygame.image.load("giant.png")
            if self.player == 2:
                self.image = pygame.image.load("giant2.png")
        if self.kind == 5:
            self.health = 80
            self.power = 9
            self.bord = (xpos - 20,ypos - 20,80,90)
            self.color = (0,255,255)
            if self.player == 1:
                self.image = pygame.image.load("goblin.png")
            if self.player == 2:
                self.image = pygame.image.load("goblin2.png")
        if self.kind == 6:
            self.health = 90
            self.power = 10
            self.bord = (xpos - 16,ypos - 16,72,82)
            self.color = (255,0,255)
            if self.player == 1:
                self.image = pygame.image.load("prince.jpg")
            if self.player == 2:
                self.image = pygame.image.load("prince2.jpg")
        if self.kind == 7:
            self.health = 50
            self.power = 6
            self.bord = (self.x - 14,self.y - 14,68,78)
            self.color = (127,127,127)
            if self.player == 1:
                self.image = pygame.image.load("skeleton.jpg")
            if self.player == 2:
                self.image = pygame.image.load("skeleton2.jpg")
        if self.kind == 8:
            self.helth = 80
            self.power = 10
            self.bord =(xpos - 18,ypos - 18,76,86)
            self.color = (200,200,200)
            if self.player == 1:
                self.image = pygame.image.load("wizard.jpg")
            if self.player == 2:
                self.image = pygame.image.load("wizard2.jpg")
        if self.kind == 9:
            return None
        pygame.draw.rect(surface,self.color,self.bord)
        surface.blit(self.image,(self.x,self.y))


pygame.init()
windowWidth = 800
windowHeight = 600
surface = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption("The Game")
backgroundgameImage=pygame.image.load("backgroundgame.jpg")

archerCImage=pygame.image.load("archercard.jpg")
barbarianCImage=pygame.image.load("barbarianCard.jpg")
dragonCImage=pygame.image.load("dragonCard.png")
giantCImage=pygame.image.load("GiantCard.png")
goblinCImage=pygame.image.load("goblinCard.png")
princeCImage=pygame.image.load("princeCard.jpg")
skeletonCImage=pygame.image.load("skeletonCard.jpg")
wizardCImage=pygame.image.load("wizardCard.jpg")
sakhtemanasliImage=pygame.image.load("sakhtemanasli.jpg")
sakhtemanfareeImage=pygame.image.load("sakhtemanfaree.jpg")

mousePosition = None
mousePressed = False


timer = 0
a,b,c,d,e,f=0,0,0,0,0,0
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
def quitGame():
    pygame.quit()
    sys.exit()
# ‘main’ loop
firsvar()
while True:
    surface.fill((0,0,0))
    surface.blit(backgroundgameImage,(0,0))
    tatbigh()
    mousePosition= pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] == True :
        mousePressed = True
    else:
        mousePressed = False
    pygame.draw.rect(surface,(100,150,200),(300-40-27,windowHeight-80-27,134,134))
    pygame.draw.rect(surface,(100,150,200),(300-40-27,-27,134,134))
    pygame.draw.rect(surface,(120,230,180),(150-70-23,windowHeight-120-23,113,113))
    pygame.draw.rect(surface,(120,230,180),(150-70-23,50-23,113,113))
    pygame.draw.rect(surface,(120,230,180),(600-150-23,windowHeight-120-23,113,113))
    pygame.draw.rect(surface,(120,230,180),(600-150-23,50-23,113,113))
    surface.blit(sakhtemanasliImage,(300 - 40,windowHeight-80))
    surface.blit(sakhtemanasliImage,(300 - 40,0))
    surface.blit(sakhtemanfareeImage,(150-70,windowHeight-120))
    surface.blit(sakhtemanfareeImage,(600-150,windowHeight-120))
    surface.blit(sakhtemanfareeImage,(150-70,50))
    surface.blit(sakhtemanfareeImage,(600-150,50))
    
    ahero = hero(a,1,100,100)
    bhero = hero(b,1,150,200)
    chero = hero(c,1,550,100)
    dhero = hero(d,1,120,190)
    ehero = hero(e,1,220,90)
    fhero = hero(f,1,280,120)
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitGame()
        if event.type == GAME_GLOBALS.QUIT:
            quitGame()
    
    pygame.display.update()
