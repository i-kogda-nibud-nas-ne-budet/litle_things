import numpy as np
lvl='''
0000001100000011
2011000000110000
1111111111111100
0000000000000000
0000000000000000
1111100000011111
1000000000000001
1001144433311001
1000000000000001
'''
# если стена только слева то L
# если стена только справа то R
# если стена только сверху то U
# если стена только снизу то D
lvl=lvl.split('\n')[1:-1]
for i in range(len(lvl)):
    lvl[i]=list(lvl[i])
arr=np.array(lvl)
print(arr)
print('*****************')
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] =='1' and 1<j<len(arr[i])-1:
            if arr[i][j+1] == '1' and  arr[i][j-1] != '1' and  arr[i][j-1] != 'R':
                arr[i][j]='R'
            if (arr[i][j-1] == '1' or arr[i][j-1] == 'R') and  arr[i][j+1] != '1' and  arr[i][j+1] != 'R':
                arr[i][j]='L'
print(arr)