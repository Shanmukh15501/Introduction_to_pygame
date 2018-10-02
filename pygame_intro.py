import pygame
pygame.init()
parent=pygame.display.set_mode((400,500))
pygame.display.set_caption("hello World")
run=True
x=50
y=50
vel=5
width=40
height=60
while(run):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        keys=pygame.key.get_pressed()
        if(keys[pygame.K_LEFT]):
           x=x-vel
        if(keys[pygame.K_RIGHT]):
           x=x+vel
        if(keys[pygame.K_UP]):
           y=y-vel
        if(keys[pygame.K_DOWN]):
           y=y+vel
        pygame.draw.rect(parent,(0,255,0),(x,y,width,height))
        pygame.display.update()
pygame.quit()
           
