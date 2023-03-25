a1=3
b1=1.9
c1=2.4

a2=5
b2=0.42
c2=-0.96

left = str(round(a1*b1,3))+'x +' + str(round(a1*c1,3))
right = str(round(a2*b2,3))+'x +' + str(round(a2*c2,3))
print(left+' = '+right)

perem = str(round(a1*b1-a2*b2,3))+'x = -' + str(round(a1*c1-a2*c2,3))
print(perem)
x= round((-1)*(a1*c1-a2*c2)/(a1*b1-a2*b2),3)
print('x = ',x)