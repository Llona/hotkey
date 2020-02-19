import enum

test = False
DEFAULT_CONFIG_NAME = 'test.cfg'
FOREGROUND_TITLE = '未命名 - 記事本'
exec_full_path = r'C:\Users\william_liu\Desktop\joytokey\JoyToKey.exe'
ini_full_path = r'C:\Users\william_liu\Documents\JoyToKey\JoyToKey.ini'


class CfgKeyEnum(enum.Enum):
    joy_to_key_cfg = 'joy_to_key'
    hot_key = 'hot_key'


class KeyGroupEnum(enum.Enum):
    modau = '魔道'
    ninja = '忍者'
    slash = '槍劍'


JoyToKeyCfg_dic = {KeyGroupEnum.modau: 'DNF魔道',
                   KeyGroupEnum.ninja: 'DNF忍者',
                   KeyGroupEnum.slash: 'DNF槍劍'}

KEY_GROUP = KeyGroupEnum.modau

