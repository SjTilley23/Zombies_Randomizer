"""
Various lists that the main file pulls from for challenges, maps, and other things
"""
Challenge = ["2 Box",
             "No Jugg",
             "Only Jugg",
             "Melee Only",
             "EE Speedrun",
             "Pap all Weapons",
             "321 Challenge",
             "No Open Doors",
             "Box Roulette",
             "Explosives Only",
             "Wall Weapons Only",
             "No Pack-a-Punch",
             "Olympia Only",
             "Spawn Room",
             "Double Bingo",
             "Bingo Blackout",
             "Bingo 4 Corners"]
Map = ["Town",
       "Farm",
       "Tranzit",
       "Bus Depot",
       "Mob",
       "Buried",
       "Die Rise",
       "Nuketown",
       "Origins"]
bDescriptions = ["Quick Revive/Afterlife",
                 "Starting Pistol",
                 "Melee/Knifing",
                 "Melee/Knife Upgrades",
                 "Hells Retriever",
                 "Equipment",
                 "Non-lethal Buildables",
                 "Lethal Buildables"]
rangesList = [(95, 145),
              (145, 195),
              (195, 245),
              (245, 295),
              (295, 345),
              (345, 395),
              (395, 445),
              (445, 495)]
redGreen = ["darkred green green darkred darkred green green darkred",
            "darkred green green green green green green green",
            "darkred green green darkred green green green green",
            "darkred darkred green green darkred darkred green darkred",
            "green green green green green green green green",
            "darkred green green green green green green green",
            "darkred green green darkred darkred green green darkred",
            "darkred green green darkred darkred green green green",
            "darkred green green darkred darkred green green darkred",
            "darkred darkred green darkred darkred green green green",
            "darkred darkred darkred green darkred green green darkred",
            "darkred green green darkred darkred green green darkred",
            "darkred darkred green darkred darkred green green darkred",
            "darkred green green darkred darkred green darkred darkred",
            "green green green green green green green green",
            "green green green green green green green green",
            "green green green green green green green green", ]
extraInfoDesc = ["Afterlife is fine if you kill yourself, but not if you die to zombies",
                 "You must eventually replace this gun in challenges that require"
                 "you to use specific guns and have this enabled",
                 "This refers to your starting knife",
                 "This includes, Glavaknuckles, Bowie Knife, Silver Spoon, and The Golden Spork",
                 "Only applicable on Mob of the Dead",
                 "Grenades, EMP's, Monkeys, Time Bombs, and Claymores are all equipment items",
                 "Zombie Shield and trample steam are fine, as long as you dont attack with them",
                 "This is any buildable designed to kill"]
cDescriptions = [
"Hit the box twice as fast as you can. You must use only those"
"2 weapons for the remainder of the game.",
"You are not allowed to buy Jugger-nog.",
"The only perk you are allowed to have is Jugger-nog.",
"You are not allowed to use guns, traps, or anything but your melee to kill zombies.",
"Complete the map's easter egg as fast as possible. Counted by round, not by time.",
"Pack-a-punch all weapons available on the map. Including the starting pistol.",
"3 Perks, 2 Box hits, 1 Pack-a-Punch. You can replace a"
"box hit with a wall weapon, but you cannot re-pack.",
"You cannot spend any points to open doors. Doors unlocked by other means are fine.",
"Starting at Round 5 you must hit the box every round and use that"
"weapon until it runs out of ammo or the round ends.",
"You must get an explosives weapon as fast as possible. After that you must only"
"use that and other explosives weapons for the remainder of the game. Grenades count.",
"You cannot hit the box for a weapon. You must buy it off a wall."
"Bowie knife and Galvaknuckles count.",
"You are not allowed to use the Pack-a-Punch machine.",
"The only weapon you can use is the olympia. Pack-a-Punch'ing is fine.",
"You cannot leave the spawn area. The spawn area is anywhere you can get without"
"triggering an event, like opening doors, falling down pits, etc.",
"You need to get 2 bingos on the bingo sheet",
"You need to get the 4 corners done on the bingo sheet",
"you need to get every challenge done on the bingo sheet"]
bingoLineList = [(0, 60, 800, 60),
                 (0, 210, 800, 210),
                 (0, 360, 800, 360),
                 (0, 510, 800, 510),
                 (0, 660, 800, 660),
                 (0, 810, 800, 810),
                 (150, 60, 150, 810),
                 (300, 60, 300, 810),
                 (450, 60, 450, 810),
                 (600, 60, 600, 810)]
bingoCardChallengeNames = ["Mk2 Raygun",
                           "200 Headshots",
                           "Round 20",
                           "Round 25",
                           "500 Kills",
                           "Bought all wall guns",
                           "No Downs",
                           "Free Space",
                           "Pap'd 4 Guns",
                           "30 kills with Starting Pistol, no pap",
                           "4 Perks",
                           "25 Melee Kills",
                           "pap starting pistol",
                           "50 box hits",
                           "Open all doors",
                           "60k points at once",
                           "300 headshots",
                           "1000 kills",
                           "Bowie Knife",
                           "Galvaknuckles",
                           "3 box Teddys",
                           "Monkey Bombs",
                           "1 round in each room",
                           "No drops",
                           "Dont move for 1 round on any round past 10",
                           "Pistols only",
                           "spawn room until round 5",
                           "Hip Fire only",
                           "Crouch for 3 whole rounds past round 10"]
bingoBoxClickX = [(0, 150, 60, 210),
                  (0, 150, 211, 360),
                  (0, 150, 361, 510),
                  (0, 150, 511, 660),
                  (0, 150, 661, 810),
                  (151, 300, 60, 210),
                  (151, 300, 211, 360),
                  (151, 300, 361, 510),
                  (151, 300, 511, 660),
                  (151, 300, 661, 810),
                  (301, 450, 60, 210),
                  (301, 450, 211, 360),
                  (301, 450, 361, 510),
                  (301, 450, 511, 660),
                  (301, 450, 661, 810),
                  (451, 600, 60, 210),
                  (451, 600, 211, 360),
                  (451, 600, 361, 510),
                  (451, 600, 511, 660),
                  (451, 600, 661, 810),
                  (601, 750, 60, 210),
                  (601, 750, 211, 360),
                  (601, 750, 361, 510),
                  (601, 750, 511, 660),
                  (601, 750, 661, 810), ]
