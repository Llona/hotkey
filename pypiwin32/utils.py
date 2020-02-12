import ctypes
import time
import configparser
import os
import subprocess
from multiprocessing import Process


def get_foreground_title():
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
    buff = ctypes.create_unicode_buffer(length + 1)
    ctypes.windll.user32.GetWindowTextW(hwnd, buff, length + 1)
    title = buff.value
    return title


def create_process(process_list, args_list):
    process_ll = []
    count = 0

    for process_f in process_list:
        process_ll.append(Process(target=process_f, args=args_list[count]))
        count += 1

    for process in process_ll:
        process.start()

    for process in process_ll:
        process.join()


class CheckWindowsIsForeground(object):
    def __init__(self, title_name):
        self.title_name = title_name

    def loop_check_is_foreground(self, queue_h):
        pre_title = get_foreground_title()
        while True:
            time.sleep(0.1)
            current_title = get_foreground_title()
            try:
                message = queue_h.get_nowait()
                if message == 'end':
                    return
            except Exception as e:
                str(e)

            if current_title != self.title_name:
                queue_h.put('exit_foreground')
            else:
                if pre_title != current_title:
                    queue_h.put('into_foreground')
            pre_title = current_title


class IniControl(object):
    def __init__(self, ini_full_path):
        self.ini_full_path = ini_full_path
        self.ini_format = 'utf8'
        self.format_list = [None, 'utf8', 'utf-8-sig', 'utf16', 'big5', 'gbk', 'gb2312']
        self.try_ini_format()

    def try_ini_format(self):
        for file_format in self.format_list:
            try:
                config_lh = configparser.ConfigParser()
                with open(self.ini_full_path, 'r', encoding=file_format) as file:
                    config_lh.read_file(file)
                self.ini_format = file_format
                print('find correct format {} in ini file: {}'.format(file_format, self.ini_full_path))
                return
            except Exception as e:
                print('checking {} format: {}'.format(self.ini_full_path, file_format))
                str(e)

    def read_config(self, section, key):
        try:
            config_lh = configparser.ConfigParser()
            file_ini_lh = open(self.ini_full_path, 'r', encoding=self.ini_format)
            config_lh.read_file(file_ini_lh)
            file_ini_lh.close()
            return config_lh.get(section, key)
        except Exception as e:
            print("Error! 讀取ini設定檔發生錯誤! " + self.ini_full_path)
            str(e)
            raise

    def write_config(self, sections, key, value):
        try:
            config_lh = configparser.ConfigParser()
            config_lh.optionxform = str
            file_ini_lh = open(self.ini_full_path, 'r', encoding=self.ini_format)
            config_lh.read_file(file_ini_lh)
            file_ini_lh.close()

            file_ini_lh = open(self.ini_full_path, 'w', encoding=self.ini_format)
            config_lh.set(sections, key, value)
            config_lh.write(file_ini_lh)
            file_ini_lh.close()
        except Exception as e:
            print("Error! 寫入ini設定檔發生錯誤! " + self.ini_full_path)
            str(e)
            raise


class RunJoyToKey(object):
    def __init__(self, ini_full_path, exec_full_path, cfg_file_name):
        self.ini_full_path = ini_full_path
        self.exec_full_path = exec_full_path
        self.cfg_file_name = cfg_file_name
        self.cfg_key = 'FileName'
        self.cfg_section = 'LastStatus'
        self.find_command = r'tasklist /fi "imagename eq joytokey.exe"'
        self.kill_command = r'taskkill /F /IM JoyToKey.exe'

    def re_run_joy_to_key(self):
        if self.is_joytokey_runing():
            if self.set_ini_cfg():
                self.kill_joy_to_key()
                print('重新啟動JoyToKey, 使用設定檔: {}'.format(self.cfg_file_name))
                os.system('start ' + self.exec_full_path)
        else:
            self.set_ini_cfg()
            os.system('start ' + self.exec_full_path)

    def kill_joy_to_key(self):
        os.system(self.kill_command)

    def is_joytokey_runing(self):
        line = subprocess.check_output(self.find_command).decode('big5', 'ignore').split("\r\n")
        if len(line) >= 5:
            return True
        return False

    def set_ini_cfg(self):
        ini_control = IniControl(self.ini_full_path)
        cfg_value = ini_control.read_config(self.cfg_section, self.cfg_key)
        if cfg_value == self.cfg_file_name:
            print('JoyToKey現在使用 {}, 不需要更改設定'.format(cfg_value))
            return False
        else:
            ini_control.write_config(self.cfg_section, self.cfg_key, self.cfg_file_name)
            print('JoyToKey設定檔改為: {}'.format(self.cfg_file_name))
            return True
