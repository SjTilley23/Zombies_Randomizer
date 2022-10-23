import time
import pygame
import random
import math
pygame.init()
check = False
window = pygame.display.set_mode([600,600])
Type = pygame.font.SysFont("impact", 80)        
Type2 = pygame.font.SysFont("Playfair Display",50)
Type3 = pygame.font.SysFont("Tahoma",15)
previousClick = False
cyanTimer = 0
run = True
secondScreen = False
Challenge = ["2 Box","No Jugg","Only Jugg","Melee Only","EE Speedrun","Pap all Weapons","321 Challenge","Spawn Room","Box Roulette","Explosives Only","Wall Weapons Only","No Pack-a-Punch","Olympia Only"]
Map = ["Town","Farm","Tranzit","Bus Depot","Mob","Buried","Die Rise","Nuketown","Origins"]
cDescriptions = [["Hit the box twice as fast as you can.", "You must use only those 2 weapons" ,"for the remainder of the game."],["You are not allowed to buy jugg."],["The only perk allowed is jugg."],["You cannot shoot.", "You must only knife."],["Complete the map's easter egg as", "fast as possible. Counted by round", "not by time."],["Pack-a-punch all weapons available", "on the map. Including the starting", "pistol."],["3 Perks, 2 Box hits, 1 Pack-a-Punch.", "You can replace a box hit with a wall", "weapon, but you cannot re-pack"],["You must not leave the spawn area.", "The spawn area includes anywhere", "you can get without spending" ,"points."],["Starting at Round 5 you must hit the", "box every round and use that", "weapon until it runs out of ammo", "or the round ends"],["Starting at round 8 you must only", "use weapons that cause Explosions", "Grenades count."],["You cannot hit the box for a weapon.", "You must buy it off a wall. Bowie", "knife and Galvaknuckles count."],["You are not allowed to Pack-a-Punch"],["The only weapon you can use is ","the olympia"]]
bDescriptions = ["Quick Revive/Afterlife","Starting Pistol","Melee/Knifing","Melee/Knife Upgrades","Hells Retriever (if applicable)"]
redGreen = [["darkred","green","green","darkred","darkred"],["darkred","green","green","green","green"],["darkred","green","green","darkred","green"],["darkred","darkred","green","green","darkred"],["green","green","green","green","green"],["darkred","green","green","green","green"],["darkred","green","green","darkred","darkred"],["darkred","green","green","darkred","darkred"],["darkred","green","green","darkred","darkred"],["darkred","darkred","green","darkred","darkred"],["darkred","darkred","darkred","green","darkred"],["darkred","green","green","darkred","darkred"],["darkred","darkred","green","darkred","darkred"]]
check = False
clock = pygame.time.Clock()
while run:
    window.fill((119, 119, 119))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill((140,140,140))
    Click = pygame.mouse.get_pressed()

    # Generate Button
    if secondScreen == False:
        pygame.draw.rect(window, (230,20,20),(100,100,400,400))
        pygame.draw.rect(window, (0,0,0),(100,100,400,400),5)
        generateC = Type.render("Generate", True, (0,0,0))
        window.blit(generateC, (150,200))
        gChallenge = Type.render("Challenge", True, (0,0,0))
        window.blit(gChallenge, (136,300))

    # Determining if the user is on the second screen or no
    if pygame.mouse.get_pos()[0] >= 100 and pygame.mouse.get_pos()[0] <= 500 and pygame.mouse.get_pos()[1] >= 100 and pygame.mouse.get_pos()[1] <= 500 and secondScreen == False and previousClick == False and Click[0]:
        secondScreen = True
        mapNumber = random.randint(0,8)
        challengeNumber = random.randint(0,12)

    #Second Screen
    if secondScreen == True:
       
        #Redo Button
        if pygame.mouse.get_pos()[0] >= 490 and pygame.mouse.get_pos()[0] <= 590 and pygame.mouse.get_pos()[1] >= 10 and pygame.mouse.get_pos()[1] <= 60 and previousClick == False and Click[0]:
            mapNumber = random.randint(0,8)
            challengeNumber = random.randint(0,12)
            cyanTimer = 3
            check = False
        if cyanTimer > 0:
            pygame.draw.rect(window, (50,50,50), (490,10,100,50))
            cyanTimer = cyanTimer - 1
        else:
            pygame.draw.rect(window, (80,80,80),(490,10,100,50))
        pygame.draw.rect(window, (30,30,30), (490,10,100,50),5)
        redo = Type2.render("redo",True, (0,0,0))
        window.blit(redo, (503,18))
        
        #Challenge Rule Boxes
        rectdraw2 = 5
        while rectdraw2 > 0:
            pygame.draw.rect(window, (30,30,30), (10,50 + rectdraw2 * 50,35,35),5)
            rectdraw2 = rectdraw2 - 1
        for index, amount in enumerate(bDescriptions):
            bDRender = Type2.render(amount,True,(0,0,0))
            window.blit(bDRender, (50,100 + index * 50))
        pygame.draw.line(window, (0,0,0),(0,90),(360,90),5)
        pygame.draw.line(window, (0,0,0),(0,344),(360,344),5)

        #Excluding challenges on certain maps  
        while check == False:
            if challengeNumber == 4 and mapNumber != 4 and mapNumber != 8:
                mapNumber = random.randint(0,8)
                challengeNumber = random.randint(0,12)
                continue
            if mapNumber == 3 and challengeNumber == 1 or challengeNumber == 2 or challengeNumber == 5 or challengeNumber == 6 or challengeNumber == 11:
                mapNumber = random.randint(0,8)
                challengeNumber = random.randint(0,12)
                continue
            if mapNumber == 2 and challengeNumber == 5 or challengeNumber == 6 or challengeNumber == 11:
                mapNumber = random.randint(0,8)
                challengeNumber = random.randint(0,12)
                continue
            if mapNumber == 8 and challengeNumber == 12:
                mapNumber = random.randint(0,8)
                challengeNumber = random.randint(0,12)
                continue
            check = True

        # Challenge Descriptions
        for index, amount in enumerate(cDescriptions[challengeNumber]):
            cDesc = Type2.render(str(amount), True, (0,0,0))
            window.blit(cDesc, (2,360 + index * 50))

        #Red and Green Boxes 
        for index, amount in enumerate((redGreen[challengeNumber])):     
            pygame.draw.rect(window, (amount), (15,105 + index * 50,25,25))
                   
        # Displaying the Map and Challenge
        mapName = Type2.render(str(Map[mapNumber]), True, (0,0,0))
        challengeName = Type2.render(str(Challenge[challengeNumber]),True, (0,0,0))
        window.blit(mapName, (10,10))
        window.blit(challengeName, (10,50))

        #Fps Counter
        fPS = Type3.render(str(math.trunc(clock.get_fps())) + " fps", True, (0,0,0))
        window.blit(fPS, (555,580))
    
    previousClick = Click[0]
    pygame.display.flip()
    clock.tick(30)
pygame.quit()