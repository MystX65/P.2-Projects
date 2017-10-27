def intro():
    print("You wake up on the side of the beach covered in wet sand with cuts and bruises all over your body."
          "\nYou slowly stand up withstanding the pain from the wounds on your body."
          "\nYou can't recall anything"
          "\nThe light hits your face making you squint."
          "\nFinally, you see a woman dressed in a beautiful white flowy dress standing behind a palm tree staring at you")
    woman()
def introBroken():
    print("You wake up on the side of the beach covered in wet sand with cuts and bruises all over your body."
          "\nYou slowly stand up withstanding the pain from the wounds on your body."
          "\nYou suddenly felt a sharp pain in your right arm"
          "\nYou have no memory of anything that happened"
          "\nThe light hits your face making you squint."
          "\nFinally, you see...")
    print("\n1. a woman dressed in a beautiful white flowy dress standing behind a palm tree staring at you"
          "\n2. a man in a soldier's uniform staring right at you with a gun held in his hand")
    n=1
    while n == 1:
        choice = int(input())
        if choice == 1:
            woman()
            n=0
        if choice == 2:
            man()
            n=0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def introBasic():
    print("\nAt the tree, you see a man in a soldier's uniform staring right at you with a gun held in his hand.")
    man()
def introWithWoman():
    print("At the tree, you see a man in a soldier's uniform staring right at you with a gun held in his hand.")
    manwithGirl()

def manwithGirl():
    print("Seeing the woman that you are carrying, the man immediately aims his"
          " gun at your head ordering you to drop the woman."
          "You..."
          "\n1. lower the woman down to the ground gently"
          "\n2. drop her on the ground like the man ordered"
          "\n3. hold her as a shield and run away"
          "\n4. use her as hostage and force the man to drop his guns and walk away")
    n= 1
    while n==1:
        choice = int(input())
        if choice == 1:
            manwithGirl1()
            n = 0
        if choice == 2:
            manwithGirl2()
            n = 0
        if choice == 3:
            manwithGirl3()
            n = 0
        if choice == 4:
            manwithGirl4()
            n = 0
        if choice != 1 or choice != 2 or choice != 3 or choice != 4:
            print("Invalid. Enter Again.")
def manwithGirl4():
    print("The man doesn't budge and begins to shoot multiple shots into the woman making her scream in pain."
          "Instinctively, you drop the woman onto the ground.")
    manwithGirl2()
def manwithGirl3():
    print("The man begin to shoot multiple shots into the woman making her scream in pain."
          "Instinctively, you drop the woman onto the ground.")
    manwithGirl2()
def manwithGirl2():
    print("The moment that you drop the woman on the ground she begins to cry and shout."
          "\nThe man immediately shoots the woman in the face."
          "\nSurprised, you try to run, but failed miserably and ended up falling on your butt."
          "\nman: Thomas, what's wrong?"
          "\nYou:"
          "\n1. who?"
          "\n2. Who are you?"
          "\n3. do I know you?")
    n = 1
    while n ==1:
        choice = int(input())
        if choice == 1:
            manwithGirl21()
            n = 0
        if choice == 2:
            manwithGirl22()
            n = 0
        if choice == 3:
            manwithGirl23()
            n = 0
        if choice != 1 or choice != 2 or choice != 3:
            print("Invalid. Enter Again.")
def manwithGirl23():
    print("\nman: Yes, you do. I'm your ally, your friend. Trust me on this. We don't have time for chitchat.")
    manwithGirl211()
def manwithGirl22():
    manwithGirl213()
def manwithGirl21():
    print("\nman(looking concerned): You. Thomas, have you forgotten who you are?"
          "\n                         I guess that gas must've messed up your brain"
          "\nYou: "
          "\n1. I... I... I don't know"
          "\n2. What gas?"
          "\n3. There's no way that I would ever know someone that kills an innocent woman. Who are you?")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            manwithGirl211()
            n = 0
        if choice == 2:
            manwithGirl212()
            n = 0
        if choice == 3:
            manwithGirl213()
            n = 0
        if choice != 1 or choice != 2 or choice != 3:
            print("Invalid. Enter Again.")
