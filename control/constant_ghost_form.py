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


def duplicate_item_thread_func(player_cooldown, slot_cooldown, keys):
    global stop_threads
    cooldown_adjustment = 1 - player_cooldown
    current_index = 0
    while not stop_threads:
        pyautogui.keyDown(keys[current_index])
        pyautogui.keyUp(keys[current_index])
        time.sleep((slot_cooldown * cooldown_adjustment) / len(keys))
        current_index += 1
        if current_index > len(keys):
            current_index = 0


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
        slot_one_item = config['DEFAULT']['Slot1Item']
        slot_two_item = config['DEFAULT']['Slot2Item']
        slot_three_item = config['DEFAULT']['Slot3Item']
        threads = []
        if slot_one_item != slot_two_item and slot_one_item != slot_three_item:
            s1t = threading.Thread(target=slot_thread_func, args=[player_cooldown, slot_one_cooldown, '1'])
            threads.append(s1t)
        else:
            keys = ['1']
            if slot_one_item == slot_two_item:
                keys.append('2')
            if slot_one_item == slot_three_item:
                keys.append('3')
            dst = threading.Thread(target=duplicate_item_thread_func, args=[player_cooldown, slot_one_cooldown, '1'])
            threads.append(dst)
        if slot_two_item != slot_one_item:
            s2t = threading.Thread(target=slot_thread_func, args=[player_cooldown, slot_two_cooldown, '2'])
            threads.append(s2t)
        if slot_three_item != slot_one_item:
            s3t = threading.Thread(target=slot_thread_func, args=[player_cooldown, slot_three_cooldown, '3'])
            threads.append(s3t)
        stop_threads_thread = threading.Thread(target=stop_threads_func)
        for thread in threads:
            thread.start()
        stop_threads_thread.start()
        for thread in threads:
            thread.join()
        stop_threads_thread.join()
        print('Threads joined - hotkey ready')
    except:
        print('Do you have the PlayerConfig.ini in the same directory as the exe?')


if __name__ == '__main__':
    print('Setting cooldown hotkey to F6')
    print('Press F7 to stop')
    keyboard.add_hotkey('f6', smart_cooldown_spammer)
    keyboard.wait()
