import random
import math
import pygame
import pygame_twf
import pygame_ctbf
from various_lists import (Challenge, bDescriptions, redGreen, Map, rangesList, extraInfoDesc,
                           cDescriptions, bingoLineList, bingoCardChallengeNames, bingoBoxClickX)
pygame.init()
CHECK = False
bingoCardChallengeNamesRandomized = []
xBoxList = []
excludedBingoNumbers = []
Y_SHIFT = 0
fontFace = pygame.font.SysFont("impact", 80)
fontFace2 = pygame.font.SysFont("Playfair Display", 50)
fontFace3 = pygame.font.SysFont("Tahoma", 15)
fontFace4 = pygame.font.SysFont("Playfair Display", 29)
window = pygame.display.set_mode([800, 800])
PREVIOUS_CLICK = False
CYAN_TIMER = 0
GAME_GO_BRRR = True
GENERATE_SCREEN = True
SECOND_SCREEN = False
BINGO_CARD_SCREEN = False
X_SHIFT = 0
clock = pygame.time.Clock()
while GAME_GO_BRRR:
    window.fill((119, 119, 119))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_GO_BRRR = False
    window.fill((140, 140, 140))
    Click = pygame.mouse.get_pressed()

    # Generate Button
    if GENERATE_SCREEN:
        pygame.draw.rect(window, (230, 20, 20), (145, 145, 500, 500))
        pygame.draw.rect(window, (0, 0, 0), (145, 145, 500, 500), 5)
        generateC = fontFace.render("Generate", True, (0, 0, 0))
        window.blit(generateC, (245, 300))
        gChallenge = fontFace.render("Challenge", True, (0, 0, 0))
        window.blit(gChallenge, (231, 400))

    # Determining if the user is on the second screen or not
    if (pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 600
        and pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 600
            and SECOND_SCREEN is False and PREVIOUS_CLICK is False and Click[0]):
        GENERATE_SCREEN = False
        SECOND_SCREEN = True
        mapNumber = random.randint(0, 8)
        challengeNumber = random.randint(0, 16)

    # Second Screen
    if SECOND_SCREEN:
        #window = pygame.display.set_mode([800,800])

        # Redo Button
        if (pygame.mouse.get_pos()[0] >= 690 and pygame.mouse.get_pos()[0] <= 790
            and pygame.mouse.get_pos()[1] >= 10 and pygame.mouse.get_pos()[1] <= 60
                and PREVIOUS_CLICK is False and Click[0]):
            mapNumber = random.randint(0, 8)
            challengeNumber = random.randint(0, 16)
            CYAN_TIMER = 3
            CHECK = False
        if CYAN_TIMER > 0:
            pygame.draw.rect(window, (50, 50, 50), (690, 10, 100, 50))
            CYAN_TIMER = CYAN_TIMER - 1
        else:
            pygame.draw.rect(window, (80, 80, 80), (690, 10, 100, 50))
        pygame.draw.rect(window, (30, 30, 30), (690, 10, 100, 50), 5)
        redo = fontFace2.render("redo", True, (0, 0, 0))
        window.blit(redo, (703, 18))

        # Challenge Rule Boxes
        RECT_DRAW_2 = 8
        while RECT_DRAW_2 > 0:
            pygame.draw.rect(window, (30, 30, 30),
                             (10, 50 + RECT_DRAW_2 * 50, 35, 35), 5)
            RECT_DRAW_2 = RECT_DRAW_2 - 1
        for index, amount in enumerate(bDescriptions):
            bDRender = fontFace2.render(amount, True, (0, 0, 0))
            window.blit(bDRender, (50, 100 + index * 50))
        pygame.draw.line(window, (0, 0, 0), (0, 90), (360, 90), 5)
        pygame.draw.line(window, (0, 0, 0), (0, 494), (360, 494), 5)

        # Excluding challenges on certain maps
        while CHECK is False:
            if challengeNumber == 4 and mapNumber != 4 and mapNumber != 8:
                mapNumber = random.randint(0, 8)
                challengeNumber = random.randint(0, 16)
                continue
            if mapNumber == 3 and challengeNumber in [1, 2, 5, 6, 11]:
                mapNumber = random.randint(0, 8)
                challengeNumber = random.randint(0, 16)
                continue
            if mapNumber == 2 and challengeNumber in [5, 6, 11]:
                mapNumber = random.randint(0, 8)
                challengeNumber = random.randint(0, 16)
                continue
            if mapNumber == 8 and challengeNumber == 12:
                mapNumber = random.randint(0, 8)
                challengeNumber = random.randint(0, 16)
                continue
            CHECK = True

        # Challenge Descriptions
        pygame_twf.render_text_wrap(
            (cDescriptions[challengeNumber]), fontFace2, (0, 0, 0), 795, window, 0, 503, 50)

        # Red and Green Boxes
        redgreen2 = (redGreen[challengeNumber]).split()
        for index, amount in enumerate(redgreen2):
            pygame.draw.rect(window, (amount), (15, 105 + index * 50, 25, 25))

        # Displaying the Map and Challenge
        mapName = fontFace2.render(str(Map[mapNumber]), True, (0, 0, 0))
        challengeName = fontFace2.render(
            str(Challenge[challengeNumber]), True, (0, 0, 0))
        window.blit(mapName, (10, 10))
        window.blit(challengeName, (10, 50))

        # Fps Counter
        fPS = fontFace3.render(
            str(math.trunc(clock.get_fps())) + " fps", True, (0, 0, 0))
        window.blit(fPS, (755, 780))

        # Extra info on hover
        if (pygame.mouse.get_pos()[0] < 435 and pygame.mouse.get_pos()[1] > 105
                and pygame.mouse.get_pos()[1] < 505):
            for index, amount in enumerate(rangesList):
                rangetuples = amount
                if rangetuples[0] <= pygame.mouse.get_pos()[1] < rangetuples[1]:
                    displayExtraInfo = index
            pygame_ctbf.cursor_text_box((extraInfoDesc[displayExtraInfo]), fontFace3, (0, 0, 0),
                                        200, window, 15, (190, 190, 190), (0, 0, 0), 2)

        # Bingo Button
        pygame.draw.rect(window, (80, 80, 80), (665, 65, 125, 50))
        pygame.draw.rect(window, (30, 30, 30), (665, 65, 125, 50), 5)
        bingoType = fontFace2.render("Bingo", True, (0, 0, 0))
        window.blit(bingoType, (677, 72))
        if (pygame.mouse.get_pos()[0] >= 665 and pygame.mouse.get_pos()[0] <= 790
            and pygame.mouse.get_pos()[1] >= 65 and pygame.mouse.get_pos()[1] <= 115
                and PREVIOUS_CLICK is False and Click[0]):
            BINGO_CARD_SCREEN = True
            BINGO_COUNT = 1
            bingoCardChallengeNamesRandomized = []
            excludedBingoNumbers = []
            SECOND_SCREEN = False
            X_WAIT_TIME = 10

    if BINGO_CARD_SCREEN:
        # Resizing the screen
        window = pygame.display.set_mode([750, 810])
        window.fill((140, 140, 140))

        # Bingo Card Lines
        for index, amount in enumerate(bingoLineList):
            bingoStartEndCoord = amount
            pygame.draw.line(window, (0, 0, 0), (bingoStartEndCoord[0], bingoStartEndCoord[1]), (
                bingoStartEndCoord[2], bingoStartEndCoord[3]), 5)

        # Reroll bingo Card Button
        pygame.draw.rect(window, (80, 80, 80), (540, 5, 100, 50))
        pygame.draw.rect(window, (30, 30, 30), (540, 5, 100, 50), 5)
        bingoRedo = fontFace2.render("Redo", True, (0, 0, 0))
        window.blit(bingoRedo, (547, 13))
        if (pygame.mouse.get_pos()[0] > 540 and pygame.mouse.get_pos()[0] < 640
            and pygame.mouse.get_pos()[1] > 13 and pygame.mouse.get_pos()[1] < 63
                and PREVIOUS_CLICK is False and Click[0]):
            BINGO_COUNT = 1
            bingoCardChallengeNamesRandomized = []
            excludedBingoNumbers = []
            xBoxList = []

        # Bingo Card Names
        while BINGO_COUNT != 0:
            bingoPicker = random.randint(0, 28)
            if bingoPicker in excludedBingoNumbers:
                continue
            excludedBingoNumbers.append(bingoPicker)
            bingoCardChallengeNamesRandomized.append(
                bingoCardChallengeNames[bingoPicker])
            bingoChallengeAmount = len(excludedBingoNumbers)
            if bingoChallengeAmount == 25:
                BINGO_COUNT = 0
        for index, amount in enumerate(bingoCardChallengeNamesRandomized):
            if index / 5 in [1, 2, 3, 4]:
                Y_SHIFT = Y_SHIFT + 150
            if X_SHIFT > 600:
                X_SHIFT = 0
            pygame_twf.render_text_wrap(
                amount, fontFace4, (0, 0, 0), 150, window, 0 + X_SHIFT, 65 + Y_SHIFT, 18)
            X_SHIFT = X_SHIFT + 150
        Y_SHIFT = 0
        X_SHIFT = 0

        # Back Button
        pygame.draw.rect(window, (80, 80, 80), (645, 5, 100, 50))
        pygame.draw.rect(window, (30, 30, 30), (645, 5, 100, 50), 5)
        bingoType = fontFace2.render("Back", True, (0, 0, 0))
        window.blit(bingoType, (652, 13))
        if (pygame.mouse.get_pos()[0] >= 645 and pygame.mouse.get_pos()[0] <= 745
            and pygame.mouse.get_pos()[1] >= 13 and pygame.mouse.get_pos()[1] <= 63
                and PREVIOUS_CLICK is False and Click[0]):
            SECOND_SCREEN = True
            window = pygame.display.set_mode([800, 800])
            xBoxList = []
            BINGO_CARD_SCREEN = False

        # X'ing out boxes when you click on them
        if X_WAIT_TIME == 0:
            for index, amount in enumerate(bingoBoxClickX):
                coordinateTuple = amount
                if (coordinateTuple[0] <= pygame.mouse.get_pos()[0] <=
                    coordinateTuple[1] and coordinateTuple[2] <=
                    pygame.mouse.get_pos()[1] <= coordinateTuple[3]
                        and PREVIOUS_CLICK is False and Click[0]):
                    xBoxList.append(coordinateTuple)
                for index, amount in enumerate(xBoxList):
                    coordinateTuple2 = amount
                    pygame.draw.line(window, (255, 0, 0),
                                     (coordinateTuple2[0], coordinateTuple2[2]), (
                        coordinateTuple2[1], coordinateTuple2[3]), 3)
                    pygame.draw.line(window, (255, 0, 0),
                                     (coordinateTuple2[1], coordinateTuple2[2]), (
                        coordinateTuple2[0], coordinateTuple2[3]), 3)
        if X_WAIT_TIME != 0:
            X_WAIT_TIME = X_WAIT_TIME - 1

        # Removing x's when you click on them
        for index, amount in enumerate(xBoxList):
            X_BOX_LIST_REPEATS = 0
            removingIndex = index
            checkingAmount = amount
            for index, amount in enumerate(xBoxList):
                if checkingAmount == amount:
                    X_BOX_LIST_REPEATS = X_BOX_LIST_REPEATS + 1
                if X_BOX_LIST_REPEATS > 1:
                    xBoxList.remove(amount)
                    xBoxList.remove(checkingAmount)

        # Displaying Challenge on top of bingo screen
        if challengeNumber > 13:
            window.blit(challengeName, (5, 10))
        else:
            customBingoChallenge = fontFace2.render(
                "Custom Bingo", True, (0, 0, 0))
            window.blit(customBingoChallenge, (5, 10))

        # Bingo FPS
        fPS = fontFace3.render(
            str(math.trunc(clock.get_fps())) + " fps", True, (0, 0, 0))
        window.blit(fPS, (705, 790))

    PREVIOUS_CLICK = Click[0]
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
