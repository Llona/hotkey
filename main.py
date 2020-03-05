import settings
from settings import CfgKeyEnum
import utils
from hot_key import HotKey
from hot_key import KeyListener
import queue
import sys
import gui_template
import wx
import key_scan_code_sender

# import time
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
    # print(json_h['hot_key'])
    # check_foreground = utils.CheckWindowsIsForeground(settings.FOREGROUND_TITLE)

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
            for key_macro in v:
                key_name = key_macro[CfgKeyEnum.key_name.value]
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
        hotkey = event.GetText()
        # todo: open edit frame
        print(self.hotkey_dic[hotkey])

        frame = EditFrame(self, self.hotkey_dic, hotkey)
        frame.Show(True)

    @staticmethod
    def get_key_config():
        cfg_h = utils.JsonControl(settings.DEFAULT_CONFIG_NAME)
        return cfg_h.read_config()


class EditFrame(gui_template.EditFrame):
    def __init__(self, parent, hotkey_dic, hotkey):
        gui_template.EditFrame.__init__(self, parent)
        self.key_listener = None
        self.hot_key_timer = None
        self.hot_key_input = []
        self.parent = parent
        self.hotkey_dic = hotkey_dic
        self.hotkey = hotkey
        # self.choice_index = 0
        self.parent.Bind(wx.EVT_ACTIVATE, self.set_focus)

        self.init_gui()

    def init_gui(self):
        self.edit_hotkey_listCtrl.InsertColumn(0, 'KEY', width=100)
        self.edit_hotkey_listCtrl.InsertColumn(1, 'Type')
        self.edit_hotkey_listCtrl.InsertColumn(2, 'Delay')
        self.edit_hotkey_textCtrl.SetValue(self.hotkey)

        for key_macro in self.hotkey_dic[self.hotkey]:
            index = self.edit_hotkey_listCtrl.InsertItem(2, key_macro[CfgKeyEnum.key_name.value])
            self.edit_hotkey_listCtrl.SetItem(index, 1, key_macro[CfgKeyEnum.key_type.value])
            if key_macro[CfgKeyEnum.key_type.value] == CfgKeyEnum.delay.value:
                self.edit_hotkey_listCtrl.SetItem(index, 2, str(key_macro[CfgKeyEnum.delay_time.value]))

        key_type_list = ["press", "hold", "release", "delay"]
        self.edit_keytype_choice.SetItems(key_type_list)
        self.edit_keytype_choice.SetSelection(0)

        self.arrange_gui()

    def create_key_listener(self, all_key=True):
        self.key_listener = None
        self.key_listener = KeyListener()
        self.key_listener.start(all_key)
        self.hot_key_timer = utils.CreateTimer()

    def stop_key_listener(self):
        self.key_listener = None
        self.hot_key_timer.stop_count_timer()
        self.hot_key_timer = None

    def edit_hotkey(self, event):
        self.edit_hotkey_textCtrl.SetValue('')
        self.create_key_listener()
        self.hot_key_timer.start_count_timer(0.3, self.insert_hotkey_to_textctrl, repeat=True)

    def insert_hotkey_to_textctrl(self):
        input_text = ''
        self.hot_key_input = self.key_listener.get_user_input_key_list()
        for text in self.hot_key_input:
            if input_text:
                input_text = input_text + '+' + text
            else:
                input_text = text
        if self.edit_hotkey_textCtrl.GetValue() != input_text:
            self.edit_hotkey_textCtrl.SetValue(input_text)

    def edit_macro(self, event):
        self.edit_macrokey_textctrl.SetValue('')
        self.create_key_listener(all_key=False)
        self.hot_key_timer.start_count_timer(0.3, self.insert_macrokey_to_textctrl, repeat=True)

    def insert_macrokey_to_textctrl(self):
        input_key = self.key_listener.press_key_one
        textctrl_key = self.edit_macrokey_textctrl.GetValue()
        if input_key and textctrl_key != input_key:
            self.edit_macrokey_textctrl.SetValue(input_key)

    def insert_macro_to_listctrl(self, event):
        macro_key = self.edit_macrokey_textctrl.GetValue()
        if macro_key:
            selected_index = self.edit_hotkey_listCtrl.GetFirstSelected()
            if selected_index == -1:
                index = self.edit_hotkey_listCtrl.InsertItem(self.edit_hotkey_listCtrl.GetItemCount(), macro_key)
            else:
                index = self.edit_hotkey_listCtrl.InsertItem(selected_index + 1, macro_key)

            self.edit_hotkey_listCtrl.SetItem(index, 1, self.edit_macrokey_textctrl.GetValue())

    def arrange_gui(self, event=None):
        # self.choice_index = self.edit_keytype_choice.GetString(self.edit_keytype_choice.GetSelection())
        # choice selected to delay
        if self.edit_keytype_choice.GetSelection() == 3:
            self.edit_macrokey_textctrl.SetValue('delay')
            self.edit_delaytime_textCtrl.SetValue('0.5')
            self.edit_delaytime_textCtrl.SetEditable(True)
        else:
            if self.edit_macrokey_textctrl.GetValue() == 'delay':
                self.edit_macrokey_textctrl.SetValue('')
                self.edit_delaytime_textCtrl.SetValue('')
            self.edit_delaytime_textCtrl.SetEditable(False)

    def stop_edit_hotkey(self, event):
        self.stop_key_listener()
        if self.edit_hotkey_textCtrl.GetValue() == '':
            self.edit_hotkey_textCtrl.SetValue(self.hotkey)

    def stop_edit_macro(self, event):
        self.stop_key_listener()

    def set_focus(self, event):
        # print(event.GetActive())
        if event.GetActive():
            self.SetFocus()
            self.insert_edit_button.SetFocus()

    def __close_frame(self, event):
        self.parent.Unbind(wx.EVT_ACTIVATE)
        self.Destroy()


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
