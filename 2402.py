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

cube(100,70)
#cube(200,60)
exitonclick()