import turtle
import random
import time

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.setworldcoordinates(-150,-250,150,200)

#Players
player1 = raw_input("Player 1 name:")
player2 = raw_input("Player 2 name:")
player3 = raw_input("Player 3 name:")
player4 = raw_input("Player 4 name:")
x = turtle.Turtle()
y = turtle.Turtle()
z = turtle.Turtle()
w = turtle.Turtle()
for i in (x,w,y,z):
    i.ht()
    i.speed(0)
x.up()
x.goto(-140,190)
x.write(player1, False, "left", ("Arial", 20, "normal"))
y.up()
y.goto(-100,190)
y.write(player2, False, "left", ("Arial", 20, "normal"))
z.up()
z.goto(-60,190)
z.write(player3, False, "left", ("Arial", 20, "normal"))
w.up()
w.goto(-20,190)
w.write(player4, False, "left", ("Arial", 20, "normal"))

for i in (x,w,y,z):
    i.down()
    i.fd(10)
    i.backward(20)
    i.fd(10)
    i.up()
    i.rt(90)
    i.fd(10)
    i.lt(90)

one = 10
two = 10
three = 10
four = 10

score1 = turtle.Turtle()
score2 = turtle.Turtle()
score3 = turtle.Turtle()
score4 = turtle.Turtle()

for i in (score1, score2,score3,score4):
    i.ht()
    i.up()
    i.speed(0)

score1.goto(x.xcor(),x.ycor())
score2.goto(y.xcor(),y.ycor())
score3.goto(z.xcor(),z.ycor())
score4.goto(w.xcor(),w.ycor())

Line = turtle.Turtle()
Line.ht()
Line.speed(0)
Line.color("red")
Line.up()
Line.fd(100)
Line.lt(90)
Line.down()
Line.fd(170)
Line.backward(400)
Line.up()
Line.home()
Line.goto(-100,170)
Line.color("black")
Line.lt(90)
Line.down()
Line.backward(400)
writer = turtle.Turtle()
writer2 = turtle.Turtle()
writer3 = turtle.Turtle()
writer2.ht()
writer3.ht()
writer.ht()
writer2.up()
writer3.up()
writer2.speed(0)
writer3.speed(0)
writer2.rt(90)
writer2.fd(100)
writer2.lt(90)
writer3.rt(90)
writer3.fd(200)
writer.lt(90)


rounds = int(input("How many rounds are you playing?"))

t1 = turtle.Turtle()
t2= turtle.Turtle()
t3= turtle.Turtle()
t4= turtle.Turtle()
t5= turtle.Turtle()
t6= turtle.Turtle()
t7= turtle.Turtle()
t8= turtle.Turtle()
for i in (t1, t2, t3, t4, t5, t6, t7, t8):
    i.up()
    i.speed(0)
    i.shape("turtle")
black = "black"
t1.color("red",black)
t2.color("green",black)
t3.color("pink",black)
t4.color("blue",black)
t5.color("orange",black)
t6.color("yellow",black)
t7.color("purple",black)
t8.color("brown",black)



