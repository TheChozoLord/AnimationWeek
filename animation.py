# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:18:58 2024

@author: owen.merrill
"""
import pygame
pygame.init()

def main():

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Mario!")

    bImage = pygame.image.load("white.jpg")
    bImage = pygame.transform.scale(bImage, (640, 480))
    background = bImage
    
    screen.blit(background, (0, 0))
    
    # marioRun = pygame.image.load(Mario.marioRun(frame))
    # marioRun = marioRun.convert_alpha()
    # marioRun = pygame.transform.scale(marioRun, (64, 96))
    # mario_x = 0
    # mario_y = 200
    
    mario = Mario()
    allSprites = pygame.sprite.Group(mario)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False


        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()


    pygame.quit()


class Mario(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    
        self.marioRun = []
        self.marioRun.append(pygame.image.load("MarioRun-1.png"))
        self.marioRun.append(pygame.image.load("MarioRun-2.png"))
        self.marioRun.append(pygame.image.load("MarioRun-3.png"))
        self.marioRun.append(pygame.image.load("MarioRun-4.png"))

        self.image = self.marioRun[0]
        self.rect = self.image.get_rect()
        self.frame = 0
        self.hold = 0
        self.rect.y = 290

    def update(self):
        self.rect.x += 5
        self.hold += 1
        if self.rect.x > 640:
            self.rect.x = 0
            
        if self.hold == 5:
            self.hold = 0
            self.frame += 1
            if self.frame > 3:
                self.frame = 0
            
        self.image = self.marioRun[self.frame]
        
            
        
            


if __name__ == "__main__":
    main()
    
