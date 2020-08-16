import turtle
import math
import random

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
arr=[]
temp=0


def init():
    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                               WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    turtle.up()
    turtle.title('Name')
    turtle.pen()
    turtle.down()

SIDES = 50
def drawTree():
    turtle.left(90)
    turtle.down()
    choice = random.randint(0, 1)
    if choice == 0:
        s2 = random.randint(50, 150)
        turtle.forward(s2)
        turtle.right(90)
        turtle.circle(50)
        turtle.left(90)
        turtle.back(s2)
        turtle.right(90)
        turtle.up()
        turtle.forward(100)
        arr.append(s2)
    else:
        s1 = random.randint(50, 200)
        turtle.forward(s1)
        turtle.right(90)
        turtle.forward(SIDES / 2)
        s = random.randint(3, 4)
        for y in range(0, s - 1):
            turtle.left(360 / s)
            turtle.forward(SIDES)
        turtle.left(360 / s)
        turtle.forward(SIDES / 2)
        turtle.left(90)
        turtle.back(s1)
        turtle.right(90)
        turtle.up()
        turtle.forward(100)
        arr.append(s1)
def drawHouse():
    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(50 * math.sqrt(2))
    turtle.right(90)
    turtle.forward(50 * math.sqrt(2))
    turtle.right(45)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(180)
    turtle.up()
    turtle.forward(200)
    arr.append(0)
    arr.append(0)

def drawStar():
    turtle.back(100)
    turtle.left(90)
    turtle.forward(300)
    turtle.down()
    turtle.forward(25)
    turtle.back(50)
    turtle.forward(25)
    for x in range(0, 3):
        turtle.right(45)
        turtle.forward(25)
        turtle.back(50)
        turtle.forward(25)
    turtle.left(135)
    turtle.up()
    turtle.back(300)
    turtle.right(90)
    turtle.forward(100)
    turtle.done()


def main():
    t = turtle.Turtle()
    init()
    turtle.speed(5)
    temp = 0
    hp = input('How many trees in your forest?')
    demandNum = int(hp)
    num = random.randint(1, demandNum)

    for z in range(0, num):
         drawTree()

    drawHouse()
    for w in range(0, demandNum - num):
         drawTree()
    n = len(arr)
    for i in range(0,n):
        if arr[i]>temp:
            temp=arr[i]
    for k in range(0,n):
        if arr[k]==temp:
            print (arr.index(arr[k]))

    drawStar()


if __name__ == "__main__":
    main()
