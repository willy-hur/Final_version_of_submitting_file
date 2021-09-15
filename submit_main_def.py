import pygame
import time

# from TTs import*
pygame.init()  # pygame을 시작할다고 선언
interface = pygame.display.set_mode((1280, 650), 0, 32)  # 해상도 1240*720의 창을 정의


# 선택지 최대 num_size

def first_time():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("처음 방문이신가요?.", True, (0, 0, 0))
    interface.blit(message1, (400, 300))


def personal_info():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("개인정보 수집에 동의 하십니까?.", True, (0, 0, 0))
    interface.blit(message1, (400, 300))


def keyshape(counter, input_1):
    # 여기서는 키패드에서 받아온 한글, 숫자 출력문
    # 아래 4줄은 완성후 지울 예정
    if counter % 2 == 0:
        input_1 = "부산시 금정구 장전|"
    if counter % 2 == 1:
        input_1 = "엉"
    # 아래 3줄은 파이게임 창에서 택스트 출력문
    myfont = pygame.font.Font('IropkeBatangM.ttf', 35)  # 폰트 종류, 크기 설정
    message1 = myfont.render(input_1, True, (0, 0, 0))  # 출력할 텍스트, 하이라이트 색 설정
    interface.blit(message1, (465, 420))  # 출력되는 부분, 위치 설정


def edge(X_position, Y_position, X_size, Y_size):  # 사각형 선택지중 단순히 모양만 있는 부분
    color = (0, 0, 0)
    width_draw = 5
    pygame.draw.rect(interface, color, (X_position, Y_position, X_size, Y_size), width_draw)


# 열 체크하는 사진 띄우는 파트
def fever1():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_1/fever/fever_check.png'), (450, 200))
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("열 채크를 시작 합니다.", True, (0, 0, 0))
    interface.blit(message1, (400, 500))


def fever2():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_1/fever/001.png'), (450, 200))


def fever3():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_1/fever/002.png'), (400, 200))


# 파트 1의 시작. 파일 이름은 pictures에 0폴더를 경로로
# 가장 처음 시작 선별진료소 사진을 띄워준다
def part1_show():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/001.png'), (470, 200))


# 가장처음 시작 부분에 나올 문장 출력
def intro():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render('안녕하세요 이길입니다. 이 기기는 시청각장애인분들의 길이 되어주기 위하여 제작하였습니다.', True, (0, 0, 0))
    interface.blit(message1, (5, 500))


def part1_intro():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("다음으로 넘어가려면 다음을 누르세요 만약 보지 못했을 경우 뒤로 버튼을 눌러주세요.", True, (0, 0, 0))
    # 다음 버튼 핀번호 설정 포트 35
    interface.blit(message1, (5, 540))


def part1_002():
    # 음성 추가
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/002.png'), (400, 200))


def part1_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/003.png'), (550, 200))


def part1_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/004.png'), (500, 200))


def part1_005():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/005.png'), (500, 200))


def part1_006():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/006.png'), (400, 200))


def part1_007():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/0/007.png'), (400, 200))


def next():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("다음을 눌러 주세요.", True, (0, 0, 0))
    interface.blit(message1, (450, 290))


# 다음을 눌러주세요 출력 2와의 차이는 위치의 차이이다
def next_2():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("다음을 눌러 주세요.", True, (0, 0, 0))
    interface.blit(message1, (850, 550))


# 예 아니요 택스트 출력 파트
def yes(red, green, yellow):
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("예", True, (red, green, yellow))
    interface.blit(message1, (300, 500))


# 아니요를 출력
def no(red, green, yellow):
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("아니요", True, (red, green, yellow))
    interface.blit(message1, (900, 500))


def man(red, green, yellow):
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("남", True, (red, green, yellow))
    interface.blit(message1, (300, 500))


# 아니요를 출력
def woman(red, green, yellow):
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("여", True, (red, green, yellow))
    interface.blit(message1, (900, 500))


