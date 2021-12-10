import time, pyautogui

time.sleep(5)
right_arrow = (1897, 510)

bottom_line = (954, 1060)

while True:
    try:
        pyautogui.moveTo(bottom_line[0], bottom_line[1], duration=0.5)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(2)
        pyautogui.typewrite(['enter'])
        time.sleep(5)
        pyautogui.moveTo(right_arrow[0], right_arrow[1], duration=0.5)
        pyautogui.click(right_arrow[0], right_arrow[1])
        time.sleep(5)
    except Exception as e:
        input('Some error occoured')
        print(f"Error: {str(e)}")