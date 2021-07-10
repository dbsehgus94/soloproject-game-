#-*-coding:utf-8-*-
# 위 코드는 한글 출력 시 깨지는 현상을 방지하기 위한 코드입니다.
from gameclass import *

# 색깔
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Sky = (0, 255, 255)
C1_Blue = (204, 204, 255)
Gold = (255, 215, 0)

pygame.init()  # 게임 초기화
pygame.display.set_caption("Baseball Number Game")  # 게임 제목

# 배경
bg1 = pygame.image.load('C:/baseball_number_game/pictures/baseballpark1.jpg')
bg1 = pygame.transform.scale(bg1, (1000, 960))
bg2 = pygame.image.load('C:/baseball_number_game/pictures/baseballpark2.jpg')
bg2 = pygame.transform.scale(bg2, (1000, 960))
bg3 = pygame.image.load('C:/baseball_number_game/pictures/baseballpark3.jpg')
bg3 = pygame.transform.scale(bg3, (1000, 960))

bg = [bg1, bg2, bg3]  # 배경을 리스트에 모은다.
randombg = random.choice(bg)  # 3개의 배경 중 랜덤으로 하나를 배경으로 설정한다.
screen.blit(randombg, (0, 0))  # 배경화면 출력

Draw_W(screen, Black, [10, 25, 580, 600], 30)  # 왼쪽 틀 그리기
Draw_W(screen, Black, [625, 25, 365, 478], 10)  # 오른쪽 틀 그리기
Draw_W(screen, C1_Blue, [8, 650, 850, 300], 15)  # 안내창 틀 그리기
Draw(screen, Black, [16, 658, 835, 284])  # 안내창 검은 배경 그리기
Draw(screen, Black, [630, 510, 315, 130])  # 야구공 뒤 검은 배경 그리기

# 폰트 지정
myFont1 = pygame.font.Font('NanumGothicExtraBold.ttf', 30)
myFont2 = pygame.font.Font('NanumGothicExtraBold.ttf', 17)

# 폰트에 따른 설정 값을 변수에 생성합니다.
text_Title1 = myFont2.render("0부터 9 사이에 4개의 숫자를 중복되지 않게 입력하세요.(첫 번째 숫자 0 가능합니다.)", True, White)
text_Title2 = myFont2.render("12번의 기회가 주어집니다. 최소한의 힌트로 정확한 숫자를 유추하여 맞추는 게임입니다.", True, White)
text_Title3 = myFont2.render("입력하신 숫자가 랜덤으로 생성된 숫자와 비교하여 자리와 숫자가 완전히 일치하면 S가 1 증가합니다.", True, White)
text_Title4 = myFont2.render("입력하신 숫자가 랜덤으로 생성된 숫자의 리스트에 포함되지만 자릿수가 일치하지 않으면 B가 1 증가합니다.", True, White)
text_Title5 = myFont2.render("입력하신 숫자와 랜덤으로 생성된 숫자가 모두 다른 숫자이면 OUT을 출력합니다.", True, White)
text_Title6 = myFont2.render("야구공을 클릭하여 숫자를 맞추시는 데 필요없는 숫자를 지울 수 있습니다.(한번 누르면 다시 돌아오지 않습니다.)", True, White)
text_Title7 = myFont2.render("체크박스를 클릭 후 테두리 색이 파란색으로 표시되면 숫자를 입력하고 엔터를 눌러주세요.", True, White)

# 생성한 변수를 screen을 기준으로 지정한 위치에 출력합니다.
screen.blit(text_Title1, [24, 667])
screen.blit(text_Title2, [24, 697])
screen.blit(text_Title3, [24, 727])
screen.blit(text_Title4, [24, 757])
screen.blit(text_Title5, [24, 787])
screen.blit(text_Title6, [24, 817])
screen.blit(text_Title7, [24, 847])

# 화면에 class로 설정한 이미지를 띄운다.
# co.show()
B_B_0.show()
B_B_1.show()
B_B_2.show()
B_B_3.show()
B_B_4.show()
B_B_5.show()
B_B_6.show()
B_B_7.show()
B_B_8.show()
B_B_9.show()

clock = pygame.time.Clock()  # 게임 loop 주기 설정을 위한 변수
input_box = pygame.Rect(50, 952, 300, 45)  # input_box 위치 설정
color_inactive = pygame.Color('white')  # 상자가 비활성화(클릭하지 않은 상태) 상태의 색깔
color_active = pygame.Color(Sky)  # 상자를 활성화(클릭) 했을 때의 색깔
color = color_inactive  # 초기 색깔 설정은 비활성화 상태의 색깔로 설정한다.
active = False  # 초기 활성화 상태는 비활성화 상태로 설정한다.
INPUT = ''  # 초기 input_box 안의 내용을 비운다.
Text_Color = Black  # 특정 조건 만족 시 색깔을 출력하기 위한 변수 지정
done = False  # 초기에는 반복문을 실행하지 않도록 설정한다.

t_count = 1  # 입력한 횟수 -> 입력하는 순간 1회가 되어야하므로 시작을 1로 설정한다.
s_count = 0  # 스트라이크 -> 4가 되면 게임이 끝난다.
b_count = 0  # 볼 -> 사용자가 입력한 수에 따라 0 ~ 4의 값이 출력된다.

