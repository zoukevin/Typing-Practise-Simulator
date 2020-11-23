# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)

font = pygame.font.Font('freesansbold.ttf', 32)
stringToType = 'Hello'
text = font.render("Type the following: " + stringToType, True, green, blue) 
textRect = text.get_rect()  
textRect.center = (500 // 2, 500 // 2) 
currentChar = 0

# Run until the user asks to quit
running = True
finished = False
while running:

    screen.fill((255, 255, 255)) # (255, 255, 255) RGB value for WHITEfd
    if (finished == False):
        screen.blit(text, textRect) 
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                running = False
            if (finished == False):
                mods = pygame.key.get_mods()
<<<<<<< HEAD
                
                keyPressed = (pygame.key.name(event.key))
                if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                    keyPressed = keyPressed.upper()
                if (keyPressed == stringToType[currentChar]):
=======

            if (pygame.key.name(event.key) == stringToType[currentChar] or (mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS)):
                if ((pygame.key.name(event.key)).upper() == stringToType[currentChar] or pygame.key.name(event.key) == stringToType[currentChar]):
>>>>>>> 2e46be780cd34b136ca8a3faaacdfa4611009978
                    print("yes")
                    currentChar += 1
                    if (currentChar == len(stringToType)):
                        finished = True
                        print("done")
                else:
                    print("no")
<<<<<<< HEAD


  
=======
                
            
>>>>>>> 2e46be780cd34b136ca8a3faaacdfa4611009978

    # Fill the background with white
    #screen.fill((255, 255, 255))



    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()