#import matplotlib.pyplot as plt
#import numpy as np
#
#
#x = np.arange(-10, 10, 0.01)
#y = abs(x+3)
#fig, ax = plt.subplots()
#ax.plot(x, y)
#ax.grid()
#
#plt.show()
a= input()
try:
    a=int(a)
except:
    a='Ты ввел не число'
print(a)