def manwithGirl213():
    print("\nman: Trust me on this, I'm an ally. A friend. There's no point trying to get you to understand now. "
          "\n     You just have to trust me.")
    manwithGirl211()
def manwithGirl212():
    print("\nman: Don't worry about it. If I tell you now, you still won't get it. Not in the state you're in at least...")
    manwithGirl211()
def manwithGirl211():
    print("\nman(looking around): Either way, we have to get out of here now."
          "\nThe man reaches his hand down hinting to help you get up."
          "\nYou:"
          "\n1. slaps his hand away and try to escape"
          "\n2. take his hand and follow him")
    n =1
    while n ==1:
        choice = int(input())
        if choice == 1:
            manwithGirl2111()
            n = 0
        if choice == 2:
            manwithGirl2112()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def manwithGirl2112():
    manwithGirl21111()
def manwithGirl2111():
    print("\nThe man immediately pins you down before you can escape."
          "\nman(very serious tone): What are you trying to do, Thomas? You remember our orders."
          "\n                        If we don't get the cure, we're both dead. You hear me! Dead!"
          "\n                        I can't have you go running around attracting those monsters!"
          "\n                       Now you better get up and don't even think about running away!"
          "\nThe man slowly releases his grip allowing you to get up."
          "\nYou..."
          "\n1. get up slowly and follow him"
          "\n2. get up and punch him in the face")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            manwithGirl21111()
            n = 0
        if choice == 2:
            manwithGirl21112()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def manwithGirl21112():
    print("\nThe man falls backwards onto his butt."
          "\nYou..."
          "\n1. continue to attack him"
          "\n2. run away")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            manwithGirl211121()
            n = 0
        if choice == 2:
            manwithGirl211122()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def manwithGirl211122():
    manwithGirl211111()
def manwithGirl211121():
    print("\nUnfortunately, he has anticipated your move and grabs your arm and forces you to the ground."
          "\nMaking sure that you won't run, he handcuffed you forcing you to follow him.")
    manwithGirl21111()
def manwithGirl21111():
    print("\nThe two of you comes to a stop in front of a laboratory further in to the woods."
          "\nYou open the door and go in slowly."
          "\nThe man holds out his hand clearly telling you to stay."
          "\nYou:"
          "\n1. run away into the laboratory"
          "\n2. run away into the woods"
          "\n3. stay")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            manwithGirl211111()
            n = 0
        if choice == 2:
            manwithGirl211112()
            n = 0
        if choice == 3:
            manwithGirl211113()
            n = 0
        if choice != 1 or choice != 2 or choice != 3:
            print("Invalid. Enter Again.")
def manwithGirl211113():
    manwithGirl2111112()
def manwithGirl211112():
    manwithGirl211111()
def manwithGirl211111():
    print("\nThe moment that you begin to run the man takes up his gun and tells you to freeze."
          "\nYou..."
          "\n1, continue running"
          "\n2. stay ")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            manwithGirl2111111()
            n = 0
        if choice == 2:
            manwithGirl2111112()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def manwithGirl2111112():
    print("\nYou and the man reach the door with a sign that says 'Research Department'."
          "\nYou can see a glass encased bottle of liquid inside guarded by many laser beams through the window."
          "\nYou.."
          "\n1. go in through the door"
          "\n2. break the window and go through it.")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            manwithGirl21111121()
            n = 0
        elif choice == 2:
            manwithGirl21111122()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def manwithGirl21111121():
    manwithGirl2111111111()
def manwithGirl21111122():
    manwithGirl2111111112()
