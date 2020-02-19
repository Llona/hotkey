import keyboard


def print_pressed_keys(e):
    line = ', '.join(str(code) for code in keyboard._pressed_events)
    # '\r' and end='' overwrites the previous line.
    # ' '*40 prints 40 spaces at the end to ensure the previous line is cleared.
    print('\r' + line + ' ' * 40, end='')


keyboard.hook(print_pressed_keys)
keyboard.wait()

# print('Press and release your desired hotkey: ')
# hotkey = keyboard.read_hotkey()
# print('Hotkey selected: ', hotkey)
#
# def on_triggered():
#     print("Triggered!")
#
# keyboard.add_hotkey(hotkey, on_triggered)
# print("Press ESC to stop.")
# keyboard.wait('esc')