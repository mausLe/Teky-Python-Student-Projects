import turtle
import time
import random
import winsound

# Đôi khi, trình phiên dịch python không thể mở những file hình ảnh 
# trong thư mục hiện tại
# Ta cần thêm thư viện os, sys để điều chỉnh đường dẫn thực thi
import os, sys
os.chdir(os.path.dirname(sys.argv[0]))

background = "bg.gif"
apale = "yApple.gif"
musrom = "mushroom.gif"
# Chuyển động của snake
def move():
   
    if head.direction == "up":
        y = head.ycor() #y coordinate of the turtle
        head.sety(y + 20)
 
    if head.direction == "down":
        y = head.ycor() #y coordinate of the turtle
        head.sety(y - 20)
 
    if head.direction == "right":
        x = head.xcor() #y coordinate of the turtle
        head.setx(x + 20)
 
    if head.direction == "left":
        x = head.xcor() #y coordinate of the turtle
        head.setx(x - 20)

# Sử dụng phím điều khiển snake
def go_up():
    if head.direction != "down":
        head.direction = "up"
 
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
 
def go_left():
    if head.direction != "right":
        head.direction = "left"


#set up the screen
win = turtle.Screen()
win.title("Snake game")
win.bgpic(background)
win.setup(width=600,height=600)
win.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("cyan")
head.penup()
head.goto(0, 100)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
win.addshape(apale)
food.shape(apale)
food.penup()
food.shapesize(1, 1)
food.goto(0, 0)

#Score
# score
score = 0
high_score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

#Mushroom
mush = turtle.Turtle()
mush.speed(0)
win.addshape(musrom)
mush.shape(musrom)
mush.penup()
mush.shapesize(1, 1)
mush.goto(0, 0)
#pen.write("Score: 0 High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal"))

# Điều khiển snake
win.onkey(go_up, "w")
win.onkey(go_down, "s") 
win.onkey(go_right, "d")
win.onkey(go_left, "a")
win.listen()

# Tạo thân snake
tailing = []

while True:
    # Cập nhật điểm số
    win.update()
    pen.clear()
    pen.write("Score: {} High Score: {}".format(score,high_score), align="center", font=("Courier", 30, "normal"))
    
    for tail in tailing:
        if tail.distance(head) < 20:
            # time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for tail in tailing:
                tail.goto(2000, 2000)
            tailing = []
            
            score = 0
            tail.clear()

    
    # Kiểm tra các điều kiện khi snake di
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        head.goto(0, 0)
        head.direction = "stop"   
        for tail in tailing:
           tail.setposition(2000, 2000)
                
        tailing = []
        
        
        tail.clear()
        score = 0

    x=random.randint(-250,250)
    y=random.randint(-250,250)
    e=random.randint(-250,250)
    q=random.randint(-250,250)
    # Tăng điểm nếu khoảng cách snake và táo < 10
    if  head.distance(food) <20:
        food.goto(x,y)
        score=score+10
        food.setposition(x,y)
       
        tail=turtle.Turtle()
        tail.speed(0)
        tail.shape("square")
        tail.color("blue")
        tail.penup()
        tailing.append(tail)
    
    if score > high_score:
        high_score = score
    if len(tailing) > 0:
       x1 = head.xcor()
       y1 = head.ycor()
       tailing[0].goto(x1,y1)
     
    for i in range(len(tailing) - 1, 0, -1):
        x2 = tailing[i - 1].xcor()
        y2 = tailing[i - 1].ycor()

        tailing[i].setposition(x2, y2)
    # Trừ điểm nếu khoảng cách snake và Nấm độc < 10
    if head.distance(mush) <20:
        mush.goto(e,q)
        score=score-10
        mush.setposition(e,q)
        
        snakeTail = len(tailing) - 1
        tailing[snakeTail].goto(2000, 2000)
        del tailing[snakeTail]
            
    move()  
    time.sleep(0.1)