def manwithGirl2111111():
    print("\nYou keep running anticipating a shot to your head. The bullet never came."
          "\nYou thought that you would have been dead by now. You continue to run."
          "\nOut of nowhere, you get tackled. You roll on the ground with the attacker pinning you down."
          "\nUpon a closer look, you see that it was the same woman that you saw moments ago. "
          "\nYou..."
          "\n1. scream for help"
          "\n2. try to kick her off with your feet")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            manwithGirl21111111()
            n = 0
        if choice == 2:
            manwithGirl21111112()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def manwithGirl21111112():
    print("\nYou successfully kick her off you. The next second, the woman went limp with another bullet to the face that came"
          " from behind you."
          "\nFrom the entrance you hear the man shout."
          "\nman: Thomas! come back here!"
          "\nYou..."
          "\n1. run to the man"
          "\n2. continue to run the other way.")
    choice = int(input())
    if choice == 1:
        manwithGirl211111121()
    if choice == 2:
        manwithGirl211111122()
def manwithGirl211111121():
    manwithGirl211111111()
def manwithGirl211111122():
    manwithGirl211111112()
def manwithGirl21111111():
    print("\nBullets come flying over you hitting the woman straight in the face. "
          "\nThe woman flys backwards allowing you to get up."
          "\nFrom the entrance you hear the man shout."
          "\nman: Thomas! come back here!"
          "\nYou..."
          "\n1. run to the man"
          "\n2. continue to run the other way.")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            manwithGirl211111111()
            n = 0
        if choice == 2:
            manwithGirl211111112()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def manwithGirl211111112():
    print("\nWithin seconds, another wave of bullets come flying towards you."
          "\nBefore you can react, three of the bullets hit you in the back and you fall to the ground."
          "\nBefore dying you hear the man saying something."
          "\nman: I'm sorry Thomas, it has to be done."
          "\nFriendly Fire End")
def manwithGirl211111111():
    print("\nYou meet up with the man. You prepare for him to lecture you or punish you in some ways for"
          " not listening to him."
          """\nSurprisingly, the man says nothing except "let's move " """)
    print("\nYou and the man reach the door with a sign that says 'Research Department'."
          "\nYou can see a glass encased bottle of liquid inside guarded by many laser beams through the window."
          "\nYou.."
          "\n1. go in through the door"
          "\n2. break the window and go through it.")
    n=1
    while n == 1:
        choice = int(input())
        if choice == 1:
            manwithGirl2111111111()
            n = 0
        if choice == 2:
            manwithGirl2111111112()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def manwithGirl2111111112():
    manwithGirl2111111111111()
def manwithGirl2111111111():
    print("\nDoor: Locked"
          "\nImmediately after it says locked, the door requires a password to disable the alarm system."
          "\nYou..."
          "\n1. bust the door down"
          "\n2. smash the machine"
          "\n3. shoot the lock.")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            manwithGirl21111111111()
            n = 0
        if choice == 2:
            manwithGirl21111111112()
            n = 0
        if choice == 3:
            manwithGirl21111111113()
            n = 0
        if choice != 1 or choice != 2 or choice != 3:
            print("Invalid. Enter Again.")
def manwithGirl21111111113():
    manwithGirl2111111111111()
def manwithGirl21111111112():
    manwithGirl211111111111()
def manwithGirl21111111111():
    print("\nYou tackle the door with all you've got but the door is sealed shut. "
          "\nThe door does not budge"
          "\nYou..."
          "\n1. smash the machine"
          "\n2. shoot the lock"
          "\n3. break in through the window")
    n = 1
    while n ==1:
        choice = int(input())
        if choice == 1:
            manwithGirl211111111111()
            n = 0
        if choice == 2:
            manwithGirl211111111112()
            n = 0
        if choice == 3:
            manwithGirl211111111113()
            n = 0
        if choice != 1 or choice != 2 or choice != 3:
            print("Invalid. Enter Again.")
def manwithGirl211111111113():
    manwithGirl2111111111111()
