import keyboard
import settings
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
        time.sleep(0.1)
        keyboard.send(key)

    def f10_fun(self):
        self.send_key('down')
        self.send_key('up')
        self.send_key('space')

    def f11_fun(self):
        self.send_key('up')
        self.send_key('up')
        self.send_key('space')

    def f12_fun(self):
        self.send_key('up')
        self.send_key('right')
        self.send_key('space')


if __name__ == '__main__':
    if settings.CHARACTER == settings.Character.modau:
        dnf_char = DnfMagic()
