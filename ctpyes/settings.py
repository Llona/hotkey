import enum

test = False

exec_full_path = r'C:\Users\william_liu\Desktop\joytokey\JoyToKey.exe'
ini_full_path = r'C:\Users\william_liu\Documents\JoyToKey\JoyToKey.ini'


class Character(enum.Enum):
    modau = '魔道'
    ninja = '忍者'
    slash = '槍劍'


JoyToKeyCfg_dic = {Character.modau: 'dnf_魔道',
                   Character.ninja: 'dnf_忍者',
                   Character.slash: 'dnf_槍劍'}

CHARACTER = Character.modau