while not done: # done = False일 동안 반복문 지속
    # 상자 안 텍스트 설정
    Text_surface = myFont1.render(INPUT, True, color)  # 초기 설정에서 입력한 조건들을 통해 input_box 안에 text 설정을 생성한다.
    screen.fill((0, 0, 0), [0, 950, 1000, 70])  # 텍스트 상자에서 숫자가 사라지는 것을 표현하기 위한 화면 채우기
    # 텍스트가 너무 긴 경우 상자 크기 조정
    width = max(200, Text_surface.get_width() + 10)  # 텍스트 상자 너비는 최대 텍스트 길이의 + 10으로 설정한다.
    input_box.w = width  # 텍스트 상자 너비
    # 텍스트 채우기
    screen.blit(Text_surface, (input_box.x + 5, input_box.y + 5))  # Text가 상자에 너무 딱 붙지 않게 +5 정도 띄워서 출력한다.
    Draw_W(screen, color, input_box, 2)  # 입력 상자 그리기
    for event in pygame.event.get():  # 이벤트가 발생하는 동안 반복
        if event.type == pygame.QUIT:  # pygame을 종료하면
            done = True  # 반복문을 중지한다.
        if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 클릭 이벤트 시
            if input_box.collidepoint(event.pos):  # 박스를 클릭하면
                active = True  # 활성 변수로 전환한다.
            else:  # 박스 외 다른 곳을 클릭하면
                active = False  # 비활성 상태가 된다
            color = color_active if active else color_inactive  # 마우스 클릭 후 활성화가 되었다면 활성화 색깔로 그렇지 않다면 비활성화 색깔로 설정한다.
        if event.type == pygame.KEYDOWN:  # 키 입력시
            if active:  # 활성화 시
                if randombg == bg1 or randombg == bg2:  # 배경이 조건과 일치하면 글씨 색을 검은색으로
                    Text_Color = Black
                elif randombg == bg3:  # 배경이 조건과 일치하면 글씨 색을 하늘색으로
                    Text_Color = Sky
                if event.key == pygame.K_RETURN:  # 입력 박스에 숫자를 입력하고 엔터를 치면
                    if t_count == 1:  # 1번째 시도
                        print(INPUT)  # input_box에 입력한 숫자를 print한다.
                        IN_PR = return_print(INPUT)  # print값을 변수로 변환하여 게임 화면에 출력되게 한다.
                        if len(IN_PR) > 5:  # 4자리 숫자지만 엔터를 치면 len = 5로 인식되어 len > 5라고 조건을 두었다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 정확히 입력해주세요!")  # 조건에 따른 경고문1 출력
                            Warn_PR1 = return_print("4자리 숫자를 정확히 입력해주세요!")  # 경고문1을 변수로 지정한다.
                            Text_Warn1 = myFont2.render(Warn_PR1, True, Red)  # 지정한 경고문1 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn1, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문1 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == Except(IN_PR[0]) or IN_PR[1] == Except(IN_PR[1]) or IN_PR[2] == Except(IN_PR[2]) or IN_PR[3] == Except(IN_PR[3]):  # 입력한 print값이 각 자리마다 0~9가 아닌 다른 문자일 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 입력해주세요!")  # 조건에 따른 경고문2 출력
                            Warn_PR2 = return_print("4자리 숫자를 입력해주세요!")  # 경고문2를 변수로 지정한다.
                            Text_Warn2 = myFont2.render(Warn_PR2, True, Red)  # 지정한 경고문2 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn2, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문2 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == IN_PR[1] or IN_PR[0] == IN_PR[2] or IN_PR[0] == IN_PR[3] or IN_PR[1] == IN_PR[2] or IN_PR[1] == IN_PR[3] or IN_PR[2] == IN_PR[3]:  # 입력한 각각의 4자리 숫자가 1개라도 중복되는 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("중복되지 않는 숫자를 입력해주세요.")  # 조건에 따른 경고문3 출력
                            Warn_PR3 = return_print("중복되지 않는 숫자를 입력해주세요.")  # 경고문3를 변수로 지정한다.
                            Text_Warn3 = myFont2.render(Warn_PR3, True, Red)  # 지정한 경고문3 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn3, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문3 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        Text1 = myFont1.render(IN_PR, True, Text_Color)  # 위 조건에 만족하지 않는 print값을 폰트를 이용하여 Text변수를 생성한다.
                        screen.blit(Text1, [195, 40])  # 지정한 변수를 화면에 출력한다.
                        Text2 = myFont1.render(IN_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                        screen.blit(Text2, [640, 30])  # 지정한 변수를 화면에 출력한다.
                        s_count = 0  # s_count 값 설정
                        b_count = 0  # b_count 값 설정
                        for x in range(0, 4):  # x 범위 지정
                            for y in range(0, 4):  # y 범위 지정
                                if INPUT[x] == str(random1[y]) and x == y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수와 숫자 모두 같다면
                                    s_count += 1  # s_count 값을 +1 한다.
                                elif INPUT[x] == str(random1[y]) and x != y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수는 다르지만 숫자가 같다면
                                    b_count += 1  # b_count 값을 +1 한다.
                        if s_count == b_count == 0:  # 입력한 숫자 4개와 랜덤으로 생성된 숫자 4개가 다르다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("OUT")  # 조건에 따른 OUT 출력
                            OUT_PR = return_print("OUT")  # OUT 출력값을 변수로 지정한다.
                            Text_OUT1 = myFont1.render(OUT_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_OUT1, [400, 40])  # 지정한 변수를 화면에 출력한다.
                            Text_OUT2 = myFont1.render(OUT_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_OUT2, [860, 30])  # 지정한 변수를 화면에 출력한다.
                        elif s_count != 0 or b_count != 0:  # S나 B가 0이 아니라면
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print(s_count, "S", b_count, "B")  # 조건에 따른 S, B 결과값 출력
                            SB_PR = return_print(s_count, "S", b_count, "B")  # S, B 결과값을 변수로 지정한다.
                            Text_SB1 = myFont1.render(SB_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_SB1, [400, 40])  # 지정한 변수를 화면에 출력한다.
                            Text_SB2 = myFont1.render(SB_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_SB2, [860, 30])  # 지정한 변수를 화면에 출력한다.
                        print(t_count, "회")  # t_count 출력
                        INN_PR = return_print(t_count, "회")  # t_count값을 변수로 지정한다.
                        Text_INN = myFont1.render(INN_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                        screen.blit(Text_INN, [35, 40])  # 지정한 변수를 화면에 출력한다.
                        t_count += 1  # t_count값이 나왔으니 +1 한다.
                        INPUT = ''  # 입력상자에 숫자를 빈칸으로 바꾼다.
                        if s_count == 4:  # 입력한 숫자와 랜덤으로 생성한 숫자가 완벽히 일치한다면
                            Draw(screen, Black, [30, 907, 750, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("축하합니다! 콜드 게임으로 승리하셨습니다! X버튼을 눌러주세요")  # 조건 달성 시 안내문 출력
                            WIN_PR = return_print("축하합니다! 콜드 게임으로 승리하셨습니다! X버튼을 눌러주세요")  # 출력한 안내문을 변수로 지정한다.
                            Text_WIN = myFont2.render(WIN_PR, True, Green)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_WIN, [35, 907])  # 지정한 변수를 화면에 출력한다.
                    elif t_count == 2:  # 2번째 시도
                        print(INPUT)  # input_box에 입력한 숫자를 print한다.
                        IN_PR = return_print(INPUT)  # print값을 변수로 변환하여 게임 화면에 출력되게 한다.
                        if len(IN_PR) > 5:  # 4자리 숫자지만 엔터를 치면 len = 5로 인식되어 len > 5라고 조건을 두었다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 정확히 입력해주세요!")  # 조건에 따른 경고문1 출력
                            Warn_PR1 = return_print("4자리 숫자를 정확히 입력해주세요!")  # 경고문1을 변수로 지정한다.
                            Text_Warn1 = myFont2.render(Warn_PR1, True, Red)  # 지정한 경고문1 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn1, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문1 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == Except(IN_PR[0]) or IN_PR[1] == Except(IN_PR[1]) or IN_PR[2] == Except(IN_PR[2]) or IN_PR[3] == Except(IN_PR[3]):  # 입력한 print값이 각 자리마다 0~9가 아닌 다른 문자일 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 입력해주세요!")  # 조건에 따른 경고문2 출력
                            Warn_PR2 = return_print("4자리 숫자를 입력해주세요!")  # 경고문2를 변수로 지정한다.
                            Text_Warn2 = myFont2.render(Warn_PR2, True, Red)  # 지정한 경고문2 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn2, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문2 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == IN_PR[1] or IN_PR[0] == IN_PR[2] or IN_PR[0] == IN_PR[3] or IN_PR[1] == IN_PR[2] or IN_PR[1] == IN_PR[3] or IN_PR[2] == IN_PR[3]:  # 입력한 각각의 4자리 숫자가 1개라도 중복되는 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("중복되지 않는 숫자를 입력해주세요.")  # 조건에 따른 경고문3 출력
                            Warn_PR3 = return_print("중복되지 않는 숫자를 입력해주세요.")  # 경고문3를 변수로 지정한다.
                            Text_Warn3 = myFont2.render(Warn_PR3, True, Red)  # 지정한 경고문3 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn3, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문3 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        Text1 = myFont1.render(IN_PR, True, Text_Color)  # 위 조건에 만족하지 않는 print값을 폰트를 이용하여 Text변수를 생성한다.
                        screen.blit(Text1, [195, 90])  # 지정한 변수를 화면에 출력한다.
                        Text2 = myFont1.render(IN_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                        screen.blit(Text2, [640, 65])  # 지정한 변수를 화면에 출력한다.
                        s_count = 0  # s_count 값 설정
                        b_count = 0  # b_count 값 설정
                        for x in range(0, 4):  # x 범위 지정
                            for y in range(0, 4):  # y 범위 지정
                                if INPUT[x] == str(random1[y]) and x == y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수와 숫자 모두 같다면
                                    s_count += 1  # s_count 값을 +1 한다.
                                elif INPUT[x] == str(random1[y]) and x != y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수는 다르지만 숫자가 같다면
                                    b_count += 1  # b_count 값을 +1 한다.
                        if s_count == b_count == 0:  # 입력한 숫자 4개와 랜덤으로 생성된 숫자 4개가 다르다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("OUT")  # 조건에 따른 OUT 출력
                            OUT_PR = return_print("OUT")  # OUT 출력값을 변수로 지정한다.
                            Text_OUT1 = myFont1.render(OUT_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_OUT1, [400, 90])  # 지정한 변수를 화면에 출력한다.
                            Text_OUT2 = myFont1.render(OUT_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_OUT2, [860, 65])  # 지정한 변수를 화면에 출력한다.
                        elif s_count != 0 or b_count != 0:  # S나 B가 0이 아니라면
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print(s_count, "S", b_count, "B")  # 조건에 따른 S, B 결과값 출력
                            SB_PR = return_print(s_count, "S", b_count, "B")  # S, B 결과값을 변수로 지정한다.
                            Text_SB1 = myFont1.render(SB_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_SB1, [400, 90])  # 지정한 변수를 화면에 출력한다.
                            Text_SB2 = myFont1.render(SB_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_SB2, [860, 65])  # 지정한 변수를 화면에 출력한다.
                        print(t_count, "회")  # t_count 출력
                        INN_PR = return_print(t_count, "회")  # t_count값을 변수로 지정한다.
                        Text_INN = myFont1.render(INN_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                        screen.blit(Text_INN, [35, 90])  # 지정한 변수를 화면에 출력한다.
                        t_count += 1  # t_count값이 나왔으니 +1 한다.
                        INPUT = ''  # 입력상자에 숫자를 빈칸으로 바꾼다.
                        if s_count == 4:  # 입력한 숫자와 랜덤으로 생성한 숫자가 완벽히 일치한다면
                            Draw(screen, Black, [30, 907, 750, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("축하합니다! 콜드 게임으로 승리하셨습니다! X버튼을 눌러주세요")  # 조건 달성 시 안내문 출력
                            WIN_PR = return_print("축하합니다! 콜드 게임으로 승리하셨습니다! X버튼을 눌러주세요")  # 출력한 안내문을 변수로 지정한다.
                            Text_WIN = myFont2.render(WIN_PR, True, Green)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_WIN, [35, 907])  # 지정한 변수를 화면에 출력한다.
                    elif t_count == 3:  # 3번째 시도
                        print(INPUT)  # input_box에 입력한 숫자를 print한다.
                        IN_PR = return_print(INPUT)  # print값을 변수로 변환하여 게임 화면에 출력되게 한다.
                        if len(IN_PR) > 5:  # 4자리 숫자지만 엔터를 치면 len = 5로 인식되어 len > 5라고 조건을 두었다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 정확히 입력해주세요!")  # 조건에 따른 경고문1 출력
                            Warn_PR1 = return_print("4자리 숫자를 정확히 입력해주세요!")  # 경고문1을 변수로 지정한다.
                            Text_Warn1 = myFont2.render(Warn_PR1, True, Red)  # 지정한 경고문1 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn1, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문1 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == Except(IN_PR[0]) or IN_PR[1] == Except(IN_PR[1]) or IN_PR[2] == Except(IN_PR[2]) or IN_PR[3] == Except(IN_PR[3]):  # 입력한 print값이 각 자리마다 0~9가 아닌 다른 문자일 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 입력해주세요!")  # 조건에 따른 경고문2 출력
                            Warn_PR2 = return_print("4자리 숫자를 입력해주세요!")  # 경고문2를 변수로 지정한다.
                            Text_Warn2 = myFont2.render(Warn_PR2, True, Red)  # 지정한 경고문2 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn2, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문2 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == IN_PR[1] or IN_PR[0] == IN_PR[2] or IN_PR[0] == IN_PR[3] or IN_PR[1] == IN_PR[2] or IN_PR[1] == IN_PR[3] or IN_PR[2] == IN_PR[3]:  # 입력한 각각의 4자리 숫자가 1개라도 중복되는 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("중복되지 않는 숫자를 입력해주세요.")  # 조건에 따른 경고문3 출력
                            Warn_PR3 = return_print("중복되지 않는 숫자를 입력해주세요.")  # 경고문3를 변수로 지정한다.
                            Text_Warn3 = myFont2.render(Warn_PR3, True, Red)  # 지정한 경고문3 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn3, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문3 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        Text1 = myFont1.render(IN_PR, True, Text_Color)  # 위 조건에 만족하지 않는 print값을 폰트를 이용하여 Text변수를 생성한다.
                        screen.blit(Text1, [195, 140])  # 지정한 변수를 화면에 출력한다.
                        Text2 = myFont1.render(IN_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                        screen.blit(Text2, [640, 105])  # 지정한 변수를 화면에 출력한다.
                        s_count = 0  # s_count 값 설정
                        b_count = 0  # b_count 값 설정
                        for x in range(0, 4):  # x 범위 지정
                            for y in range(0, 4):  # y 범위 지정
                                if INPUT[x] == str(random1[y]) and x == y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수와 숫자 모두 같다면
                                    s_count += 1  # s_count 값을 +1 한다.
                                elif INPUT[x] == str(random1[y]) and x != y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수는 다르지만 숫자가 같다면
                                    b_count += 1  # b_count 값을 +1 한다.
                        if s_count == b_count == 0:  # 입력한 숫자 4개와 랜덤으로 생성된 숫자 4개가 다르다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("OUT")  # 조건에 따른 OUT 출력
                            OUT_PR = return_print("OUT")  # OUT 출력값을 변수로 지정한다.
                            Text_OUT1 = myFont1.render(OUT_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_OUT1, [400, 140])  # 지정한 변수를 화면에 출력한다.
                            Text_OUT2 = myFont1.render(OUT_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_OUT2, [860, 105])  # 지정한 변수를 화면에 출력한다.
                        elif s_count != 0 or b_count != 0:  # S나 B가 0이 아니라면
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print(s_count, "S", b_count, "B")  # 조건에 따른 S, B 결과값 출력
                            SB_PR = return_print(s_count, "S", b_count, "B")  # S, B 결과값을 변수로 지정한다.
                            Text_SB1 = myFont1.render(SB_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_SB1, [400, 140])  # 지정한 변수를 화면에 출력한다.
                            Text_SB2 = myFont1.render(SB_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_SB2, [860, 105])  # 지정한 변수를 화면에 출력한다.
                        print(t_count, "회")  # t_count 출력
                        INN_PR = return_print(t_count, "회")  # t_count값을 변수로 지정한다.
                        Text_INN = myFont1.render(INN_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                        screen.blit(Text_INN, [35, 140])  # 지정한 변수를 화면에 출력한다.
                        t_count += 1  # t_count값이 나왔으니 +1 한다.
                        INPUT = ''  # 입력상자에 숫자를 빈칸으로 바꾼다.
                        if s_count == 4:  # 입력한 숫자와 랜덤으로 생성한 숫자가 완벽히 일치한다면
                            Draw(screen, Black, [30, 907, 750, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("축하합니다! 콜드 게임으로 승리하셨습니다! X버튼을 눌러주세요")  # 조건 달성 시 안내문 출력
                            WIN_PR = return_print("축하합니다! 콜드 게임으로 승리하셨습니다! X버튼을 눌러주세요")  # 출력한 안내문을 변수로 지정한다.
                            Text_WIN = myFont2.render(WIN_PR, True, Green)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_WIN, [35, 907])  # 지정한 변수를 화면에 출력한다.
                    elif t_count == 4:  # 4번째 시도
                        print(INPUT)  # input_box에 입력한 숫자를 print한다.
                        IN_PR = return_print(INPUT)  # print값을 변수로 변환하여 게임 화면에 출력되게 한다.
                        if len(IN_PR) > 5:  # 4자리 숫자지만 엔터를 치면 len = 5로 인식되어 len > 5라고 조건을 두었다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 정확히 입력해주세요!")  # 조건에 따른 경고문1 출력
                            Warn_PR1 = return_print("4자리 숫자를 정확히 입력해주세요!")  # 경고문1을 변수로 지정한다.
                            Text_Warn1 = myFont2.render(Warn_PR1, True, Red)  # 지정한 경고문1 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn1, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문1 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == Except(IN_PR[0]) or IN_PR[1] == Except(IN_PR[1]) or IN_PR[2] == Except(IN_PR[2]) or IN_PR[3] == Except(IN_PR[3]):  # 입력한 print값이 각 자리마다 0~9가 아닌 다른 문자일 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 입력해주세요!")  # 조건에 따른 경고문2 출력
                            Warn_PR2 = return_print("4자리 숫자를 입력해주세요!")  # 경고문2를 변수로 지정한다.
                            Text_Warn2 = myFont2.render(Warn_PR2, True, Red)  # 지정한 경고문2 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn2, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문2 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == IN_PR[1] or IN_PR[0] == IN_PR[2] or IN_PR[0] == IN_PR[3] or IN_PR[1] == IN_PR[2] or IN_PR[1] == IN_PR[3] or IN_PR[2] == IN_PR[3]:  # 입력한 각각의 4자리 숫자가 1개라도 중복되는 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("중복되지 않는 숫자를 입력해주세요.")  # 조건에 따른 경고문3 출력
                            Warn_PR3 = return_print("중복되지 않는 숫자를 입력해주세요.")  # 경고문3를 변수로 지정한다.
                            Text_Warn3 = myFont2.render(Warn_PR3, True, Red)  # 지정한 경고문3 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn3, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문3 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        Text1 = myFont1.render(IN_PR, True, Text_Color)  # 위 조건에 만족하지 않는 print값을 폰트를 이용하여 Text변수를 생성한다.
                        screen.blit(Text1, [195, 190])  # 지정한 변수를 화면에 출력한다.
                        Text2 = myFont1.render(IN_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                        screen.blit(Text2, [640, 145])  # 지정한 변수를 화면에 출력한다.
                        s_count = 0  # s_count 값 설정
                        b_count = 0  # b_count 값 설정
                        for x in range(0, 4):  # x 범위 지정
                            for y in range(0, 4):  # y 범위 지정
                                if INPUT[x] == str(random1[y]) and x == y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수와 숫자 모두 같다면
                                    s_count += 1  # s_count 값을 +1 한다.
                                elif INPUT[x] == str(random1[y]) and x != y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수는 다르지만 숫자가 같다면
                                    b_count += 1  # b_count 값을 +1 한다.
                        if s_count == b_count == 0:  # 입력한 숫자 4개와 랜덤으로 생성된 숫자 4개가 다르다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("OUT")  # 조건에 따른 OUT 출력
                            OUT_PR = return_print("OUT")  # OUT 출력값을 변수로 지정한다.
                            Text_OUT1 = myFont1.render(OUT_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_OUT1, [400, 190])  # 지정한 변수를 화면에 출력한다.
                            Text_OUT2 = myFont1.render(OUT_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_OUT2, [860, 145])  # 지정한 변수를 화면에 출력한다.
                        elif s_count != 0 or b_count != 0:  # S나 B가 0이 아니라면
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print(s_count, "S", b_count, "B")  # 조건에 따른 S, B 결과값 출력
                            SB_PR = return_print(s_count, "S", b_count, "B")  # S, B 결과값을 변수로 지정한다.
                            Text_SB1 = myFont1.render(SB_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_SB1, [400, 190])  # 지정한 변수를 화면에 출력한다.
                            Text_SB2 = myFont1.render(SB_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_SB2, [860, 145])  # 지정한 변수를 화면에 출력한다.
                        print(t_count, "회")  # t_count 출력
                        INN_PR = return_print(t_count, "회")  # t_count값을 변수로 지정한다.
                        Text_INN = myFont1.render(INN_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                        screen.blit(Text_INN, [35, 190])  # 지정한 변수를 화면에 출력한다.
                        t_count += 1  # t_count값이 나왔으니 +1 한다.
                        INPUT = ''  # 입력상자에 숫자를 빈칸으로 바꾼다.
                        if s_count == 4:  # 입력한 숫자와 랜덤으로 생성한 숫자가 완벽히 일치한다면
                            Draw(screen, Black, [30, 907, 750, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("축하합니다! 콜드 게임으로 승리하셨습니다! X버튼을 눌러주세요")  # 조건 달성 시 안내문 출력
                            WIN_PR = return_print("축하합니다! 콜드 게임으로 승리하셨습니다! X버튼을 눌러주세요")  # 출력한 안내문을 변수로 지정한다.
                            Text_WIN = myFont2.render(WIN_PR, True, Green)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_WIN, [35, 907])  # 지정한 변수를 화면에 출력한다.
                    elif t_count == 5:  # 5번째 시도
                        print(INPUT)  # input_box에 입력한 숫자를 print한다.
                        IN_PR = return_print(INPUT)  # print값을 변수로 변환하여 게임 화면에 출력되게 한다.
                        if len(IN_PR) > 5:  # 4자리 숫자지만 엔터를 치면 len = 5로 인식되어 len > 5라고 조건을 두었다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 정확히 입력해주세요!")  # 조건에 따른 경고문1 출력
                            Warn_PR1 = return_print("4자리 숫자를 정확히 입력해주세요!")  # 경고문1을 변수로 지정한다.
                            Text_Warn1 = myFont2.render(Warn_PR1, True, Red)  # 지정한 경고문1 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn1, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문1 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == Except(IN_PR[0]) or IN_PR[1] == Except(IN_PR[1]) or IN_PR[2] == Except(IN_PR[2]) or IN_PR[3] == Except(IN_PR[3]):  # 입력한 print값이 각 자리마다 0~9가 아닌 다른 문자일 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 입력해주세요!")  # 조건에 따른 경고문2 출력
                            Warn_PR2 = return_print("4자리 숫자를 입력해주세요!")  # 경고문2를 변수로 지정한다.
                            Text_Warn2 = myFont2.render(Warn_PR2, True, Red)  # 지정한 경고문2 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn2, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문2 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == IN_PR[1] or IN_PR[0] == IN_PR[2] or IN_PR[0] == IN_PR[3] or IN_PR[1] == IN_PR[2] or IN_PR[1] == IN_PR[3] or IN_PR[2] == IN_PR[3]:  # 입력한 각각의 4자리 숫자가 1개라도 중복되는 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("중복되지 않는 숫자를 입력해주세요.")  # 조건에 따른 경고문3 출력
                            Warn_PR3 = return_print("중복되지 않는 숫자를 입력해주세요.")  # 경고문3를 변수로 지정한다.
                            Text_Warn3 = myFont2.render(Warn_PR3, True, Red)  # 지정한 경고문3 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn3, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문3 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        Text1 = myFont1.render(IN_PR, True, Text_Color)  # 위 조건에 만족하지 않는 print값을 폰트를 이용하여 Text변수를 생성한다.
                        screen.blit(Text1, [195, 240])  # 지정한 변수를 화면에 출력한다.
                        Text2 = myFont1.render(IN_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                        screen.blit(Text2, [640, 185])  # 지정한 변수를 화면에 출력한다.
                        s_count = 0  # s_count 값 설정
                        b_count = 0  # b_count 값 설정
                        for x in range(0, 4):  # x 범위 지정
                            for y in range(0, 4):  # y 범위 지정
                                if INPUT[x] == str(random1[y]) and x == y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수와 숫자 모두 같다면
                                    s_count += 1  # s_count 값을 +1 한다.
                                elif INPUT[x] == str(random1[y]) and x != y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수는 다르지만 숫자가 같다면
                                    b_count += 1  # b_count 값을 +1 한다.
                        if s_count == b_count == 0:  # 입력한 숫자 4개와 랜덤으로 생성된 숫자 4개가 다르다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("OUT")  # 조건에 따른 OUT 출력
                            OUT_PR = return_print("OUT")  # OUT 출력값을 변수로 지정한다.
                            Text_OUT1 = myFont1.render(OUT_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_OUT1, [400, 240])  # 지정한 변수를 화면에 출력한다.
                            Text_OUT2 = myFont1.render(OUT_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_OUT2, [860, 185])  # 지정한 변수를 화면에 출력한다.
                        elif s_count != 0 or b_count != 0:  # S나 B가 0이 아니라면
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print(s_count, "S", b_count, "B")  # 조건에 따른 S, B 결과값 출력
                            SB_PR = return_print(s_count, "S", b_count, "B")  # S, B 결과값을 변수로 지정한다.
                            Text_SB1 = myFont1.render(SB_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_SB1, [400, 240])  # 지정한 변수를 화면에 출력한다.
                            Text_SB2 = myFont1.render(SB_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_SB2, [860, 185])  # 지정한 변수를 화면에 출력한다.
                        print(t_count, "회")  # t_count 출력
                        INN_PR = return_print(t_count, "회")  # t_count값을 변수로 지정한다.
                        Text_INN = myFont1.render(INN_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                        screen.blit(Text_INN, [35, 240])  # 지정한 변수를 화면에 출력한다.
                        t_count += 1  # t_count값이 나왔으니 +1 한다.
                        INPUT = ''  # 입력상자에 숫자를 빈칸으로 바꾼다.
                        if s_count == 4:  # 입력한 숫자와 랜덤으로 생성한 숫자가 완벽히 일치한다면
                            Draw(screen, Black, [30, 907, 750, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("축하합니다! 콜드 게임으로 승리하셨습니다! X버튼을 눌러주세요")  # 조건 달성 시 안내문 출력
                            WIN_PR = return_print("축하합니다! 콜드 게임으로 승리하셨습니다! X버튼을 눌러주세요")  # 출력한 안내문을 변수로 지정한다.
                            Text_WIN = myFont2.render(WIN_PR, True, Green)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_WIN, [35, 907])  # 지정한 변수를 화면에 출력한다.
                    elif t_count == 6:  # 6번째 시도
                        print(INPUT)  # input_box에 입력한 숫자를 print한다.
                        IN_PR = return_print(INPUT)  # print값을 변수로 변환하여 게임 화면에 출력되게 한다.
                        if len(IN_PR) > 5:  # 4자리 숫자지만 엔터를 치면 len = 5로 인식되어 len > 5라고 조건을 두었다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 정확히 입력해주세요!")  # 조건에 따른 경고문1 출력
                            Warn_PR1 = return_print("4자리 숫자를 정확히 입력해주세요!")  # 경고문1을 변수로 지정한다.
                            Text_Warn1 = myFont2.render(Warn_PR1, True, Red)  # 지정한 경고문1 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn1, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문1 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == Except(IN_PR[0]) or IN_PR[1] == Except(IN_PR[1]) or IN_PR[2] == Except(IN_PR[2]) or IN_PR[3] == Except(IN_PR[3]):  # 입력한 print값이 각 자리마다 0~9가 아닌 다른 문자일 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 입력해주세요!")  # 조건에 따른 경고문2 출력
                            Warn_PR2 = return_print("4자리 숫자를 입력해주세요!")  # 경고문2를 변수로 지정한다.
                            Text_Warn2 = myFont2.render(Warn_PR2, True, Red)  # 지정한 경고문2 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn2, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문2 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == IN_PR[1] or IN_PR[0] == IN_PR[2] or IN_PR[0] == IN_PR[3] or IN_PR[1] == IN_PR[2] or IN_PR[1] == IN_PR[3] or IN_PR[2] == IN_PR[3]:  # 입력한 각각의 4자리 숫자가 1개라도 중복되는 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("중복되지 않는 숫자를 입력해주세요.")  # 조건에 따른 경고문3 출력
                            Warn_PR3 = return_print("중복되지 않는 숫자를 입력해주세요.")  # 경고문3를 변수로 지정한다.
                            Text_Warn3 = myFont2.render(Warn_PR3, True, Red)  # 지정한 경고문3 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn3, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문3 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        Text1 = myFont1.render(IN_PR, True, Text_Color)  # 위 조건에 만족하지 않는 print값을 폰트를 이용하여 Text변수를 생성한다.
                        screen.blit(Text1, [195, 290])  # 지정한 변수를 화면에 출력한다.
                        Text2 = myFont1.render(IN_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                        screen.blit(Text2, [640, 225])  # 지정한 변수를 화면에 출력한다.
                        s_count = 0  # s_count 값 설정
                        b_count = 0  # b_count 값 설정
                        for x in range(0, 4):  # x 범위 지정
                            for y in range(0, 4):  # y 범위 지정
                                if INPUT[x] == str(random1[y]) and x == y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수와 숫자 모두 같다면
                                    s_count += 1  # s_count 값을 +1 한다.
                                elif INPUT[x] == str(random1[y]) and x != y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수는 다르지만 숫자가 같다면
                                    b_count += 1  # b_count 값을 +1 한다.
                        if s_count == b_count == 0:  # 입력한 숫자 4개와 랜덤으로 생성된 숫자 4개가 다르다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("OUT")  # 조건에 따른 OUT 출력
                            OUT_PR = return_print("OUT")  # OUT 출력값을 변수로 지정한다.
                            Text_OUT1 = myFont1.render(OUT_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_OUT1, [400, 290])  # 지정한 변수를 화면에 출력한다.
                            Text_OUT2 = myFont1.render(OUT_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_OUT2, [860, 225])  # 지정한 변수를 화면에 출력한다.
                        elif s_count != 0 or b_count != 0:  # S나 B가 0이 아니라면
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print(s_count, "S", b_count, "B")  # 조건에 따른 S, B 결과값 출력
                            SB_PR = return_print(s_count, "S", b_count, "B")  # S, B 결과값을 변수로 지정한다.
                            Text_SB1 = myFont1.render(SB_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_SB1, [400, 290])  # 지정한 변수를 화면에 출력한다.
                            Text_SB2 = myFont1.render(SB_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_SB2, [860, 225])  # 지정한 변수를 화면에 출력한다.
                        print(t_count, "회")  # t_count 출력
                        INN_PR = return_print(t_count, "회")  # t_count값을 변수로 지정한다.
                        Text_INN = myFont1.render(INN_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                        screen.blit(Text_INN, [35, 290])  # 지정한 변수를 화면에 출력한다.
                        t_count += 1  # t_count값이 나왔으니 +1 한다.
                        INPUT = ''  # 입력상자에 숫자를 빈칸으로 바꾼다.
                        if s_count == 4:  # 입력한 숫자와 랜덤으로 생성한 숫자가 완벽히 일치한다면
                            Draw(screen, Black, [30, 907, 750, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("축하합니다! 승리하셨습니다! X버튼을 눌러주세요")  # 조건 달성 시 안내문 출력
                            WIN_PR = return_print("축하합니다! 승리하셨습니다! X버튼을 눌러주세요")  # 출력한 안내문을 변수로 지정한다.
                            Text_WIN = myFont2.render(WIN_PR, True, Green)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_WIN, [35, 907])  # 지정한 변수를 화면에 출력한다.
                    elif t_count == 7:  # 7번째 시도
                        print(INPUT)  # input_box에 입력한 숫자를 print한다.
                        IN_PR = return_print(INPUT)  # print값을 변수로 변환하여 게임 화면에 출력되게 한다.
                        if len(IN_PR) > 5:  # 4자리 숫자지만 엔터를 치면 len = 5로 인식되어 len > 5라고 조건을 두었다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 정확히 입력해주세요!")  # 조건에 따른 경고문1 출력
                            Warn_PR1 = return_print("4자리 숫자를 정확히 입력해주세요!")  # 경고문1을 변수로 지정한다.
                            Text_Warn1 = myFont2.render(Warn_PR1, True, Red)  # 지정한 경고문1 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn1, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문1 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == Except(IN_PR[0]) or IN_PR[1] == Except(IN_PR[1]) or IN_PR[2] == Except(IN_PR[2]) or IN_PR[3] == Except(IN_PR[3]):  # 입력한 print값이 각 자리마다 0~9가 아닌 다른 문자일 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 입력해주세요!")  # 조건에 따른 경고문2 출력
                            Warn_PR2 = return_print("4자리 숫자를 입력해주세요!")  # 경고문2를 변수로 지정한다.
                            Text_Warn2 = myFont2.render(Warn_PR2, True, Red)  # 지정한 경고문2 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn2, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문2 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == IN_PR[1] or IN_PR[0] == IN_PR[2] or IN_PR[0] == IN_PR[3] or IN_PR[1] == IN_PR[2] or IN_PR[1] == IN_PR[3] or IN_PR[2] == IN_PR[3]:  # 입력한 각각의 4자리 숫자가 1개라도 중복되는 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("중복되지 않는 숫자를 입력해주세요.")  # 조건에 따른 경고문3 출력
                            Warn_PR3 = return_print("중복되지 않는 숫자를 입력해주세요.")  # 경고문3를 변수로 지정한다.
                            Text_Warn3 = myFont2.render(Warn_PR3, True, Red)  # 지정한 경고문3 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn3, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문3 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        Text1 = myFont1.render(IN_PR, True, Text_Color)  # 위 조건에 만족하지 않는 print값을 폰트를 이용하여 Text변수를 생성한다.
                        screen.blit(Text1, [195, 340])  # 지정한 변수를 화면에 출력한다.
                        Text2 = myFont1.render(IN_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                        screen.blit(Text2, [640, 265])  # 지정한 변수를 화면에 출력한다.
                        s_count = 0  # s_count 값 설정
                        b_count = 0  # b_count 값 설정
                        for x in range(0, 4):  # x 범위 지정
                            for y in range(0, 4):  # y 범위 지정
                                if INPUT[x] == str(random1[y]) and x == y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수와 숫자 모두 같다면
                                    s_count += 1  # s_count 값을 +1 한다.
                                elif INPUT[x] == str(random1[y]) and x != y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수는 다르지만 숫자가 같다면
                                    b_count += 1  # b_count 값을 +1 한다.
                        if s_count == b_count == 0:  # 입력한 숫자 4개와 랜덤으로 생성된 숫자 4개가 다르다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("OUT")  # 조건에 따른 OUT 출력
                            OUT_PR = return_print("OUT")  # OUT 출력값을 변수로 지정한다.
                            Text_OUT1 = myFont1.render(OUT_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_OUT1, [400, 340])  # 지정한 변수를 화면에 출력한다.
                            Text_OUT2 = myFont1.render(OUT_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_OUT2, [860, 265])  # 지정한 변수를 화면에 출력한다.
                        elif s_count != 0 or b_count != 0:  # S나 B가 0이 아니라면
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print(s_count, "S", b_count, "B")  # 조건에 따른 S, B 결과값 출력
                            SB_PR = return_print(s_count, "S", b_count, "B")  # S, B 결과값을 변수로 지정한다.
                            Text_SB1 = myFont1.render(SB_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_SB1, [400, 340])  # 지정한 변수를 화면에 출력한다.
                            Text_SB2 = myFont1.render(SB_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_SB2, [860, 265])  # 지정한 변수를 화면에 출력한다.
                        print(t_count, "회")  # t_count 출력
                        INN_PR = return_print(t_count, "회")  # t_count값을 변수로 지정한다.
                        Text_INN = myFont1.render(INN_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                        screen.blit(Text_INN, [35, 340])  # 지정한 변수를 화면에 출력한다.
                        t_count += 1  # t_count값이 나왔으니 +1 한다.
                        INPUT = ''  # 입력상자에 숫자를 빈칸으로 바꾼다.
                        if s_count == 4:  # 입력한 숫자와 랜덤으로 생성한 숫자가 완벽히 일치한다면
                            Draw(screen, Black, [30, 907, 750, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("축하합니다! 승리하셨습니다! X버튼을 눌러주세요")  # 조건 달성 시 안내문 출력
                            WIN_PR = return_print("축하합니다! 승리하셨습니다! X버튼을 눌러주세요")  # 출력한 안내문을 변수로 지정한다.
                            Text_WIN = myFont2.render(WIN_PR, True, Green)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_WIN, [35, 907])  # 지정한 변수를 화면에 출력한다.
                    elif t_count == 8:  # 8번째 시도
                        print(INPUT)  # input_box에 입력한 숫자를 print한다.
                        IN_PR = return_print(INPUT)  # print값을 변수로 변환하여 게임 화면에 출력되게 한다.
                        if len(IN_PR) > 5:  # 4자리 숫자지만 엔터를 치면 len = 5로 인식되어 len > 5라고 조건을 두었다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 정확히 입력해주세요!")  # 조건에 따른 경고문1 출력
                            Warn_PR1 = return_print("4자리 숫자를 정확히 입력해주세요!")  # 경고문1을 변수로 지정한다.
                            Text_Warn1 = myFont2.render(Warn_PR1, True, Red)  # 지정한 경고문1 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn1, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문1 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == Except(IN_PR[0]) or IN_PR[1] == Except(IN_PR[1]) or IN_PR[2] == Except(IN_PR[2]) or IN_PR[3] == Except(IN_PR[3]):  # 입력한 print값이 각 자리마다 0~9가 아닌 다른 문자일 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 입력해주세요!")  # 조건에 따른 경고문2 출력
                            Warn_PR2 = return_print("4자리 숫자를 입력해주세요!")  # 경고문2를 변수로 지정한다.
                            Text_Warn2 = myFont2.render(Warn_PR2, True, Red)  # 지정한 경고문2 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn2, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문2 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == IN_PR[1] or IN_PR[0] == IN_PR[2] or IN_PR[0] == IN_PR[3] or IN_PR[1] == IN_PR[2] or IN_PR[1] == IN_PR[3] or IN_PR[2] == IN_PR[3]:  # 입력한 각각의 4자리 숫자가 1개라도 중복되는 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("중복되지 않는 숫자를 입력해주세요.")  # 조건에 따른 경고문3 출력
                            Warn_PR3 = return_print("중복되지 않는 숫자를 입력해주세요.")  # 경고문3를 변수로 지정한다.
                            Text_Warn3 = myFont2.render(Warn_PR3, True, Red)  # 지정한 경고문3 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn3, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문3 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        Text1 = myFont1.render(IN_PR, True, Text_Color)  # 위 조건에 만족하지 않는 print값을 폰트를 이용하여 Text변수를 생성한다.
                        screen.blit(Text1, [195, 390])  # 지정한 변수를 화면에 출력한다.
                        Text2 = myFont1.render(IN_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                        screen.blit(Text2, [640, 305])  # 지정한 변수를 화면에 출력한다.
                        s_count = 0  # s_count 값 설정
                        b_count = 0  # b_count 값 설정
                        for x in range(0, 4):  # x 범위 지정
                            for y in range(0, 4):  # y 범위 지정
                                if INPUT[x] == str(random1[y]) and x == y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수와 숫자 모두 같다면
                                    s_count += 1  # s_count 값을 +1 한다.
                                elif INPUT[x] == str(random1[y]) and x != y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수는 다르지만 숫자가 같다면
                                    b_count += 1  # b_count 값을 +1 한다.
                        if s_count == b_count == 0:  # 입력한 숫자 4개와 랜덤으로 생성된 숫자 4개가 다르다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("OUT")  # 조건에 따른 OUT 출력
                            OUT_PR = return_print("OUT")  # OUT 출력값을 변수로 지정한다.
                            Text_OUT1 = myFont1.render(OUT_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_OUT1, [400, 390])  # 지정한 변수를 화면에 출력한다.
                            Text_OUT2 = myFont1.render(OUT_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_OUT2, [860, 305])  # 지정한 변수를 화면에 출력한다.
                        elif s_count != 0 or b_count != 0:  # S나 B가 0이 아니라면
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print(s_count, "S", b_count, "B")  # 조건에 따른 S, B 결과값 출력
                            SB_PR = return_print(s_count, "S", b_count, "B")  # S, B 결과값을 변수로 지정한다.
                            Text_SB1 = myFont1.render(SB_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_SB1, [400, 390])  # 지정한 변수를 화면에 출력한다.
                            Text_SB2 = myFont1.render(SB_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_SB2, [860, 305])  # 지정한 변수를 화면에 출력한다.
                        print(t_count, "회")  # t_count 출력
                        INN_PR = return_print(t_count, "회")  # t_count값을 변수로 지정한다.
                        Text_INN = myFont1.render(INN_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                        screen.blit(Text_INN, [35, 390])  # 지정한 변수를 화면에 출력한다.
                        t_count += 1  # t_count값이 나왔으니 +1 한다.
                        INPUT = ''  # 입력상자에 숫자를 빈칸으로 바꾼다.
                        if s_count == 4:  # 입력한 숫자와 랜덤으로 생성한 숫자가 완벽히 일치한다면
                            Draw(screen, Black, [30, 907, 750, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("축하합니다! 승리하셨습니다! X버튼을 눌러주세요")  # 조건 달성 시 안내문 출력
                            WIN_PR = return_print("축하합니다! 승리하셨습니다! X버튼을 눌러주세요")  # 출력한 안내문을 변수로 지정한다.
                            Text_WIN = myFont2.render(WIN_PR, True, Green)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_WIN, [35, 907])  # 지정한 변수를 화면에 출력한다.
                    elif t_count == 9:  # 9번째 시도
                        print(INPUT)  # input_box에 입력한 숫자를 print한다.
                        IN_PR = return_print(INPUT)  # print값을 변수로 변환하여 게임 화면에 출력되게 한다.
                        if len(IN_PR) > 5:  # 4자리 숫자지만 엔터를 치면 len = 5로 인식되어 len > 5라고 조건을 두었다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 정확히 입력해주세요!")  # 조건에 따른 경고문1 출력
                            Warn_PR1 = return_print("4자리 숫자를 정확히 입력해주세요!")  # 경고문1을 변수로 지정한다.
                            Text_Warn1 = myFont2.render(Warn_PR1, True, Red)  # 지정한 경고문1 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn1, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문1 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == Except(IN_PR[0]) or IN_PR[1] == Except(IN_PR[1]) or IN_PR[2] == Except(IN_PR[2]) or IN_PR[3] == Except(IN_PR[3]):  # 입력한 print값이 각 자리마다 0~9가 아닌 다른 문자일 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 입력해주세요!")  # 조건에 따른 경고문2 출력
                            Warn_PR2 = return_print("4자리 숫자를 입력해주세요!")  # 경고문2를 변수로 지정한다.
                            Text_Warn2 = myFont2.render(Warn_PR2, True, Red)  # 지정한 경고문2 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn2, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문2 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == IN_PR[1] or IN_PR[0] == IN_PR[2] or IN_PR[0] == IN_PR[3] or IN_PR[1] == IN_PR[2] or IN_PR[1] == IN_PR[3] or IN_PR[2] == IN_PR[3]:  # 입력한 각각의 4자리 숫자가 1개라도 중복되는 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("중복되지 않는 숫자를 입력해주세요.")  # 조건에 따른 경고문3 출력
                            Warn_PR3 = return_print("중복되지 않는 숫자를 입력해주세요.")  # 경고문3를 변수로 지정한다.
                            Text_Warn3 = myFont2.render(Warn_PR3, True, Red)  # 지정한 경고문3 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn3, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문3 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        Text1 = myFont1.render(IN_PR, True, Text_Color)  # 위 조건에 만족하지 않는 print값을 폰트를 이용하여 Text변수를 생성한다.
                        screen.blit(Text1, [195, 440])  # 지정한 변수를 화면에 출력한다.
                        Text2 = myFont1.render(IN_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                        screen.blit(Text2, [640, 345])  # 지정한 변수를 화면에 출력한다.
                        s_count = 0  # s_count 값 설정
                        b_count = 0  # b_count 값 설정
                        for x in range(0, 4):  # x 범위 지정
                            for y in range(0, 4):  # y 범위 지정
                                if INPUT[x] == str(random1[y]) and x == y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수와 숫자 모두 같다면
                                    s_count += 1  # s_count 값을 +1 한다.
                                elif INPUT[x] == str(random1[y]) and x != y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수는 다르지만 숫자가 같다면
                                    b_count += 1  # b_count 값을 +1 한다.
                        if s_count == b_count == 0:  # 입력한 숫자 4개와 랜덤으로 생성된 숫자 4개가 다르다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("OUT")  # 조건에 따른 OUT 출력
                            OUT_PR = return_print("OUT")  # OUT 출력값을 변수로 지정한다.
                            Text_OUT1 = myFont1.render(OUT_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_OUT1, [400, 440])  # 지정한 변수를 화면에 출력한다.
                            Text_OUT2 = myFont1.render(OUT_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_OUT2, [860, 345])  # 지정한 변수를 화면에 출력한다.
                        elif s_count != 0 or b_count != 0:  # S나 B가 0이 아니라면
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print(s_count, "S", b_count, "B")  # 조건에 따른 S, B 결과값 출력
                            SB_PR = return_print(s_count, "S", b_count, "B")  # S, B 결과값을 변수로 지정한다.
                            Text_SB1 = myFont1.render(SB_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_SB1, [400, 440])  # 지정한 변수를 화면에 출력한다.
                            Text_SB2 = myFont1.render(SB_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_SB2, [860, 345])  # 지정한 변수를 화면에 출력한다.
                        print(t_count, "회")  # t_count 출력
                        INN_PR = return_print(t_count, "회")  # t_count값을 변수로 지정한다.
                        Text_INN = myFont1.render(INN_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                        screen.blit(Text_INN, [35, 440])  # 지정한 변수를 화면에 출력한다.
                        t_count += 1  # t_count값이 나왔으니 +1 한다.
                        INPUT = ''  # 입력상자에 숫자를 빈칸으로 바꾼다.
                        Draw(screen, Black, [30, 907, 750, 30])
                        print("정규이닝 끝! 연장전 시작!")  # t_count == 9 and s_count != 4일 경우 print값 출력
                        INFO = return_print("정규이닝 끝! 연장전 시작!")  # 출력된 print값을 변수로 지정
                        Text_INFO = myFont2.render(INFO, True, Sky)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                        screen.blit(Text_INFO, [35, 907])
                        if s_count == 4:  # 입력한 숫자와 랜덤으로 생성한 숫자가 완벽히 일치한다면
                            Draw(screen, Black, [30, 907, 750, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("축하합니다! 승리하셨습니다! X버튼을 눌러주세요")  # 조건 달성 시 안내문 출력
                            WIN_PR = return_print("축하합니다! 승리하셨습니다! X버튼을 눌러주세요")  # 출력한 안내문을 변수로 지정한다.
                            Text_WIN = myFont2.render(WIN_PR, True, Green)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_WIN, [35, 907])  # 지정한 변수를 화면에 출력한다.
                    elif t_count == 10:  # 10번째 시도
                        print(INPUT)  # input_box에 입력한 숫자를 print한다.
                        IN_PR = return_print(INPUT)  # print값을 변수로 변환하여 게임 화면에 출력되게 한다.
                        if len(IN_PR) > 5:  # 4자리 숫자지만 엔터를 치면 len = 5로 인식되어 len > 5라고 조건을 두었다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 정확히 입력해주세요!")  # 조건에 따른 경고문1 출력
                            Warn_PR1 = return_print("4자리 숫자를 정확히 입력해주세요!")  # 경고문1을 변수로 지정한다.
                            Text_Warn1 = myFont2.render(Warn_PR1, True, Red)  # 지정한 경고문1 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn1, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문1 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == Except(IN_PR[0]) or IN_PR[1] == Except(IN_PR[1]) or IN_PR[2] == Except(IN_PR[2]) or IN_PR[3] == Except(IN_PR[3]):  # 입력한 print값이 각 자리마다 0~9가 아닌 다른 문자일 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 입력해주세요!")  # 조건에 따른 경고문2 출력
                            Warn_PR2 = return_print("4자리 숫자를 입력해주세요!")  # 경고문2를 변수로 지정한다.
                            Text_Warn2 = myFont2.render(Warn_PR2, True, Red)  # 지정한 경고문2 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn2, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문2 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == IN_PR[1] or IN_PR[0] == IN_PR[2] or IN_PR[0] == IN_PR[3] or IN_PR[1] == IN_PR[2] or IN_PR[1] == IN_PR[3] or IN_PR[2] == IN_PR[3]:  # 입력한 각각의 4자리 숫자가 1개라도 중복되는 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("중복되지 않는 숫자를 입력해주세요.")  # 조건에 따른 경고문3 출력
                            Warn_PR3 = return_print("중복되지 않는 숫자를 입력해주세요.")  # 경고문3를 변수로 지정한다.
                            Text_Warn3 = myFont2.render(Warn_PR3, True, Red)  # 지정한 경고문3 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn3, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문3 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        Text1 = myFont1.render(IN_PR, True, Text_Color)  # 위 조건에 만족하지 않는 print값을 폰트를 이용하여 Text변수를 생성한다.
                        screen.blit(Text1, [195, 490])  # 지정한 변수를 화면에 출력한다.
                        Text2 = myFont1.render(IN_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                        screen.blit(Text2, [640, 385])  # 지정한 변수를 화면에 출력한다.
                        s_count = 0  # s_count 값 설정
                        b_count = 0  # b_count 값 설정
                        for x in range(0, 4):  # x 범위 지정
                            for y in range(0, 4):  # y 범위 지정
                                if INPUT[x] == str(random1[y]) and x == y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수와 숫자 모두 같다면
                                    s_count += 1  # s_count 값을 +1 한다.
                                elif INPUT[x] == str(random1[y]) and x != y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수는 다르지만 숫자가 같다면
                                    b_count += 1  # b_count 값을 +1 한다.
                        if s_count == b_count == 0:  # 입력한 숫자 4개와 랜덤으로 생성된 숫자 4개가 다르다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("OUT")  # 조건에 따른 OUT 출력
                            OUT_PR = return_print("OUT")  # OUT 출력값을 변수로 지정한다.
                            Text_OUT1 = myFont1.render(OUT_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_OUT1, [400, 490])  # 지정한 변수를 화면에 출력한다.
                            Text_OUT2 = myFont1.render(OUT_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_OUT2, [860, 385])  # 지정한 변수를 화면에 출력한다.
                        elif s_count != 0 or b_count != 0:  # S나 B가 0이 아니라면
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print(s_count, "S", b_count, "B")  # 조건에 따른 S, B 결과값 출력
                            SB_PR = return_print(s_count, "S", b_count, "B")  # S, B 결과값을 변수로 지정한다.
                            Text_SB1 = myFont1.render(SB_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_SB1, [400, 490])  # 지정한 변수를 화면에 출력한다.
                            Text_SB2 = myFont1.render(SB_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_SB2, [860, 385])  # 지정한 변수를 화면에 출력한다.
                        print(t_count, "회")  # t_count 출력
                        INN_PR = return_print(t_count, "회")  # t_count값을 변수로 지정한다.
                        Text_INN = myFont1.render(INN_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                        screen.blit(Text_INN, [35, 490])  # 지정한 변수를 화면에 출력한다.
                        t_count += 1  # t_count값이 나왔으니 +1 한다.
                        INPUT = ''  # 입력상자에 숫자를 빈칸으로 바꾼다.
                        if s_count == 4:  # 입력한 숫자와 랜덤으로 생성한 숫자가 완벽히 일치한다면
                            Draw(screen, Black, [30, 907, 750, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("축하합니다! 승리하셨습니다! X버튼을 눌러주세요")  # 조건 달성 시 안내문 출력
                            WIN_PR = return_print("축하합니다! 승리하셨습니다! X버튼을 눌러주세요")  # 출력한 안내문을 변수로 지정한다.
                            Text_WIN = myFont2.render(WIN_PR, True, Green)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_WIN, [35, 907])  # 지정한 변수를 화면에 출력한다.
                    elif t_count == 11:  # 11번째 시도
                        print(INPUT)  # input_box에 입력한 숫자를 print한다.
                        IN_PR = return_print(INPUT)  # print값을 변수로 변환하여 게임 화면에 출력되게 한다.
                        if len(IN_PR) > 5:  # 4자리 숫자지만 엔터를 치면 len = 5로 인식되어 len > 5라고 조건을 두었다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 정확히 입력해주세요!")  # 조건에 따른 경고문1 출력
                            Warn_PR1 = return_print("4자리 숫자를 정확히 입력해주세요!")  # 경고문1을 변수로 지정한다.
                            Text_Warn1 = myFont2.render(Warn_PR1, True, Red)  # 지정한 경고문1 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn1, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문1 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == Except(IN_PR[0]) or IN_PR[1] == Except(IN_PR[1]) or IN_PR[2] == Except(IN_PR[2]) or IN_PR[3] == Except(IN_PR[3]):  # 입력한 print값이 각 자리마다 0~9가 아닌 다른 문자일 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 입력해주세요!")  # 조건에 따른 경고문2 출력
                            Warn_PR2 = return_print("4자리 숫자를 입력해주세요!")  # 경고문2를 변수로 지정한다.
                            Text_Warn2 = myFont2.render(Warn_PR2, True, Red)  # 지정한 경고문2 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn2, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문2 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == IN_PR[1] or IN_PR[0] == IN_PR[2] or IN_PR[0] == IN_PR[3] or IN_PR[1] == IN_PR[2] or IN_PR[1] == IN_PR[3] or IN_PR[2] == IN_PR[3]:  # 입력한 각각의 4자리 숫자가 1개라도 중복되는 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("중복되지 않는 숫자를 입력해주세요.")  # 조건에 따른 경고문3 출력
                            Warn_PR3 = return_print("중복되지 않는 숫자를 입력해주세요.")  # 경고문3를 변수로 지정한다.
                            Text_Warn3 = myFont2.render(Warn_PR3, True, Red)  # 지정한 경고문3 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn3, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문3 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        Text1 = myFont1.render(IN_PR, True, Text_Color)  # 위 조건에 만족하지 않는 print값을 폰트를 이용하여 Text변수를 생성한다.
                        screen.blit(Text1, [195, 535])  # 지정한 변수를 화면에 출력한다.
                        Text2 = myFont1.render(IN_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                        screen.blit(Text2, [640, 425])  # 지정한 변수를 화면에 출력한다.
                        s_count = 0  # s_count 값 설정
                        b_count = 0  # b_count 값 설정
                        for x in range(0, 4):  # x 범위 지정
                            for y in range(0, 4):  # y 범위 지정
                                if INPUT[x] == str(random1[y]) and x == y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수와 숫자 모두 같다면
                                    s_count += 1  # s_count 값을 +1 한다.
                                elif INPUT[x] == str(random1[y]) and x != y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수는 다르지만 숫자가 같다면
                                    b_count += 1  # b_count 값을 +1 한다.
                        if s_count == b_count == 0:  # 입력한 숫자 4개와 랜덤으로 생성된 숫자 4개가 다르다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("OUT")  # 조건에 따른 OUT 출력
                            OUT_PR = return_print("OUT")  # OUT 출력값을 변수로 지정한다.
                            Text_OUT1 = myFont1.render(OUT_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_OUT1, [400, 535])  # 지정한 변수를 화면에 출력한다.
                            Text_OUT2 = myFont1.render(OUT_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_OUT2, [860, 425])  # 지정한 변수를 화면에 출력한다.
                        elif s_count != 0 or b_count != 0:  # S나 B가 0이 아니라면
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print(s_count, "S", b_count, "B")  # 조건에 따른 S, B 결과값 출력
                            SB_PR = return_print(s_count, "S", b_count, "B")  # S, B 결과값을 변수로 지정한다.
                            Text_SB1 = myFont1.render(SB_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_SB1, [400, 535])  # 지정한 변수를 화면에 출력한다.
                            Text_SB2 = myFont1.render(SB_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_SB2, [860, 425])  # 지정한 변수를 화면에 출력한다.
                        print(t_count, "회")  # t_count 출력
                        INN_PR = return_print(t_count, "회")  # t_count값을 변수로 지정한다.
                        Text_INN = myFont1.render(INN_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                        screen.blit(Text_INN, [35, 535])  # 지정한 변수를 화면에 출력한다.
                        t_count += 1  # t_count값이 나왔으니 +1 한다.
                        INPUT = ''  # 입력상자에 숫자를 빈칸으로 바꾼다.
                        if s_count == 4:  # 입력한 숫자와 랜덤으로 생성한 숫자가 완벽히 일치한다면
                            Draw(screen, Black, [30, 907, 750, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("축하합니다! 승리하셨습니다! X버튼을 눌러주세요")  # 조건 달성 시 안내문 출력
                            WIN_PR = return_print("축하합니다! 승리하셨습니다! X버튼을 눌러주세요")  # 출력한 안내문을 변수로 지정한다.
                            Text_WIN = myFont2.render(WIN_PR, True, Green)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_WIN, [35, 907])  # 지정한 변수를 화면에 출력한다.
                    elif t_count == 12:  # 12번째 시도
                        print(INPUT)  # input_box에 입력한 숫자를 print한다.
                        IN_PR = return_print(INPUT)  # print값을 변수로 변환하여 게임 화면에 출력되게 한다.
                        if len(IN_PR) > 5:  # 4자리 숫자지만 엔터를 치면 len = 5로 인식되어 len > 5라고 조건을 두었다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 정확히 입력해주세요!")  # 조건에 따른 경고문1 출력
                            Warn_PR1 = return_print("4자리 숫자를 정확히 입력해주세요!")  # 경고문1을 변수로 지정한다.
                            Text_Warn1 = myFont2.render(Warn_PR1, True, Red)  # 지정한 경고문1 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn1, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문1 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == Except(IN_PR[0]) or IN_PR[1] == Except(IN_PR[1]) or IN_PR[2] == Except(IN_PR[2]) or IN_PR[3] == Except(IN_PR[3]):  # 입력한 print값이 각 자리마다 0~9가 아닌 다른 문자일 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("4자리 숫자를 입력해주세요!")  # 조건에 따른 경고문2 출력
                            Warn_PR2 = return_print("4자리 숫자를 입력해주세요!")  # 경고문2를 변수로 지정한다.
                            Text_Warn2 = myFont2.render(Warn_PR2, True, Red)  # 지정한 경고문2 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn2, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문2 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        elif IN_PR[0] == IN_PR[1] or IN_PR[0] == IN_PR[2] or IN_PR[0] == IN_PR[3] or IN_PR[1] == IN_PR[2] or IN_PR[1] == IN_PR[3] or IN_PR[2] == IN_PR[3]:  # 입력한 각각의 4자리 숫자가 1개라도 중복되는 경우
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("중복되지 않는 숫자를 입력해주세요.")  # 조건에 따른 경고문3 출력
                            Warn_PR3 = return_print("중복되지 않는 숫자를 입력해주세요.")  # 경고문3를 변수로 지정한다.
                            Text_Warn3 = myFont2.render(Warn_PR3, True, Red)  # 지정한 경고문3 파일을 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_Warn3, [35, 907])  # 지정한 변수를 화면에 출력한다.
                            continue  # 위 조건 달성 시 경고문3 출력 후 아래 조건을 수행하지 않고 다시 현재 조건문으로 점프한다.
                        Text1 = myFont1.render(IN_PR, True, Text_Color)  # 위 조건에 만족하지 않는 print값을 폰트를 이용하여 Text변수를 생성한다.
                        screen.blit(Text1, [195, 580])  # 지정한 변수를 화면에 출력한다.
                        Text2 = myFont1.render(IN_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                        screen.blit(Text2, [640, 465])  # 지정한 변수를 화면에 출력한다.
                        s_count = 0  # s_count 값 설정
                        b_count = 0  # b_count 값 설정
                        for x in range(0, 4):  # x 범위 지정
                            for y in range(0, 4):  # y 범위 지정
                                if INPUT[x] == str(random1[y]) and x == y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수와 숫자 모두 같다면
                                    s_count += 1  # s_count 값을 +1 한다.
                                elif INPUT[x] == str(random1[y]) and x != y:  # 입력한 숫자와 랜덤으로 생성된 숫자가 자릿수는 다르지만 숫자가 같다면
                                    b_count += 1  # b_count 값을 +1 한다.
                        if s_count == b_count == 0:  # 입력한 숫자 4개와 랜덤으로 생성된 숫자 4개가 다르다.
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("OUT")  # 조건에 따른 OUT 출력
                            OUT_PR = return_print("OUT")  # OUT 출력값을 변수로 지정한다.
                            Text_OUT1 = myFont1.render(OUT_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_OUT1, [400, 580])  # 지정한 변수를 화면에 출력한다.
                            Text_OUT2 = myFont1.render(OUT_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_OUT2, [860, 465])  # 지정한 변수를 화면에 출력한다.
                        elif s_count != 0 or b_count != 0:  # S나 B가 0이 아니라면
                            Draw(screen, Black, [30, 907, 600, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print(s_count, "S", b_count, "B")  # 조건에 따른 S, B 결과값 출력
                            SB_PR = return_print(s_count, "S", b_count, "B")  # S, B 결과값을 변수로 지정한다.
                            Text_SB1 = myFont1.render(SB_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_SB1, [400, 580])  # 지정한 변수를 화면에 출력한다.
                            Text_SB2 = myFont1.render(SB_PR, True, Gold)  # 배경 때문에 글자가 안 보일 경우를 대비하여 다른 색깔로 Text변수를 생성한다.
                            screen.blit(Text_SB2, [860, 465])  # 지정한 변수를 화면에 출력한다.
                        print(t_count, "회")  # t_count 출력
                        INN_PR = return_print(t_count, "회")  # t_count값을 변수로 지정한다.
                        Text_INN = myFont1.render(INN_PR, True, Text_Color)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                        screen.blit(Text_INN, [35, 580])  # 지정한 변수를 화면에 출력한다.
                        t_count += 1  # t_count값이 나왔으니 +1 한다.
                        INPUT = ''  # 입력상자에 숫자를 빈칸으로 바꾼다.
                        if s_count == 4:  # 입력한 숫자와 랜덤으로 생성한 숫자가 완벽히 일치한다면
                            Draw(screen, Black, [30, 907, 750, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                            print("축하합니다! 마지막 기회에서 승리하셨습니다! X버튼을 눌러주세요")  # 조건 달성 시 안내문 출력
                            WIN_PR = return_print("축하합니다! 마지막 기회에서 승리하셨습니다! X버튼을 눌러주세요")  # 출력한 안내문을 변수로 지정한다.
                            Text_WIN = myFont2.render(WIN_PR, True, Green)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                            screen.blit(Text_WIN, [35, 907])  # 지정한 변수를 화면에 출력한다.
                    if t_count == 13 and s_count != 4: # 12회의 기회를 초과하고 s_count가 4가 아닌 경우
                        Draw(screen, Black, [30, 907, 750, 30])  # 경고문/안내문이 뜨기 전 기존에 있는 경고문/안내문을 지우기 위해 도형을 그린다.
                        print("패배하셨습니다...정답은 {}{}{}{}입니다. X버튼을 눌러주세요.".format(random1[0],random1[1],random1[2],random1[3]))  # 위 조건 만족 시 안내문 출력과 문자열을 보기 좋게 출력하기 위한 format을 활용하여 정답 출력
                        INFO2 = return_print("패배하셨습니다...\n정답은 {}{}{}{}입니다. X버튼을 눌러주세요.".format(random1[0],random1[1],random1[2],random1[3]))  # 출력값을 변수로 지정
                        Text_INFO2 = myFont2.render(INFO2, True, Red)  # 지정한 변수를 폰트를 이용하여 Text변수로 생성한다.
                        screen.blit(Text_INFO2, [35, 907])

                elif event.key == pygame.K_BACKSPACE:  # Backspace 입력 시
                    INPUT = INPUT[:-1]  # 문자 하나를 지운다.
                else:
                    INPUT += event.unicode  # Enter키를 누르면 print(INPUT) 코드를 수행할 수 있게 해준다.

        if event.type == pygame.MOUSEBUTTONDOWN:  # 숫자 야구공 아이콘 클릭시 도형을 만들어 아이콘이 사라지는 것처럼 만든다.
            if 631 <= event.pos[0] <= 691 and 510 <= event.pos[1] <= 570:  # 조건에 맞는 위치를 클릭하면
                Draw(screen, Black, [631, 510, 60, 60])  # 지정한 위치에 그림을 그린다.
            elif 694 <= event.pos[0] <= 754 and 511 <= event.pos[1] <= 570:  # 조건에 맞는 위치를 클릭하면
                Draw(screen, Black, [694, 511, 60, 60])  # 지정한 위치에 그림을 그린다.
            elif 757 <= event.pos[0] <= 817 and 510 <= event.pos[1] <= 570:  # 조건에 맞는 위치를 클릭하면
                Draw(screen, Black, [757, 510, 60, 60])  # 지정한 위치에 그림을 그린다.
            elif 820 <= event.pos[0] <= 880 and 510 <= event.pos[1] <= 570:  # 조건에 맞는 위치를 클릭하면
                Draw(screen, Black, [820, 510, 60, 60])  # 지정한 위치에 그림을 그린다.
            elif 883 <= event.pos[0] <= 943 and 510 <= event.pos[1] <= 570:  # 조건에 맞는 위치를 클릭하면
                Draw(screen, Black, [883, 510, 60, 60])  # 지정한 위치에 그림을 그린다.
            elif 631 <= event.pos[0] <= 691 and 575 <= event.pos[1] <= 635:  # 조건에 맞는 위치를 클릭하면
                Draw(screen, Black, [631, 575, 60, 60])  # 지정한 위치에 그림을 그린다.
            elif 694 <= event.pos[0] <= 754 and 575 <= event.pos[1] <= 635:  # 조건에 맞는 위치를 클릭하면
                Draw(screen, Black, [694, 575, 60, 60])  # 지정한 위치에 그림을 그린다.
            elif 757 <= event.pos[0] <= 817 and 575 <= event.pos[1] <= 635:  # 조건에 맞는 위치를 클릭하면
                Draw(screen, Black, [757, 575, 60, 60])  # 지정한 위치에 그림을 그린다.
            elif 820 <= event.pos[0] <= 880 and 575 <= event.pos[1] <= 635:  # 조건에 맞는 위치를 클릭하면
                Draw(screen, Black, [820, 575, 60, 60])  # 지정한 위치에 그림을 그린다.
            elif 883 <= event.pos[0] <= 943 and 575 <= event.pos[1] <= 635:  # 조건에 맞는 위치를 클릭하면
                Draw(screen, Black, [883, 575, 60, 60])  # 지정한 위치에 그림을 그린다.
    clock.tick(30)  # 초당 30번의 화면을 출력
    pygame.display.update()  # 전체 screen 업데이트
pygame.quit()  # pygame 종료

# 원래는 t_count == 12 or s_count == 4일 경우 게임을 자동으로 종료하는 코드를 작성하려고 했지만 게임 완료 후 자신이 입력했던 숫자를 보고
# 어느 부분에서 잘못 판단해서 숫자 유추가 꼬였다던가 등의 자기 자신만의 피드백을 했던 경험을 토대로 게임을 스스로 피드백 후 종료하는 방향으로 잡았습니다.