from turtle import *
from random import randrange
from freegames import square, vector

#define la posicion inicial de la comida
food = vector(0, 0)
#define la posicion inicial de la serpiente
snake = [vector(10, 0)]
aim = vector(0, -10)

#Define colores, x=cuerpo z=comida
colors  = {1:'pink',2:'yellow',3:'blue',4:'orange',5:'purple'}
x = randrange(1, 6)
z = randrange(1, 6)

#define un cambio en x,y
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        if x in colors:
            y = colors [x]
        square(body.x, body.y, 9, y)

    if z in colors:
        w = colors [z]
    square(food.x, food.y, 9, w)
    update()
    ontimer(move, 100)
    
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
