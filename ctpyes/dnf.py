import keyboard
import settings
from key_sender import Key, press
import time


class DnfMagic(object):
    def __init__(self):
        self.regist_hotkey()

    def regist_hotkey(self):
        keyboard.add_hotkey('F10', self.f10_fun)
        keyboard.add_hotkey('F11', self.f11_fun)
        keyboard.add_hotkey('F12', self.f12_fun)
        keyboard.wait('esc')

    @staticmethod
    def send_key(key):
        # time.sleep(0.1)
        press(key)

    def f10_fun(self):
        self.send_key(Key.downarrow)
        self.send_key(Key.uparrow)
        self.send_key(Key.space)

    def f11_fun(self):
        self.send_key(Key.uparrow)
        self.send_key(Key.uparrow)
        self.send_key(Key.space)

    def f12_fun(self):
        self.send_key(Key.uparrow)
        self.send_key(Key.rightarrow)
        self.send_key(Key.space)


if __name__ == '__main__':
    if settings.CHARACTER == settings.Character.modau:
        dnf_char = DnfMagic()