def manwithGirl211111111112():
    manwithGirl2111111111113()
def manwithGirl211111111111():
    print("\nThe machine screen cracks."
          "\nYou hear the speaker announcing."
          "\nSpeaker: Intruder alert! Intruder alert! Self-destruct in t - 5 minutes"
          "\nYou... "
          "\n1. break in through the window."
          "\n2. run out the building."
          "\n3. shoot the lock.")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            manwithGirl2111111111111()
            n = 0
        if choice == 2:
            manwithGirl2111111111112()
            n = 0
        if choice == 3:
            manwithGirl2111111111113()
            n = 0
        if choice != 1 or choice != 2 or choice != 3:
            print("Invalid. Enter Again.")
def manwithGirl2111111111113():
    print("\nUnfortunately, the lock is bullet proof, and the bullets ricochet back into you."
          "\nYou fall upon receiving the bullets in your body."
          "\nThe man also falls with you."
          "\nBoth people die of over bleeding."
          "\nFool's End")
def manwithGirl2111111111112():
    print("\nYou and the man run out the building with a minute to spare. The building blows up behind you along with the "
          "\ncure inside it. Knowing that he has failed his mission the man became depressed."
          "\nYou..."
          "\n1. comfort him"
          "\n2. go back to the laboratory to see if the cure has somehow survived")
    n = 1
    while n ==1:
        choice = int(input())
        if choice == 1:
            manwithGirl21111111111121()
            n = 0
        if choice == 2:
            manwithGirl21111111111122()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def manwithGirl21111111111121():
    print("\nman: GET AWAY FROM ME!"
          "\n You slowly walk backwards"
          "\n The man gets up with tears in his face"
          "\n man: Look at what you've done"
          "\n He holds up his gun pointing directly at you and he shoots."
          "\n You feel the pain and collapsed on the floor."
          "\n Before passing out, you hear another gunshot and see that the man in front of you has also fallen."
          "\n You die."
          "\n Coward's End")
def manwithGirl21111111111122():
    print("\nYou walk back to the laboratory without the man. You can see debris flung everywhere."
          "\nThere are many unexplained body parts which you don't even dare think about where they come from."
          "\nIn the center of the explosion lies a shiny bottle of liquid. The cure."
          "\nYou go in to retrieve the cure. Almost immediately after retrieving the cure, a helicopter appears."
          "\nYou hear the man screaming something about failing the mission."
          "\nThe next second, you hear a gunshot. When you arrive at where the man is, the man has suicided."
          "\nThe helicopter lowers its ladder and you climbed on."
          "\nYou flew away from the mysterious island."
          "\nLone Hero Ending")
def manwithGirl2111111111111():
    print("\nYou go into the lab and you see the cure."
          "\nThe man tells you to wait."
          "\nYou..."
          "\n1. wait"
          "\n2. reach for the cure.")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            manwithGirl21111111111111()
            n = 0
        if choice == 2:
            manwithGirl21111111111112()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def manwithGirl21111111111112():
    print("\nBefore reaching the cure, the gatling gun appears from the side of the wall and begins to shoot"
          " around the room. "
          "\nYour head gets lodged with many bullets and you die."
          "\nFool's End")
def manwithGirl21111111111111():
    print("\nThe man reaches into his pocket and throws a modified EMP that shuts down the security inside the room."
          "\nHe grabs the cure and signals you to follow him out."
          "\nSpeaker: Self-destruct in t - 3 minutes"
          "\nAs you get closer to the entrance, you see a pack of creatures that looks familiar to you."
          "\nYou recognize the pale face and the flowy white dress. "
          "\nYou see a pack of identical woman standing in front of the entrance blocking your only way out."
          "\nThe man turns around and sees another hoard of women getting closer."
          "\nYou..."
          "\n1. take the cure and push the man into the hoard blocking the entrance."
          "\n2. volunteer to distract the hoard while the man gets outside")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            manwithGirl211111111111111()
            n = 0
        if choice == 2:
            manwithGirl211111111111112()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def manwithGirl211111111111112():
    print("\nBefore the man can stop you, you walk into the crowd of women where they begin to grab you."
          "\nYou feel the pain of your body ripping into shreds."
          "\nYou die a horrendous death."
          "\nHero End")
