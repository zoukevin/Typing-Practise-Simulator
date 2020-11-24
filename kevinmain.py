# Simple pygame program

# Simple pygame program
from randomSentence import getRandomSentence, getRandomWord
from countdown import countdown

# Import and initialize the pygame library
import pygame
pygame.init()

#--------------------------------------------------------------------------------------------------------------------------------------------
# Set up the drawing window
x = 1000
y = 700
screen = pygame.display.set_mode([x, y])

# Colours
white = (255, 255, 255) 
grey = (220, 220, 220)
black = (0, 0, 0)

# Title format and position
titleFont = pygame.font.Font('freesansbold.ttf', 36) 
title = titleFont.render("Type the following:", True, black, grey)
titleRect = title.get_rect()  
titleRect.center = (x // 2, y // 8)

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

running = True

while (running == True):
    # String to type
    stringToType = ""
    for i in range(1):
        stringToType += getRandomSentence() + " "
    stringToType = stringToType.strip()


    # Split string to fit word wrap
    stringList = []

    # Font for the string of words
    font = pygame.font.Font('freesansbold.ttf', 26) 

    # first, split the text into words
    words = stringToType.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            # appends into the array depending on font width and font height until it reaches the allowed width
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > 800:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    #Character index
    currentChar = 0

    # Run until the user asks to quit
    ready = False
    finished = False
    completedLines = []
    completedCharacters = ""

    #Show welcome screen
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
    
    #Show countdown
    countdown(black, grey, x, y, screen)

    while not finished:
        if (finished == False): 
            # Title text
            screen.blit(title, titleRect)

            # Random sentences
            printText = ""
            textLeft = 125
            textBottom = 175   
            for x in lines:
                printText = font.render(x, True, black, grey)
                textRect = printText.get_rect()
                textRect.left = (textLeft)
                textRect.bottom = (textBottom)
                textBottom += 50
                screen.blit(printText, textRect)
            textBottom = 175

            x = completedCharacters
            printText = font.render(x, True, grey, black)
            textRect = printText.get_rect()
            textRect.left = (textLeft)
            textRect.bottom = (textBottom)
            textBottom += 50
            screen.blit(printText, textRect) 
        
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quitting")
                finished = True
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    running = False
                if (finished == False):
                    if (event.unicode == stringToType[currentChar]):
                        print("yes")
                        completedCharacters += stringToType[currentChar]
                        currentChar += 1
                        if (currentChar == len(stringToType)):
                            finished = True
                            currentChar = 0
                            completedCharacters = ""
                            completedLines.append(completedCharacters)
                            print("done")
                    else:
                        if not(event.key == pygame.K_LSHIFT or event.key == pygame.K_CAPSLOCK):
                            print("no")
                            

        # Flip the display
        pygame.display.flip()

# Done! Time to quit.
pygame.quit()