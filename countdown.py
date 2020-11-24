import pygame

def countdown(black, grey, x, y, screen):

    countdown = pygame.font.Font('freesansbold.ttf', 70) 
    countdown3 = countdown.render("3", True, black, grey)
    countdown3Rect = countdown3.get_rect()  
    countdown3Rect.center = (x // 2, y // 2)

    countdown2 = countdown.render("2", True, black, grey)
    countdown2Rect = countdown2.get_rect()  
    countdown2Rect.center = (x // 2, y // 2)

    countdown1 = countdown.render("1", True, black, grey)
    countdown1Rect = countdown1.get_rect()  
    countdown1Rect.center = (x // 2, y // 2) 

    screen.blit(countdown3, countdown3Rect)
    pygame.display.flip()
    pygame.time.wait(1000)

    screen.fill(grey)
    screen.blit(countdown2, countdown2Rect)
    pygame.display.flip()
    pygame.time.wait(1000)

    screen.fill(grey)
    screen.blit(countdown1, countdown1Rect)
    pygame.display.flip()
    pygame.time.wait(1000)
    screen.fill(grey)
