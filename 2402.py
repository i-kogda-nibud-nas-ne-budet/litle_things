from turtle import*
speed(0)
def cube(lenght,angle):
    for i in range(5):
      forward(lenght)
      left(90)
    right(angle)
    forward(lenght//2)
    left(angle)
    forward(lenght)
    left((90-angle)+90)
    forward(lenght//2)
    left(180)
    forward(lenght//2)
    left(90+angle)
    forward(lenght)
    left(90-angle)
    forward(lenght//2)
    goto(0,0)
    left(90+angle)

#width(5)
#color('cyan')
#cube(200,80)
#color('red')
#cube(200,70)
#color('orange')
#cube(200,60)

def square(lenght,my_color):
    begin_fill()
    color(my_color)
    for i in range(4):
      forward(lenght)
      left(90)
    end_fill()

square(20,'red')
forward(20)
square(20,'cyan')

exitonclick()