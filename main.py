import os

#os.system(r'cd C:\Projects\litle_things\bin')
#from play import*
#
#
#lvl='''
#00101
#10011
#10201
#00001
#11111
#'''
#lvl=lvl.replace('\n','')
#for i in range(5):
#    for j in range(5):
#        if lvl[5*i+j]=='0':
#            new_circle(x=100*j,y=-100*i,radius=20)
#        elif lvl[5*i+j]=='1':
#            new_circle(x=100*j,y=-100*i,radius=20,color='red')
#        elif lvl[5*i+j]=='2':
#            new_circle(x=100*j,y=-100*i,radius=20,color='green')
#
#
#start_program()

def array_diff(a, b):
    q=[]
    for i in range(len(a)):
        if a[i] not in b:
            q.append(a[i])
    return q

#print('apples, pears # and bananas\ngrapes\nbananas !apples')

q='apples, pears # and bananas\ngrapes\nbananas !apples'
print(q[2:4])