fibs=[1,1]
j=0
for i in range(2,20+1):
    j+=1
    fibs.append(fibs[i-1]+fibs[i-2])
print(fibs)
print(j)

#i=0
#def fibo(n):
#    global i
#    i=i+1
#    print('Я вызываю рекурсию от ', n)
#    if n<=1:
#        return 1
#    else:
#        return fibo(n-1)+fibo(n-2)
#print(fibo(20))
#print(i)

#def factorial(n):
#
#    print('Я вызываю рекурсию от ', n)
#    if n==1:
#        return 1
#    else:
#        return n*factorial(n-1)
#print(factorial(10))