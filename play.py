from randomSentence import getRandomSentence, getRandomWord
import pygame
import time

def startTyping(screen):

    x = 1000
    y = 700

    white = (255, 255, 255) 
    grey = (220, 220, 220)
    black = (0, 0, 0)

    titleFont = pygame.font.Font('freesansbold.ttf', 36) 
    title = titleFont.render("Type the following:", True, black, grey)
    titleRect = title.get_rect()  
    titleRect.center = (x // 2, y // 8)

    NUMSENTENCES = 3
    stringToType = ""
    for i in range(NUMSENTENCES):
        stringToType += getRandomSentence() + " "
    stringToType = stringToType.strip()


    font = pygame.font.Font('freesansbold.ttf', 26)
    words = stringToType.split()

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

    currentChar = 0
    finished = False
    completedCharacters = ""
    currentLine = 0
    start = time.time()

    #Begin typing loop
    while not finished:
        
        if (finished == False): 
            # Title text
            screen.blit(title, titleRect)

            # Random sentences
            printText = ""
            textLeft = 125
            textBottom = 175   
            for x in range(len(lines)):
                if (x < currentLine):
                    printText = font.render(lines[x], True, grey, black)
                else:
                    printText = font.render(lines[x], True, black, grey)
                textRect = printText.get_rect()
                textRect.left = (textLeft)
                textRect.bottom = (textBottom)
                textBottom += 50
                screen.blit(printText, textRect)
            textBottom = 175 + currentLine*50
            printText = font.render(completedCharacters, True, grey, black)
            textRect = printText.get_rect()
            textRect.left = (textLeft)
            textRect.bottom = (textBottom)
            screen.blit(printText, textRect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quitting")
                finished = True
            if event.type == pygame.KEYDOWN:
                if (finished == False):
                    if (event.unicode == stringToType[currentChar]):
                        print("yes")
                        completedCharacters += stringToType[currentChar]
                        if (completedCharacters == " "):
                            completedCharacters = ""
                        currentChar += 1
                        if (completedCharacters == lines[currentLine]):
                            completedCharacters = ""
                            currentLine += 1
                            print("going to next line")
                        if (currentChar == len(stringToType)):
                            finished = True
                            currentChar = 0
                            finish = time.time()
                            print("Finished.")
                            secondsToFinish = finish - start
                            print("Took " + str(secondsToFinish) + " seconds to complete.\n")
                            print("WPM: ", 6*NUMSENTENCES/(secondsToFinish/60))
                            break
                        print(lines[currentLine])
                        print(completedCharacters)
                    else:
                        if not(event.key == pygame.K_LSHIFT or event.key == pygame.K_CAPSLOCK):
                            print("no")
        # Flip the display
        pygame.display.flip()