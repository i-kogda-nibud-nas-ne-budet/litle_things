dino='''
00000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000011111111111111111111110000000000000
00000000000000000000000000000000000011111111111111111111111111110000000000
00000000000000000000000000000000000011111101111111111111111111110000000000
00000000000000000000000000000000000011111111111111111111111111110000000000
00000000000000000000000000000000000011111111111111111111111111110000000000
00000000000000000000000000000000000011111111111111111111111111110000000000
00000000000000000000000000000000000011111111111111111111111111110000000000
00000000000000000000000000000000000011111111111111111111111111110000000000
00000000000000000000000000000000000011111111111111111111110000000000000000
00000000000000000000000000000000000011111111111111111111110000000000000000
00000000111000000000000000000000011111111111111000000000000000000000000000
00000000111000000000000000000111111111111111111000000000000000000000000000
00000000111111000000000001111111111111111111111111111000000000000000000000
00000000111111110000000101111111111111111111111111111000000000000000000000
00000000111111111000001111111111111111111111111000111000000000000000000000
00000000111111111111111111111111111111111111111000000000000000000000000000
00000000111111111111111111111111111111111111111000000000000000000000000000
00000000111111111111111111111111111111111111111000000000000000000000000000
00000000000111111111111111111111111111111111111000000000000000000000000000
00000000000000111111111111111111111111111111000000000000000000000000000000
00000000000000111111111111111111111111111111000000000000000000000000000000
00000000000000000111111111111111111111111100000000000000000000000000000000
00000000000000000000111111111111111111100000000000000000000000000000000000
00000000000000000000001111111110011111100000000000000000000000000000000000
00000000000000000000001111110000001011100000000000000000000000000000000000
00000000000000000000001111110000000011100000000000000000000000000000000000
00000000000000000000001111110000000011111100000000000000000000000000000000
00000000000000000000001111110000000011111100000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000
'''
dino=dino.replace(' ','0')
for i in range(len(dino)):
    if dino[i] !='0' and dino[i]!='\n':
        dino=dino.replace(dino[i],'1')
print(dino)
# create   