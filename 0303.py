from turtle import*
image='''
01010101
10101010
01010101
10101010
01010101
10101010
01010101
10101010'''
def pixel(lenght,my_color):
  sq(lenght,my_color)
  forward(lenght)
def sq(lenght,my_color):
  begin_fill()
  color(my_color)
  for i in range(4):
    forward(lenght)
    left(90)
  end_fill()
speed(0)
amount_string=0
for i in image:
  if i=='0':
    pixel(20,'black')
  if i=='1':
    pixel(20,'cyan')
  if i=='\n':
    amount_string+=1
    goto(0,amount_string*(-20))

exitonclick()