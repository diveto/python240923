import pyautogui
import time
import keyboard
import random

# 화면 크기 확인
screen_width, screen_height = pyautogui.size()

try:
    while True:
        # 랜덤 좌표 생성 (화면 크기 내에서)
        random_x = random.randint(0, screen_width)
        random_y = random.randint(0, screen_height)

        # 마우스를 랜덤 좌표로 1초 동안 이동
        pyautogui.moveTo(random_x, random_y, duration=1)
        time.sleep(1)  # 1초 대기

        # # 또 다른 랜덤 좌표로 마우스를 이동
        # random_x = random.randint(0, screen_width)
        # random_y = random.randint(0, screen_height)
        # pyautogui.moveTo(random_x, random_y, duration=1)
        # time.sleep(1)  # 1초 대기

        # 'q' 키가 눌리면 루프 종료
        if keyboard.is_pressed('q'):
            print("프로그램이 종료됩니다.")
            break

except KeyboardInterrupt:
    print("프로그램이 강제 종료되었습니다.")
