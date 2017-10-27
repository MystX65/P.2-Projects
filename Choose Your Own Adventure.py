
def NerdIntro():
    print("\n   You're finally a junior. Tomorrow is the first day of school, and you know it's going to be your worst year with so many classes and extracurriculars that you have to worry about."
          "You know that making a good impression on the teachers is the only way that will get you through this year.")
    print("\n Clock: 6:00 a.m.")
    print("\n *buzz *buzz"
          "\n You barely hear the sound of your alarm clock. "
          "Do you:"
          "\n1. wake up"
          "\n2. continue sleeping through the alarm"
          "\n3. hit the snooze button")
    choice = int(raw_input("You decided to... "))
    if choice == 1:
        NerdChoice1()
    if choice == 2:
        NerdChoice2()
    if choice == 3:
        NerdChoice3()
def NerdChoice1():
    print("\n You wake up and you get yourself ready for your first day as a Junior."
          "\nYou got to your zero period class, and you saw your AP US History teacher, Mr. Paccone."
          "\n You..."
          "\n1. say goodmorning and introduce yourself"
          "\n2. stay as quiet as possible and sit in a chair")
    choice = int(raw_input("you decided to..."))
    if choice == 1:
        NerdChoice11()
    if choice == 2:
        NerdChoice12()
def NerdChoice2():
    print("\nClock: 6:40 a.m."
          "\n Your mom busts through your door and shouts for you to wake up."
          "\n You ..."
          "\n1. ignore her and continue sleeping"
          "\n2. wake up immediately and got ready within 5 minutes and rushes out the door"
          "\n3. asks for five more minutes of sleep ")
    choice = int(raw_input("You..."))
    if choice == 1:
        NerdChoice21()
    if choice == 2:
        NerdChoice22()
    if choice == 3:
        NerdChoice23()
def NerdChoice3():
    print("\nClock: 6:30 a.m."
          "\n *buzz *buzz"
          "You hear the sound of your alarm once more. "
          "Do you..."
          "\n1. hit the snooze button"
          "\n2. get up and prepare for school")
    choice = int(raw_input("You..."))
    if choice == 1:
        NerdChoice31()
    if choice ==2:
        NerdChoice32()
def NerdChoice11():
    print("You go up to Mr. Paccone and introduce yourself and greet him. He returns your gesture and you got past 0 period without any trouble.")
    print("You arrived at your 1st period class, AP Lang. The teacher is Mrs. Davidson. You walk into the classroom and hear music that you like."
          "You..."
          "\n1. greet her and talk about the music"
          "\n2. walk and sit down at a desk without talking to her")
    choice = int(raw_input("You..."))
    if choice ==1:
        NerdChoice111()
    if choice ==2:
        NerdChoice112()
def NerdChoice12():
    print("You got through 0 period without Mr. Paccone ever recognizing you.")
    print( "You arrived at your 1st period class, AP Lang. The teacher is Mrs. Davidson. You walk into the classroom and hear music that you like."
    "You..."
    "\n1. greet her and talk about the music"
    "\n2. walk and sit down at a desk without talking to her")
    choice = int(raw_input("You..."))
    if choice == 1:
        NerdChoice111()
    if choice == 2:
        NerdChoice112()
def NerdChoice21():
    print("Your mom slaps you awake, and now you face is red. You reached 0 period at 7:15 a.m. Already late you slowly walk into the classroom where everyone stares at you. Embarrassed, you make a fool out of yourself, and was unable to focus on anything for the rest of the day. Because of this, you failed to make an impression on the teachers, and you were unable to get good grades. You have Failed.")
    gameover()
def gameover():
    print("GAMEOVER")
def NerdChoice22():
    print("You arrived at 0 period barely on time. You sat down without being able to talk to Mr. Paccone personally. 0 period passes by in a flash and you are now going to your 1st period.")
    print("You arrived at your 1st period class, AP Lang. The teacher is Mrs. Davidson. You walk into the classroom and hear music that you like."
    "You..."
    "\n1. greet her and talk about the music"
    "\n2. walk and sit down at a desk without talking to her")
    choice = int(raw_input("You..."))
    if choice == 1:
        NerdChoice111()
    if choice == 2:
        NerdChoice112()
def NerdChoice23():
    print("Your mom decided to let you sleep for five more minutes."
          "\nClock: 7:00a.m."
          "\n You have lost track of time and your mom has forgotten to wake you up."
          "You reached 0 period at 7:15 a.m. Already late you slowly walk into the classroom where everyone stares at you. Embarrassed, you make a fool out of yourself, and was unable to focus on anything for the rest of the day. Because of this, you failed to make an impression on the teachers, and you were unable to get good grades.You have Failed.")
    gameover()
def NerdChoice31():
    print("Clock: 6:45")
    print("\n *buzz *buzz"
          "\nYou ..."
          "\n1. "
          "\n2. "
          "\n3. ")
#def JockIntro():
#def GeekIntro():
def main():
    print("Junior Year")
    a = raw_input("Do you want to play as a Jock, a Nerd")
    NerdIntro()
main()
