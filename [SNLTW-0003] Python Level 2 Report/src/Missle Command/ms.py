import turtle
import math
import random
import os, sys

import winsound

os.chdir(os.path.dirname(sys.argv[0]))

screen=turtle.Screen()
screen.bgpic("bg.gif")
screen.setup(1200,700)


# Đăng ký hình ảnh ironman.gif
turtle.register_shape('ironman.gif')

# TODO
# Đăng ký hình ảnh spaceship.gif
# Đăng ký hình ảnh bullet.gif
# 2 dòng code
turtle.register_shape('spaceship.gif')
turtle.register_shape('bullet.gif')

mouse = turtle.Turtle()
mouse.speed(0)
mouse.penup()
mouse.shape("circle")
mouse.color("green")
mouse.right(90)

# Viết cho bullet
# Khởi tạo bullet
bullet = turtle.Turtle()
bullet.speed(0)
bullet.penup()
bullet.shape('bullet.gif')
bullet.hideturtle()
bullet.left(90)
state='ready'

# Make the Tkinter object
scrTKobj = screen.getcanvas()


def func(event):
    print(event.x-600, (event.y*-1)+350)
    mouse.setposition(event.x-600, (event.y*-1)+350)
    # global pointerX, pointerY
    # pointerX = event.x
    # pointerY = event.y

    # return (event.x, event.y)

scrTKobj.bind('<Motion>', func)


point = 0
spaceship = turtle.Turtle()
spaceship.speed(0)
spaceship.penup()
spaceship.shape('spaceship.gif')
spaceship.goto(-450,270)

def spaceship_move():
    # TODO
    # Di chuyển forward 20 pixel
    spaceship.forward(20)

    # Nếu vị trí x của spaceship (xcor) > 450 hoặc vị trí x của spaceship < -450
    # spaceship xoay trái 180 độ
    # Thay đổi vị trí y thành spaceship.ycor() - 30 (dùng hàm sety)]
    if spaceship.xcor() > 450 or spaceship.xcor() < -450:
        spaceship.left(180)
        x = spaceship.xcor()
        y = spaceship.ycor() - 30
        spaceship.goto(x, y)
    #### 4 dòng code
    
    turtle.ontimer(spaceship_move,t=40)

spaceship_move()

chooseMissle = 2

player1 = turtle.Turtle()
player1.speed(0)
player1.penup()
player1.shape('ironman.gif')
player1.goto(-400,-270) 


player2 = turtle.Turtle()
player2.speed(0)
player2.penup()
player2.shape('ironman.gif')
player2.goto(0,-270) 

player3 = turtle.Turtle()
player3.speed(0)
player3.penup()
player3.shape('ironman.gif')
player3.goto(400,-270) 

dirTurtle = turtle.Turtle()
dirTurtle.speed(0)
dirTurtle.penup()
dirTurtle.hideturtle()

def right():
    # TODO
    # di chuyển người chơi theo hướng tương ứng
    # 3 dòng code
    x = player1.xcor()
    y = player1.ycor()
    bullet.setposition(0, 0)
    bullet.showturtle()
    player1.goto(x + 40, y)

def left():
    # TODO
    # di chuyển người chơi theo hướng tương ứng
    # 3 dòng code
    x = player1.xcor()
    y = player1.ycor()
    bullet.setposition(0, 0)
    bullet.showturtle()
    player1.goto(x - 40, y)  

def start_fire():
    global state
    bullet.showturtle()

    fire_angle = 90


    if chooseMissle == 1:
        bullet.goto(player1.xcor(),player1.ycor())
        fire_angle = angle(mouse.xcor() - player1.xcor(), mouse.ycor() - player1.ycor())

    elif chooseMissle == 2:
        bullet.goto(player2.xcor(),player2.ycor())
        fire_angle = angle(mouse.xcor() - player2.xcor(), mouse.ycor() - player2.ycor())

    else:
        bullet.goto(player3.xcor(),player3.ycor())
        fire_angle = angle(mouse.xcor() - player3.xcor(), mouse.ycor() - player3.ycor())

    bullet.setheading(fire_angle)

    state='fire'
    winsound.PlaySound("laser.wav", winsound.SND_ASYNC)

    fire()

def fire():
    global state, point
    if (bullet.ycor()>350): # Kiểm tra đạn ra khỏi màn hình
        state = 'ready'
    
    if distance(bullet,spaceship)<70: # Kiểm tra khoảng cách tới đối phương
        score_player.clear()
        winsound.PlaySound("Explosion.wav", winsound.SND_ASYNC)
        point += 1 
        score_player.write('Player:'+str(point),align = 'left',font=('Arial',20,'bold'))
        state = 'ready'

        bullet.hideturtle()
        spaceship.goto(-450,200)
        screen.update()

    if state == 'fire':
        bullet.showturtle()
        # x=bullet.xcor()
        # y=bullet.ycor()+30
        # bullet.goto(x,y)
        bullet.forward(30)
        turtle.ontimer(fire,t=30)

def changeMissleA():
    global chooseMissle
    chooseMissle = 1
    print("Change to missle 1")
    mouse.color("red")

def changeMissleB():
    global chooseMissle
    chooseMissle = 2
    print("Change to missle 2")
    mouse.color("green")

def changeMissleC():
    global chooseMissle
    chooseMissle = 3
    print("Change to missle 3")
    mouse.color("blue")

turtle.onkeypress(changeMissleA, 'a')
turtle.onkeypress(changeMissleB, 's')
turtle.onkeypress(changeMissleC, 'd')

turtle.listen()

def distance(a,b):
    # TODO
    # tính khóa cách giữa 2 đối tượng a và b
    # 1 dòng code. Google thư viện turtle và tham khảo thuộc tính distance

    kc = a.distance(b)
    return kc

def angle(x, y):
    mult = x
    norm = math.sqrt(x**2 + y**2)

    angle = round(math.acos(mult/norm)*180/math.pi)
    print("ANGLE: ", angle)

    return (angle)



screen.tracer(0)


score_player = turtle.Turtle()
score_player.speed(0)
score_player.color("white")
score_player.penup()
score_player.goto(-550, 300)
scorestring = "Player: 0"
score_player.write(scorestring, False, align="left", font=("Arial", 20, "bold"))
score_player.hideturtle()

# TODO: Sử dụng hàm onkeypress() và listen() để bắt sự kiện nhấn nút điều khiển
# có thể dùng w/a/s/d hoặc các phím mũi tên
# nhớ kiểm tra ký tự khi dùng bộ gõ telex nha
# vi w = ư, aa = â, dd = đ

turtle.onkeypress(right, "Right")
turtle.onkeypress(left, "Left")

turtle.onkeypress(start_fire, "space")

turtle.listen()

screen.tracer(0)
while True:

    # print("pointer pos: ", (e[0], e[1]))
    screen.update()

