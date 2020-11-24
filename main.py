# Simple pygame program
from countdown import countdown
from welcome import welcome
from play import startTyping
from ending import ending

import pygame
import time

pygame.init()

x = 1000
y = 700
screen = pygame.display.set_mode([x, y])

white = (255, 255, 255) 
grey = (220, 220, 220)
black = (0, 0, 0)

titleFont = pygame.font.Font('freesansbold.ttf', 36) 
title = titleFont.render("Type the following:", True, black, grey)
titleRect = title.get_rect()  
titleRect.center = (x // 2, y // 8)

welcome(black, grey, x, y, screen)    
countdown(black, grey, x, y, screen)
check = True

while check:
    wpm, totalNum, mistakes = startTyping(screen)
    check = ending(black, grey, x, y, screen, totalNum, mistakes, wpm)