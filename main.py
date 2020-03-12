# _*_ coding:utf-8 _*_

import settings
from settings import CfgKeyEnum
from settings import ChoiceKeyTypes
import utils
from hot_key import HotKey
from hot_key import KeyListener
import queue
import sys
import gui_template
import wx
import key_scan_code_sender
from collections import OrderedDict
# import os
# import time
# import multiprocessing
# from multiprocessing import Process, Queue


thread_queue = queue.Queue()


def remove_comment_from_cfg(hotkey_cfg):
    for hotkey, macro_list in hotkey_cfg.items():
        macro_count = 0
        for macro_dic in macro_list:
            if CfgKeyEnum.comment.value in macro_dic.keys():
                del hotkey_cfg[hotkey][macro_count]
            macro_count += 1

    return hotkey_cfg


def start_cmd():
    # joytokey_cfg = settings.JoyToKeyCfg_dic[settings.KEY_GROUP]
    # key_group = settings.KEY_GROUP
    json_h = utils.JsonControl(settings.DEFAULT_CONFIG_NAME)
    json_h = json_h.read_config()

    hotkey_cfg = remove_comment_from_cfg(json_h['hot_key'])

    run_joy_to_key = utils.RunJoyToKey(settings.ini_full_path, settings.exec_full_path, json_h['joy_to_key'])
    run_joy_to_key.re_run_joy_to_key()

    code_sender = key_scan_code_sender.ScanCodeSender()
    hot_key = HotKey(code_sender, thread_queue)
    hot_key.regist_hotkey(hotkey_cfg)

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
        self.cfg_folder_path = settings.CONFIG_FOLDER_PATH
        self.cfg_file_path = ''
        # self.open_setting_frame()

    def open_setting_frame(self):

        frame = SettingFrame(self, self.cfg_folder_path)
        frame.Show(True)


