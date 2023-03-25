from play import*
set_backdrop('violet')
blocks=[]
texts=[]
xo='XO'
q=0
for i in [-1,0,1]:
    for j in [-1,0,1]:
        block=new_box('cyan',i*300,j*300,300,300,'orange',10)
        blocks.append(block)
@repeat_forever
def game():
    global q
    for block in blocks:
        if block.is_clicked:
            text=new_text(xo[q%2],block.x,block.y,'white',300)
            q+=1
            texts.append(text)
start_program()