def manwithGirl211111111111111():
    print("\nSurprised the man falls forward into the crowd creating a space for you to escape."
          "\nYou run for it out into the forest."
          "\nYou continue running without looking behind and you hear an explosion behind you as "
          " debris bloody body parts from the explosion come shooting toward you."
          "\nYou reach your original waking place where you see a helicopter lowering its ladder to you."
          "\nInstinctively, you climbed on to the ladder and you fly away from this horrifying island."
          "\nSurvivalist's End")
def manwithGirl1():
    print("\nAs you lower the woman down, the woman eyes spring open and she bites your neck"
          "\nBefore long, you hear a gun shot, and you see the woman drop dead."
          "\nHowever, when you try to get up, you can't."
          "\nYou realize you are turning extremely pale like the girl before you."
          "\nYou feel the man's gun beginning to raise again."
          "\nYou..."
          "\n1. run away"
          "\n2. stay there and await your imminent death")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            manwithGirl11()
            n = 0
        if choice == 2:
            manwithGirl12()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def manwithGirl11():
    print("\nBefore the man can get his gun up to your head, you sprint away."
          "\nYou hear shots fired behind you."
          "\nAs you run, you realize how fast you have become and that you crave brains.")
    print("\nYou live out the rest of your undead life as a zombie."
          "\nZombie Ending")
def manwithGirl12():
    print("\nYou remain motionless."
          "\nYou can hear the man saying something."
          "\nman: Goodbye friend"
          "\nYou died"
          "\nHuman Ending")

def woman():
    print("\nYou wipe the sand that was on your face and rub your eyes in disbelief."
          "\nHappy to finally see another living soul around the area, you..."
          "\n1. run toward her"
          "\n2. wave at her telling her to get close"
          "\n3. slowly back away and go back to the tree")
    n = 1
    while n ==1:
        choice = int(input())
        if choice == 1:
            woman1()
            n = 0
        if choice == 2:
            woman2()
            n = 0
        if choice == 3:
            woman3()
            n = 0
        if choice != 1 or choice != 2 or choice != 3:
            print("Invalid. Enter Again.")
def woman3():
    introBasic()
def woman2():
    print("\nShe seems to not hear you."
          "\nYou..."
          "\n1. continue to wave at her telling her to get close."
          "\n2. run towards her."
          "\n3. slowly back away and go back to the tree.")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            woman21()
            n = 0
        if choice == 2:
            woman22()
            n = 0
        if choice == 3:
            woman23()
            n = 0
        if choice != 1 or choice != 2 or choice != 3:
            print("Invalid. Enter Again.")
def woman23():
    introBasic()
def woman22():
    woman1()
def woman21():
    print("\nShe still doesn't budge."
          "\nYou... "
          "\n1. continue doing the same thing"
          "\n2. run towards her."
          "\n3. slowly back away and go back to the tree.")
    n = 1
    while n ==1:
        choice = int(input())
        if choice == 1:
            woman211()
            n = 0
        if choice == 2:
            woman212()
            n = 0
        if choice == 3:
            woman213()
            n = 0
        if choice != 1 or choice != 2 or choice != 3:
            print("Invalid. Enter Again.")
def woman213():
    introBasic()
def woman212():
    woman1()
