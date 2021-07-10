import pygame  # python을 통해 게임을 만들 수 있도록 지원해주는 모듈
from io import StringIO  # 메세지나 프린트 값을 파일로 읽고 쓸 수 있도록 지원해주는 python 모듈
import re # 지정한 범위나 지정한 범위 이외의 값을 지정해주는 python 모듈
import random # 난수를 생성해주는 모듈

# 게임창 옵션 설정
size = [1000, 1020]  # 게임창의 크기를 설정한다.
screen = pygame.display.set_mode(size)  # 크기 옵션을 넣으면서 동시에 변수로 지정한다.
random1 = random.sample(range(0, 10), 4)  # 0부터 9까지의 각각 다른 랜덤한 4자리 숫자 생성하는 모듈을 변수로 지정한다.

class obj:  # 이미지 불러오기 및 출력을 위한 class
    def __init__(self, x, y, width, height): # 위치와 크기를 설정한다
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def load_img(self, address):
        if address[-3:] == "png": # address 문장의 뒤에서부터 3글자가 "png"라면
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)

    def change_size(self, sx, sy): # 크기를 변경한다.
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()

    def show(self): # 화면에 표시한다.
        screen.blit(self.img, (self.x, self.y))

# class를 이용하여 이미지를 설정한다.
'''
co = obj(780, 760, 200, 150)
co.load_img("C:/pictures/coach.png")
co.change_size(200, 200)
'''
B_B_0 = obj(631, 510, 60, 60)
B_B_0.load_img("C:/baseball_number_game/pictures/Baseball_Button0.png")
B_B_0.change_size(60, 60)

B_B_1 = obj(694, 511, 60, 60)
B_B_1.load_img("C:/baseball_number_game/pictures/Baseball_Button1.png")
B_B_1.change_size(60, 60)

B_B_2 = obj(757, 510, 60, 60)
B_B_2.load_img("C:/baseball_number_game/pictures/Baseball_Button2.png")
B_B_2.change_size(60, 60)

B_B_3 = obj(820, 510, 60, 60)
B_B_3.load_img("C:/baseball_number_game/pictures/Baseball_Button3.png")
B_B_3.change_size(60, 60)

B_B_4 = obj(883, 510, 60, 60)
B_B_4.load_img("C:/baseball_number_game/pictures/Baseball_Button4.png")
B_B_4.change_size(60, 60)

B_B_5 = obj(631, 575, 60, 60)
B_B_5.load_img("C:/baseball_number_game/pictures/Baseball_Button5.png")
B_B_5.change_size(60, 60)

B_B_6 = obj(694, 575, 60, 60)
B_B_6.load_img("C:/baseball_number_game/pictures/Baseball_Button6.png")
B_B_6.change_size(60, 60)

B_B_7 = obj(757, 575, 60, 60)
B_B_7.load_img("C:/baseball_number_game/pictures/Baseball_Button7.png")
B_B_7.change_size(60, 60)

B_B_8 = obj(820, 575, 60, 60)
B_B_8.load_img("C:/baseball_number_game/pictures/Baseball_Button8.png")
B_B_8.change_size(60, 60)

B_B_9 = obj(883, 575, 60, 60)
B_B_9.load_img("C:/baseball_number_game/pictures/Baseball_Button9.png")
B_B_9.change_size(60, 60)


def return_print(*message): # print값을 변수로 설정할 수 있도록 함수를 지정한다.
    io = StringIO()
    print(*message, file=io)
    return io.getvalue()

def Draw_W(screen, color, Rect, Width):  # 숫자 입력에 대한 결과를 출력하는 전광판을 생성하는 함수
    pygame.draw.rect(screen, color, Rect, Width)

def Draw(screen, color, Rect):  # 화면에 도형을 생성하는 함수
    pygame.draw.rect(screen, color, Rect)

def Except(readData):  # 지정한 범위 외에는 결과값이 출력하도록 하는 함수
    text = re.sub(r"[0-9]", "", readData) # 0-9를 제외한 나머지는 경고창이 뜨도록 설정한다.
    return text