for n in range(rounds):
    writer.clear()
    writer2.clear()
    writer3.clear()
    a = False
    s = False
    d = False
    f = False
    g = False
    h = False
    j = False
    k = False

    a1 = False
    s1 = False
    d1 = False
    f1 = False
    g1 = False
    h1 = False
    j1 = False
    k1 = False

    a2 = False
    s2 = False
    d2 = False
    f2 = False
    g2 = False
    h2 = False
    j2 = False
    k2 = False

    e = "1st Place"
    r = "2nd Place"
    t = "3rd Place"
    y = False
    u = False
    i = False

    t1.goto(-100,-200)
    t2.goto(-100,-150)
    t3.goto(-100,-100)
    t4.goto(-100,-50)
    t5.goto(-100,0)
    t6.goto(-100,50)
    t7.goto(-100,100)
    t8.goto(-100,150)

    t1.write("1", False, "left", ("Arial", 20, "normal"))
    t2.write("2", False, "left", ("Arial", 20, "normal"))
    t3.write("3", False, "left", ("Arial", 20, "normal"))
    t4.write("4", False, "left", ("Arial", 20, "normal"))
    t5.write("5", False, "left", ("Arial", 20, "normal"))
    t6.write("6", False, "left", ("Arial", 20, "normal"))
    t7.write("7", False, "left", ("Arial", 20, "normal"))
    t8.write("8", False, "left", ("Arial", 20, "normal"))

    one  = str(one)
    two =  str(two)
    three = str(three)
    four = str(four)

    bet1 = raw_input(player1 + ": Which color do you want to bet on: ")
    b1 = int(input("You have " + one+ " coin(s). How much do you want to bet?" ))
    bet2 = raw_input(player2 + ": Which color do you want to bet on: ")
    b2 = int(input("You have " + two + " coin(s). How much do you want to bet?"))
    bet3 = raw_input(player3 + ": Which color do you want to bet on: ")
    b3 = int(input("You have " + three + " coin(s). How much do you want to bet?"))
    bet4 = raw_input(player4 + ": Which color do you want to bet on: ")
    b4 = int(input("You have " + four + " coin(s). How much do you want to bet?"))

    one = int(one)
    two = int(two)
    three = int(three)
    four = int(four)

    one = one - b1
    two = two - b2
    three = three - b3
    four = four - b4

    writer.color('black')
    writer.write("3...",False, "center",("Arial",100,"normal"))
    time.sleep(1)
    writer.clear()
    writer.write("2...",False, "center",("Arial",100,"normal"))
    time.sleep(1)
    writer.clear()
    writer.write("1...", False, "center", ("Arial", 100, "normal"))
    time.sleep(1)
    writer.clear()
    writer.write("Go!",False, "center",("Arial",100,"normal"))
    time.sleep(1)
    writer.clear()

