import keyboard
from settings import ScanCodeEmu
from abc import ABC, abstractmethod
import utils


class HotKey(object):
    def __init__(self, key_sender, thread_queue):
        self.thread_queue = thread_queue
        self.key_sender = key_sender

    def regist_hotkey(self, hotkey_group):
        # keyboard.add_hotkey('esc', self.stop_hotkey_waiting)
        for dic_key, dic_value in hotkey_group.items():
            key_macro_list = tuple(dic_value)
            keyboard.add_hotkey(dic_key, self.send_hot_key, args=[key_macro_list])
        # keyboard.add_hotkey('F2', self.hotkey_fun)

        # hotkey_listen = utils.CreateThread(self.thread_queue, 'stop_hotkey')
        # hotkey_listen.start()
        # hotkey_listen.join()

        keyboard.wait('esc')
        # queue_h.put('end')

    def stop_hotkey_waiting(self):
        self.thread_queue.put('stop_hotkey')

    def send_hot_key(self, key_macro_list):
        try:
            for i in key_macro_list:
                # todo: only send scan code now, implement support both virtual code and scan code later
                self.send_key(ScanCodeEmu[i].value)
        except Exception as e:
            print('key define error {}'.format(e))

    def send_key(self, key):
        # time.sleep(0.1)
        key_press(self.key_sender, key)

    @staticmethod
    def hotkey_fun():
        print(utils.get_foreground_title())


class KeySender(ABC):
    @abstractmethod
    def key_press(self, key_code):
        return


def key_press(obj, key_code):
    return obj.key_press(key_code)
