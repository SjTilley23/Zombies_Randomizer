import random
Challenge = ["2 Box","No Jugg","Only Jugg","Melee Only","EE Speedrun","Pap all Guns","321 Challenge","Spawn Room","Box Roulette","Wall Weapons Only","No Pack-a-Punch","Olympia Only","Explosives Only"]
Map = ["Town","Farm","Tranzit","Bus Depot","Mob","Buried","Die Rise"]
x = 0
while x == 0:
    Request = input("Enter a Command: ")
    if Request == "Challenge":
       
       # Challenge Info
        while x == 0:
            MapNumber = random.randint(0,6)
            ChallengeNumber = random.randint(0,12)
            if MapNumber != 4:
                if ChallengeNumber == 4:
                    continue
                if MapNumber == 1:
                    if ChallengeNumber in (5,6,10):
                        continue
                    break
                if MapNumber == 3:
                    if ChallengeNumber in (1,2,5,6,10):
                        continue
                    break
                break
            break
        print((Map[MapNumber]),",",(Challenge[ChallengeNumber]))
        continue  

   # Rules of Challenges
    if Request == "Rules":
        print("No Quick Revive. Knives are allowed in all challenges. Hell's Retriever and Knife upgrades are not allowed unless specified")
        continue
    if Request == "321" or Request == "321 Challenge":
        print("3 Perks 2 Box Hits 1 PAP")
    if Request == "Box Roulette":
        print("after round 5 you must hit the box and use that gun for the entire round, or until it runs out of ammo")
        continue
    if Request == "2 Box":
        print("You have to hit the box twice and use those weapons for the remainder of the game. Wall weapons are not allowed.")
    if Request == "Help" or Request == "help":
        print("\nChallenge - Request a Challenge \nRules - General Overview of Rules \n[Challenge Name] - Overview of the Challenge \nEnd - Stop the Program\n")
    if Request == "End":
        break