#turtle movement/winner
    for x in range(100):
        if i:
            time.sleep(2)
            break
        if t1.xcor() >= 100:
            if u == True and a == False and a1 == False:
                writer3.color("red")
                writer3.write("Red is " + t, False, "center", ("Arial", 100, "normal"))
                i = True
                u = False
                a2 = True
        if t2.xcor() >= 100:
            if u == True and s == False and s1 == False:
                writer3.color("green")
                writer3.write("Green is " + t, False, "center", ("Arial", 100, "normal"))
                i = True
                u = False
                s2 = True
        if t3.xcor() >= 100:
            if u == True and d == False and d1 == False:
                writer3.color("pink")
                writer3.write("Pink is " + t, False, "center", ("Arial", 100, "normal"))
                i = True
                u = False
                d2 = True
        if t4.xcor() >= 100:
            if u == True and f == False and f1 == False:
                writer3.color("blue")
                writer3.write("Blue is " + t, False, "center", ("Arial", 100, "normal"))
                i = True
                u = False
                f2 = True
        if t5.xcor() >= 100:
            if u == True and g == False and g1 == False:
                writer3.color("orange")
                writer3.write("Orange is " + t, False, "center", ("Arial", 100, "normal"))
                i = True
                u = False
                g2 = True
        if t6.xcor() >= 100:
            if u == True and h == False and h1 == False:
                writer3.color("yellow")
                writer3.write("Yellow is " + t, False, "center", ("Arial", 100, "normal"))
                i = True
                u = False
                h2 = True
        if t7.xcor() >= 100:
            if u == True and j == False and j1 == False:
                writer3.color("purple")
                writer3.write("Purple is " + t, False, "center", ("Arial", 100, "normal"))
                i = True
                u = False
                j2 = True
        if t8.xcor() >= 100:
            if u == True and k == False and k1 == False:
                writer3.color("brown")
                writer3.write("Brown is " + t, False, "center", ("Arial", 100, "normal"))
                i = True
                u = False
                k2 = True
        if t1.xcor() >= 100:
            if y == True and a == False:
                writer2.color("red")
                writer2.write("Red is " + r, False, "center", ("Arial", 100, "normal"))
                u = True
                y = False
                a1 = True
        if t2.xcor() >= 100:
            if y == True and s == False:
                writer2.color("green")
                writer2.write("Green is " + r, False, "center", ("Arial", 100, "normal"))
                u = True
                y = False
                s1 = True
        if t3.xcor() >= 100:
            if y == True and d == False:
                writer2.color("pink")
                writer2.write("Pink is " + r, False, "center", ("Arial", 100, "normal"))
                u = True
                y = False
                d1 = True
        if t4.xcor() >= 100:
            if y == True and f == False:
                writer2.color("blue")
                writer2.write("Blue is " + r, False, "center", ("Arial", 100, "normal"))
                u = True
                y = False
                f1 = True
        if t5.xcor() >= 100:
            if y == True and g == False:
                writer2.color("orange")
                writer2.write("Orange is " + r, False, "center", ("Arial", 100, "normal"))
                u = True
                y = False
                g1 = True
        if t6.xcor() >= 100:
            if y == True and h == False:
                writer2.color("yellow")
                writer2.write("Yellow is " + r, False, "center", ("Arial", 100, "normal"))
                u = True
                y = False
                h1 = True
        if t7.xcor() >= 100:
            if y == True and j == False:
                writer2.color("purple")
                writer2.write("Purple is " + r, False, "center", ("Arial", 100, "normal"))
                u = True
                y = False
                j1 = True
        if t8.xcor() >= 100:
            if y == True and k == False:
                writer2.color("brown")
                writer2.write("Brown is " + r, False, "center", ("Arial", 100, "normal"))
                u = True
                y = False
                k1 = True
        if t4.xcor() < 100:
            t4.fd(random.randrange(1, 10))
        if t1.xcor() < 100:
            t1.fd(random.randrange(1, 10))
        if t8.xcor() < 100:
            t8.fd(random.randrange(1, 10))
        if t7.xcor() < 100:
            t7.fd(random.randrange(1, 10))
        if t5.xcor() < 100:
            t5.fd(random.randrange(1, 10))
        if t6.xcor() < 100:
            t6.fd(random.randrange(1, 10))
        if t3.xcor() < 100:
            t3.fd(random.randrange(1, 10))
        if t2.xcor() < 100:
            t2.fd(random.randrange(1, 10))
        if t1.xcor() >= 100:
            if t4.xcor() < 100:
                if t2.xcor() < 100:
                    if t3.xcor() < 100:
                        if t7.xcor() < 100:
                            if t5.xcor() < 100:
                                if t6.xcor() < 100:
                                    if t8.xcor() < 100:
                                        writer.color("red")
                                        writer.write("Red is "+ e, False, "center", ("Arial", 100, "normal"))
                                        a = True
                                        y = True
        if t2.xcor() >= 100:
            if t4.xcor() < 100:
                if t1.xcor() < 100:
                    if t3.xcor() < 100:
                        if t7.xcor() < 100:
                            if t5.xcor() < 100:
                                if t6.xcor() < 100:
                                    if t8.xcor() < 100:
                                        writer.color("green")
                                        writer.write("Green is " + e, False, "center", ("Arial", 100, "normal"))
                                        s = True
                                        y = True
        if t3.xcor() >= 100:
            if t4.xcor() < 100:
                if t2.xcor() < 100:
                    if t1.xcor() < 100:
                        if t7.xcor() < 100:
                            if t5.xcor() < 100:
                                if t6.xcor() < 100:
                                    if t8.xcor() <= 100:
                                        writer.color("pink")
                                        writer.write("Pink is " +e, False, "center", ("Arial", 100, "normal"))
                                        d = True
                                        y = True
        if t4.xcor() >= 100:
            if t1.xcor() < 100:
                if t2.xcor() < 100:
                    if t3.xcor() < 100:
                        if t7.xcor() < 100:
                            if t5.xcor() < 100:
                                if t6.xcor() < 100:
                                    if t8.xcor() < 100:
                                        writer.color("blue")
                                        writer.write("Blue is "+ e, False, "center", ("Arial", 100, "normal"))
                                        f = True
                                        y = True
        if t5.xcor() >= 100:
            if t4.xcor() < 100:
                if t2.xcor() < 100:
                    if t3.xcor() < 100:
                        if t7.xcor() < 100:
                            if t1.xcor() < 100:
                                if t6.xcor() < 100:
                                    if t8.xcor() < 100:
                                        writer.color("orange")
                                        writer.write("Orange is "+e, False, "center", ("Arial", 100, "normal"))
                                        g = True
                                        y =True
        if t6.xcor() >= 100:
            if t4.xcor() < 100:
                if t2.xcor() < 100:
                    if t3.xcor() < 100:
                        if t7.xcor() < 100:
                            if t5.xcor() < 100:
                                if t1.xcor() < 100:
                                    if t8.xcor() < 100:
                                        writer.color("yellow")
                                        writer.write("Yellow is "+e, False, "center", ("Arial", 100, "normal"))
                                        h = True
                                        y = True
        if t7.xcor() >= 100:
            if t4.xcor() < 100:
                if t2.xcor() < 100:
                    if t3.xcor() < 100:
                        if t1.xcor() < 100:
                            if t5.xcor() < 100:
                                if t6.xcor() < 100:
                                    if t8.xcor() < 100:
                                        writer.color("purple")
                                        writer.write("Purple is "+ e, False, "center", ("Arial", 100, "normal"))
                                        j = True
                                        y = True
        if t8.xcor() >= 100:
            if t4.xcor() < 100:
                if t2.xcor() < 100:
                    if t3.xcor() < 100:
                        if t7.xcor() < 100:
                            if t5.xcor() < 100:
                                if t6.xcor() < 100:
                                    if t1.xcor() < 100:
                                        writer.color("brown")
                                        writer.write("Brown is " + e, False, "center", ("Arial", 100, "normal"))
                                        k = True
                                        y = True

