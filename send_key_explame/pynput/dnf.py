from pynput.keyboard import Key
from key_record import KeyRecord
import settings


class DnfMagic(KeyRecord):
    def __init__(self):
        super(DnfMagic, self).__init__()

    def run_keys(self):
        # print('pressed keys: {0}'.format(self.pressed_key))
        if len(self.pressed_key) == 1:
            if Key.f10 in self.pressed_key:
                self.key_send(Key.down)
                self.key_send(Key.up)
                self.key_send(Key.space)
            if Key.f11 in self.pressed_key:
                self.key_send(Key.up)
                self.key_send(Key.up)
                self.key_send(Key.space)
            if Key.f12 in self.pressed_key:
                self.key_send(Key.up)
                self.key_send(Key.right)
                self.key_send(Key.space)


if __name__ == '__main__':
    if settings.CHARACTER == settings.Character.modau:
        dnf_char = DnfMagic()
