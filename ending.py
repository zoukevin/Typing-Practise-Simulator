import pygame 
import math
from play import startTyping

def ending(black, grey, x, y, screen, totalNum, mistakes, wpm):
    quit = False
    wpm = math.floor(wpm)
    accuracy = math.floor((totalNum/(totalNum+mistakes)) * 100)

    #Message 1
    if (accuracy <= 50):
        message1 = "Good attempt!"
    elif (accuracy > 50 and accuracy < 76):
        message1 = "Great job!"
    else:
        message1 = "Excellent work!"

    #Message2
    if mistakes == 1:
        message2 = "You have typed a total of " + str(totalNum) + " characters with a total of " + str(mistakes) + " mistake"
    else:
        message2 = "You have typed a total of " + str(totalNum) + " characters with a total of " + str(mistakes) + " mistakes"

    message3 = " with a speed of " + str(wpm) + " words per minute. and an accuracy of " + str(accuracy) + "%."
    message4 = "Press R to retry or Q to quit"

    # Ending format and position
    titleFont = pygame.font.Font('freesansbold.ttf', 46) 
    titleMessage = titleFont.render(message1, True, black, grey)
    titleMessageRect = titleMessage.get_rect()  
    titleMessageRect.center = (x // 2, y // 2.5)

    font = pygame.font.Font('freesansbold.ttf', 26) 
    message = font.render(message2, True, black, grey)
    messageRect = message.get_rect()  
    messageRect.center = (x // 2, y // 2)

    messageNext = font.render(message3, True, black, grey)
    messageNextRect = messageNext.get_rect()  
    messageNextRect.center = (x // 2, 375)

    optionFont = pygame.font.Font('freesansbold.ttf', 26) 
    optionMessage = optionFont.render(message4, True, black, grey)
    optionRect = optionMessage.get_rect()  
    optionRect.center = (x // 2, 500)

    while quit == False:
        screen.fill(grey)
        screen.blit(titleMessage, titleMessageRect)
        screen.blit(message, messageRect)
        screen.blit(messageNext, messageNextRect)
        screen.blit(optionMessage, optionRect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("quitting")
                quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    screen.fill(grey)
                    return True
                if event.key == pygame.K_q:
                    quit = True
                    pygame.quit()