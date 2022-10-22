import enum
import pygame
import random
pygame.init()
window = pygame.display.set_mode([600,600])
Type = pygame.font.SysFont("impact", 80)
Type2 = pygame.font.SysFont("Playfair Display",50)
previousClick = False
run = True
secondScreen = False
Challenge = ["2 Box","No Jugg","Only Jugg","Melee Only","EE Speedrun","Pap all Guns","321 Challenge","Spawn Room","Box Roulette","Explosives Only","Wall Weapons Only","No Pack-a-Punch","Olympia Only"]
Map = ["Town","Farm","Tranzit","Bus Depot","Mob","Buried","Die Rise","Nuketown","Origins"]
cDescriptions = ["unos","dos","tres","quatro","cinco","seis","siete","ocho","nueve","diez","once","doce","trece"]
bDescriptions = ["Quick Revive/Afterlife","Starting Pistol","Melee/Knifing","Melee/Knife Upgrades","Hells Retriever"]
redGreen = [["darkred","green","green","darkred","darkred"],["darkred","green","green","green","green"],["darkred","green","green","darkred","green"],["darkred","darkred","green","green","darkred"],["green","green","green","green","green"],["darkred","green","green","green","green"],["darkred","green","green","darkred","darkred"],["darkred","green","green","darkred","darkred"],["darkred","green","green","darkred","darkred"],["darkred","darkred","green","darkred","darkred"],["darkred","darkred","darkred","green","darkred"],["darkred","green","green","darkred","darkred"],["darkred","darkred","green","darkred","darkred"]]
check = False
while run:
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
        pygame.draw.rect(window, (80,80,80),(490,10,100,50))
        pygame.draw.rect(window, (30,30,30), (490,10,100,50),5)
        redo = Type2.render("redo",True, (0,0,0))
        window.blit(redo, (503,18))
        if pygame.mouse.get_pos()[0] >= 490 and pygame.mouse.get_pos()[0] <= 590 and pygame.mouse.get_pos()[1] >= 10 and pygame.mouse.get_pos()[1] <= 60 and previousClick == False and Click[0]:
            mapNumber = random.randint(0,8)
            challengeNumber = random.randint(0,12)
        
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
        if challengeNumber == 4 and mapNumber != 4 and mapNumber != 8:
            continue
        if mapNumber == 3 and challengeNumber == 1 or challengeNumber == 2 or challengeNumber == 5 or challengeNumber == 6 or challengeNumber == 11:
            continue
        if mapNumber == 2 and challengeNumber == 5 or challengeNumber == 6 or challengeNumber == 11:
            continue
        if mapNumber == 8 and challengeNumber == 12:
            continue

        # Challenge Descriptions
        dChallenge = Type2.render((cDescriptions[challengeNumber]), True, (0,0,0))
        window.blit(dChallenge, (10,350))

        #Red and Green Boxes 
        for index, amount in enumerate((redGreen[challengeNumber])):     
            pygame.draw.rect(window, (amount), (15,105 + index * 50,25,25))
            
            
        # Displaying the Map and Challenge
        mapName = Type2.render(str(Map[mapNumber]), True, (0,0,0))
        challengeName = Type2.render(str(Challenge[challengeNumber]),True, (0,0,0))
        window.blit(mapName, (10,10))
        window.blit(challengeName, (10,50))


            
    
    
    
    
    
    previousClick = Click[0]
    pygame.display.flip()
pygame.quit()