class SettingFrame(gui_template.SettingFrame):
    def __init__(self, parent, cfg_file_path=None):
        gui_template.SettingFrame.__init__(self, parent)
        if cfg_file_path:
            self.cfg_file_path = cfg_file_path
        else:
            self.cfg_file_path = settings.DEFAULT_CONFIG_NAME
        self.config_data = OrderedDict()
        self.hotkey_dic = {}
        self.jot_to_key_cfg = ''
        self.init_gui_value()

    def init_gui_value(self):
        self.init_gui_listctrl()

    def init_gui_listctrl(self):
        self.hotkey_listctrl.DeleteAllItems()
        self.hotkey_listctrl.InsertColumn(0, 'KEY', width=200)
        self.hotkey_listctrl.InsertColumn(1, 'Comment', width=150)
        self.hotkey_listctrl.InsertColumn(2, 'MACROS', width=500)

        self.config_data = self.get_key_config()
        self.jot_to_key_cfg = self.config_data[CfgKeyEnum.joy_to_key_cfg.value]
        self.hotkey_dic = self.config_data[CfgKeyEnum.hot_key.value]

        item_index = 0
        for hotkey, macro_list in self.hotkey_dic.items():
            self.set_item_date(item_index, hotkey, macro_list)
            item_index += 1

        print(self.get_listctrl_all_col(self.hotkey_listctrl, 0))

    def set_item_date(self, item_index, hotkey, macro_list):
        macro_key_name = ''
        comment = ''
        index = self.hotkey_listctrl.InsertItem(item_index, hotkey)
        for key_macro in macro_list:
            if CfgKeyEnum.comment.value in key_macro:
                comment = key_macro[CfgKeyEnum.comment.value]
                continue
            key_name = key_macro[CfgKeyEnum.key_name.value]
            if macro_key_name:
                macro_key_name = macro_key_name + '+' + key_name
            else:
                macro_key_name = key_name

        self.hotkey_listctrl.SetItem(index, 2, macro_key_name)
        if comment:
            self.hotkey_listctrl.SetItem(index, 1, comment)
        return index

    @staticmethod
    def get_listctrl_all_col(list_ctrl, col_num):
        col_data = []
        count = list_ctrl.GetItemCount()
        for row in range(count):
            item = list_ctrl.GetItem(itemIdx=row, col=col_num)
            col_data.append(item.GetText())
        return col_data

    # def get_listctrl_row_data(self, list_ctrl, row_index):
    #     print(list_ctrl.GetItem(row_index, 0).GetText())

    def edit_hotkey(self, event):
        hotkey = event.GetText()
        # print(self.hotkey_dic[hotkey])
        self.open_editor_frame(hotkey)

    def add_new_hotkey(self, event=None):
        self.open_editor_frame(None)

    def delete_hotkey(self, evnet=None):
        selected_index = self.hotkey_listctrl.GetFirstSelected()
        if selected_index > -1:
            self.hotkey_listctrl.DeleteItem(selected_index)

        if selected_index > 0:
            self.hotkey_listctrl.Select(selected_index - 1)
        else:
            self.hotkey_listctrl.Select(selected_index)
        self.hotkey_listctrl.SetFocus()

    def item_move_up(self, event=None):
        selected_index = self.hotkey_listctrl.GetFirstSelected()
        if selected_index > 0:
            hot_key = self.hotkey_listctrl.GetItem(selected_index, 0).GetText()
            self.hotkey_listctrl.DeleteItem(selected_index)

            new_index = self.set_item_date(selected_index - 1, hot_key, self.hotkey_dic[hot_key])
            self.hotkey_listctrl.Select(new_index)
        self.hotkey_listctrl.SetFocus()

    def item_move_down(self, event=None):
        selected_index = self.hotkey_listctrl.GetFirstSelected()
        if selected_index < self.hotkey_listctrl.GetItemCount():
            hot_key = self.hotkey_listctrl.GetItem(selected_index, 0).GetText()
            self.hotkey_listctrl.DeleteItem(selected_index)

            new_index = self.set_item_date(selected_index + 1, hot_key, self.hotkey_dic[hot_key])
            self.hotkey_listctrl.Select(new_index)
        self.hotkey_listctrl.SetFocus()

    def open_editor_frame(self, hotkey):
        frame = EditFrame(self, self.cfg_file_path, self.config_data, hotkey)
        frame.Show(True)

    def get_key_config(self):
        cfg_h = utils.JsonControl(self.cfg_file_path)
        return cfg_h.read_config()

    def get_gui_hotkey_list(self):
        return self.get_listctrl_all_col(self.hotkey_listctrl, 0)

    def save_to_cfg(self, event=None):
        gui_hotkey_list = self.get_gui_hotkey_list()
        new_hotkey_data = self.config_data.copy()
        new_hotkey_data[CfgKeyEnum.hot_key.value] = OrderedDict()
        for hotkey in gui_hotkey_list:
            new_hotkey_data[CfgKeyEnum.hot_key.value][hotkey] = self.config_data[CfgKeyEnum.hot_key.value][hotkey]

        json_h = utils.JsonControl(self.cfg_file_path)
        json_h.write_config(new_hotkey_data)
        self.__close_frame()

    def __close_frame(self, event=None):
        self.Destroy()


