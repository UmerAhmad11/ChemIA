import pygame, sys
pygame.init()
screen = pygame.display.set_mode([800,600])
white = [255, 255, 255]
red = [255, 0, 0]
screen.fill(white)
pygame.display.update()


run = True
while run:
    pygame.time.delay(100)
  
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        
    


