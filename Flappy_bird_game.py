# -*- coding: utf-8 -*-

import pygame
import random
import time

pygame.init()
displayh=600
displayw=800
gamedisplay=pygame.display.set_mode((displayw,displayh))
gamedisplay.fill((255,255,255))
pygame.display.set_caption("Flappy bird game")
clock=pygame.time.Clock()


def text_objects(text,font):
    textsurface=font.render(text,True,(0,0,0))
    return textsurface,textsurface.get_rect()

def button(color,x,y,l,h,text,action=None):
    mouse=pygame.mouse.get_pos()
    pygame.draw.rect(gamedisplay,color,(x,y,l,h))
    
    
    if x<mouse[0]<x+l and y<mouse[1]<y+h:
        if pygame.mouse.get_pressed()[0]:    
            action()
            
    small=pygame.font.Font("freesansbold.ttf",20)
    textsurface,textrect=text_objects(text,small)
    textrect=((x+l/2),(y+h/2))
    gamedisplay.blit(textsurface,textrect)
            
                
def ext():
    pygame.quit()
    quit()

    
#intro page
def intro():
    intro=True
    def start():
        nonlocal intro
        intro=False

    smalltext=pygame.font.Font("freesansbold.ttf",80)
    textsurface,textrect=text_objects("flappy bird game",smalltext)
    while intro:
        

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                ext()
                
        textrect.center=(displayw/2,displayh/2)
        gamedisplay.blit(textsurface,textrect)
        button((200,0,0),150,450,100,50,"quit",ext)
        button((0,200,0),550,450,100,50,"start",start)
        
        pygame.display.update()
        clock.tick(15)
def scoredisplay(text):
    largetext=pygame.font.Font('freesansbold.ttf',55)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=(displayw/2,20)
    gamedisplay.blit(textsurf,textrect)
    pygame.display.update()    
def message_display(text):
    largetext=pygame.font.Font('freesansbold.ttf',115)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((displayw/2),displayh/2)
    gamedisplay.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(2)

#main loop
def gameloop():
    gamedisplay.fill((82,179,173))
    birdx=25
    birdy=displayh/2
    x=displayw+10
    vb=1
    y=0
    vt=5
    
    
    w=30
    h=random.randrange(displayh*0.25,displayh*0.75)    
    score=0
    crashed=False
    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                ext()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    birdy-=25
        gamedisplay.fill((82,179,173))
        scoredisplay(str(score))
        x=x-vt
        birdy=birdy+vb
        gamedisplay.fill((82,179,173))    
        pygame.draw.rect(gamedisplay,(200,0,0),(birdx,birdy,25,25))
        pygame.draw.rect(gamedisplay,(0,0,0),(x,y,w,h))
        pygame.draw.rect(gamedisplay,(0,0,0),(x,y+h+70,w,displayh-y-h-70))
        if birdy<y+h or birdy>y+h+50 :
            if (x<birdx and birdx<x+w) or (x<birdx+25 and birdx+25<x+w): 
                crashed=True
                message_display('U crashed')
        if birdy<0 or birdy+25>displayh:
            crashed=True
            message_display("U crashed")
        if x+w<0 :
            x=displayw
            h=random.randrange(displayh*0.25,displayh*0.75)
            score+=1
            
        pygame.display.update()
        clock.tick(30)
        
        

    
        
intro()
gameloop()
ext()
