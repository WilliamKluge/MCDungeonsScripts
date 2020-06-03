import threading
import time
import pyautogui
import keyboard


def __ghost_form_thread_function(player_cooldown):
    ghost_cloak_cooldown = 6
    while not keyboard.is_pressed('f7'):
        pyautogui.keyDown('1')
        pyautogui.keyUp('1')
        time.sleep((ghost_cloak_cooldown*player_cooldown)/2)
        pyautogui.keyDown('2')
        pyautogui.keyUp('2')
        time.sleep((ghost_cloak_cooldown*player_cooldown)/2)


def __ghost_form_speed_thread_function(player_cooldown):
    boots_cooldown = 5
    while not keyboard.is_pressed('f7'):
        pyautogui.keyDown('3')
        pyautogui.keyUp('3')
        time.sleep((boots_cooldown*player_cooldown))


def constant_ghost_form(player_cooldown):
    ghost_thread = threading.Thread(target=__ghost_form_thread_function, args=[player_cooldown])
    speed_thread = threading.Thread(target=__ghost_form_speed_thread_function, args=[player_cooldown])
    ghost_thread.start()
    speed_thread.start()
    ghost_thread.join()
    speed_thread.join()


if __name__ == '__main__':
    player_cooldown_percent = 1 - (int(input('Enter your total cooldown percentage as a whole number (be nice or it '
                                             'will crash, not validating this): ')) / 100)
    print('Registering hotkey for ghost form on f6')
    keyboard.add_hotkey('f6', constant_ghost_form, args=[player_cooldown_percent])
    keyboard.wait()
