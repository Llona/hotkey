import keyboard
import settings
from key_sender import *
import utils


class HotKey(object):
    def __init__(self, thread_queue):
        self.thread_queue = thread_queue

    def regist_hotkey(self, hotkey_group):
        # keyboard.add_hotkey('esc', self.stop_hotkey_waiting)
        for key, value in hotkey_group.items():
            key_macro_list = tuple(value)
            keyboard.add_hotkey(key, self.send_hot_key, args=[key_macro_list])
        # keyboard.add_hotkey('F2', lambda: self.send_hot_key(key_macro_list))
        # if settings.test:
        #     keyboard.add_hotkey('F10', self.f10_fun)
        #     keyboard.add_hotkey('F11', self.f11_fun)
        #     keyboard.add_hotkey('F12', self.f12_fun)
        # elif hotkey_group == settings.KeyGroupEnum.modau:
        #     keyboard.add_hotkey('F10', self.modau_f10_fun)
        #     keyboard.add_hotkey('F11', self.modau_f11_fun)
        #     keyboard.add_hotkey('F12', self.modau_f12_fun)
        #
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
                self.send_key(Key[i].value)
        except Exception as e:
            print('key define error {}'.format(e))

    @staticmethod
    def send_key(key):
        # time.sleep(0.1)
        key_press(key)

    def hotkey_fun(self):
        self.send_key(Key.DIK_DOWN.value)
        self.send_key(Key.DIK_UP.value)
        self.send_key(Key.DIK_SPACE.value)

    def f10_fun(self):
        # self.get_foreground_title()
        self.send_key(Key.DIK_DOWN.value)
        self.send_key(Key.DIK_UP.value)
        self.send_key(Key.DIK_SPACE.value)

    def f11_fun(self):
        self.send_key(Key.DIK_UP.value)
        self.send_key(Key.DIK_UP.value)
        self.send_key(Key.DIK_SPACE.value)

    def f12_fun(self):
        print(utils.get_foreground_title())
        # self.send_key(Key.DIK_UP.value)
        # self.send_key(Key.DIK_RIGHT.value)
        # self.send_key(Key.DIK_SPACE.value)

    # 魔道
    def modau_f10_fun(self):
        self.send_key(Key['DIK_DOWN'].value)
        self.send_key(Key.DIK_UP.value)
        self.send_key(Key.DIK_SPACE.value)

    def modau_f11_fun(self):
        self.send_key(Key.DIK_UP.value)
        self.send_key(Key.DIK_UP.value)
        self.send_key(Key.DIK_SPACE.value)

    def modau_f12_fun(self):
        self.send_key(Key.DIK_UP.value)
        self.send_key(Key.DIK_RIGHT.value)
        self.send_key(Key.DIK_SPACE.value)
