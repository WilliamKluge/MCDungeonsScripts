import threading
import time
import pyautogui
import keyboard
import configparser


stop_threads = False


def stop_threads_func():
    global stop_threads
    while not keyboard.is_pressed('f7'):
        time.sleep(0.01)
    print('Setting the stop thread variable to true')
    stop_threads = True


def slot_thread_func(player_cooldown, slot_cooldown, key):
    global stop_threads
    cooldown_adjustment = 1 - player_cooldown
    while not stop_threads:
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)
        time.sleep(slot_cooldown * cooldown_adjustment)


def smart_cooldown_spammer():
    global stop_threads
    print('Reading values from PlayerConfig.ini')
    stop_threads = False
    try:
        config = configparser.ConfigParser()
        config.read('PlayerConfig.ini')
        player_cooldown = float(config['DEFAULT']['PlayerCooldown']) + float(config['DEFAULT']['AdditionalReduction'])
        slot_one_cooldown = int(config['DEFAULT']['Slot1Cooldown'])
        slot_two_cooldown = int(config['DEFAULT']['Slot2Cooldown'])
        slot_three_cooldown = int(config['DEFAULT']['Slot3Cooldown'])
        s1t = threading.Thread(target=slot_thread_func, args=[player_cooldown, slot_one_cooldown, '1'])
        s2t = threading.Thread(target=slot_thread_func, args=[player_cooldown, slot_two_cooldown, '2'])
        s3t = threading.Thread(target=slot_thread_func, args=[player_cooldown, slot_three_cooldown, '3'])
        stop_threads_thread = threading.Thread(target=stop_threads_func)
        s1t.start()
        s2t.start()
        s3t.start()
        stop_threads_thread.start()
        s1t.join()
        s2t.join()
        s3t.join()
        stop_threads_thread.join()
        print('Threads joined - hotkey ready')
    except:
        print('Do you have the PlayerConfig.ini in the same directory as the exe?')


if __name__ == '__main__':
    print('Setting cooldown hotkey to F6')
    print('Press F7 to stop')
    keyboard.add_hotkey('f6', smart_cooldown_spammer)
    keyboard.wait()
