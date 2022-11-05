import time
import pygame
import random
import math
import PygameTWF
import PygameCTBF
from VariousLists import Challenge, bDescriptions, redGreen, Map, rangesList, extraInfoDesc, cDescriptions, bingoLineList, bingoCardChallengeNames
pygame.init()
check = False
yShift = 0
window = pygame.display.set_mode([800,800])
fontFace = pygame.font.SysFont("impact", 80)        
fontFace2 = pygame.font.SysFont("Playfair Display",50)
fontFace3 = pygame.font.SysFont("Tahoma",15)
fontFace4 = pygame.font.SysFont("Playfair Display", 30)
previousClick = False
cyanTimer = 0
gameGoBRRR = True
generateScreen = True
secondScreen = False
bingoCardScreen = False
xShift = 0
clock = pygame.time.Clock()
while gameGoBRRR:
    window.fill((119, 119, 119))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameGoBRRR = False
    window.fill((140,140,140))
    Click = pygame.mouse.get_pressed()

    # Generate Button
    if generateScreen == True:
        pygame.draw.rect(window, (230,20,20),(145,145,500,500))
        pygame.draw.rect(window, (0,0,0),(145,145,500,500),5)
        generateC = fontFace.render("Generate", True, (0,0,0))
        window.blit(generateC, (245,300))
        gChallenge = fontFace.render("Challenge", True, (0,0,0))
        window.blit(gChallenge, (231,400))

    # Determining if the user is on the second screen or not
    if pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 600 and pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 600 and secondScreen == False and previousClick == False and Click[0]:
        generateScreen = False
        secondScreen = True
        mapNumber = random.randint(0,8)
        challengeNumber = random.randint(0,13)

    #Second Screen
    if secondScreen:
        bingoCardScreen = False
       
        #Redo Button
        if pygame.mouse.get_pos()[0] >= 690 and pygame.mouse.get_pos()[0] <= 790 and pygame.mouse.get_pos()[1] >= 10 and pygame.mouse.get_pos()[1] <= 60 and previousClick == False and Click[0]:
            mapNumber = random.randint(0,8)
            challengeNumber = random.randint(0,13)
            cyanTimer = 3
            check = False
        if cyanTimer > 0:
            pygame.draw.rect(window, (50,50,50), (690,10,100,50))
            cyanTimer = cyanTimer - 1
        else:
            pygame.draw.rect(window, (80,80,80),(690,10,100,50))
        pygame.draw.rect(window, (30,30,30), (690,10,100,50),5)
        redo = fontFace2.render("redo",True, (0,0,0))
        window.blit(redo, (703,18))
        
        #Challenge Rule Boxes
        rectdraw2 = 8
        while rectdraw2 > 0:
            pygame.draw.rect(window, (30,30,30), (10,50 + rectdraw2 * 50,35,35),5)
            rectdraw2 = rectdraw2 - 1
        for index, amount in enumerate(bDescriptions):
            bDRender = fontFace2.render(amount,True,(0,0,0))
            window.blit(bDRender, (50,100 + index * 50))
        pygame.draw.line(window, (0,0,0),(0,90),(360,90),5)
        pygame.draw.line(window, (0,0,0),(0,494),(360,494),5)

        #Excluding challenges on certain maps  
        while check == False:
            if challengeNumber == 4 and mapNumber != 4 and mapNumber != 8:
                mapNumber = random.randint(0,8)
                challengeNumber = random.randint(0,13)
                continue
            if mapNumber == 3 and challengeNumber in [1,2,5,6,11]:
                mapNumber = random.randint(0,8)
                challengeNumber = random.randint(0,13)
                continue
            if mapNumber == 2 and challengeNumber in [5,6,11]:
                mapNumber = random.randint(0,8)
                challengeNumber = random.randint(0,13)
                continue
            if mapNumber == 8 and challengeNumber == 12:
                mapNumber = random.randint(0,8)
                challengeNumber = random.randint(0,13)
                continue
            check = True

        # Challenge Descriptions
        PygameTWF.renderTextWrap((cDescriptions[challengeNumber]), fontFace2, (0,0,0), 795, window, 0,503,50)

        #Red and Green Boxes 
        redgreen2 = (redGreen[challengeNumber]).split()
        for index, amount in enumerate(redgreen2):
            pygame.draw.rect(window, (amount), (15,105 + index * 50,25,25))

        # Displaying the Map and Challenge
        mapName = fontFace2.render(str(Map[mapNumber]), True, (0,0,0))
        challengeName = fontFace2.render(str(Challenge[challengeNumber]),True, (0,0,0))
        window.blit(mapName, (10,10))
        window.blit(challengeName, (10,50))

        #Fps Counter
        fPS = fontFace3.render(str(math.trunc(clock.get_fps())) + " fps", True, (0,0,0))
        window.blit(fPS, (755,780))
    
        # Extra info on hover
        if pygame.mouse.get_pos()[0] < 435 and pygame.mouse.get_pos()[1] > 105 and pygame.mouse.get_pos()[1] < 505:
            for index, amount in enumerate(rangesList):
                rangetuples = amount
                if rangetuples[0] <= pygame.mouse.get_pos()[1] < rangetuples[1]:
                    displayExtraInfo = index
            PygameCTBF.cursorTextBox((extraInfoDesc[displayExtraInfo]),fontFace3,(0,0,0),200,window,15,(190,190,190),(0,0,0),2)

        # Bingo Button
        pygame.draw.rect(window, (80,80,80), (665,75,125,50))
        pygame.draw.rect(window, (30,30,30), (665,75,125,50),5)
        bingoType = fontFace2.render("Bingo", True, (0,0,0))
        window.blit(bingoType,(677,82))
        if pygame.mouse.get_pos()[0] >= 665 and pygame.mouse.get_pos()[0] <= 790 and pygame.mouse.get_pos()[1] >= 75 and pygame.mouse.get_pos()[1] <= 125 and previousClick == False and Click[0]:
            secondScreen = False
            bingoCardScreen = True 

    if bingoCardScreen:
        #resizing the screen
        window = pygame.display.set_mode([750,810])
        window.fill((140,140,140))

        #Back Button
        pygame.draw.rect(window, (80,80,80), (645,5,100,50))
        pygame.draw.rect(window, (30,30,30), (645,5,100,50),5)
        bingoType = fontFace2.render("Back", True, (0,0,0))
        window.blit(bingoType,(652,13))
        if pygame.mouse.get_pos()[0] >= 645 and pygame.mouse.get_pos()[0] <= 745 and pygame.mouse.get_pos()[1] >= 10 and pygame.mouse.get_pos()[1] <= 60 and previousClick == False and Click[0]:
            secondScreen = True
            window = pygame.display.set_mode([800,800])

        #Bingo Card Lines
        for index, amount in enumerate(bingoLineList):
            bingoStartEndCoord = amount
            pygame.draw.line(window, (0,0,0), (bingoStartEndCoord[0],bingoStartEndCoord[1]),(bingoStartEndCoord[2],bingoStartEndCoord[3]),5)

        #Bingo Card Names
        for index, amount in enumerate(bingoCardChallengeNames):
            if index / 5 in [1,2,3,4]:
                yShift = yShift + 150
            if xShift > 600:
                xShift = 0
            PygameTWF.renderTextWrap(amount, fontFace4, (0,0,0), 150, window, 0 + xShift, 65 + yShift, 10)
            xShift = xShift + 150
        yShift = 0
        xShift = 0



    previousClick = Click[0]
    pygame.display.flip()
    clock.tick(30)
pygame.quit()