class EditFrame(gui_template.EditFrame):
    def __init__(self, parent, cfg_file_path, config_data, hotkey):
        gui_template.EditFrame.__init__(self, parent)
        self.key_listener = None
        self.hot_key_timer = None
        self.hot_key_input = []
        self.cfg_file_path = cfg_file_path
        self.parent = parent
        self.config_data = config_data
        self.hotkey = hotkey
        if self.hotkey:
            self.one_hotkey_dic = {self.hotkey: self.config_data[CfgKeyEnum.hot_key.value][self.hotkey]}
        else:
            self.one_hotkey_dic = None
            # print(self.one_hotkey_dic)
        # self.config_data = config_date
        # self.choice_index = 0
        self.parent.Bind(wx.EVT_ACTIVATE, self.set_focus)

        self.init_gui()

    def init_gui(self):
        comment = ''

        # init list ctrl title
        self.edit_hotkey_listCtrl.InsertColumn(0, 'KEY', width=100)
        self.edit_hotkey_listCtrl.InsertColumn(1, 'Type')
        self.edit_hotkey_listCtrl.InsertColumn(2, 'Delay')

        if self.hotkey:
            # init hotkey text ctrl
            self.edit_hotkey_textCtrl.SetValue(self.hotkey)
            # init list ctrl item
            item_index = 0
            for key_macro in self.one_hotkey_dic[self.hotkey]:
                if CfgKeyEnum.comment.value in key_macro:
                    comment = key_macro[CfgKeyEnum.comment.value]
                    continue
                index = self.edit_hotkey_listCtrl.InsertItem(item_index, key_macro[CfgKeyEnum.key_name.value])
                self.edit_hotkey_listCtrl.SetItem(index, 1, key_macro[CfgKeyEnum.key_type.value])
                if key_macro[CfgKeyEnum.key_type.value] == CfgKeyEnum.delay.value:
                    self.edit_hotkey_listCtrl.SetItem(index, 2, str(key_macro[CfgKeyEnum.delay_time.value]))
                item_index += 1
            self.edit_comment_textCtrl.SetValue(comment)

        # init choice
        key_type_list = list(ChoiceKeyTypes.values())
        self.edit_keytype_choice.SetItems(key_type_list)
        self.edit_keytype_choice.SetSelection(0)

        self.arrange_gui_state()

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
            if self.is_choice_delay():
                if not self.check_delay_time_input():
                    wx.MessageBox('Input delay time format error,\n\n'
                                  'input delay time: {} format is wrong,\n'
                                  'should float format, for example: 5, 1, 0.5 or 0.3...\n'
                                  .format(self.edit_delaytime_textCtrl.GetValue()),
                                  'Error', wx.OK | wx.ICON_ERROR)
                    return

            selected_index = self.edit_hotkey_listCtrl.GetFirstSelected()
            if selected_index == -1:
                index = self.edit_hotkey_listCtrl.InsertItem(self.edit_hotkey_listCtrl.GetItemCount(), macro_key)
            else:
                index = self.edit_hotkey_listCtrl.InsertItem(selected_index + 1, macro_key)

            if self.is_choice_delay():
                self.edit_hotkey_listCtrl.SetItem(index, 1, self.edit_macrokey_textctrl.GetValue())
                self.edit_hotkey_listCtrl.SetItem(index, 2, self.edit_delaytime_textCtrl.GetValue())
            else:
                self.edit_hotkey_listCtrl.SetItem(index, 1, ChoiceKeyTypes[self.edit_keytype_choice.GetSelection()])

            self.edit_hotkey_listCtrl.Select(index)
            self.edit_hotkey_listCtrl.SetFocus()

    def check_delay_time_input(self):
        try:
            float(self.edit_delaytime_textCtrl.GetValue())
            return True
        except Exception as e:
            print('delay time not float format: {}'.format(e))
            return False

    def del_selected_listctrl(self, event):
        selected_index = self.edit_hotkey_listCtrl.GetFirstSelected()
        if selected_index > -1:
            self.edit_hotkey_listCtrl.DeleteItem(selected_index)

        if selected_index > 0:
            self.edit_hotkey_listCtrl.Select(selected_index - 1)
        else:
            self.edit_hotkey_listCtrl.Select(selected_index)
        self.edit_hotkey_listCtrl.SetFocus()

    def del_all_listctrl(self, event):
        self.edit_hotkey_listCtrl.DeleteAllItems()

    def user_input_to_dic(self):
        hot_key = self.edit_hotkey_textCtrl.GetValue()
        macro_key_list = []
        item_count = self.edit_hotkey_listCtrl.GetItemCount()
        col_count = self.edit_hotkey_listCtrl.GetColumnCount()
        macro_key_list.append({CfgKeyEnum.comment.value: self.edit_comment_textCtrl.GetValue()})
        for row in range(item_count):
            macro_dic = {}
            for col in range(col_count):
                data = self.edit_hotkey_listCtrl.GetItem(itemIdx=row, col=col).GetText()
                if col == 0:
                    macro_dic[CfgKeyEnum.key_name.value] = data
                elif col == 1:
                    macro_dic[CfgKeyEnum.key_type.value] = data
                elif col == 2:
                    if data:
                        macro_dic[CfgKeyEnum.delay_time.value] = float(data)

            macro_key_list.append(macro_dic)

        hot_key_dic = {hot_key: macro_key_list}
        return hot_key_dic

    def arrange_gui_state(self, event=None):
        # choice selected to delay
        if self.is_choice_delay():
            self.edit_macrokey_textctrl.SetValue('delay')
            self.edit_delaytime_textCtrl.SetValue('0.5')
            self.edit_delaytime_textCtrl.SetEditable(True)
        else:
            if self.edit_macrokey_textctrl.GetValue() == 'delay':
                self.edit_macrokey_textctrl.SetValue('')
                self.edit_delaytime_textCtrl.SetValue('')
            self.edit_delaytime_textCtrl.SetEditable(False)

        self.insert_edit_button.SetFocus()

    def is_choice_delay(self):
        delay_index = max(ChoiceKeyTypes.keys())
        if self.edit_keytype_choice.GetSelection() == delay_index:
            return True
        else:
            return False

    def reset_macro_edit(self, event):
        self.edit_keytype_choice.SetSelection(0)
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

    def close_frame_no_save(self, event):
        self.Close()

    def close_frame_save_config(self, event):
        # print(self.config_data)
        user_input_hotkey_dic = self.user_input_to_dic()
        user_input_hotkey = list(user_input_hotkey_dic.keys())[0]

        if self.hotkey:
            if self.hotkey != user_input_hotkey:
                self.over_write_hotkey_cfg(user_input_hotkey_dic)
            else:
                print('hotkey no modify, save to cfg file')
                self.config_data[CfgKeyEnum.hot_key.value][self.hotkey] = user_input_hotkey_dic[self.hotkey]
                self.save_change_to_cfg()
                self.__close_frame()
        else:
            if user_input_hotkey in self.config_data[CfgKeyEnum.hot_key.value].keys():
                self.over_write_hotkey_cfg(user_input_hotkey_dic)
            else:
                self.config_data[CfgKeyEnum.hot_key.value].update(user_input_hotkey_dic)
                self.save_change_to_cfg()
                self.__close_frame()

    def over_write_hotkey_cfg(self, new_hotkey):
        dlg = wx.MessageDialog(None,
                               'Your hotkey setting was changed,\n\n'
                               'Press YES to Override setting,\n'
                               'press NO for cancle\n',
                               'Question', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_INFORMATION)
        result = dlg.ShowModal()
        if result == wx.ID_YES:
            # do yes
            if self.hotkey:
                del self.config_data[CfgKeyEnum.hot_key.value][self.hotkey]
            self.config_data[CfgKeyEnum.hot_key.value].update(new_hotkey)
            self.save_change_to_cfg()
            self.__close_frame()
        else:
            # do no
            print('press no, do nothing')
        dlg.Destroy()

    def save_change_to_cfg(self):
        json_h = utils.JsonControl(self.cfg_file_path)
        json_h.write_config(self.config_data)
        # self.config_data[CfgKeyEnum.hot_key]
        # self.Close()

    def __close_frame(self, event=None):
        self.parent.Unbind(wx.EVT_ACTIVATE)
        self.parent.init_gui_value()
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
        # os.system("del " + settings.DEFAULT_CONFIG_NAME)
        # os.system("copy " + settings.TEST_CONFIG_NAME + " " + settings.DEFAULT_CONFIG_NAME)
        start_gui()
    else:
        start_cmd()
    # self.need_timer_restart = True
    # self.print_log(q)
