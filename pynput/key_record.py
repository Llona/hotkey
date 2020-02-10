from pynput import keyboard
from pynput.keyboard import Key, Controller
from time import sleep


class KeyRecord(object):
    def __init__(self):
        self.pressed_key = set()
        self.key_sender = Controller()
        while True:
            with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
                listener.join()

    def run_keys(self):
        print('pressed keys: {0}'.format(self.pressed_key))

    def key_send(self, key):
        sleep(0.1)
        self.key_sender.press(key)
        self.key_sender.release(key)

    def on_press(self, key):
        # try:
        #     # self.pressed_key.add(key.char)
        #     self.pressed_key.add(key)
        # except AttributeError:
        #     self.pressed_key.add(key)
        self.pressed_key.add(key)
        self.run_keys()

    def on_release(self, key):
        # print('{0} released'.format(key))
        try:
            self.pressed_key.remove(key)
        except:
            pass
        if key == Key.esc:
            print('ESC key release')
            self.key_sender.ctrl_pressed('s')
            # return False