#point distribution
    if a:
        if bet1.lower() in ['red']:
            one = 3*b1 +one
        if bet2.lower() in ['red']:
            two = 3*b2 + two
        if bet3.lower() in ['red']:
            three = 3*b3 + three
        if bet4.lower() in ['red']:
            four = 3*b4 + four
    if s:
        if bet1.lower() in ['green']:
            one = 3 * b1 + one
        if bet2.lower() in ['green']:
            two = 3 * b2 + two
        if bet3.lower() in ['green']:
            three = 3 * b3 + three
        if bet4.lower() in ['green']:
            four = 3 * b4 + four
    if d:
        if bet1.lower() in ['pink']:
            one = 3 * b1 + one
        if bet2.lower() in ['pink']:
            two = 3 * b2 + two
        if bet3.lower() in ['pink']:
            three = 3 * b3 + three
        if bet4.lower() in ['pink']:
            four = 3 * b4 + four
    if f:
        if bet1.lower() in ['blue']:
            one = 3 * b1 + one
        if bet2.lower() in ['blue']:
            two = 3 * b2 + two
        if bet3.lower() in ['blue']:
            three = 3 * b3 + three
        if bet4.lower() in ['blue']:
            four = 3 * b4 + four
    if g:
        if bet1.lower() in ['orange']:
            one = 3 * b1 + one
        if bet2.lower() in ['orange']:
            two = 3 * b2 + two
        if bet3.lower() in ['orange']:
            three = 3 * b3 + three
        if bet4.lower() in ['orange']:
            four = 3 * b4 + (four - b4)
    if h:
        if bet1.lower() in ['yellow']:
            one = 3 * b1 + one
        if bet2.lower() in ['yellow']:
            two = 3 * b2 + two
        if bet3.lower() in ['yellow']:
            three = 3 * b3 + three
        if bet4.lower() in ['yellow']:
            four = 3 * b4 + four
    if j:
        if bet1.lower() in ['purple']:
            one = 3 * b1 + one
        if bet2.lower() in ['purple']:
            two = 3 * b2 + two
        if bet3.lower() in ['purple']:
            three = 3 * b3 + three
        if bet4.lower() in ['purple']:
            four = 3 * b4 + four
    if k:
        if bet1.lower() in ['brown']:
            one = 3 * b1 + one
        if bet2.lower() in ['brown']:
            two = 3 * b2 + two
        if bet3.lower() in ['brown']:
            three = 3 * b3 + three
        if bet4.lower() in ['brown']:
            four = 3 * b4 +four
    if a1:
        if bet1.lower() in ['red']:
            one = 2 * b1 + one
        if bet2.lower() in ['red']:
            two = 2 * b2 + two
        if bet3.lower() in ['red']:
            three = 2 * b3 + three
        if bet4.lower() in ['red']:
            four = 2 * b4 + four
    if s1:
        if bet1.lower() in ['green']:
            one = 2 * b1 + one
        if bet2.lower() in ['green']:
            two = 2 * b2 + two
        if bet3.lower() in ['green']:
            three = 2 * b3 + three
        if bet4.lower() in ['green']:
            four = 2 * b4 + four
    if d1:
        if bet1.lower() in ['pink']:
            one = 2 * b1 + one
        if bet2.lower() in ['pink']:
            two = 2 * b2 + two
        if bet3.lower() in ['pink']:
            three = 2 * b3 + three
        if bet4.lower() in ['pink']:
            four = 2 * b4 + four
    if f1:
        if bet1.lower() in ['blue']:
            one = 2 * b1 + one
        if bet2.lower() in ['blue']:
            two = 2 * b2 + two
        if bet3.lower() in ['blue']:
            three = 2 * b3 + three
        if bet4.lower() in ['blue']:
            four = 2 * b4 + four
    if g1:
        if bet1.lower() in ['orange']:
            one = 2 * b1 + one
        if bet2.lower() in ['orange']:
            two = 2 * b2 +two
        if bet3.lower() in ['orange']:
            three = 2 * b3 + three
        if bet4.lower() in ['orange']:
            four = 2 * b4 + four
    if h1:
        if bet1.lower() in ['yellow']:
            one = 2 * b1 + one
        if bet2.lower() in ['yellow']:
            two = 2 * b2 + two
        if bet3.lower() in ['yellow']:
            three = 2 * b3 + three
        if bet4.lower() in ['yellow']:
            four = 2 * b4 + four
    if j1:
        if bet1.lower() in ['purple']:
            one = 2 * b1 + one
        if bet2.lower() in ['purple']:
            two = 2 * b2 + two
        if bet3.lower() in ['purple']:
            three = 2 * b3 + three
        if bet4.lower() in ['purple']:
            four = 2 * b4 + four
    if k1:
        if bet1.lower() in ['brown']:
            one = 2 * b1 + one
        if bet2.lower() in ['brown']:
            two = 2 * b2 + two
        if bet3.lower() in ['brown']:
            three = 2 * b3 + three
        if bet4.lower() in ['brown']:
            four = 2 * b4 + four
    if a2:
        if bet1.lower() in ['red']:
            one = one + b1
        if bet2.lower() in ['red']:
            two = two + b2
        if bet3.lower() in ['red']:
            three = three + b3
        if bet4.lower() in ['red']:
            four = four + b4
    if s2:
        if bet1.lower() in ['green']:
            one = one + b1
        if bet2.lower() in ['green']:
            two = two + b2
        if bet3.lower() in ['green']:
            three = three + b3
        if bet4.lower() in ['green']:
            four = four + b4
    if d2:
        if bet1.lower() in ['pink']:
            one = one + b1
        if bet2.lower() in ['pink']:
            two = two + b2
        if bet3.lower() in ['pink']:
            three = three + b3
        if bet4.lower() in ['pink']:
            four = four + b4
    if f2:
        if bet1.lower() in ['blue']:
            one = one + b1
        if bet2.lower() in ['blue']:
            two = two + b2
        if bet3.lower() in ['blue']:
            three = three + b3
        if bet4.lower() in ['blue']:
            four = four + b4
    if g2:
        if bet1.lower() in ['orange']:
            one = one + b1
        if bet2.lower() in ['orange']:
            two = two + b2
        if bet3.lower() in ['orange']:
            three = three + b3
        if bet4.lower() in ['orange']:
            four = four + b4
    if h2:
        if bet1.lower() in ['yellow']:
            one = one + b1
        if bet2.lower() in ['yellow']:
            two = two + b2
        if bet3.lower() in ['yellow']:
            three = three + b3
        if bet4.lower() in ['yellow']:
            four = four + b4
    if j2:
        if bet1.lower() in ['purple']:
            one = one + b1
        if bet2.lower() in ['purple']:
            two = two + b2
        if bet3.lower() in ['purple']:
            three = three + b3
        if bet4.lower() in ['purple']:
            four = four + b4
    if k2:
        if bet1.lower() in ['brown']:
            one = one + b1
        if bet2.lower() in ['brown']:
            two = two + b2
        if bet3.lower() in ['brown']:
            three = three + b3
        if bet4.lower() in ['brown']:
            four = four + b4

    score1.clear()
    score1.write(one,False,"center", ("Arial",10,"normal"))
    score2.clear()
    score2.write(two,False,"center", ("Arial",10,"normal"))
    score3.clear()
    score3.write(three,False,"center", ("Arial",10,"normal"))
    score4.clear()
    score4.write(four,False,"center", ("Arial",10,"normal"))

