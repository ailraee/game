import pygame,sys
import pygame.locals as game_globals
import pygame.event as game_event
pygame.init()
surface=pygame.display.set_mode((600,800))
click=False
x=400
y=300
img=pygame.image.load('barbarian.jpg')
pos=(x,y)
while True:
    surface.fill((0,0,0))
    surface.blit(img,(x,y))
    for event in game_event.get():
        if event.type==game_globals.QUIT:
            pygame.quit()
            sys.exit()
    if  pygame.mouse.get_pressed()[0] and x<=pygame.mouse.get_pos()[0]<=x+40 and y<=pygame.mouse.get_pos()[1]<=y+50:
        click=True
    if not pygame.mouse.get_pressed()[0]:
        click=False
    if click:
        x=pygame.mouse.get_pos()[0]
        y=pygame.mouse.get_pos()[1]
        pos=(x,y)
        print(pos)
    else:
        x=pos[0]
        y=pos[1]
    pygame.display.flip()