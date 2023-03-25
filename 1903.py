import pygame
from random import randint

pygame.init()
back=(200,255, 255) 
mw = pygame.display.set_mode((500, 500)) 
mw.fill(back)
clock = pygame.time.Clock()
BLACK = (0,0,0)
LIGT_BLUE= (200,200,255)
GREEN=(0,255,0)
RED=(255,0,0)
YELLOW=(255,255,0)
pygame.time.Clock()
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
while True:
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
          x, y = event.pos
          for i in range(len(cards)):
            if cards[i].collidepoint(x,y):
                if cards[i].text == 'clik!':
                    cards[i].fill_color=GREEN
                else:
                    cards[i].fill_color=RED
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
    pygame.display.update()
    clock.tick(60)