writer.clear()
writer2.clear()
writer3.clear()
for i in (t1,t2,t3,t4,t5,t6,t7,t8,Line):
    i.ht()
    i.clear()
writer.color("black")
if one > two and one>three and one>four:
            writer.write(player1 + " Wins",False,"center", ("Arial",100,"normal"))
if two > one and two>three and two>four:
            writer.write(player2 + " Wins",False,"center", ("Arial",100,"normal"))
if three > two and three>one and three>four:
            writer.write(player3 + " Wins",False,"center", ("Arial",100,"normal"))
if four > two and four>three and four>one:
            writer.write(player1 + " Wins",False,"center", ("Arial",100,"normal"))
if one == two and one > three and one > four:
    writer.write(player1 + " and " + player2 + " Win",False,"center", ("Arial",100,"normal"))
if one == three and one != two and one != four:
    writer.write(player1 + " and " + player3 + " Win", False, "center", ("Arial", 100, "normal"))
if one == four and one > three and one >= two:
    writer.write(player1 + " and " + player4 + " Win",False,"center", ("Arial",100,"normal"))
if three == two and three > one and three > four:
    writer.write(player2 + " and " + player3 + " Win",False,"center", ("Arial",100,"normal"))
if two == four and two > three and two > one:
    writer.write(player2 + " and " + player4 + " Win", False, "center", ("Arial", 100, "normal"))
if three == four and three > one and three > two:
    writer.write(player3 + " and " + player4 + " Win",False,"center", ("Arial",100,"normal"))
if one == three and one == four and one > two:
    writer.write(player1 + ", "+ player3 + ",and " + player4 + " Win",False,"center", ("Arial",100,"normal"))
if one == two and one == four and one > three:
    writer.write(player1 + ", "+ player2 + ",and " + player4 + " Win",False,"center", ("Arial",100,"normal"))
if two == three and two == four and two > one:
    writer.write(player2 + ", "+ player3 + ",and " + player4 + " Win",False,"center", ("Arial",100,"normal"))
if one == three and one == two and one > four:
    writer.write(player1 + ", "+ player2 + ",and " + player3 + " Win",False,"center", ("Arial",100,"normal"))
if one == three and one == four and one == two:
    writer.write("Draw",False,"center", ("Arial",100,"normal"))

wn.exitonclick()
