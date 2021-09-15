from TTs import *
from submit_main_def import *
import csv


counter = 0
FPSCLOCK = pygame.time.Clock()
pygame.init()
# 추후에 바뀔예정
run = True
part = 0
right = 0
p_part = 0
ko = 0
num = 0
start = 0
step = 0
fever = 0
input_t = 0
first = 0
key_1 = 0
X_position = 100
Y_position = 150
X_size = 150
Y_size = 150
red = 0
green = 0
yellow = 0
num_input = 0
button_next = 0
button_down = 0
s = 0 #한번만 읽도록 만드는 일종의 카운터
n = 0 #테스트용
input_1 = ''
check = 0
check_front = 0
intro_page = 0
end = 0
checking_personal_info = 0
extra_TTs = 0
checking_gpio = 0
#show = 33
import csv
# visit = 첫방문질문 리스트
# visits = 대답받는 리스트
# visit_num = 대답받는 값
visits = []
sexs = []
births = []
p_nums = []
whys = []
agrees = []
names = []
num_input = 1
checking_gpio = 0

# pygame 본격 시작문
while run:
    checking_gpio = 0
    num_input = 0
    if check == 1:
        n = 0
    if check_front == 1:
        n = 0
    pygame.display.flip()  # 디스플레이
    pressed = pygame.key.get_pressed()  # 키보드 인식을 위한, getpressed는 키가 눌렸을때를 인식

    for event in pygame.event.get():
        interface.fill((255, 255, 255))  # 디스플레이 배경색 RGB
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    part2_symptom_002()

    pygame.display.update()
    # FPSCLOCK.tick(500)
    pygame.time.delay(500)
    #check_front = 0
pygame.quit()
#f.close()
