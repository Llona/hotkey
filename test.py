import json
# import utils
# import time
import keyboard as keyboard
import utils
import queue
from settings import MappingCharToKey
from settings import ScanCode
from time import sleep
import key_scan_code_sender
import threading
# import settings

# a = "3"
#
#
# time.sleep(float(a))
# print(float(a))
thread_queue = queue.Queue()


# from pynput import keyboard
# from pynput.keyboard import Controller


# key_sender = Controller()


# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(key))
#
#
# def on_release(key):
#     print('{0} released'.format(key))
#     if key == keyboard.Key.esc:
#         key_sender.ctrl_pressed('c')
#         return False
#         # raise MyException(key)
#
#
# while True:
#     with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#         listener.join()


class CreateBurstSendThread(threading.Thread):
    def __init__(self, key_code, delay_time=None):
        super(CreateBurstSendThread, self).__init__()
        self.__paus_flag = threading.Event()
        self.__paus_flag.set()
        self.__running = threading.Event()
        self.__running.set()
        self.key_code = key_code
        if delay_time:
            self.burst_delay = delay_time
        else:
            self.burst_delay = 0.1
        self.key_sender = key_scan_code_sender.ScanCodeSender()

    def run(self):
        while self.__running.isSet():
            self.__paus_flag.wait()
            self.key_sender.key_press(self.key_code)
            sleep(self.burst_delay)

    def pause(self):
        self.__paus_flag.clear()

    def resume(self):
        self.__paus_flag.set()

    def stop(self):
        self.__paus_flag.set()
        self.__running.clear()


class Test1(object):
    def __init__(self):
        self.burst_sender = None
        self.is_burst_sending = False

        self.pre_key_time = 0

        keyboard.hook_key('a', self.run_burst_one_key)
        keyboard.wait('esc')

    def run_burst_one_key(self, key):
        if key.event_type == 'down':
            if not self.is_burst_sending:
                self.is_burst_sending = True
                key_code = ScanCode[key.name]
                self.burst_sender = CreateBurstSendThread(key_code)
                # self.burst_sender.set_key_code(key_code)
                self.burst_sender.start()
        else:
            monitor_key_timer = utils.CreateTimer()
            monitor_key_timer.start_count_timer(0.52, self.stop_burst_key, args=(key.name,))

    def stop_burst_key(self, key_name):
        if not keyboard.is_pressed(key_name):
            self.is_burst_sending = False
            self.burst_sender.stop()


k = Test1()


class Test(object):
    def __init__(self, thread_queue):
        self.thread_queue = thread_queue
        self.press_key_list = []

    def start_key_listener(self):
        keyboard.hook(self.test)
        keyboard.wait('esc')
        # key_listen = utils.CreateEmptyThread(self.thread_queue, 'stop_key_listener')
        # key_listen.start()
        # key_listen.join()

    def test(self, key_event):
        if key_event.event_type == 'up':
            print(self.mapping_special_char(key_event.name.lower()))
            # print(key_event.scan_code)

    def mapping_special_char(self, special_char):
        if special_char in MappingCharToKey:
            return MappingCharToKey[special_char]

    def store_key(self, key_event):
        if key_event.event_type == 'down':
            if key_event.name not in self.press_key_list:
                self.press_key_list.append(key_event.name)
                # print(key_event.name)
        else:
            print(self.press_key_list)
            self.press_key_list = []


# a = Test(thread_queue)
# a.start_key_listener()



# cfg_jh = utils.JsonControl(settings.DEFAULT_CONFIG_NAME)
# cfg_h = cfg_jh.read_config()
# print(cfg_h)
#
# jot_to_key_cfg = cfg_h[CfgKeyEnum.joy_to_key_cfg.value]
# hotkey_dic = cfg_h[CfgKeyEnum.hot_key.value]
#
# for k, v in hotkey_dic.items():
#     all_key_name = ''
#     for key_macro in v:
#         if all_key_name:
#             all_key_name = all_key_name + '+' + key_macro[CfgKeyEnum.key_name.value]
#         else:
#             all_key_name = key_macro[CfgKeyEnum.key_name.value]
#     print(all_key_name)
