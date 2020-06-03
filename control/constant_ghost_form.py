import threading
import time
import pyautogui
import keyboard
import configparser


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
    ghost_thread = threading.Thread(target=__ghost_form_thread_function, args=[player_cooldown-.015])
    speed_thread = threading.Thread(target=__ghost_form_speed_thread_function, args=[player_cooldown-.015])
    ghost_thread.start()
    speed_thread.start()
    ghost_thread.join()
    speed_thread.join()


def spam_ghost_form():
    while not keyboard.is_pressed('f7'):
        pyautogui.keyDown('1')
        pyautogui.keyUp('1')
        pyautogui.keyDown('2')
        pyautogui.keyUp('2')
        pyautogui.keyDown('3')
        pyautogui.keyUp('3')
        time.sleep(.1)





def smart_cooldown_spammer():
    config = configparser.ConfigParser()
    config.read('PlayerConfig.ini')
    player_cooldown = float(config['DEFAULT']['PlayerCooldown'])
    slot_one_cooldown = int(config['DEFAULT']['Slot1Cooldown'])
    slot_two_cooldown = int(config['DEFAULT']['Slot2Cooldown'])
    slot_three_cooldown = int(config['DEFAULT']['Slot3Cooldown'])


if __name__ == '__main__':
    keyboard.add_hotkey('f6', smart_cooldown_spammer)
    keyboard.wait()
