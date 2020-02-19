import settings
from settings import CfgKeyEnum
import utils
from hot_key import HotKey
import queue
import sys
import gui_template
import wx
import key_scan_code_sender
# import multiprocessing
# from multiprocessing import Process, Queue


thread_queue = queue.Queue()


def start_cmd():
    # joytokey_cfg = settings.JoyToKeyCfg_dic[settings.KEY_GROUP]
    # key_group = settings.KEY_GROUP
    json_h = utils.JsonControl(settings.DEFAULT_CONFIG_NAME)
    json_h = json_h.read_config()

    run_joy_to_key = utils.RunJoyToKey(settings.ini_full_path, settings.exec_full_path, json_h['joy_to_key'])
    run_joy_to_key.re_run_joy_to_key()

    code_sender = key_scan_code_sender.ScanCodeSender()
    hot_key = HotKey(code_sender, thread_queue)
    hot_key.regist_hotkey(json_h['hot_key'])

    check_foreground = utils.CheckWindowsIsForeground(settings.FOREGROUND_TITLE)

    # check_foreground_thread = utils.CreateThread(thread_queue, 'stop_foreground_check')
    #
    # check_foreground_thread.start()
    # check_foreground_thread.join()

    # q = Queue()
    # process_lt = [hot_key.regist_hotkey, check_foreground.loop_check_is_foreground]
    # args_lt = [(key_group, q,), (q,)]
    #
    # all_process = Process(target=utils.create_process, args=(process_lt, args_lt,))
    # all_process.start()

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


class HotKeyFrame(gui_template.HotKeyFrame):
    def __init__(self, parent):
        gui_template.HotKeyFrame.__init__(self, parent)


class SettingFrame(gui_template.SettingFrame):
    def __init__(self, parent):
        gui_template.SettingFrame.__init__(self, parent)
        self.hotkey_dic = {}
        self.jot_to_key_cfg = ''
        self.init_gui_value()

    def init_gui_value(self):
        self.init_gui_listctrl()

    def init_gui_listctrl(self):
        self.hotkey_listctrl.InsertColumn(0, 'KEY', width=300)
        self.hotkey_listctrl.InsertColumn(1, 'MACROS', width=500)

        cfg_h = self.get_key_config()
        self.jot_to_key_cfg = cfg_h[CfgKeyEnum.joy_to_key_cfg.value]
        self.hotkey_dic = cfg_h[CfgKeyEnum.hot_key.value]

        for k, v in self.hotkey_dic.items():
            all_key_name = ''
            index = self.hotkey_listctrl.InsertItem(2, k)
            for key_name in v:
                if all_key_name:
                    all_key_name = all_key_name + '+' + key_name
                else:
                    all_key_name = key_name
            self.hotkey_listctrl.SetItem(index, 1, all_key_name)

        print(self.get_listctrl_all_col(self.hotkey_listctrl, 0))

    @staticmethod
    def get_listctrl_all_col(list_ctrl, col_num):
        col_data = []
        count = list_ctrl.GetItemCount()
        for row in range(count):
            item = list_ctrl.GetItem(itemIdx=row, col=col_num)
            col_data.append(item.GetText())
        return col_data

    def edit_hotkey(self, event):
        dic_key = event.GetText()
        # todo: open edit frame
        print(self.hotkey_dic[dic_key])

        frame = EditFrame(self)
        frame.Show(True)

    @staticmethod
    def get_key_config():
        cfg_h = utils.JsonControl(settings.DEFAULT_CONFIG_NAME)
        return cfg_h.read_config()


class EditFrame(gui_template.EditFrame):
    def __init__(self, parent):
        gui_template.EditFrame.__init__(self, parent)
        self.parent = parent
        self.parent.Bind(wx.EVT_ACTIVATE, self.set_focus)

    def set_focus(self, event):
        print(event.GetActive())
        if event.GetActive():
            self.SetFocus()
            self.edit_listctrl.SetFocus()


def start_gui():
    import ctypes
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    except Exception as e:
        print('set DPI awareness fail, only need in windows, skip it: {}'.format(e))
    app = wx.App(False)
    # frame = HotKeyFrame(None)
    frame = SettingFrame(None)
    frame.Show(True)
    # start the applications
    app.MainLoop()


if __name__ == '__main__':
    # multiprocessing.freeze_support()
    if len(sys.argv) > 1:
        start_gui()
    else:
        start_cmd()
    # self.need_timer_restart = True
    # self.print_log(q)
