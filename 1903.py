import pygame
from random import randint
import time

pygame.init()
back=(200,255, 255) 
mw = pygame.display.set_mode((500, 500)) 
mw.fill(back)
clock = pygame.time.Clock()
BLACK = (0,0,0)
LIGHT_BLUE= (200,200,255)
GREEN=(0,255,0)
RED=(255,0,0)
YELLOW=(255,255,0)
pygame.time.Clock()
start_time = time.time()
end_time =start_time +10
class TextArea():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
       self.rect = pygame.Rect(x, y, width, height)
       self.fill_color = color
    def set_text(self, text, fsize=40, text_color=BLACK):
       self.text = text
       self.image = pygame.font.Font(None, fsize).render(text, True, text_color)  
    def draw(self, shift_x=0, shift_y=0):
       pygame.draw.rect(mw, self.fill_color, self.rect)
       mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))  
    def collidepoint(self, x, y):
       return self.rect.collidepoint(x, y)
cards=[]
num_cards=4
xx=50
for i in range(num_cards):
    for j in range(num_cards):
        card=TextArea(xx,i*100+50,80,80,(255,255,0))
        card.set_text('')
        cards.append(card)
        xx+=100
    xx=50
wait=40
rand_num=-7
time_txt=TextArea(0,0,60,20,back)
time_txt.set_text('Время',30)
time_int_txt=TextArea(0,30,60,20,back)
time_int_txt.set_text('10',30)
point_txt=TextArea(440,0,60,20,back)
point_txt.set_text('Счёт',30)
points_int_txt=TextArea(440,30,60,20,back)
points_int_txt.set_text('0',30)
points=0
while True:
    mw.fill(back)
    time_int_txt.set_text(str(int(end_time-time.time())))
    points_int_txt.set_text(str(points))
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
          x, y = event.pos
          for i in range(len(cards)):
            if cards[i].collidepoint(x,y):
                if cards[i].text == 'clik!':
                    cards[i].fill_color=GREEN
                    points+=1
                else:
                    cards[i].fill_color=RED
                    points-=1
    if wait==0:
        wait=40
        rand_num=randint(0,len(cards)-1)
        for i in range(len(cards)):
            cards[i].fill_color=YELLOW
            if i==rand_num:
                cards[i].set_text('clik!')
            else:
                cards[i].set_text('')
    else:
        wait-=1
    for i in range(len(cards)):
        cards[i].draw(20,35)
    time_txt.draw(10,10)
    point_txt.draw(10,10)
    time_int_txt.draw(0,0)
    points_int_txt.draw(10,10)
    if (int(end_time-time.time()))<0:
        if points >=5:
            finish=TextArea(0,0,550,550,(0,255,0))
            finish.set_text("GAME OVER",150)
            finish.draw(100,10)
        else:
            finish=TextArea(0,0,550,550,(255,0,0))
            finish.set_text("GAME OVER",150)
            finish.draw(100,10)
    pygame.display.update()
    clock.tick(60)