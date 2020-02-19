from pynput import keyboard
from pynput.keyboard import Controller


key_sender = Controller()


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))


def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        key_sender.ctrl_pressed('c')
        return False
        # raise MyException(key)


while True:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
