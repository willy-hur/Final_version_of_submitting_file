from TTs import *
from submit_main_def import *
import csv
from main_test import*

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
s = 0  # 한번만 읽도록 만드는 일종의 카운터
n = 0  # 테스트용
input_1 = ''
check = 0
check_front = 0
intro_page = 0
end = 0
checking_personal_info = 0
extra_TTs = 0
checking_gpio = 0
end = 0
dong = 0
sex_s = 0

visit_num = 0
# show = 33
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
adress = ['서구']
adress_1 = []
num_input = 1
checking_gpio = 0
tts_for_juso = 0
count_juso = 0
JUSO_GU = 0
z = 0
global sex_num
sex_num = 3

# pygame 본격 시작문
while run:

    checking_gpio = 0
    num_input = 1
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
            elif event.key == pygame.K_SPACE:
                step += 1
                check = 1
                # check_front = 1
            elif event.key == pygame.K_0:
                step -= 1
                s -= 2
                check = 1
            elif event.key == pygame.K_1:
                counter += 1
            elif event.key == pygame.K_a:
                checking_gpio = 1
            elif event.key == pygame.K_9:
                num_input = 1
            elif event.key == pygame.K_8:
                button_down += 1
                checking_gpio = 0
            elif event.key == pygame.K_2:
                step = 0
                part = 2
                p_part = 0
                fever = 0
                s = 9
            elif event.key == pygame.K_3:
                part = 2
                step = 3
                p_part = 2

    # 본격 시작
    if step == 0 and part == 0 and p_part == 0:  # 파트를 각각 part p_part, step로써 분리, step는 각 마지막 폴터안에 있는 사진기준
        part1_show()
        part1_intro()
        intro()
        check = 0
        if n == 1:
            while s < 1:
                speak('안녕하세요 이길입니다. 이기기는 시청각장애인분들의 길이 되어주기 위하여 제작하였습니다.')
                speak('먼저 검사에 대한 설명으로 시작을 하겠습니다. 다음으로 넘어가려면 다음을, 이전으로 돌아가려면, 뒤로 버튼을 눌러주세요')
                s += 1
    if step == -1 and part == 1 and p_part == 0:
        step = 0
        part = 0
        p_part = 0

    if step == 1 and part == 0 and p_part == 0:
        part = 1
        step = 0

    if step == 0 and part == 1 and p_part == 0:
        part1_002()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 2:
                speak('기다려요')
                s += 1
    if step == 1 and part == 1 and p_part == 0:
        part1_003()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 3:
                speak('접수해요')
                s += 1
    # if step == 3 and part == 1 and p_part == 0:
    # part1_004()
    if step == 2 and part == 1 and p_part == 0:
        part1_005()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 4:
                speak('검체 체취를 위한 병을 수령하로 가세요')
                s += 1
    # if step == 5 and part == 1 and p_part == 0:
    # part1_006()
    if step == 3 and part == 1 and p_part == 0:
        part1_007()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 5:
                speak('코 면봉검사, 입 면봉검사, 필요시, 가래 검사를 할 예정입니다.')
                s += 1
    if step == 4 and part == 1 and p_part == 0:
        part = 2
        step = 0
        fever = 1
    if step == -1 and part == 2 and p_part == 0 and fever == 1:
        step = 3
        part = 1
        p_part = 0
        fever = 0
    if step == 0 and part == 2 and p_part == 0 and fever == 1:
        next()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 6:
                speak('여기까지 전반적인 설명이였습니다. 다음 버튼을 눌러주세요')
                s += 1
    # 열체크
    if fever == 1 and step == 1 and part == 2 and p_part == 0:
        fever1()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 7:
                speak('열체크를 시작합니다.')
                s += 1
    if fever == 1 and step == 2 and part == 2 and p_part == 0:
        fever2()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 8:
                speak('귀를 보이게 해주세요')
                s += 1
    if fever == 1 and step == 3 and part == 2 and p_part == 0:
        fever3()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 9:
                speak('의사 선생님이 귀에 열 재요')
                s += 1
    if fever == 1 and step == 4 and part == 2 and p_part == 0:
        step = 0
        fever = 0

    # 주소등 신상정보
    if step == -1 and part == 2 and p_part == 0 and fever != 1:
        fever = 1
        step = 3
        part = 2
        p_part = 0
    if step == 0 and part == 2 and p_part == 0 and fever != 1:
        part2_start()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 10:
                speak('문진표 작성을 시작합니다.')
                s += 1
        # sleep(5)
    if step == 1 and part == 2 and p_part == 0 and fever != 1:
        p_part = 1
    # if part == 2 and step == 2 and p_part == 1:
    # part2_family_001()
    if part == 2 and step == 1 and p_part == 1:
        numsize = len(visit)
        # 답변 숫자 입력한 후 다음 누름

        X_position = 295
        Y_position = 505
        X_size = 55
        Y_size = 55
        num_input = 3
        first_time()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while extra_TTs < 1:
                speak('처음 방분이신가요?.')
                extra_TTs += 1
        yes(red, green, yellow)
        no(red, green, yellow)

        if button_down == 0:
            X_position = 295
            Y_position = 505
            X_size = 55
            Y_size = 55
            edge(X_position, Y_position, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while checking_personal_info < 1:
                    speak('예')
                    checking_personal_info += 1
                check = 1
            if checking_gpio == 1:
                num_input = 1
                visit_num = num_input
                visits.append(visit[visit_num - 1])

        if button_down == 1:
            X_position = 895
            Y_position = 505
            X_size = 145
            Y_size = 55
            edge(X_position, Y_position, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while checking_personal_info < 2:
                    speak('아니요')
                    checking_personal_info += 1

                check = 1
            if checking_gpio == 1:
                num_input = 2
                visit_num = num_input
                visits.append(visit[visit_num - 1])

        # print("처음 방문이신 가요?")
        # print("1.예 2.아니오")  # 만약에 재방문이면 step4 에서 step 9로 이동
        # visit_num = 0
        # num_input = 0
        # numsuze = 0
        print(visits)
    if part == 2 and step == 2 and p_part == 1:
        button_down = 0
        name_def()
        part2_family_001()
        input_1 = "너"
        keyshape(counter, input_1)
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 11:
                speak('이름을 입력해주세요.')
                s += 1
        if checking_gpio == 1:
            num_input = "홍길동"
            name_num = 1

            print("이름을 입력해 주세요")
            # jamo_join_input
            name = num_input  # 이름 입력받아야함
            # 답변 숫자 입력한 후 다음 누름
            names.append(name)
            num_input = 0
            print(names[0])
    if part == 2 and step == 3 and p_part == 1:
        numsize = len(sex)
        sex_num = num_input
        part2_family_002()
        sex_def()
        man(red, green, yellow)
        woman(red, green, yellow)
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 12:
                speak('성별을 입력해주세요.')
                s += 1
        checking_gpio = 0
        if button_down == 0:
            X_position = 295
            Y_position = 505
            X_size = 55
            Y_size = 55
            edge(X_position, Y_position, X_size, Y_size)

            # sexs.append(sex[sex_num - 1])
            # sexs.append(sex[sex_num - 1])
            # sex_num = 0
            numsize = 0
            num_input = 0

            if n == 1:
                while checking_personal_info < 2:
                    speak('남성')
                    checking_personal_info += 1
                check = 1
            if checking_gpio == 1 and button_down == 0 and checking_personal_info == 1:
                sex_num = 1
            sexs.insert(0, sex[sex_num-1])

        if button_down == 1:
            X_position = 895
            Y_position = 505
            X_size = 55
            Y_size = 55
            edge(X_position, Y_position, X_size, Y_size)

            # sex_num = 0
            numsize = 0
            num_input = 0
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while checking_personal_info < 3:
                    speak('여성')
                    checking_personal_info += 1
                check = 1
            if checking_gpio == 1 and button_down == 1 and checking_personal_info == 2:
                sex_num = 2
            sexs.insert(0, sex[sex_num - 1])



            # print("성별을 선택해 주세요")
            # print("1. 남, 2. 여")

            # 답변 숫자 입력한 후 다음 누름

    if part == 2 and step == 4 and p_part == 1:
        part2_family_005()
        birth_def()
        keyboard_input(num_input)
        num_input = input_1
        keyshape(counter, input_1)
        button_down = 0
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 13:
                speak('생년월일을 입력해주세요.')
                s += 1
        # print("생년월일을 입력해 주세요")
        if checking_gpio == 1:
            birth = num_input
            # 답변 숫자 입력한 후 다음 누름
            births.append(birth)
            birth = 0
            num_input = 0
            print(births[0])
            file_name = names[0] + births[0] + sexs[0]
            f = open(file_name, 'w', encoding='utf-8')
            wr = csv.writer(f)
            wr.writerow([1, '이름 생년월일 성별', names[0] + births[0] + sexs[0]])

        if visits[0] == '아니오':
            file_name = names[0] + births[0] + sexs[0]
            # f = open(file_name,'r', encoding='utf-8')
            f = open(file_name, 'a', encoding='utf-8')
            # lines = csv.reader(f)
            wr = csv.writer(f)
            if part == 2 and step == 5 and p_part == 1:
                step = 0
                p_part = 3
    if part == 2 and step == 5 and p_part == 1:
        part2_family_004()
        keyshape(counter, input_1)
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 14:
                speak('전화번호를 입력해주세요.')
                s += 1
        # print("전화번호를 입력해주세요")
        if checking_gpio == 1:
            num_input = "01012345678"
            p_num = num_input
            # 답변 숫자 입력한 후 다음 누름
            p_nums.append(p_num)
            p_num = 0
            num_input = 0
            wr.writerow([2, '전화번호', p_nums[0]])
        print(p_nums)

    if part == 2 and step == 6 and p_part == 1:
        # 꼭꼭 주소 추가하기...
        part2_family_003()
        juso()
        keyshape(counter, input_1)
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while tts_for_juso < 1:
                speak('주소를 입력해주세요, 맞는 번호를 누르시면 됩니다.')
                tts_for_juso += 1
    if part == 2 and step == 7 and p_part == 1:
        end = 0

        juso_gu()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while tts_for_juso < 17:
                JUSO_GU = ad[count_juso]
                speak(JUSO_GU)
                count_juso += 1
                tts_for_juso += 1
            check = 1

        if checking_gpio == 1 and dong != 1:
            num_input = 2
            ad_len = len(ad)
            # num input받고
            ad_num = num_input
            adress.insert(0, ad[ad_num - 1])
            print(adress)
            ad_num = 0

            wr.writerow([3, '주소, 구:', adress[0]])

            # checking_gpio = 0
            dong = 1
        if adress[0] == '1.중구':  # 중구
            checking_gpio = 0
            count_juso = 0
            juso_junggo()
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while tts_for_juso < 28:
                    JUSO_GU = ad_jg[count_juso]
                    speak(JUSO_GU)
                    count_juso += 1
                    tts_for_juso += 1
                check = 1

            if checking_gpio == 1:
                num_input = 1
                numsize = len(ad_jg)
                ad_num = num_input
                adress_1.insert(0, ad_jg[ad_num - 1])
                ad_num = 0
                num_input = 0
                wr.writerow([3, '주소 동:', adress_1[0]])

            print(adress)


        elif adress[0] == '2.서구':  # 서구
            print(tts_for_juso )
            count_juso = 0
            juso_sugu()
            if check == 1:
                n = 0
            else:
                n = 1
            check = 0
            if n == 1:
                while tts_for_juso < 27:
                    JUSO_GU = ad_sg[count_juso]
                    speak(JUSO_GU)
                    count_juso += 1
                    tts_for_juso += 1
                check = 0
                checking_gpio = 0
            if checking_gpio == 1:
                num_input = 1
                checking_gpio = 0
                numsize = len(ad_jg)
                ad_num = num_input
                adress_1.insert(0,ad_sg[ad_num - 1])
                ad_num = 0
                num_input = 0
                wr.writerow([3, '주소 동:', adress_1[0]])

            print(adress)

        elif adress[0] == '3.동구':  # 동구
            checking_gpio = 0
            count_juso = 0
            juso_donggu()
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while tts_for_juso < 21:
                    JUSO_GU = ad_dg[count_juso]
                    speak(JUSO_GU)
                    count_juso += 1
                    tts_for_juso += 1
                check = 0
            if checking_gpio == 1:
                num_input = 1
                ad_num = num_input
                numsize = len(ad_dg)
                adress_1.insert(0, ad_dg[ad_num - 1])
                wr.writerow([3, '주소 동:', adress_1[0]])
                ad_num = 0
                num_input = 0

                print(adress)


        elif adress[0] == '4.영도구':  # 영도구
            checking_gpio = 0
            count_juso = 0
            juso_yongdogu()
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while tts_for_juso < 25:
                    JUSO_GU = ad_ydg[count_juso]
                    speak(JUSO_GU)
                    count_juso += 1
                    tts_for_juso += 1
                check = 0
            if checking_gpio == 1:
                num_input = 1
                ad_num = num_input
                numsize = len(ad_ydg)
                adress_1.insert(0,ad_ydg[ad_num - 1])
                wr.writerow([3, '주소 동:', adress_1[0]])
                ad_num = 0
                num_input = 0

            print(adress)


        elif adress[0] == '5.부산진구':  # 부산진구
            checking_gpio = 0
            count_juso = 0
            juso_busanjingu()
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while tts_for_juso < 28:
                    JUSO_GU = ad_jg[count_juso]
                    speak(JUSO_GU)
                    count_juso += 1
                    tts_for_juso += 1
                check = 0
            if checking_gpio == 1:
                num_input = 1
                ad_num = num_input
                numsize = len(ad_jg)
                adress_1.insert(0,ad_jg[ad_num - 1])
                wr.writerow([3, '주소 동:', adress_1[0]])
                ad_num = 0
                num_input = 0

            print(adress)


        elif adress[0] == '6.동래구':  # 동래구
            checking_gpio = 0
            count_juso = 0
            juso_donglaygu()
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while tts_for_juso < 25:
                    JUSO_GU = ad_drg[count_juso]
                    speak(JUSO_GU)
                    count_juso += 1
                    tts_for_juso += 1
                check = 0
            if checking_gpio == 1:
                num_input = 1
                ad_num = num_input
                numsize = len(ad_drg)
                adress_1.insert(0,ad_drg[ad_num - 1])
                wr.writerow([3, '주소 동:', adress_1[0]])
                ad_num = 0
                num_input = 0

            print(adress)


        elif adress[0] == '7.남구':  # 남구
            checking_gpio = 0
            count_juso = 0
            juso_namgu()
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while tts_for_juso < 23:
                    JUSO_GU = ad_ng[count_juso]
                    speak(JUSO_GU)
                    count_juso += 1
                    tts_for_juso += 1
                check = 0
            if checking_gpio == 1:
                num_input = 1
                ad_num = num_input
                numsize = len(ad_ng)
                adress_1.insert(0,ad_ng[ad_num - 1])
                wr.writerow([3, '주소 동:', adress_1[0]])
                ad_num = 0
                num_input = 0

            print(adress)


        elif adress[0] == '8.북구':  # 북구
            checking_gpio = 0
            count_juso = 0
            juso_bokygu()
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while tts_for_juso < 22:
                    JUSO_GU = ad_bg[count_juso]
                    speak(JUSO_GU)
                    count_juso += 1
                    tts_for_juso += 1
                check = 0
            if checking_gpio == 1:
                num_input = 1
                ad_num = num_input
                numsize = len(ad_bg)
                adress_1.insert(0,ad_bg[ad_num - 1])
                wr.writerow([3, '주소 동:', adress_1[0]])
                ad_num = 0
                num_input = 0

            print(adress)


        elif adress[0] == '9.해운대구':  # 해운대구
            checking_gpio = 0
            count_juso = 0
            juso_heyundaygu()
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while tts_for_juso < 25:
                    JUSO_GU = ad_hudg[count_juso]
                    speak(JUSO_GU)
                    count_juso += 1
                    tts_for_juso += 1
                check = 0
            if checking_gpio == 1:
                num_input = 1
                ad_num = num_input
                numsize = len(ad_hudg)
                adress_1.insert(0,ad_hudg[ad_num - 1])
                wr.writerow([3, '주소 동:', adress_1[0]])
                ad_num = 0
                num_input = 0

                print(adress)


        elif adress[0] == '10.사하구':  # 사하구
            checking_gpio = 0
            count_juso = 0
            juso_sahagu()
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while tts_for_juso < 25:
                    JUSO_GU = ad_shg[count_juso]
                    speak(JUSO_GU)
                    count_juso += 1
                    tts_for_juso += 1
                check = 0
            if checking_gpio == 1:
                num_input = 1
                ad_num = num_input
                numsize = len(ad_shg)
                adress_1.insert(0,ad_shg[ad_num - 1])
                wr.writerow([3, '주소 동:', adress_1[0]])
                ad_num = 0
                num_input = 0

            print(adress)


        elif adress[0] == '11.금정구':  # 금정구
            checking_gpio = 0
            count_juso = 0
            juso_gumjunggu()
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while tts_for_juso < 30:
                    JUSO_GU = ad_gjg[count_juso]
                    speak(JUSO_GU)
                    count_juso += 1
                    tts_for_juso += 1
                check = 0
            if checking_gpio == 1:
                num_input = 1
                ad_num = num_input
                numsize = len(ad_gjg)
                adress_1.insert(0,ad_gjg[ad_num - 1])
                wr.writerow([3, '주소 동:', adress_1[0]])
                ad_num = 0
                num_input = 0

            print(adress)

        elif adress[0] == '12.강서구':  # 강서구
            checking_gpio = 0
            count_juso = 0
            juso_gangsogu()
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while tts_for_juso < 38:
                    JUSO_GU = ad_gsg[count_juso]
                    speak(JUSO_GU)
                    count_juso += 1
                    tts_for_juso += 1
                check = 0
            if checking_gpio == 1:
                num_input = 1
                ad_num = num_input
                numsize = len(ad_gsg)
                adress_1.insert(0,ad_gsg[ad_num - 1])
                wr.writerow([3, '주소 동:', adress_1[0]])
                ad_num = 0
                num_input = 0

            print(adress)


        elif adress[0] == '13.연제구':  # 연제구
            checking_gpio = 0
            count_juso = 0
            juso_yenjaegu()
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while tts_for_juso < 19:
                    JUSO_GU = ad_yjg[count_juso]
                    speak(JUSO_GU)
                    count_juso += 1
                    tts_for_juso += 1
                check = 0
            if checking_gpio == 1:
                num_input = 1
                ad_num = num_input
                numsize = len(ad_yjg)
                adress_1.insert(0,ad_yjg[ad_num - 1])
                wr.writerow([3, '주소 동:', adress_1[0]])
                ad_num = 0
                num_input = 0

            print(adress)


        elif adress[0] == '14.수영구':  # 수영구
            checking_gpio = 0
            count_juso = 0
            juso_suyonggu()
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while tts_for_juso < 22:
                    JUSO_GU = ad_syg[count_juso]
                    speak(JUSO_GU)
                    count_juso += 1
                    tts_for_juso += 1
                check = 0
            if checking_gpio == 1:
                num_input = 1
                ad_num = num_input
                numsize = len(ad_syg)
                adress_1.insert(0,ad_syg[ad_num - 1])
                wr.writerow([3, '주소 동:', adress_1[0]])
                ad_num = 0
                num_input = 0

                print(adress)


        elif adress[0] == '15.사상구':  # 사상구
            checking_gpio = 0
            count_juso = 0
            juso_sasanggu()
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while tts_for_juso < 25:
                    JUSO_GU = ad_ssg[count_juso]
                    speak(JUSO_GU)
                    count_juso += 1
                    tts_for_juso += 1
                check = 0
            if checking_gpio == 1:
                num_input = 1
                ad_num = num_input
                numsize = len(ad_ssg)
                adress_1.insert(0,ad_ssg[ad_num - 1])
                wr.writerow([3, '주소 동:', adress_1[0]])
                ad_num = 0
                num_input = 0

            print(adress)


        elif adress[0] == '16.기장구':  # 기장구
            checking_gpio = 0
            count_juso = 0
            juso_gijianggu()
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while tts_for_juso < 22:
                    JUSO_GU = ad_kjg[count_juso]
                    speak(JUSO_GU)
                    count_juso += 1
                    tts_for_juso += 1
            if checking_gpio == 1:
                num_input = 1
                ad_num = num_input
                numsize = len(ad_kjg)
                adress_1.insert(0,ad_kjg[ad_num - 1])
                wr.writerow([3, '주소 동:', adress_1[0]])
                ad_num = 0
                num_input = 0

            print(adress)

        print("상세주소를 입력해 주세요")
        # 주소 입력받기
        # adress.append(?)
        print(adress)
        # ad_num=num_input 주소받기

        # wr.writerow([3, '상세 주소', adress[]])

    if part == 2 and step == 8 and p_part == 1:
        step = 0
        p_part = 3
        checking_gpio = 0
    #####################################
    # 접촉위치
    if part == 2 and step == 0 and p_part == 3:
        check_T()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 15:
                speak('접촉 경위를 확인 합니다. 이곳에 오신 이유를 선택해주세요.')
                s += 1

    if part == 2 and step == 1 and p_part == 3:
        input_mode = 3
        X_position = 195
        Y_position = 145
        X_size = 150
        Y_size = 150
        numsize = len(why)

        part2_travel_final()
        if button_down == 0:
            edge(X_position, Y_position, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 16:
                    speak('자가격리.')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 1
                why_num = num_input
                whys.append(why[0])
                wr.writerow([4, '검사경위', whys[0]])
            checking_gpio = 0
        if button_down == 1:
            edge(X_position + 200, Y_position, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 17:
                    speak('증상이 있어서 왔어요.')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 2
                why_num = num_input
                whys.append(why[1])
                wr.writerow([4, '검사경위', whys[0]])
            checking_gpio = 0
        if button_down == 2:
            edge(X_position + 400, Y_position, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 18:
                    speak('보건소 재난문자 연락받고 왔어요.')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 3
                why_num = num_input
                whys.append(why[2])
                wr.writerow([4, '검사경위', whys[0]])
            checking_gpio = 0
        if button_down == 3:
            edge(X_position + 600, Y_position, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 19:
                    speak('해외입국.')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 4
                why_num = num_input
                whys.append(why[3])
                wr.writerow([4, '검사경위', whys[0]])
            checking_gpio = 0
        if button_down == 4:
            edge(X_position, Y_position + 200, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 20:
                    speak('집단 발병지역에 방문했어요')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 5
                why_num = num_input
                whys.append(why[4])
                wr.writerow([4, '검사경위', whys[0]])
            checking_gpio = 0
        if button_down == 5:
            edge(X_position + 200, Y_position + 200, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 21:
                    speak('확진자와 접촉했어요.')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 6
                why_num = num_input
                whys.append(why[5])
                wr.writerow([4, '검사경위', whys[0]])
            checking_gpio = 0
        if button_down == 6:
            edge(X_position + 400, Y_position + 200, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 22:
                    speak('본인 판단으로 왔어요.')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 7
                why_num = num_input
                whys.append(why[6])
                wr.writerow([4, '검사경위', whys[0]])
            checking_gpio = 0
        # num_input = 0 여기서는 초기화 하면 x

    ########################################################################
    if part == 2 and step == 2 and p_part == 3:
        step = 8
        p_part = 1
        button_down = 0
    if part == 2 and step == 9 and p_part == 1:
        check_S()

        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 17:
                speak('증상 확인란입니다. 맞는 증상을 찾아주세요')
                s += 1
    if part == 2 and step == 8 and p_part == 1:
        p_part = 2
        step = 1
    # 증상 파트 시작
    if part == 2 and step == 1 and p_part == 2:
        part2_symptom_001()
        next_2()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 17:
                speak('현재 어떻게 아파요?')
                speak('다음 버튼을 눌러주세요')
                s += 2
    if part == 2 and step == 2 and p_part == 2:
        X_position = 100
        Y_position = 150
        X_size = 150
        Y_size = 150
        part2_symptom_002()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 19:
                speak('아래 버튼을 누르면 증상 종류를 선택할 수 있습니다. 맞는 증상을 선택하시고 다음 버튼을 누르세요')
                s += 1
        # if part == 2 and step == 3 and p_part == 2:
        numsize = len(symptom)
        symptoms = []
        symptom_num = num_input  # 사이사이에 다음버튼 넣기
        # input_mode가 3일때
        input_mode = 3
        if button_down == 0:
            edge(X_position, Y_position, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 20:
                    speak('열나요.')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 1
                symptom = "고열(37.5이상)"
                symptoms.append(symptom)
                wr.writerow([4.5, '증상', symptoms])
        if button_down == 1:
            edge(X_position + 150, Y_position, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 21:
                    speak('기침나요.')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 2
                symptom = "기침"
                symptoms.append(symptom)
                wr.writerow([4.5, '증상', symptoms])

        if button_down == 2:
            edge(X_position + 300, Y_position, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 22:
                    speak('숨쉬기 힘들어요.')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 3
                symptom = "호흡곤란"
                symptoms.append(symptom)
                wr.writerow([4.5, '증상', symptoms])
        if button_down == 3:
            edge(X_position + 450, Y_position, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 23:
                    speak('가슴이 답답해요.')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 4
                symptom = "가슴통증"
                symptoms.append(symptom)
                wr.writerow([4.5, '증상', symptoms])
        if button_down == 4:
            edge(X_position + 600, Y_position, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 24:
                    speak('목이 아파요.')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 5
                symptom = "인후통"
                symptoms.append(symptom)
                wr.writerow([4.5, '증상', symptoms])
        if button_down == 5:
            edge(X_position + 750, Y_position, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 25:
                    speak('냄새를 못 맡아요.')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 6
                symptom = "후각상실"
                symptoms.append(symptom)
                wr.writerow([4.5, '증상', symptoms])
        if button_down == 6:
            edge(X_position + 900, Y_position, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 26:
                    speak('가래가 있어요.')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 7
                symptom = "가래"
                symptoms.append(symptom)
                wr.writerow([4.5, '증상', symptoms])
        if button_down == 7:
            edge(X_position, Y_position + 150, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 27:
                    speak('몸살있어요나 근육통이 있어요.')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 8
                symptom = "근육통"
                symptoms.append(symptom)
                wr.writerow([4.5, '증상', symptoms])
        if button_down == 8:
            edge(X_position + 150, Y_position + 150, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 28:
                    speak('으슬으슬 떨려요')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 9
                symptom = "오한"
                symptoms.append(symptom)
                wr.writerow([4.5, '증상', symptoms])
        if button_down == 9:
            edge(X_position + 300, Y_position + 150, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 29:
                    speak('콧물 나요')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 10
                symptom = "콧물"
                symptoms.append(symptom)
                wr.writerow([4.5, '증상', symptoms])
        if button_down == 10:
            edge(X_position + 450, Y_position + 150, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 30:
                    speak('머리가 아파요')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 11
                symptom = "두통"
                symptoms.append(symptom)
                wr.writerow([4.5, '증상', symptoms])
        if button_down == 11:
            edge(X_position + 600, Y_position + 150, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 31:
                    speak('설사해요')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 12
                symptom = "설사"
                symptoms.append(symptom)
                wr.writerow([4.5, '증상', symptoms])
        if button_down == 12:
            edge(X_position + 750, Y_position + 150, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 32:
                    speak('맛을 잘 못느껴요')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 13
                symptom = "미각상실"
                symptoms.append(symptom)
                wr.writerow([4.5, '증상', symptoms])
        if button_down == 13:
            edge(X_position + 900, Y_position + 150, X_size, Y_size)
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while s < 33:
                    speak('증상이 없어요')
                    s += 1
                check = 1
            if checking_gpio == 1:
                num_input = 14
                symptom = "증상없음"
                symptoms.append(symptom)
                wr.writerow([4.5, '증상', symptoms])

        print(symptoms)
        button_down = 0

    if part == 2 and step == 3 and p_part == 2:

        umsize = len(agree)
        agree_num = num_input
        checking_gpio == 0
        X_position = 295
        Y_position = 505
        X_size = 55
        Y_size = 55
        num_input = 3
        personal_info()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while extra_TTs < 2:
                speak('개인정보 수집에 동의하시나요?.')
                extra_TTs += 1
        yes(red, green, yellow)
        no(red, green, yellow)
        edge(X_position, Y_position, X_size, Y_size)
        if button_down == 0:
            X_position = 295
            Y_position = 505
            X_size = 55
            Y_size = 55
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while checking_personal_info < 4:
                    speak('예')
                    checking_personal_info += 1
                check = 1
            if checking_gpio == 1:
                num_input = 1
                agrees.append(agree[0])
                wr.writerow([5, '개인정보 수집 동의여부', agrees[0]])
                checking_gpio == 0
        if button_down == 1:
            X_position = 895
            Y_position = 505
            X_size = 145
            Y_size = 55
            if check == 1:
                n = 0
            check = 0
            if n == 1:
                while checking_personal_info < 5:
                    speak('아니요')
                    checking_personal_info += 1
                check = 1
            if checking_gpio == 1:
                num_input = 2
                agrees.append(agree[1])
                wr.writerow([5, '개인정보 수집 동의여부', agrees[0]])
                checking_gpio == 0

        print(agrees)
    if part == 2 and step == 4 and p_part == 2:
        part = 3
        step = 0
        p_part = 0
    # 상담 부분 뺼예정...

    # 코
    # if part == 3 and step == 1 and p_part == 0:
    # part3_start()
    if part == 3 and step == 0 and p_part == 0:
        print(s)
        part3_intro()
        print(s)
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 21:
                speak('검사를 시작하겠습니다. 검사단계는 코 면봉검사, 입 면봉검사, 그리고 필요시 가래검사가 있습니다.')
                s += 1

    if part == 3 and step == 1 and p_part == 0:
        part3_N_000()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 22:
                speak('먼저 코 면봉 검사를 시작하겠습니다.')
                s += 1
    if part == 3 and step == 2 and p_part == 0:
        part3_N_001()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 23:
                speak('머리를 뒤로 해요.')
                s += 1
    if part == 3 and step == 3 and p_part == 0:
        part3_N_002()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 24:
                speak('눈을 감아요.')
                s += 1
    if part == 3 and step == 4 and p_part == 0:
        part3_N_003()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 25:
                speak('의사 선생님이 면봉을 코에 넣어요.')
                s += 1
    if part == 3 and step == 5 and p_part == 0:
        part3_N_004()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 26:
                speak('면봉으로 코안을 문질러요.')
                s += 1
    if part == 3 and step == 6 and p_part == 0:
        step = 0
        p_part = 1
    # 입
    if part == 3 and step == 0 and p_part == 1:
        part3_M_intro()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 27:
                speak('입 면봉 검사를 실시합니다.')
                s += 1
    if part == 3 and step == 1 and p_part == 1:
        part3_M_001()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 28:
                speak('마스크를 아래로 내려요.')
                s += 1
    if part == 3 and step == 2 and p_part == 1:
        part3_M_002()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 29:
                speak('머리를 뒤로 해요.')
                s += 1
    if part == 3 and step == 3 and p_part == 1:
        part3_M_003()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 30:
                speak('입을 벌려요.')
                s += 1
    if part == 3 and step == 4 and p_part == 1:
        part3_M_004()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 31:
                speak('아~ 소리를 길게 내요.')
                s += 1
    if part == 3 and step == 5 and p_part == 1:
        part3_M_005()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 32:
                speak('의사 선생님이 면봉을 입에 넣어요.')
                s += 1
    if part == 3 and step == 6 and p_part == 1:
        part3_M_006()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 33:
                speak('면봉으로 입 안을 문질러요.')
                s += 1
    if part == 3 and step == 7 and p_part == 1:
        step = 0
        p_part = 2
    # 가래
    if part == 3 and step == 0 and p_part == 2:
        part3_P_intro()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 34:
                speak('가래검사를 시작합니다.')
                s += 1
    if part == 3 and step == 1 and p_part == 2:
        part3_P_001()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 35:
                speak('마스크를 쓰고 입안에서 가래르 모아요.')
                s += 1
    if part == 3 and step == 2 and p_part == 2:
        part3_P_002()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 36:
                speak('통으로 가래를 뱉어요.')
                s += 1

    if part == 3 and step == 3 and p_part == 2:
        part = 4
        step = 0
        p_part = 0
    # 집
    if part == 4 and step == 0 and p_part == 0:
        part4_H_intro()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 37:
                speak('검사가 모두 끝났습니다. 다음은 집에서의 주의사항입니다.')
                s += 1
    if part == 4 and step == 1 and p_part == 0:
        part4_H_001()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 38:
                speak('결과는 내일 휴대폰으로 문자 받으실거예요.')
                s += 1
    if part == 4 and step == 2 and p_part == 0:
        part4_H_002()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 39:
                speak('하루 동안 밖에 나가면 안 돼요.')
                s += 1
    if part == 4 and step == 3 and p_part == 0:
        part4_H_003()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 40:
                speak('집에만 있어야 해요.')
                s += 1
    if part == 4 and step == 4 and p_part == 0:
        part4_H_004()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 41:
                speak('집에에서는 따로 생활해요.')
                s += 1
    if part == 4 and step == 5 and p_part == 0:
        part4_H_005()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 42:
                speak('하루 동안 혼자 밥 먹고 혼자 자요.')
                s += 1
    if part == 4 and step == 6 and p_part == 0:
        part4_H_006()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 43:
                speak('같이 밥먹고 같이 자는건 안 돼요.')
                s += 1
    if part == 4 and step == 7 and p_part == 0:
        part4_H_007()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 44:
                speak('마스크 쓰고 2미터 떨어져서 대화해주세요.')
                s += 1
    if part == 4 and step == 8 and p_part == 0:
        part4_H_008()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 45:
                speak('대중교통 이용을 자제해주세요.')
                s += 1
    if part == 4 and step == 9 and p_part == 0:
        part4_H_009()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 46:
                speak('가능한 도보, 자가용이나 택시를 이용하여 귀가해주세요.')
                s += 1
    if part == 4 and step == 10 and p_part == 0:
        part4_H_010()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 47:
                speak('뒷자석에 있다면 대각선에있는 좌석에 앉아주세요.')
                s += 1
    if part == 4 and step == 11 and p_part == 0:
        step = 0
        p_part = 1
    # 화장실
    if part == 4 and step == 0 and p_part == 1:
        part4_B_intro()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 48:
                speak('화장실 이용시 주의사항입니다.')
                s += 1
    if part == 4 and step == 1 and p_part == 1:
        part4_B_001()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 49:
                speak('만약 화장실이 1개면.')
                s += 1
    if part == 4 and step == 2 and p_part == 1:
        part4_B_002()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 50:
                speak('대소변 보고 물내려요.')
                s += 1
    if part == 4 and step == 3 and p_part == 1:
        part4_B_003()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 51:
                speak('락스와 변기 주변 1미터를 닦아주세요.')
                s += 1
    if part == 4 and step == 4 and p_part == 1:
        part4_B_004()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 52:
                speak('30분 환기후 다시 이용해주세요.')
                s += 1
    if part == 4 and step == 5 and p_part == 1:
        part4_B_005()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 53:
                speak('화장실이 2개면.')
                s += 1
    if part == 4 and step == 6 and p_part == 1:
        part4_B_006()
        if check == 1:
            n = 0
        check = 0
        if n == 1:
            while s < 54:
                speak('따로 사용하시면 됩니다.')
                s += 1

    pygame.display.update()
    # FPSCLOCK.tick(500)
    pygame.time.delay(500)
    n = 1
    # check_front = 0
pygame.quit()
# f.close()