# 파트2의 시작 경로 위치는 picture의 1 폴더
def part2_start():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("문진표 작성을 시작합니다.", True, (0, 0, 0))
    interface.blit(message1, (400, 300))


# part2 사진출력
def part2_family_001():
    source = 'C:/Users\/JunJe Hur/Desktop/picture/1/family/001.png'
    interface.blit(pygame.image.load(source), (550, 250))


# 글씨를 화면으로 출력하는 코드
def name_def():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 38)
    message1 = myfont.render("이름을 입력해주세요.", True, (0, 0, 0))
    interface.blit(message1, (460, 150))


def sex_def():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 38)
    message1 = myfont.render("성별을 입력해주세요.", True, (0, 0, 0))
    # 다음 버튼 핀번호 설정 포트 35
    interface.blit(message1, (460, 150))


def birth_def():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 38)
    message1 = myfont.render("생년월일을 입력해주세요.", True, (0, 0, 0))
    # 다음 버튼 핀번호 설정 포트 35
    interface.blit(message1, (460, 150))


def phone_number():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 38)
    message1 = myfont.render("전화 번호를 입력해주세요.", True, (0, 0, 0))
    # 다음 버튼 핀번호 설정 포트 35
    interface.blit(message1, (300, 100))


def juso():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("주소를 입력해주세요, 맞는 번호를 누르시면 됩니다.", True, (0, 0, 0))
    interface.blit(message1, (200, 100))


def part2_family_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/family/002.png'), (550, 250))


#############################################
def part2_family_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/family/003.png'), (450, 200))


##############################################
def part2_family_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/family/004.png'), (200, 200))


def part2_family_005():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/family/005.png'), (525, 230))


def part2_family_006():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/family/006.png'), (200, 200))


# 파트2에서 symptom부분의 p_part
def check_S():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("증상 확인란 입니다.", True, (0, 0, 0))
    interface.blit(message1, (10, 300))


# 이부분은 아래 여행력 확인 부분
def check_T():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 30)
    message1 = myfont.render("접촉 경위를 확인 합니다. 이곳을 방문하게된 이유와 맞는 것을 골라주세요", True, (0, 0, 0))
    interface.blit(message1, (10, 300))


# 파트2에서 symptom부분의 p_part
def part2_symptom_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/001.png'), (200, 200))


def part2_symptom_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/002.png'), (100, 150))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/003.png'), (100, 300))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/010.png'), (850, 160))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/011.png'), (850, 310))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/012.png'), (1010, 310))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/009.png'), (1010, 160))


def part2_symptom_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/004.png'), (200, 200))


def part2_symptom_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/005.png'), (200, 200))


def part2_symptom_005():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/006.png'), (200, 200))


def part2_symptom_006():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/007.png'), (200, 200))


def part2_symptom_007():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/symptom/008.png'), (200, 200))


# 파트2에서 travel 부분의 p_part

def part2_travel_final():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/001.png'), (200, 150))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/002.png'), (400, 150))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/003.png'), (600, 150))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/004.png'), (800, 150))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/005.png'), (200, 350))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/006.png'), (400, 350))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/007.jpg'), (600, 350))


def part2_travel_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/001.png'), (200, 200))


def part2_travel_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/002.png'), (200, 200))
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/003.png'), (200, 200))


def part2_travel_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/004.png'), (200, 200))


def part2_travel_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/1/travel/005.png'), (200, 200))


# 파트3 위치는 pictures부분에서 2_1폴더
def part3_start():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_1/Medical_office_001.png'), (0, 0))


''''
def part3_1_Counseling001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_1/Counseling/Medical_office_001.png'), (200, 200))
'''


# 코 검사
def part3_intro():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/Medical_office_002.png'), (0, 0))


def part3_N_000():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/nose_swab_test.png'), (200, 200))


def part3_N_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/N001.png'), (200, 200))


def part3_N_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/N002.png'), (200, 200))


def part3_N_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/N003.png'), (200, 200))


def part3_N_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/N004.png'), (200, 200))


