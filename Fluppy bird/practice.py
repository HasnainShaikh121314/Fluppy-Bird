import pygame 
import random
pygame.init()

screen=pygame.display.set_mode((400,470))

pygame.display.set_caption(("Fluppy bird"))
running=True



class load :
    def __init__(self,a):
        self.image=a
    def loadimg(self):
        c=pygame.image.load(self.image+".png") 
        return c   
bgobj1=load("background/bg2")
background1=bgobj1.loadimg()
bgobj3=load("background/bg2")
background3=bgobj3.loadimg()
bgobj2=load("background/ground")
background2=bgobj2.loadimg()
bgobj4=load("background/ground")
background4=bgobj4.loadimg()
goob5=load("gameover")
gameoverimg=goob5.loadimg()
startbobg6=load("play button")
startb=startbobg6.loadimg()



ground_scroller1=0
ground_scroller2=220
speed=2
#towerobj1=load("towerlower")
#towerobj1=load("towerlower")
#towerlower=towerobj1.loadimg()
#towerobj2=load("towerupper")
#towerupper=towerobj2.loadimg()
tower1img=[]
tower2img=[]
towerx=[]
tower1y=[]
tower2y=[]
towerx_c=[]
tx=482
numeric=4
tower1yl=[-100,-120,0]
tower2yl=[250,230,350]
rect1=[]
def towerload():
    tx=482
    for i in range(numeric):
        
        
        tower1img.append(pygame.image.load('towerupper.png'))
        tower2img.append(pygame.image.load('towerlower.png'))
        l=random.choice(tower1yl)
        indx=tower1yl.index(l)
        tower1y.append(l)
        tower2y.append(tower2yl[indx])
        towerx.append(tx)
        towerx_c.append(tx)
        
        tx+=140
towerload()
button1=pygame.Rect(164,230,70,40)

birdlist=["bird1","bird2","bird3"]
birdvar=birdlist[0]
birdx=50
birdy=200
bi=0
i=0
jumpl=False
jump=False
jump_h=6
gravity=3
velocity=jump_h
checkjmp=0
start=False
gameover=False
gameover1=True
CLOCK=pygame.time.Clock()

def background():
      screen.blit(background1,(0,0))
      screen.blit(background3,(220,0))
      

while running:    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running =False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if start==False or gameover:
                if button1.collidepoint(event.pos):
                    start=True
        
        if event.type==pygame.KEYDOWN:
           if event.key==pygame.K_SPACE:
               
               jumpl=False
               jump=True
    
    if start==False:
        #c=pygame.mouse.get_pos()
        bird=pygame.image.load("bird/"+birdvar+".png")
        background()
        screen.blit(background2,(ground_scroller1,395))
        screen.blit(background4,(ground_scroller2,395))    
        
        screen.blit(startb,(60,180))
        if gameover1:
            screen.blit(gameoverimg,(120,100))
        if i%6==0:
            if  bi==len(birdlist):
                bi=0
                
                    
            birdvar=birdlist[bi]
            bi+=1
        
        i+=1
        screen.blit(bird,(40,birdy))
       # pygame.draw.rect(screen,(255,0,0),button1)
       
     
    
    if start:
        rect3=pygame.Rect(birdx,birdy,10,10)
        bird=pygame.image.load("bird/"+birdvar+".png")
        background()
      

        
        if jump:
            birdy-=velocity
            checkjmp+=1
            bi=2
            
            if checkjmp>=8  :
                checkjmp=0
                jumpl=True
                jump=False
            
        if jumpl:
            bi=0
            
            birdy+=gravity
            pygame.transform.rotate(bird,-90)
            


        for j in range(numeric):
            rect1=pygame.Rect(towerx[j],tower1y[j],43,252)  
            rect2=pygame.Rect(towerx[j],tower2y[j],43,252) 
            towerx[j]-=1
            
            if towerx[j]<-30:
                towerx_c[j]+=50
                towerx[j]=500
            screen.blit(tower1img[j],(towerx[j],tower1y[j]))
            screen.blit(tower2img[j],(towerx[j],tower2y[j]))
            if rect3.colliderect(rect2):
                 gameover=True
                 start =False

            if rect3.colliderect(rect1):
                gameover=True
                start=False
        if birdy>=395:
            gameover=True
            start =False
        
            
        screen.blit(background2,(ground_scroller1,395))
        screen.blit(background4,(ground_scroller2,395))    
        ground_scroller1-=speed
        ground_scroller2-=speed
        
        if i%20==0:
            ground_scroller2=220    
        if i%20==0:
            ground_scroller1=0

        
        if i%6==0:
            if  bi==len(birdlist):
                bi=0
                
                    
            birdvar=birdlist[bi]
            bi+=1
        
        i+=1
        
        
        screen.blit(bird,(40,birdy))


    if gameover:
       
       birdx=50
       birdy=200
      
       towerx_c[0]+=50
       towerx[0]=1000
       background()
       
       screen.blit(startb,(60,180))
       
       screen.blit(gameoverimg,(120,100))
       gameover=False
       gameover1=True

    pygame.display.update()
    CLOCK.tick(60)