def woman211():
    print("\n Instead of walking towards you, she flew towards you as you"
          " see the beast that had just tackled her from behind."
          "\nLanding right next to you, your feet get soaked in the fresh blood oozing out of the woman's head"
          "\nYou..."
          "\n1. check the woman."
          "\n2. run away.")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            woman2111()
            n = 0
        if choice == 2:
            woman2112()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def woman2111():
    print("\nUpon checking the woman, the woman, obviously dead, has a knife under her sleeves."
          "\nYou..."
          "\n1. take the knife and run."
          "\n2. take the knife and fight.")
    n = 1
    while n == 1:
        choice =int(input())
        if choice == 1:
            woman21111()
            n = 0
        if choice == 2:
            woman21112()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def woman21112():
    print("\nYou turn around and you see the beast ready to jump at you."
          "\nYou..."
          "\n1. throw the knife at it."
          "\n2. wait for the tiger to jump forward before you stab it in mid-air.")
    n = 1
    while n ==1:
        choice = int(input())
        if choice == 1:
            woman211121()
            n = 0
        if choice == 2:
            woman211122()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def woman211122():
    print("\nThe beast jumps forward, and your knife goes through its belly."
          "\nThe beast cowards in fear as it runs off dripping a yellow liquid with the knife still attached "
          " to its bleeding stomach."
          "\nYou..."
          "\n1. investigate the liquid"
          "\n2. go back to the tree")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            woman2111221()
            n = 0
        if choice == 2:
            woman2111222()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def woman2111222():
    introBasic()
def woman2111221():
    print("\nYou bend down on your knees and scoop up the liquid with your right hand."
          "\nThe moment that the liquid touches your right hand, your hand begins to melt."
          "\nOut of shock, you faint.")
    introBroken()
def woman211121():
    print("\nThe handle of the knife hits the beast directly in the head"
          " and angers the beast."
          "\nThe beast jumps forward and bites your right arm off."
          "\nYou black out immediately.")
    introBroken()
def woman21111():
    print("\nUnfortunately, the time that you take checking the woman allowed the beast to move in on you. "
          "\nBefore you are able to run, the beast bite off your right arm"
          "\nThe extreme pain causes you to faint immediately.")
    introBroken()
def woman2112():
    woman111131()
def woman1():
    print("\nAbout twenty feet behind the mysterious woman, you see a beast with sharp fangs preparing to leap forward."
          "\nYou..."
          "\n1. yell at her to get away"
          "\n2. sprint the rest of the way and tackle her out of the beast's path"
          "\n3. turn the other way and run")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            woman11()
            n = 0
        if choice == 2:
            woman12()
            n = 0
        if choice == 3:
            woman13()
            n = 0
        if choice != 1 or choice != 2 or choice != 3:
            print("Invalid. Enter Again.")
def woman13():
    woman111131()
def woman12():
    print("\nYou succesfully saved the woman's life."
          "\nGetting up from the ground, you feel her holding on to your right wrist."
          "\nYou know that the beast will come back for another attack fast, so"
          " you turned around trying to hurry the woman to get up as well."
          "\nThe woman got up; however, she won't run with you."
          "\nYou..."
          "\n1. carry her on your back and start running."
          "\n2. let go of her and run."
          "\n3. stay there and fight.")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            woman121()
            n = 0
        if choice == 2:
            woman122()
            n = 0
        if choice == 3:
            woman123()
            n = 0
        if choice != 1 or choice != 2 or choice != 3:
            print("Invalid. Enter Again.")
def woman122():
    woman111131()
def woman123():
    print("\nAs you are about to make your attack against the beast, the woman, with a knife that must have been hidden in her dress, cuts off your right arm."
          "\nOut of shock, you black out immediately.")
    introBroken()
def woman121():
    print("\nAs you are about to scoop her up with your other arm, the woman begins to scream and shout."
          "\nYou..."
          "\n1. knock her out with your fists."
          "\n2. abandon her and run away.")
    n = 1
    while n == 1:
        choice =int(input())
        if choice == 1:
            woman1211()
            n = 0
        if choice == 2:
            woman1212()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def woman1212():
    woman111131()