# 입 검사
def part3_M_intro():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/mouth_swab_test.png'), (200, 200))


def part3_M_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/M001.png'), (200, 200))


def part3_M_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/M002.png'), (200, 200))


def part3_M_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/M003.png'), (200, 200))


def part3_M_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/M004.png'), (200, 200))


def part3_M_005():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/M005.png'), (200, 200))


def part3_M_006():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/M006.png'), (200, 200))


# 가래
def part3_P_intro():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/phlegm_test.png'), (100, 100))


def part3_P_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/P001.png'), (200, 200))


def part3_P_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/P002.png'), (200, 200))


def part3_P_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/P003.png'), (200, 200))


def part3_P_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/2_2/P004.png'), (200, 200))


# 집
def part4_H_intro():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("집에서 해야할 주의 사항입니다.", True, (0, 0, 0))
    interface.blit(message1, (10, 300))


def part4_H_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/001.png'), (200, 200))


def part4_H_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/002.png'), (200, 200))


def part4_H_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/003.png'), (200, 200))


def part4_H_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/004.png'), (200, 200))


def part4_H_005():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/005.png'), (200, 200))


def part4_H_006():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/006.png'), (200, 200))


def part4_H_007():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/007.png'), (200, 200))


def part4_H_008():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/008.png'), (200, 200))


def part4_H_009():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/009.png'), (200, 200))


def part4_H_010():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/010.png'), (200, 200))


# 화장실
def part4_B_intro():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 50)
    message1 = myfont.render("화장실에서 해야할 주의 사항입니다.", True, (0, 0, 0))
    interface.blit(message1, (10, 300))


def part4_B_001():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/bathroom/001.png'), (200, 200))


def part4_B_002():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/bathroom/002.png'), (200, 200))


def part4_B_003():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/bathroom/003.png'), (200, 200))


def part4_B_004():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/bathroom/004.png'), (200, 200))


def part4_B_005():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/bathroom/005.png'), (200, 200))


def part4_B_006():
    interface.blit(pygame.image.load('C:/Users\/JunJe Hur/Desktop/picture/3/bathroom/006.png'), (200, 200))


def juso_gu():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("1. 중구, 2. 서구, 3. 동구, 4. 영도구, 5. 부산진구, 6. 동래구, 7. 남구, 8. 북구, 9. 해운대구,", True, (0, 0, 0))
    interface.blit(message1, (5, 420))
    message2 = myfont.render("10. 사하구, 11. 금정구, 12. 강서구, 13. 연제구, 14.수영구, 15. 사상구, 16. 기장구.", True, (0, 0, 0))
    # 다음 버튼 핀번호 설정 포트 35
    interface.blit(message2, (5, 460))


def juso_junggo():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("1. 영주동, 2. 대창동, 3. 중앙동, 4. 동광동, 5. 대청동, 6. 보수동, 7. 부평동, ", True, (0, 0, 0))
    interface.blit(message1, (5, 500))
    message2 = myfont.render("8. 신창동, 9. 창선동, 10. 광복동, 11. 남포동.", True, (0, 0, 0))
    # 다음 버튼 핀번호 설정 포트 35
    interface.blit(message2, (5, 540))


def juso_sugu():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("1. 동대신동, 2. 서대신동, 3. 부용동, 4. 부민동, 5. 토성동, 6. 아미동,", True, (0, 0, 0))
    interface.blit(message1, (5, 500))
    message2 = myfont.render("7. 조장동, 8. 충무동, 9. 남부민동, 10. 암남동.", True, (0, 0, 0))
    # 다음 버튼 핀번호 설정 포트 35
    interface.blit(message2, (5, 540))


def juso_donggu():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("1. 초량동, 2. 수정동, 3. 좌천동, 4. 범일동.", True, (0, 0, 0))
    interface.blit(message1, (5, 500))


