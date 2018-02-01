import pygame,sys,random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
#classes

#class hero:
   # def __init__

#variable
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

windowsWidth = 800
windowsHeight = 600

a = pygame.time.Clock()

mousePosition = None
mousePressed = False

gameOver = False

oneplayer = False
twoplayer = False

safhe1 = False
safhe = True

winplayer1=False
winplayer2=False
wincomputer=False


backgroundImage = pygame.image.load("background.png")
safhe1Image = pygame.image.load("safhe1.jpg")
player1Image = pygame.image.load("oneplayer.png")
player2Image = pygame.image.load("twoplayer.png")
clickImage = pygame.image.load("click.png")

wincomputerImage = pygame.image.load("wincomputer.jpg")
waitImage = pygame.image.load("wait.png")
icon=pygame.image.load('icon.jpg')

timer = 0
#function
def gameOut():
    pygame.quit()
    sys.exit()
def fsafhe():
    global safhe,safhe1
    safhe = False
    safhe1 = True
    surface.fill((255,255,255))
def checkbox(xpos1,xpos2,ypos1,ypos2):
    if mousePosition[0] > xpos1 and mousePosition[0] < xpos2:
        if mousePosition[1] > ypos1 and mousePosition[1]< ypos2:
            return True
    return False
def fsafhe1():
    global oneplayer,twoplayer
    surface.blit(safhe1Image,(0,0))
    surface.blit(player1Image,(windowsWidth/2 - 380,windowsHeight/2))
    surface.blit(player2Image,(windowsWidth/2 + 200,windowsHeight/2))
    if mousePressed ==True and checkbox(windowsWidth/2 - 380,windowsWidth/2 - 380+154,windowsHeight/2,windowsHeight/2+75):
        oneplayer = True
    if mousePressed == True and checkbox(windowsWidth/2 + 200,windowsWidth/2 +380+154,windowsHeight/2,windowsHeight/2+75):
        twoplayer = True
def foneplayer():
    import local
def ftwoplayer():
    import two_player
    
pygame.init()
flags=GAME_GLOBALS.DOUBLEBUF
surface = pygame.display.set_mode((windowsWidth,windowsHeight),flags)
pygame.display.set_caption("Clash Royal")
pygame.display.set_icon(icon)
def main():
    global timer,safhe,safhe1,mousePosition,mousePressed,oneplayer,twoplayer
    while True:
        timer = GAME_TIME.get_ticks()
        mousePosition= pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] == True :
            mousePressed = True
        else:
            mousePressed = False
        if safhe == True:
            surface.blit(backgroundImage,(0,0))
            if timer > 0 and timer < 4000 :
                surface.blit(waitImage,(windowsWidth/2 -150,windowsHeight-75))
            if timer > 4000:
                surface.blit(clickImage,(windowsWidth/2 -63,windowsHeight-67))
                if mousePressed ==True and checkbox(windowsWidth/2 -63,windowsWidth/2 -63 + 154,windowsHeight-75,windowsHeight):
                    fsafhe()
        if safhe1 == True:
            fsafhe1()
        if oneplayer == True:
            foneplayer()
        if twoplayer == True:
            ftwoplayer()
            
        for event in GAME_EVENTS.get():
            if event.type==pygame.QUIT:
                gameOut()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameOut()
                if event.key == pygame.K_SPACE:
                    oneplayer = False
                    twoplayer = False
                    fsafhe()
        pygame.display.update()
main()
