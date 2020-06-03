import threading
import time
import pyautogui
import keyboard


def __ghost_form_thread_function():
    while not keyboard.is_pressed('f2'):
        pyautogui.keyDown('1')
        pyautogui.keyUp('1')
        time.sleep(1.3)
        pyautogui.keyDown('2')
        pyautogui.keyUp('2')
        time.sleep(1.3)


def __ghost_form_speed_thread_function():
    while not keyboard.is_pressed('f2'):
        pyautogui.keyDown('3')
        pyautogui.keyUp('3')
        time.sleep(5*.48)


def constant_ghost_form():
    ghost_thread = threading.Thread(target=__ghost_form_thread_function)
    speed_thread = threading.Thread(target=__ghost_form_speed_thread_function)
    ghost_thread.start()
    speed_thread.start()
    ghost_thread.join()
    speed_thread.join()


if __name__ == '__main__':
    print('Registering hotkey for ghost form on f1')
    keyboard.add_hotkey('f1', constant_ghost_form)
    keyboard.wait()