def juso_yongdogu():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("1. 대교동, 2. 대평동, 3. 남항동, 4. 영선동, 5. 신성동, ", True, (0, 0, 0))
    interface.blit(message1, (5, 500))
    message2 = myfont.render("6. 봉래동, 7. 청학동, 8. 동삼동.", True, (0, 0, 0))
    # 다음 버튼 핀번호 설정 포트 35
    interface.blit(message2, (5, 540))


def juso_busanjingu():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("1. 양정동, 2. 전포동, 3. 부전동, 4. 범천동, 5. 범전동, 6. 연지동,", True, (0, 0, 0))
    interface.blit(message1, (5, 500))
    message2 = myfont.render("7. 초읍동, 8.부암동, 9. 당감동, 10. 가야동, 11. 개금동.", True, (0, 0, 0))
    # 다음 버튼 핀번호 설정 포트 35
    interface.blit(message2, (5, 540))


def juso_donglaygu():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("1. 명장동, 2. 안락동, 3. 칠산동, 4. 낙민동, 5. 복천동, 6. 수안동,", True, (0, 0, 0))
    interface.blit(message1, (5, 500))
    message2 = myfont.render("7. 명륜동, 8. 온천동, 9. 사직동.", True, (0, 0, 0))
    # 다음 버튼 핀번호 설정 포트 35
    interface.blit(message2, (5, 540))


def juso_namgu():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("1. 대연동, 2. 용호동, 3. 용당동, 4. 문현동, 5. 우암동, 6. 감만동", True, (0, 0, 0))
    interface.blit(message1, (5, 500))


def juso_bokygu():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("1. 금곡동, 2. 화명동, 3. 만덕동, 4. 덕천동, 5. 구포동.", True, (0, 0, 0))
    interface.blit(message1, (5, 500))


def juso_heyundaygu():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("1. 반송동, 2. 석대동, 3. 반여동, 4. 재송동, 5. 우동, 6. 중동, 7. 좌동, 8. 송정동", True, (0, 0, 0))
    interface.blit(message1, (5, 500))


def juso_sahagu():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("1. 괴정동, 2. 당리동, 3. 하단동, 4. 신평동, 5. 장림동, 6. 다대동, 7. 구평동, 8. 감천동", True, (0, 0, 0))
    interface.blit(message1, (5, 500))


def juso_gumjunggu():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("1. 두구동, 2. 노포동, 3. 청룡동, 4. 남산동, 5. 선동, 6. 오륜동, 7. 구서동, 8. 장전동,", True, (0, 0, 0))
    interface.blit(message1, (5, 500))
    message2 = myfont.render("9. 부곡동, 10. 서동, 11. 금사동, 12. 회동동, 13. 금성동.", True, (0, 0, 0))
    # 다음 버튼 핀번호 설정 포트 35
    interface.blit(message2, (5, 540))


def juso_gangsogu():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("1. 대저1동, 2. 강동동, 3. 명지동, 4. 죽림동, 5. 식만동, 6. 죽동동, 7. 봉림동, 8. 송정동, 9. 화전동,", True,
                             (0, 0, 0))
    interface.blit(message1, (5, 460))
    message2 = myfont.render(" 10. 녹산동, 11. 생곡동, 12.구랑동, 13. 지사동, 14. 미음동, 15. 범방동, 16. 신호동", True, (0, 0, 0))
    # 다음 버튼 핀번호 설정 포트 35
    interface.blit(message2, (5, 500))
    message3 = myfont.render("17. 동선동, 18. 성북동, 19. 눌차동, 20. 천성동, 21. 대항동.", True, (0, 0, 0))
    # 다음 버튼 핀번호 설정 포트 35
    interface.blit(message3, (5, 540))


def juso_yenjaegu():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("1. 거제동, 2. 연산동.", True, (0, 0, 0))
    interface.blit(message1, (5, 500))


def juso_suyonggu():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("1. 망미동, 2. 수영동, 3. 민락동, 4. 광안동, 5. 남천동.", True, (0, 0, 0))
    interface.blit(message1, (5, 500))


