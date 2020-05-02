import pygame, sys
pygame.init()
screen = pygame.display.set_mode((430,410))
white = [255, 255, 255]
red = [255, 0, 0]
screen.fill(white)
pygame.display.update()
ball = pygame.draw.ellipse(screen, (255, 50, 50), (176, 134, 30, 30))
ball_dragging = False
ball_2 = pygame.draw.ellipse(screen, (255, 50, 50), (200, 134, 30, 30))
ball_3 = pygame.draw.ellipse(screen, (255, 50, 50), (100, 134, 30, 30))
ball_4 = pygame.draw.ellipse(screen, (255, 50, 50), (150, 134, 30, 30))
ball_5 = pygame.draw.ellipse(screen, (255, 50, 50), (250, 134, 30, 30))


pygame.display.update()

run = True
while run:  
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if ball.collidepoint(event.pos):
                    ball_dragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = ball.x - mouse_x
                    offset_y = ball.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                ball_dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if ball_dragging:
                mouse_x, mouse_y = event.pos
                ball.x = mouse_x + offset_x
                ball.y = mouse_y + offset_y


        
    screen.fill((255,255,255))
    pygame.draw.ellipse(screen, (255, 50, 50), ball)
    pygame.draw.ellipse(screen, (255, 50, 50), ball_2)
    pygame.draw.ellipse(screen, (255, 50, 50), ball_3)
    pygame.draw.ellipse(screen, (255, 50, 50), ball_4)
    pygame.draw.ellipse(screen, (255, 50, 50), ball_5)
    pygame.display.update()

pygame.quit()