def woman1211():
    print("\nShe instantly falls silent, and you ran back to the tree before the beast notices that you had "
          "escaped with the girl.")
    introWithWoman()
def woman11():
    print("\nShe seems to not hear you."
          "\nYou..."
          "\n1. continue to yell at her"
          "\n2. turn the other way and run")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            woman111()
            n = 0
        if choice == 2:
            woman112()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def woman112():
    woman111131()
def woman111():
    print("\nShe still doesn't budge."
          "\nYou watch her get torn into pieces."
          "\n1. Fight the monster"
          "\n2. turn the other way and run")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            woman1111()
            n = 0
        if choice == 2:
            woman1112()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def woman1112():
    woman111131()
def woman1111():
    print("\nThe beast is about to attack."
          "\nYou..."
          "\n1. get ready to dodge and then attack full on"
          "\n2. attack it before it can attack you"
          "\n3. use the dead woman as a shield and hit the beast with your fist"
          "\n4. turn the other way and run")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            woman11111()
            n = 0
        if choice == 2:
            woman11112()
            n = 0
        if choice == 3:
            woman11113()
            n = 0
        if choice == 4:
            woman11114()
            n = 0
        if choice != 1 or choice != 2 or choice != 3 or choice != 4:
            print("Invalid. Enter Again.")
def woman11114():
    woman111131()
def woman11112():
    print("\nYou run straight towards the beast preparing to punch its face with all you've got."
          "\nUnfortunately, the beast is faster."
          "\nIt pins you down with ease, and it bites off your right arm"
          "\nImmediately, you blackout")
    introBroken()
def woman11113():
    print("\nAs you reach down to grab the dead woman, the beast lunges at you."
          "\nFortunately, you are able to get to the woman in time"
          "\nYou hold the woman up, and the beast bites on the woman once more,"
          " and it gets its teeth stuck inside the woman"
          "\nYou..."
          "\n1. run away"
          "\n2. attack it with all you've got")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            woman111131()
            n = 0
        if choice == 2:
            woman111132()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def woman111131():
    print("\nThe moment that you started running away, the beast stops chasing you."
          "\nRelieved, you go back to where you started.")
    introBasic()
def woman11111():
    print("\nThe beast lunges at you but you were prepared."
          "\nYou..."
          "\n1. roll under"
          "\n2. dodge to the right"
          "\n3. dodge to the left"
          "\n4. jump back")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            woman111111()
            n = 0
        if choice == 2:
            woman111112()
            n = 0
        if choice == 3:
            woman111113()
            n = 0
        if choice == 4:
            woman111114()
            n = 0
        if choice != 1 or choice != 2 or choice != 3 or choice != 4:
            print("Invalid. Enter Again.")
def woman111111():
    print("\nYou sucessfully dodge the attack; however, the tail, covered in sharp razor blades, grazes your face"
          " and you begin to feel sleepy"
          "\nYou..."
          "\n1. continue to fight"
          "\n2. run away"
          "\n3. give up on fighting")
    n = 1
    while n ==1:
        choice = int(input())
        if choice == 1:
            woman1111111()
            n = 0
        if choice == 2:
            woman1111112()
            n = 0
        if choice == 3:
            woman1111113()
            n = 0
        if choice != 1 or choice != 2 or choice != 3:
            print("Invalid. Enter Again.")
def woman1111112():
    print("\nYou run away as fast as you can, but you continue to get dizzier."
          "\nBefore you know it, the lights are out")
    intro()
def woman1111111():
    print("\nYou jump onto the beast's back and you started pounding him with your bare fist"
          "; however, the longer that you are in physical contact with the beast, the sleepier you get,"
          "\nBefore you know it, the lights are out")
    intro()
