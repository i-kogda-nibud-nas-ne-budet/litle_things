import pygame
from random import randint
pygame.init()
#создание окна игры
clock = pygame.time.Clock()
back = (192, 67, 200) #цвет фона (background)
mw = pygame.display.set_mode((500, 500)) #окно программы (main window)
mw.fill(back)
#цвета
BLACK = (0, 0, 0)
LIGHT_BLUE = (200, 200, 255)
class TextArea():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        """ область: прямоугольник в нужном месте и нужного цвета """
        #запоминаем прямоугольник:
        self.rect = pygame.Rect(x, y, width, height)
        #цвет заливки - или переданный параметр, или общий цвет фона
        self.fill_color = color
    #установить текст
    def set_text(self, text, fsize=12, text_color=BLACK):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True, text_color) 
    #отрисовка прямоугольника с текстом
    def draw(self, shift_x=0, shift_y=0):
       pygame.draw.rect(mw, self.fill_color, self.rect)
       mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))   
#создание карточек
quest_card = TextArea(0, 100, 290, 70, LIGHT_BLUE)
quest_card.set_text("Вопрос", 75)
ans_card = TextArea(120, 240, 290, 70, LIGHT_BLUE)
ans_card.set_text("Answer", 75)
#основной цикл игры
while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                rand_value=randint(1,3)
                if rand_value==1:
                    quest_card.set_text("qqqqq", 75)
                elif rand_value==2:
                    quest_card.set_text("wwwww", 75)
                else:
                    quest_card.set_text("eeeee", 75)
            if event.key == pygame.K_a:
                rand_value=randint(1,3)
                if rand_value==1:
                    ans_card.set_text("aaaaa", 75)
                elif rand_value==2:
                    ans_card.set_text("sssss", 75)
                else:
                    ans_card.set_text("ddddd", 75)
    quest_card.draw(10,10)
    ans_card.draw(50,10)
    pygame.display.update()
    clock.tick(40)
       