def juso_sasanggu():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("1. 삼락동, 2. 모라동, 3. 덕포동, 4. 괘법동, 5. 감전동, 6. 주례동, 7. 학장동, 8. 엄궁동.", True, (0, 0, 0))
    interface.blit(message1, (5, 500))


def juso_gijianggu():
    myfont = pygame.font.Font('IropkeBatangM.ttf', 33)
    message1 = myfont.render("1. 기장읍, 2. 장안읍, 3. 정관읍, 4. 일광면, 5. 철마면.", True, (0, 0, 0))
    interface.blit(message1, (5, 500))


ad = ['1.중구', '2.서구', '3.동구', '4.영도구', '5.부산진구', '6.동래구', '7.남구', '8.북구', '9.해운대구', '10.사하구', '11.금정구', '12.강서구', '13.연제구', '14.수영구', '15.사상구',
      '16.기장구']
ad_jg = ['1.영주동', '2.대창동', '3.중앙동', '4.동광동', '5.대창동', '6.보수동', '7.부평동', '8.신창동', '9.창선동', '10.광복동', '11.남포동']

ad_sg = ['1.동대신동', '2.서대신동', '3.부용동', '4.부민동', '5.토성동', '6.아미동', '7.조장동', '8.충무동', '9.남부민동', '10.암남동']

ad_dg = ['1.초량동', '2.수정동', '3.좌천동', '4.범일동']

ad_ydg = ['1.대교동', '2.대평동', '3.남항동', '4.영선동', '5.신성동', '6.봉래동', '7.청학동', '8.동삼동']

ad_jg = ['1.양정동', '2.전포동', '3.부전동', '4.범천동', '5.범전동', '6.연지동', '7.초읍동', '8.부암동', '9.당감동', '10.가야동', '11.개금동']

ad_drg = ['1.명장동', '2.안락동', '3.칠산동', '4.낙민동', '5.복천동', '6.수안동', '7.명륜동', '8.온천동', '9.사직동']

ad_ng = ['1.대연동', '2.용호동', '3.용당동', '4.문현동', '5.우암동', '6.감만동']

ad_bg = ['1.금곡동', '2.화명동', '3.만덕동', '4.덕천동', '5.구포동']

ad_hudg = ['1.반송동', '2.석대동', '3.반여동', '4.재송동', '5.우동', '6.중동', '7.좌동', '8.송정동']

ad_shg = ['1.괴정동', '2.당리동', '3.하단동', '4.신평동', '5.장림동', '6.다대동', '7.구평동', '8.감천동']

ad_gjg = ['1.두구동', '2.노포동', '3.청룡동', '4.남산동', '5.선동', '6.오륜동', '7.구서동', '8.장전동', '9.부곡동', '10.서동', '11.금사동', '12.회동동', '13.금성동']

ad_gsg = ['1.대저1동', '2.강동동', '3.명지동', '4.죽림동', '5.식만동', '6.죽동동', '7.봉림동', '8.송정동', '9.화전동', '10.녹산동', '11.생곡동', '12.구랑동', '13.지사동', '14.미음동',
                      '15.범방동', '16.신호동', '17.동선동', '18.성북동', '19.눌차동', '20.천성동', '21.대항동']

ad_yjg = ['1.거제동', '2.연산동']

ad_syg = ['1.망미동', '2.수영동', '3.민락동', '4.광안동', '5.남천동']

ad_ssg = ['1.삼락동', '2.모라동', '3.덕포동', '4.괘법동', '5.감전동', '6.주례동', '7.학장동', '8.엄궁동']

ad_kjg = ['1.기장읍', '2.장안읍', '3.정관읍', '4.일광면', '5.철마면']

why = ['자가격리', '유증상자', '보건소 재난문자 연락', '해외입국자', '집단발생지 방문자', '확진자접촉', '본인판단']

symptom = ['고열(37.5이상)', '기침', '호흡곤란', '가슴통증', '인후통', '후각상실', '가래', '근육', '오한', '콧물', '두통', '설사', '미각상실',
                   '증상없음']

agree = ['예', '아니오']

visit = ['예', '아니오']

