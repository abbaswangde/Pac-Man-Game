from random import choice
from turtle import *
from freegames import floor, vector
import turtle


def main(score1):
    #The Main loop for introduction and about page.
    #The Indroduction page.
    speed(0)
    bgcolor("black")
    title("Pacman Game")
    #bgpic("pacman.png")
    screen = turtle.Screen()
    screen.title("Pacman Game")
    screen.bgcolor("black")
    title_turtle = turtle.Turtle()
    title_turtle.speed(0)
    title_turtle.color("white")
    title_turtle.penup()
    title_turtle.goto(0, screen.window_height() // 2 - 50)  # Adjust the y-coordinate as needed
    title_turtle.write("Pacman Game", align="center", font=("Arial", 24, "bold"))
    title_turtle.hideturtle()
    
    color("white")
    up()
    goto(570.0,-327.0)
    down()
    style = ('calibri light', 30, 'bold')
    write("START",font=style,align='center')
    hideturtle()

    up()
    goto(-570.0,-327.0)
    down()
    write("ABOUT",font=style,align='center')
    
    def cor(a,b):
        #The onscreenclick fuction
        def no(x,y):

            q=0
            if x>-680.0 and x<671.0 and y<354.0 and y>-340.0:
                q+=1
                
        if a<-480.0 and a>-620.0 and b<-280.0 and b>-330.0:
            reset()
            onscreenclick(no,1)
            def bck(a,b):

                if a<-480.0 and a>-620.0 and b<-280.0 and b>-330.0:
                    reset()
                    clear()
                    main()
                    
                if a>480.0 and a<620.0 and b<-280.0 and b>-330.0:
                    reset()
                    bgcolor("black")
                    #bgpic("pacman.png")

                    state = {'score': 0}
                    path = Turtle(visible=False)
                    writer = Turtle(visible=False)
                    aim = vector(5, 0)
                    pacman = vector(0, -80)#Location of Pacman.
                    ghosts = [
                        [vector(-180, 160), vector(5, 0)],#Locations of Ghosts.
                        [vector(-200, -260), vector(0, 5)],
                        [vector(100, 160), vector(0, -5)],
                        [vector(160, -240), vector(-5, 0)],
                    ]

                    tiles = [
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,#Map for the pacman and ghosts to go
                        1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,#The zero'0' is blocked and one'1' is allowed for Pacman and ghosts to go.
                        1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0,
                        1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0,
                        1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0,
                        1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,
                        1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0,
                        1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0,
                        1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0,
                        1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0,
                        0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0,
                        1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
                        1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0,
                        1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0,
                        0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0,
                        1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,
                        1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
                        1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
                        1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
                        1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0,
                        1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0,
                        1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0,
                        1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0,
                        1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0,
                        1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    ]

                    def square(x, y):
                        #To Draw square using path at (x, y).
                        path.up()
                        path.goto(x, y)
                        path.down()
                        path.begin_fill()

                        for count in range(4):
                            path.forward(20)
                            path.left(90)

                        path.end_fill()

                    def offset(point):
                        #To Return offset of point in tiles.
                        x = (floor(point.x, 20) + 200) / 20
                        y = (180 - floor(point.y, 20)) / 20
                        index = int(x + y * 20)
                        return index

                    def valid(point):
                        #To Return True if point is valid in tiles.
                        index = offset(point)

                        if tiles[index] == 0:
                            return False

                        index = offset(point + 19)

                        if tiles[index] == 0:
                            return False

                        return point.x % 20 == 0 or point.y % 20 == 0

                    def world():
                        #To Draw world using path.
                        bgcolor('black')
                        path.color('blue')

                        for index in range(len(tiles)):
                            tile = tiles[index]

                            if tile > 0:
                                x = (index % 20) * 20 - 200
                                y = 180 - (index // 20) * 20
                                square(x, y)

                                if tile == 1:
                                    path.up()
                                    path.goto(x + 10, y + 10)
                                    path.dot(5, 'yellow')

                    def move():
                        #To Move pacman and all ghosts.
                        writer.undo()
                        writer.write(state['score'])

                        clear()

                        if valid(pacman + aim):
                            pacman.move(aim)

                        index = offset(pacman)

                        if tiles[index] == 1:
                            tiles[index] = 2
                            state['score'] += 1
                            x = (index % 20) * 20 - 200
                            y = 180 - (index // 20) * 20
                            square(x, y)

                        up()
                        goto(pacman.x + 10, pacman.y + 10)
                        dot(20, 'yellow')

                        for point, course in ghosts:
                            if valid(point + course):
                                point.move(course)
                            else:
                                options = [
                                    vector(5, 0),
                                    vector(-5, 0),
                                    vector(0, 5),
                                    vector(0, -5),
                                ]
                                plan = choice(options)
                                course.x = plan.x
                                course.y = plan.y
                                
                            up()
                            goto(point.x + 10, point.y + 10)
                            dot(20, "red")

                        update()

                        for point, course in ghosts:
                            if abs(pacman - point) < 20:
                                return

                        ontimer(move, 100)

                    def change(x, y):
                        #To Change pacman aim if valid.
                        if valid(pacman + vector(x, y)):
                            aim.x = x
                            aim.y = y

                    setup(420, 420, 370, 0)
                    hideturtle()
                    tracer(False)
                    writer.goto(200, 160)
                    writer.color('white')
                    writer.write(state['score'])
                    score1.append(state['score'])
                    listen()

                    #To change the direction of Pacman.
                    onkey(lambda: change(5, 0), 'Right')
                    onkey(lambda: change(-5, 0), 'Left')
                    onkey(lambda: change(0, 5), 'Up')
                    onkey(lambda: change(0, -5), 'Down')
                    world()
                    move()

                    def co(a,b):
                        q=0
                        if a>4540.0 and a<5580.0 and b<-1930.0 and b>-2850.0:
                            q+=1
                    
                    onscreenclick(co,1)

            onscreenclick(bck,1)

            #The about page.
            bgcolor("black")
            #bgpic("pacman.png")
            speed(0)
            
            color("white")
            up()
            goto(570.0,-327.0)
            down()
            write("START",font=style,align='center')
            hideturtle()

            up()
            goto(-10.0 ,150.0)
            down()
            style0 = ('calibri light', 32, 'bold')
            write("Python Project",font=style0,align='center')

            up()
            goto(-350.0, 70.0)
            down()
            style1 = ('calibri light', 29)
            write("This Python Project was done by:",font=style1,align='center')

            up()
            goto(-575.0, -40.0)
            down()
            style2 = ('calibri', 22)
            write("1. Muhammad Abbas Wangde\n2. Muhib Ahmed\n3. Mohammed Faraz",font=style2)

            up()
            goto(0, -40.0)
            down()
            write("Class XII-D\nClass XII-D\nClass XII-D",font=style2)

            up()
            goto(-545.0, -110.0)
            down()
            write("Controls",font=style1,align='center')

            up()
            goto(-575.0, -258.0)
            down()
            write("The controls of this PACMAN game are UP, DOWN, LEFT, RIGHT.\nTo play this PACMAN game properly you have to press the keys not once but continuously.\nThere is only one LIFE in this game.\nTHANK YOU",font=style2)
            
            up()
            goto(-570.0,-327.0)
            down()
            write("BACK",font=style,align='center')
            hideturtle()
            
        if a>480.0 and a<620.0 and b<-280.0 and b>-330.0:
            reset()
            bgcolor("black")
            #bgpic("pacman.png")

            state = {'score': 0}
            path = Turtle(visible=False)
            writer = Turtle(visible=False)
            aim = vector(5, 0)
            pacman = vector(0, -80)#Location of Pacman.
            ghosts = [
                [vector(-180, 160), vector(5, 0)],#Locations of Ghosts.
                [vector(-200, -260), vector(0, 5)],
                [vector(100, 160), vector(0, -5)],
                [vector(160, -240), vector(-5, 0)],
            ]

            tiles = [
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,#Map for the pacman and ghosts to go
                1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,#The zero'0' is blocked and one'1' is allowed for Pacman and ghosts to go.
                1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0,
                1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0,
                1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0,
                1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,
                1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0,
                1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0,
                1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0,
                1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0,
                0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0,
                1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
                1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0,
                1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0,
                0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0,
                1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,
                1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
                1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
                1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
                1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0,
                1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0,
                1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0,
                1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0,
                1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            ]

            def square(x, y):
                #To Draw square using path at (x, y).
                path.up()
                path.goto(x, y)
                path.down()
                path.begin_fill()

                for count in range(4):
                    path.forward(20)
                    path.left(90)

                path.end_fill()

            def offset(point):
                #To Return offset of point in tiles.
                x = (floor(point.x, 20) + 200) / 20
                y = (180 - floor(point.y, 20)) / 20
                index = int(x + y * 20)
                return index
            def valid(point):
                #To Return True if point is valid in tiles.
                index = offset(point)

                if tiles[index] == 0:
                    return False

                index = offset(point + 19)

                if tiles[index] == 0:
                    return False

                return point.x % 20 == 0 or point.y % 20 == 0

            def world():
                #To Draw world using path.
                bgcolor('black')
                path.color('blue')

                for index in range(len(tiles)):
                    tile = tiles[index]

                    if tile > 0:
                        x = (index % 20) * 20 - 200
                        y = 180 - (index // 20) * 20
                        square(x, y)

                        if tile == 1:
                            path.up()
                            path.goto(x + 10, y + 10)
                            path.dot(5, 'yellow')

            def move():
                #To Move pacman and all ghosts.
                writer.undo()
                writer.write(state['score'])

                clear()

                if valid(pacman + aim):
                    pacman.move(aim)

                index = offset(pacman)

                if tiles[index] == 1:
                    tiles[index] = 2
                    state['score'] += 1
                    score1.append(state['score'])
                    x = (index % 20) * 20 - 200
                    y = 180 - (index // 20) * 20
                    square(x, y)

                up()
                goto(pacman.x + 10, pacman.y + 10)
                dot(20, 'yellow')

                for point, course in ghosts:
                    if valid(point + course):
                        point.move(course)
                    else:
                        options = [
                            vector(5, 0),
                            vector(-5, 0),
                            vector(0, 5),
                            vector(0, -5),
                        ]
                        plan = choice(options)
                        course.x = plan.x
                        course.y = plan.y
                        
                    up()
                    goto(point.x + 10, point.y + 10)
                    dot(20, "red")

                update()


                for point, course in ghosts:
                    if abs(pacman - point) < 20:
                        return

                ontimer(move, 100)


            def change(x, y):
                #To Change pacman aim if valid.
                if valid(pacman + vector(x, y)):
                    aim.x = x
                    aim.y = y

            setup(420, 420, 370, 0)
            hideturtle()
            tracer(False)
            writer.goto(200, 160)
            writer.color('white')
            writer.write(state['score'])
            listen()

            #To change the direction of Pacman.
            onkey(lambda: change(5, 0), 'Right')
            onkey(lambda: change(-5, 0), 'Left')
            onkey(lambda: change(0, 5), 'Up')
            onkey(lambda: change(0, -5), 'Down')
            world()
            move()


            def co(a,b):
                q=0
                if a>4540.0 and a<5580.0 and b<-1930.0 and b>-2850.0:
                    q+=1

            
            onscreenclick(co,1)

    onscreenclick(cor,1)


s = []
main(s)
done()
print("Your score is = ",s[len(s)-1])
print("Thank You for Playing")








