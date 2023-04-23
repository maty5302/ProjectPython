import pygame
import random
from blocks import Blocks
from collisions import Collision

class Tetris:
    def checkCollision(self) -> bool:
        return Collision.checkCollisionsDown(self.blocks, self.counter-1, self.width,self.height)

    def checkemptyBlocks(self):
        for i in self.blocks:
            if i.rects == []:
                self.blocks.remove(i) 
                self.counter-=1 

    def checkRows(self):
        width = self.width/2*1.5
        width = int(width)
        for i in range(self.height-39, -39, -40):
            counter = 0
            for j in range(1, width, 40):
                for k in self.blocks:
                    if k == self.blocks[self.counter-1]:
                        continue
                    for l in k.rects:
                        if l.x == j and l.y == i:
                            counter += 1
                            continue
            if counter == width/40:
                self.points += counter

                toremove = []
                for k in self.blocks:
                    for l in k.rects:
                        if l.y == i:
                            toremove.append(l)
                
                self.rowDeleteAnimation(toremove,i)

    
    def rowDeleteAnimation(self, toremove,i):
        for k in self.blocks:
            for l in toremove:
                if l in k.rects:
                    k.rects.remove(l)
                    self.refresh()
                    pygame.time.delay(10)

        for k in self.blocks:
            for l in k.rects:
                if l.y < i:
                    l.y += 40

    def GameOverAnimation(self):
        for i in range(self.height, -40, -40):
            for j in range(1, 600, 40):
                pygame.draw.rect(self.screen, (255,255,255), (j,i,40,40))
                pygame.display.flip()
                pygame.time.delay(10)
        font = pygame.font.SysFont("Arial", 12)
        gameovertext = self.font.render("GAME OVER", True, (255,0,0))
        gameoverinstrtext = font.render("To restart press R", True, (0,0,0))
        
        self.screen.blit(gameovertext, (250, 300))
        self.screen.blit(gameoverinstrtext, (255, 330))
        pygame.display.flip()

    def checkGameOver(self):
        self.refresh()
        for i in self.blocks:
            if i.rects == []:
                continue
            for j in i.rects:
                if j.y == 1:
                    self.running = False
                    self.GameOverAnimation()
                    self.checkHighscore()
                    return True
        return False
    
    def checkHighscore(self):
        if self.points > self.highscore:
            self.highscore = self.points
            with open("highscore.txt", "w") as f:
                f.write(str(self.highscore))
                f.close()

    def tobottom(self):
        while not self.checkCollision():
            self.blocks[self.counter-1].move(0,40)
            self.refresh()

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_LEFT:
                    ret = Collision.checkCollisionsLeft(self.blocks, self.counter-1)
                    if not ret:           
                        self.blocks[self.counter-1].move(-40,0)
                        self.refresh()
                elif event.key == pygame.K_RIGHT:
                    ret = Collision.checkCollisionsRight(self.blocks, self.counter-1)
                    if not ret:
                        self.blocks[self.counter-1].move(40,0)
                        self.refresh()
                elif event.key == pygame.K_DOWN:
                    ret = self.checkCollision()
                    if not ret:
                        self.blocks[self.counter-1].move(0,40)
                        self.refresh()
                elif event.key == pygame.K_UP:
                    self.blocks[self.counter-1].rotate(self.blocks,self.width,self.height)
                    pass
                elif event.key == pygame.K_SPACE:
                    self.tobottom()
                elif event.key == pygame.K_p: 
                    if self.speed < 0.3:                   
                        self.speed+=0.01
                elif event.key == pygame.K_m:
                    if self.speed > 0.05:
                        self.speed-=0.01
                elif event.key == pygame.K_r:
                    self.restart()

    def restart(self):
        self.points = 0
        self.counter = 0
        self.blocks = []
        self.running = True
        self.random = random.randint(0,6)
        self.refresh()                
    

    def refresh(self):
            self.screen.fill(self.background)
            pygame.draw.line(self.screen, (255,255,255), (600,0), (600,800), 5)
            self.pointstext = self.font.render("Score: " + str(self.points), True, (255,255,255))
            self.nexttext = self.font.render("Next:", True, (255,255,255))
            self.speedtext = self.font.render("Speed: " + str(round(self.speed*20,2)), True, (255,255,255))
            highscoretext = self.font.render("Highest score: " + str(self.highscore), True, (255,255,255))
            self.screen.blit(highscoretext, (625, 100))
            self.nextBlock = Blocks(self.screen, 625, 300, self.random)
            self.nextBlock.draw()
            self.screen.blit(self.nexttext, (650, 250))
            self.screen.blit(self.pointstext, (650, 150))
            self.screen.blit(self.speedtext, (650, 550))
            self.playground()
            if not self.blocks == []:
                for i in self.blocks:
                    i.draw()
            pygame.display.flip()    
    def playground(self):
        width = self.width/2*1.5
        width = int(width)
        for i in range(0, width, 40):
            pygame.draw.line(self.screen, (255,255,255), (i,0), (i,800), 1)
        for i in range(0, self.height, 40):
            pygame.draw.line(self.screen, (255,255,255), (0,i), (width,i), 1)
            
    def __init__(self):
        self.highscore = 0
        self.points = 0 
        self.speed = 0.05
        self.counter = 0
        self.random = 0
        self.blocks = []
        self.width = 800
        self.height = 800
        self.background = (0,0,0)
        self.clock = pygame.time.Clock()
        self.delta = self.clock.tick(60)/1000.0
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.font = pygame.font.SysFont("Arial", 20)
        try:
            f = open("highscore.txt", "r")
            score = f.readline()
            self.highscore = int(score)
        except:
            self.highscore = 0
        self.refresh() 
    
    def main_loop(self):
        
        self.running = True
        self.random = random.randint(1,7) 
        while self.running:
            self.clock.tick(self.speed/self.delta)   
            self.handle_keys() 
            self.checkRows()
            self.checkemptyBlocks()           
            if self.checkGameOver():
                loop = True
                while loop:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False
                            return
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                self.running = False
                                return
                            elif event.key == pygame.K_r:
                                self.restart()
                                loop = False

            if(self.checkCollision()==True or self.counter == 0):
                if self.counter != 0:
                    self.points += 1            
                self.randompos = random.randint(0,11)*40+1
                self.blocks.append(Blocks(self.screen, self.randompos, 1, self.random))
                self.random = random.randint(1,7)                
                self.counter += 1
            
            #print(self.blocks[self.counter-1].rects[0].x, self.blocks[self.counter-1].rects[0].y)   

            ret = self.checkCollision()
            if not ret:
                self.blocks[self.counter-1].move(0,40)
                self.refresh()
    
    def firstPage(self):
        self.screen.fill(self.background)
        self.font = pygame.font.SysFont("Arial", 40)
        self.text = self.font.render("Tetris", True, (255,255,255))
        self.screen.blit(self.text, (320, 200))
        self.font = pygame.font.SysFont("Arial", 20)
        self.text = self.font.render("Press any key to start", True, (255,255,255))
        self.screen.blit(self.text, (280, 300))
        block = Blocks(self.screen, 50, 50, 1)
        block.draw()
        block = Blocks(self.screen, 550, 50, 4)
        block.draw()
        pygame.display.flip()
        loop = True
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return
                    else:
                        loop = False
                        self.main_loop()
            
             

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Tetris - by PRU0059")
    tetris = Tetris()
    tetris.firstPage()
    pygame.quit()