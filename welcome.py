import pygame 

def welcome(black, grey, x, y, screen):
    ready = False
    # Welcome format and position
    welcomeFont = pygame.font.Font('freesansbold.ttf', 46) 
    welcome = welcomeFont.render("Welcome to typing simulator", True, black, grey)
    welcomeRect = welcome.get_rect()  
    welcomeRect.center = (x // 2, y // 2.5)

    # Welcome message
    messageFont = pygame.font.Font('freesansbold.ttf', 32) 
    wMessage = messageFont.render("Press the spacebar key to begin", True, black, grey)
    wMessageRect = wMessage.get_rect()  
    wMessageRect.center = (x // 2, y // 2)  
    screen.fill(grey)
    screen.blit(welcome, welcomeRect)
    screen.blit(wMessage, wMessageRect)
    pygame.display.flip()

    while ready == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quitting")
                pygame.display.flip()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ready = True
    screen.fill(grey)                
    pygame.display.flip()