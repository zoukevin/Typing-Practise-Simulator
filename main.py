# Simple pygame program

# Simple pygame program
from randomSentence import getRandomSentence, getRandomWord

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

# String to type
stringToType = getRandomSentence()

# Split string to fit word wrap
string1 = ""
string2 = ""
string3 = ""
string4 = ""
string5 = ""
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

#string1 = lines[0]
#string2 = lines[1]
#string3 = lines[2]
#string4 = lines[3]
#string5 = lines[4]

# String format and position for split lines

#text1 = font.render(string1, True, black, grey) 
#text1Rect = text1.get_rect()  
#text1Rect.left = (125) 
#text1Rect.bottom = (175)

#text2 = font.render(string2, True, black, grey) 
#text2Rect = text2.get_rect()
#text2Rect.left = (125)   
#text2Rect.bottom = (225) 

#text3 = font.render(string3, True, black, grey) 
#text3Rect = text1.get_rect() 
#text3Rect.left = (125)   
#text3Rect.bottom = (275) 

#text4 = font.render(string4, True, black, grey) 
#text4Rect = text4.get_rect()
#text4Rect.left = (125)    
#text4Rect.bottom = (325) 

#text5 = font.render(string5, True, black, grey) 
#text5Rect = text1.get_rect()
#text5Rect.left = (125)    
#text5Rect.bottom = (375) 

#Character index
currentChar = 0

#--------------------------------------------------------------------------------------------------------------------------------------------


# Run until the user asks to quit
running = True
finished = False
while running:

    screen.fill(grey)
    
    if (finished == False): 
#--------------------------------------------------------------------------------------------------------------------------------------------
        screen.blit(title, titleRect)

        printText = ""
        textLeft = 125
        textBottom = 175   
        for x in range(len(lines)):
            printText = font.render(lines[x], True, black, grey)
            textRect = printText.get_rect()
            textRect.left = (textLeft)
            textRect.bottom = (textBottom)
            textBottom += 50
            screen.blit(printText, textRect)
 
        #screen.blit(text1, text1Rect)
        #screen.blit(text2, text2Rect)
        #screen.blit(text3, text3Rect)
        #screen.blit(text4, text4Rect)
        #screen.blit(text5, text5Rect) 
#--------------------------------------------------------------------------------------------------------------------------------------------
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                running = False
            if (finished == False):
                mods = pygame.key.get_mods()
                if (event.unicode == stringToType[currentChar]):
                    print("yes")
                    currentChar += 1
                    if (currentChar == len(stringToType)):
                        finished = True
                        print("done")
                else:
                    print("no")

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()