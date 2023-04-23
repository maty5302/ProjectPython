import pygame
import copy
from collisions import Collision

class Blocks:

    def __init__(self, screen, x, y,random):
        self.screen = screen
        self.x = x
        self.y = y
        self.degrees = 0
        self.width = 39
        self.height = 39
        self.color = (0,0,0)
        self.random = random
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect2 = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect3 = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect4 = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rects = [self.rect, self.rect2, self.rect3, self.rect4]
        self.make_shape()

    def move(self, x, y):
        self.rect.x += x 
        self.rect.y += y 
        self.rect2.x += x
        self.rect2.y += y
        self.rect3.x += x
        self.rect3.y += y
        self.rect4.x += x
        self.rect4.y += y  

    def draw(self):
        for rect in self.rects:
            pygame.draw.rect(self.screen, self.color, rect)

    def make_shape(self):
        #I block
        if self.random == 7:
            self.rect2.x = self.x + 40
            self.rect3.x = self.x + 80
            self.rect4.x = self.x + 120
            self.color = (255,0,0)
        elif self.random == 1: #L block
            self.rect2.x= self.x + 40
            self.rect3.x = self.x + 80
            self.rect4.y = self.y + 40
            self.color = (255,255,0)
        elif self.random == 2: #Z block
            self.rect2.x = self.x + 40
            self.rect3.x = self.x + 40
            self.rect3.y = self.y + 40
            self.rect4.x = self.x + 80
            self.rect4.y = self.y + 40
            self.color = (0,255,0)
        elif self.random == 3: #T block
            self.rect2.x = self.x + 40
            self.rect3.x = self.x + 80
            self.rect4.x = self.x + 40
            self.rect4.y = self.y + 40 
            self.color = (0,0,255)
        elif self.random == 4: #S block
            self.rect.y = self.y + 40
            self.rect2.x = self.x + 40
            self.rect2.y = self.y + 40
            self.rect3.x = self.x + 40
            self.rect4.x = self.x + 80
            self.color = (0,255,255)
        elif self.random == 5: #ctverec lol
            self.rect2.x = self.x + 40
            self.rect3.y = self.y + 40
            self.rect4.x = self.x + 40
            self.rect4.y = self.y + 40
            self.color = (255,0,255)
        elif self.random == 6: #J block
            self.rect2.x = self.x + 40
            self.rect3.x = self.x + 80
            self.rect4.x = self.x + 80
            self.rect4.y = self.y + 40
            self.color = (100,0,0)


    def rotate(self,blocks,width,height):
        temp = copy.deepcopy(self.rects)
        self.degrees += 90
        if self.degrees == 360:
                self.degrees = 0
        if self.random == 7:                
            if self.degrees == 90 or self.degrees == 270:
                self.rect.x += 40
                self.rect.y -= 40
                self.rect3.x -= 40
                self.rect3.y += 40
                self.rect4.x -= 80
                self.rect4.y += 80
            else:
                self.rect.x -= 40
                self.rect.y += 40
                self.rect3.x += 40
                self.rect3.y -= 40
                self.rect4.x += 80
                self.rect4.y -= 80
        elif self.random == 1:
            if self.degrees == 90:
                self.rect.x += 40
                self.rect.y -= 40
                self.rect3.x -= 40
                self.rect3.y += 40
                self.rect4.y -= 80
            elif self.degrees == 180:
                self.rect.x += 40
                self.rect.y += 40
                self.rect3.x -= 40
                self.rect3.y -= 40
                self.rect4.x += 80
            elif self.degrees == 270:
                self.rect.x -= 40
                self.rect.y += 40
                self.rect3.x += 40
                self.rect3.y -= 40
                self.rect4.y += 80
            else:
                self.rect.x -= 40
                self.rect.y -= 40
                self.rect3.x += 40
                self.rect3.y += 40
                self.rect4.x -= 80
                self.degrees=0
        elif self.random == 2:
            if self.degrees ==90 or self.degrees == 270:
                self.rect.x += 40
                self.rect.y -= 40
                self.rect3.x -= 40
                self.rect3.y -= 40
                self.rect4.x -= 80
            else:
                self.rect.x -= 40
                self.rect.y += 40
                self.rect3.x += 40
                self.rect3.y += 40
                self.rect4.x += 80
        elif self.random == 3:
            if self.degrees == 90:
                self.rect.x += 40
                self.rect.y -= 40
                self.rect3.x -= 40
                self.rect3.y += 40
                self.rect4.x -= 40
                self.rect4.y -= 40
            elif self.degrees == 180:
                self.rect.x += 40
                self.rect.y += 40
                self.rect3.x -= 40
                self.rect3.y -= 40
                self.rect4.x += 40
                self.rect4.y -= 40
            elif self.degrees == 270:
                self.rect.x -= 40
                self.rect.y += 40
                self.rect3.x += 40
                self.rect3.y -= 40
                self.rect4.x += 40
                self.rect4.y += 40
            else:
                self.rect.x -= 40
                self.rect.y -= 40
                self.rect3.x += 40
                self.rect3.y += 40
                self.rect4.x -= 40
                self.rect4.y += 40
        elif self.random == 4:
            if self.degrees == 90 or self.degrees == 270:
                self.rect.x += 40
                self.rect.y -= 40
                self.rect3.x += 40
                self.rect3.y += 40
                self.rect4.y += 80
            else:
                self.rect.x -= 40
                self.rect.y += 40
                self.rect3.x -= 40
                self.rect3.y -= 40
                self.rect4.y -= 80
        elif self.random == 5:
            #there is nothing to do heree
            pass
        elif self.random == 6:
            if self.degrees == 90:
                self.rect.x += 40
                self.rect.y -= 40
                self.rect3.x -= 40
                self.rect3.y += 40
                self.rect4.x -= 80
            elif self.degrees ==180:
                self.rect.x += 40
                self.rect.y += 40
                self.rect3.x -= 40
                self.rect3.y -= 40
                self.rect4.y -= 80
            elif self.degrees == 270:
                self.rect.x -= 40
                self.rect.y += 40
                self.rect3.x += 40
                self.rect3.y -= 40
                self.rect4.x += 80
            else:
                self.rect.x -= 40
                self.rect.y -= 40
                self.rect3.x += 40
                self.rect3.y += 40
                self.rect4.y += 80
                


        if Collision.checkCollisionRotate(blocks,self,width,height):
            self.rect.x = temp[0].x
            self.rect.y = temp[0].y
            self.rect2.x = temp[1].x
            self.rect2.y = temp[1].y
            self.rect3.x = temp[2].x
            self.rect3.y = temp[2].y
            self.rect4.x = temp[3].x
            self.rect4.y = temp[3].y
            self.degrees -= 90
            if self.degrees == -90:
                self.degrees = 270

        



        