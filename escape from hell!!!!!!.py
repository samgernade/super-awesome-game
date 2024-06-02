import pygame, sys
from pygame.locals import * 

pygame.init()

WINDOW = pygame.display.set_mode((1000,600)) #Defining Window and its size
pygame.display.set_caption('First Pygame') #Defining the window caption
myfont = pygame.font.SysFont("monospace", 15)

# render text
label = myfont.render("ESCAPE FROM HELL AAAAAAAAAAAAAAAA", 4, (0,255,40))
label2 = myfont.render("you won yaayyyyyy hooray", 4, (0,255,40))

def death():
    for x in explosionlist:
        pygame.time.delay(200)
        explosion = pygame.image.load(x)
        WINDOW.blit(explosion,(x1,y1))
        pygame.display.flip()
RED = (255,0,0)
WEIRDRED = (255,10,50)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
PURPLE = (128,0,128)
WHITE = (255,255,255)
BLACK = (0,0,0)
FPS = 200
clock = pygame.time.Clock()
x1 = 0
y1 = 570
fnx = 300
fny = 3000
ex = 300
ey = 300
ly = 300
winner = False
dead = False
won = False
level1 = True
level2 = False
level3 = False
notdead = True
doorunlocked = False
greenfn = pygame.image.load('green fortnite.png')
volcano = pygame.image.load('stupidvolcano!!.jpg')
direction1 = 'down'
lava = pygame.image.load('lava.png')
lava2 = pygame.image.load('lava - Copy.png')
explosion = pygame.image.load('explosionframe1.png')
explosionlist = ['explosionframe1.png','explosionframe2.png','explosionframe4.png','explosionframe5.png','explosionframe6.png']
while True: #Forever Lo       
    WINDOW.fill(WHITE)
    
    WINDOW.blit(volcano,(0,0))
    WINDOW.blit(greenfn,(fnx,fny))
    key = pygame.key.get_pressed()
    player =  pygame.draw.rect(WINDOW,BLUE,(x1,y1,30,30))
    if key[pygame.K_0]:
        level1 = False
        level2 = True
    if notdead == True:
            if key[pygame.K_UP] and y1 > 0:
                y1 -= 1
            if key[pygame.K_RIGHT] and x1 < 970:
                x1 += 1
            if key[pygame.K_LEFT] and x1 > 0:
                x1 -= 1
            if key[pygame.K_DOWN] and y1 < 570:
                y1 += 1
    for event in pygame.event.get(): #Event Loop
            if event.type == QUIT: #Checks if you hit the "X" in the window
                pygame.quit()
                sys.exit()
    if dead == True:
        death() 
    if level1 == True:
        WINDOW.blit(label, (50, 50))
        if won == False:
            goodunscaryrectangle = pygame.draw.rect(WINDOW,GREEN,(970,0,30,30))
            lavasprite = WINDOW.blit(lava,(300,ly))
            lavasprite2 = WINDOW.blit(lava2,(100,100))
            lavasprite3 = WINDOW.blit(lava2,(600,400))
            lavasprite4 = WINDOW.blit(lava2,(600,500))
        if won == True:
            level1 = False
            level2 = True
        if player.colliderect(lavasprite):
            dead = True
        if player.colliderect(lavasprite2):
            dead = True
        if player.colliderect(lavasprite3):
            dead = True
        if player.colliderect(lavasprite3):
            dead = True
        if player.colliderect(goodunscaryrectangle):
            won = True
        if ly == 300:
            direction1 = 'up'
        if ly == 0:
            direction1 = 'down'
        if direction1 == 'down':
            ly +=1
        if direction1 == 'up':
            ly -=1
    if level2 == True:
            verygoodunscarysuperawesomerectangle = pygame.draw.rect(WINDOW,GREEN,(0,0,30,30))
            lava1 = pygame.draw.rect(WINDOW,RED,(0,200,1000,400))
            lava2 = pygame.draw.rect(WINDOW,RED,(600,0,80,160))
            lava3 = pygame.draw.rect(WINDOW,RED,(520,0,80,100))
            lava4 = pygame.draw.rect(WINDOW,RED,(480,150,80,100))
            lava5 = pygame.draw.rect(WINDOW,RED,(250,100,230,100))
            if player.colliderect(lava1):
                dead = True
            if player.colliderect(lava2):
                dead = True
            if player.colliderect(lava3):
                dead = True
            if player.colliderect(lava4):
                dead = True
            if player.colliderect(lava5):
                dead = True
            if player.colliderect(verygoodunscarysuperawesomerectangle):
                level2 = False
                level3 = True
    if level3 == True:
        VERYVERYVERYAWESOMESAUCESUPERCOOLSIGMASUPERGOODGREATAWESOMEGODLYFREAKINGDOODADILYHUGGABLEDRUGGABLESNUGGLEABLErectangle = pygame.draw.rect(WINDOW,GREEN,(0,570,30,30))
        bad = pygame.draw.rect(WINDOW,WEIRDRED,(0,100,900,400))
        verybad = pygame.draw.rect(WINDOW,WEIRDRED,(80,0,30,60))
        verybad2 = pygame.draw.rect(WINDOW,WEIRDRED,(160,40,30,60))
        verybad3 = pygame.draw.rect(WINDOW,WEIRDRED,(240,0,200,50))
        verybad4 = pygame.draw.rect(WINDOW,WEIRDRED,(660,40,30,90))
        verybad5 = pygame.draw.rect(WINDOW,WEIRDRED,(740,40,60,100))
        switch = pygame.draw.rect(WINDOW,WHITE,(705,60,15,25))
        lockeddoor = pygame.draw.rect(WINDOW,WHITE,(870,0,30,100))
        verybad6 = pygame.draw.rect(WINDOW,WEIRDRED,(900,100,50,30))
        verybad7 = pygame.draw.rect(WINDOW,WEIRDRED,(950,200,50,30))
        verybad8 = pygame.draw.rect(WINDOW,WEIRDRED,(900,300,50,30))
        verybad9 = pygame.draw.rect(WINDOW,WEIRDRED,(950,400,50,30))
        verybad10 = pygame.draw.rect(WINDOW,WEIRDRED,(900,470,50,30))
        verybad11 = pygame.draw.rect(WINDOW,WEIRDRED,(31,550,100,100))
        if player.colliderect(verybad):
                dead = True
        if player.colliderect(verybad2):
                dead = True
        if player.colliderect(verybad3):
                dead = True
        if player.colliderect(verybad4):
                dead = True
        if player.colliderect(verybad5):
                dead = True
        if player.colliderect(verybad6):
                dead = True
        if player.colliderect(verybad7):
                dead = True
        if player.colliderect(verybad8):
                dead = True
        if player.colliderect(verybad9):
                dead = True
        if player.colliderect(verybad10):
                dead = True
        if player.colliderect(verybad11):
                dead = True
        if player.colliderect(bad):
             dead = True
        if player.colliderect(switch):
            doorunlocked = True
        if player.colliderect(lockeddoor):
                if doorunlocked == False:
                     dead = True
                if doorunlocked == True:
                     pass
        if player.colliderect(VERYVERYVERYAWESOMESAUCESUPERCOOLSIGMASUPERGOODGREATAWESOMEGODLYFREAKINGDOODADILYHUGGABLEDRUGGABLESNUGGLEABLErectangle):
             winner = True
    if winner == True:
         level3 = False
    if winner == True:
        WINDOW.blit(label2,(100,100))
        pygame.time.wait(5000)
        dead = True
        
        
    pygame.display.update() #Updates Screen
    clock.tick(FPS)