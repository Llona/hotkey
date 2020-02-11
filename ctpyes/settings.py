import enum

test = False

exec_full_path = r'C:\Users\kkss\Desktop\JoyToKeyNoinstall\JoyToKey.exe'
ini_full_path = r'C:\Users\kkss\Desktop\JoyToKeyNoinstall\JoyToKey.ini'


class Character(enum.Enum):
    modau = '魔道'
    ninja = '忍者'
    slash = '槍劍'


JoyToKeyCfg_dic = {Character.modau: 'DNF魔道',
                   Character.ninja: 'DNF忍者',
                   Character.slash: 'DNF槍劍'}

CHARACTER = Character.modau
