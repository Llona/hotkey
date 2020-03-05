import keyboard
from settings import ScanCode
from settings import CfgKeyEnum
from settings import MappingCharToKey
from abc import ABC, abstractmethod
import utils
from time import sleep
# from threading import Thread


class KeyListener(object):
    def __init__(self):
        self.thread_queue = None
        self.press_key_list = []
        self.user_press_list = []
        self.press_key_one = None
        self.key_press_prev_status = 'up'

    def start(self, all_key=True):
        if all_key:
            keyboard.hook(self.key_listener)
        else:
            keyboard.hook(self.one_key_listener)
        # keyboard.wait('esc')
        # key_listen = utils.CreateEmptyThread(self.thread_queue, 'stop_key_listener')
        # key_listen.start()
        # key_listen.join()

    def one_key_listener(self, key_event):
        if key_event.event_type == 'down':
            self.press_key_one = self.mapping_special_char(key_event.name.lower())

    def key_listener(self, key_event):
        if key_event.event_type == 'down':
            if self.key_press_prev_status == 'up':
                self.user_press_list = []

            if key_event.name not in self.press_key_list:
                self.press_key_list.append(self.mapping_special_char(key_event.name.lower()))
                self.user_press_list = self.press_key_list

            if self.key_press_prev_status != key_event.event_type:
                self.key_press_prev_status = 'down'
        else:
            self.key_press_prev_status = 'up'
            self.press_key_list = []
            # self.thread_queue.put('stop_key_listener')

    @staticmethod
    def mapping_special_char(special_char):
        if special_char in MappingCharToKey:
            return MappingCharToKey[special_char]
        else:
            return special_char

    def get_user_input_key_list(self):
        return self.user_press_list


class HotKey(object):
    def __init__(self, key_sender, thread_queue):
        self.thread_queue = thread_queue
        self.key_sender = key_sender

    def regist_hotkey(self, hotkey_group):
        # keyboard.add_hotkey('esc', self.stop_hotkey_waiting)
        # key_macro_list = []
        for hot_key, key_macro_list in hotkey_group.items():
            keyboard.add_hotkey(hot_key, self.send_hot_key, args=[key_macro_list])
        # keyboard.add_hotkey('F2', self.hotkey_fun)

        # hotkey_listen = utils.CreateEmptyThread(self.thread_queue, 'stop_hotkey')
        # hotkey_listen.start()
        # hotkey_listen.join()

        keyboard.wait('esc')
        # queue_h.put('end')

    def stop_hotkey_waiting(self):
        self.thread_queue.put('stop_hotkey')

    def send_hot_key(self, key_macro_list):
        try:
            for key_macro in key_macro_list:
                # todo: only send scan code now, implement support both virtual code and scan code later
                if key_macro[CfgKeyEnum.key_type.value] == CfgKeyEnum.delay.value:
                    sleep(key_macro['time'])
                    continue

                key_code = ScanCode[key_macro[CfgKeyEnum.key_name.value]]
                if key_macro[CfgKeyEnum.key_type.value] == CfgKeyEnum.press.value:
                    key_press(self.key_sender, key_code)
                elif key_macro[CfgKeyEnum.key_type.value] == CfgKeyEnum.hold.value:
                    hold_press_key(self.key_sender, key_code)
                elif key_macro[CfgKeyEnum.key_type.value] == CfgKeyEnum.release.value:
                    hold_press_key(self.key_sender, key_code)
                else:
                    raise
        except Exception as e:
            print('key define error {}'.format(e))

    def send_key(self, key_code):
        key_press(self.key_sender, key_code)

    def hold_key(self, key_code):
        hold_press_key(self.key_sender, key_code)

    def release_key(self, key_code):
        release_key(self.key_sender, key_code)

    @staticmethod
    def hotkey_fun():
        print(utils.get_foreground_title())


class KeySender(ABC):
    @abstractmethod
    def key_press(self, key_code):
        return

    @abstractmethod
    def hold_press_key(self, key_code):
        return

    @abstractmethod
    def release_key(self, key_code):
        return


def key_press(obj, key_code):
    return obj.key_press(key_code)


def hold_press_key(obj, key_code):
    return obj.hold_press_key(key_code)


def release_key(obj, key_code):
    return obj.release_key(key_code)
