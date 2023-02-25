from play import *
# 1 квадрат 2 круг 3 черный круг 4 черный квадрат
lvl='''
1112211334443412
1121321234132431
3213242132412343
3214213243121311
3243241324321324
2313214132342314
1121321234132431
3213242132412343
3214213243121311
'''

w = 1920//16
h = 1080//9
xx =-(1920//2)
yy = (1080//2)+0.5*h
for i in lvl:
    if i=='1':
        s1=new_box('cyan',xx,yy,w,h)
    elif i=='2':
        s2=new_circle('orange',xx,yy,w//2)
    elif i=='3':
        s2=new_circle('black',xx,yy,w//2)
    elif i=='4':
        s2=new_box('black',xx,yy,w,h)
    else:
        yy-=h
        xx =-(1920//2)-0.5*w
    xx+=w

start_program()
    