# _*_ coding:UTF-8 _*_
import ctypes
import time
from hot_key import KeySender
# import hot_key
from settings import ScanCode


SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class InputI(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", InputI)]


class ScanCodeSender(KeySender):
    def __init__(self):
        super(ScanCodeSender, self).__init__()

    @staticmethod
    def get_key_scan_code(code_name):
        return ScanCode[code_name]

    def hold_press_key(self, scan_code):
        extra = ctypes.c_ulong(0)
        ii_ = InputI()
        ii_.ki = KeyBdInput(0, scan_code, 0x0008, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    def release_key(self, scan_code):
        extra = ctypes.c_ulong(0)
        ii_ = InputI()
        ii_.ki = KeyBdInput(0, scan_code, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    def key_press(self, scan_code):
        self.hold_press_key(scan_code)
        time.sleep(0.02)
        self.release_key(scan_code)
        time.sleep(0.01)


# if __name__ == '__main__':
#     print(Key.DIK_UP.value)
    # up = Key.DIK_UP
    # for i in range(200):
    #     # PressKey(code)
    #     PressKey(up)
    #     time.sleep(0.1)
    #     # ReleaseKey(code)
    #     ReleaseKey(up)
    #     time.sleep(1)
