import settings
import utils
from hot_key import HotKey
import multiprocessing
from multiprocessing import Process, Queue


def start():
    joytokey_cfg = settings.JoyToKeyCfg_dic[settings.KEY_GROUP]
    key_group = settings.KEY_GROUP

    run_joy_to_key = utils.RunJoyToKey(settings.ini_full_path, settings.exec_full_path, joytokey_cfg)
    run_joy_to_key.re_run_joy_to_key()
    hot_key = HotKey()
    # dnf_char.regist_hotkey(character)

    check_foreground = utils.CheckWindowsIsForeground(settings.FOREGROUND_TITLE)

    q = Queue()
    process_lt = [hot_key.regist_hotkey, check_foreground.loop_check_is_foreground]
    args_lt = [(key_group, q,), (q,)]

    all_process = Process(target=utils.create_process, args=(process_lt, args_lt,))
    all_process.start()

    # while True:
    #     time.sleep(0.1)
    #     try:
    #         message = q.get_nowait()
    #
    #         if message == 'exit_foreground':
    #             keyboard.send('esc')
    #             process_lt = [check_foreground.loop_check_is_foreground]
    #             args_lt = [(q,)]
    #
    #             all_process = Process(target=create_process, args=(process_lt, args_lt,))
    #             all_process.start()
    #         elif message == 'into_foreground':
    #             process_lt = [dnf_char.regist_hotkey]
    #             args_lt = [(character, q,)]
    #
    #             all_process = Process(target=create_process, args=(process_lt, args_lt,))
    #             all_process.start()
    #     except:
    #         pass


if __name__ == '__main__':
    multiprocessing.freeze_support()
    start()
    # self.need_timer_restart = True
    # self.print_log(q)