def woman1111113():
    print("\nThe beast suddenly stops in front of you when it tries to attack once more."
          "\nIt sniffs you, and then it turns and walks away."
          "\nYou..."
          "\n1. follow it"
          "\n2. stay where you are and rest")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            woman11111131()
            n = 0
        if choice == 2:
            woman11111132()
            n = 0
        if choice != 1 or choice != 2:
            print("Invalid. Enter Again.")
def woman11111131():
    print("\nSensing animosity towards it, the beast turns around and jumps at you."
          "\nUnable to react fast enough, your right hand gets bitten off"
          "\nAlmost instantaneously, you fainted.")
    introBroken()
def woman11111132():
    print("\nBefore you know it, you fell asleep")
    intro()
def woman111112():
    print("\nYou successfully dodge the attack; however, moving too fast, you hit the palm tree head first "
          "causing you to faint.")
    intro()
def woman111113():
    print("\nYou successfully dodge the attack and you jumped onto its back "
          "and you started pounding him with your bare fist"
          "; however, the longer that you are in physical contact with the beast, the sleepier you get,"
          "\nBefore you know it, the lights are out")
    intro()
def woman111114():
    print("\nYou jump backwards. Unfortunately, the jump is too short and your right arm gets bitten off."
          "\nInstantaneously, you faint")
    introBroken()
def woman111132():
    woman1111111()

def main():
    print("FORGOTTEN")
    gender = raw_input("\nMale or Female:")
    if gender.lower() in ['male']:
        print("")
    else:
        print("Too bad, you're a male now.")
    intro()

def man():
    print("You walk up to the man quietly"
          "The man follows you with his eyes continuing to stare at you."
          "As you get closer, the man begins to lift up his gun"
          "You..."
          "\n1. stop and raise your hand showing that you have no concealed weapon."
          "\n2. run away as fast as possible."
          "\n3. stop in your track."
          "\n4. jump forward trying to grab hold of the gun before he aims it at you.")
    n = 1
    while n == 1:
        choice = int(input())
        if choice == 1:
            man1()
            n = 0
        elif choice == 2:
            man2()
            n = 0
        elif choice == 3:
            man3()
            n = 0
        elif choice == 4:
            man4()
            n = 0
        if choice != 1 or choice != 2 or choice != 3 or choice != 4:
            print("Invalid. Enter Again.")
def man4():
    manwithGirl21112()
def man3():
    man1()
def man2():
    manwithGirl2111()
def man1():
    print("The man lowers his gun and walks toward you."
          "The man speaks."
          "\nman: Thomas. Are you okay?"
          "\nConfused, you reply"
          "\n1. who?"
          "\n2. Who are you?"
          "\n3. do I know you?")
    n = 1
    while n ==1:
        choice = int(input())
        if choice == 1:
            manwithGirl21()
            n = 0
        if choice == 2:
            manwithGirl22()
            n = 0
        if choice == 3:
            manwithGirl23()
            n = 0
        if choice != 1 or choice != 2 or choice != 3:
            print("Invalid. Enter Again.")

def mn():
    print("Staring at two different views on your window ledge"
          "\ncoffee is going cold, it's like time froze"
          "\nthere you go wishing floating down our wishing well"
          "\nIt's like I'm always causing trouble, causing hell"
          "\nI didn't mean to put you throuhg it I can tell"
          "\nWe can not sweep this under the carpet"
          "\n"
          "\nI hope that I can turn back the time"
          "\nto make it all alright, all alright for us"
          "\nI promise to make a new world, for us two"
          "\nwith you in the middle"
          "\n"
          "\nLying down beside you what's going through your head"
          "\nthe silence in the air, felt like my soul froze"
          "\nam i just overthinking feelings I conceal"
          "\nThis gut feeling I'm trying to get off me as well"
          "\nI hope we find our missing pieces and just chill"
          "\nWe can not sweep it under the carpet"
          "\n"
          "\nI hope that I can turn back the time"
          "\nto make it all alright, all alright for us"
          "\nI promise to make a new world, for us two"
          "\nwith you in the middle")

main()
