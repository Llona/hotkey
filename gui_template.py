# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class HotKeyFrame
###########################################################################

class HotKeyFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"AJ-HotKey", pos = wx.DefaultPosition, size = wx.Size( 798,689 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer_left = wx.BoxSizer( wx.HORIZONTAL )

        bSizer_listbox = wx.BoxSizer( wx.VERTICAL )

        sbSizer_keylist = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"HotKey Group" ), wx.VERTICAL )

        m_listBox_keylistChoices = [ u"Default" ]
        self.m_listBox_keylist = wx.ListBox( sbSizer_keylist.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,550 ), m_listBox_keylistChoices, wx.LB_HSCROLL )
        sbSizer_keylist.Add( self.m_listBox_keylist, 1, wx.EXPAND, 5 )

        bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button109 = wx.Button( sbSizer_keylist.GetStaticBox(), wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer18.Add( self.m_button109, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_button110 = wx.Button( sbSizer_keylist.GetStaticBox(), wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer18.Add( self.m_button110, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_button111 = wx.Button( sbSizer_keylist.GetStaticBox(), wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer18.Add( self.m_button111, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        sbSizer_keylist.Add( bSizer18, 1, wx.EXPAND, 5 )


        bSizer_listbox.Add( sbSizer_keylist, 1, wx.EXPAND|wx.LEFT, 5 )


        bSizer_left.Add( bSizer_listbox, 1, wx.EXPAND|wx.ALL, 5 )

        bSizer_right = wx.BoxSizer( wx.VERTICAL )

        self.m_dataViewCtrl1 = wx.dataview.DataViewCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer_right.Add( self.m_dataViewCtrl1, 1, wx.ALL|wx.EXPAND, 5 )

        sbSizer_joytokey = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"JoyToKey" ), wx.VERTICAL )

        self.m_checkBox1 = wx.CheckBox( sbSizer_joytokey.GetStaticBox(), wx.ID_ANY, u"使用JoyToKey", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer_joytokey.Add( self.m_checkBox1, 0, wx.ALL, 5 )

        bSizer_joytokey_path = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_path = wx.StaticText( sbSizer_joytokey.GetStaticBox(), wx.ID_ANY, u"JoyToKey路徑", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_path.Wrap( -1 )

        bSizer_joytokey_path.Add( self.m_staticText_path, 0, wx.ALL, 5 )

        bSizer_joytokey_path_input = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl55 = wx.TextCtrl( sbSizer_joytokey.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer_joytokey_path_input.Add( self.m_textCtrl55, 1, wx.ALL, 5 )

        self.m_button210 = wx.Button( sbSizer_joytokey.GetStaticBox(), wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer_joytokey_path_input.Add( self.m_button210, 0, wx.ALL, 5 )


        bSizer_joytokey_path.Add( bSizer_joytokey_path_input, 1, wx.EXPAND, 5 )


        sbSizer_joytokey.Add( bSizer_joytokey_path, 0, wx.EXPAND, 5 )

        bSizer_joytokey_ini = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText_ini = wx.StaticText( sbSizer_joytokey.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_ini.Wrap( -1 )

        bSizer_joytokey_ini.Add( self.m_staticText_ini, 0, wx.ALL, 5 )

        bSizerjoytokey_ini_input = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl551 = wx.TextCtrl( sbSizer_joytokey.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerjoytokey_ini_input.Add( self.m_textCtrl551, 1, wx.ALL, 5 )

        self.m_button2101 = wx.Button( sbSizer_joytokey.GetStaticBox(), wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizerjoytokey_ini_input.Add( self.m_button2101, 0, wx.ALL, 5 )


        bSizer_joytokey_ini.Add( bSizerjoytokey_ini_input, 1, wx.EXPAND, 5 )


        sbSizer_joytokey.Add( bSizer_joytokey_ini, 0, wx.EXPAND, 5 )

        bSizer_joytokey_cfg = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText402 = wx.StaticText( sbSizer_joytokey.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText402.Wrap( -1 )

        bSizer_joytokey_cfg.Add( self.m_staticText402, 0, wx.ALL, 5 )

        bSizer_joytokey_cfg_input = wx.BoxSizer( wx.HORIZONTAL )

        self.m_textCtrl552 = wx.TextCtrl( sbSizer_joytokey.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer_joytokey_cfg_input.Add( self.m_textCtrl552, 1, wx.ALL, 5 )

        self.m_button2102 = wx.Button( sbSizer_joytokey.GetStaticBox(), wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer_joytokey_cfg_input.Add( self.m_button2102, 0, wx.ALL, 5 )


        bSizer_joytokey_cfg.Add( bSizer_joytokey_cfg_input, 1, wx.EXPAND, 5 )


        sbSizer_joytokey.Add( bSizer_joytokey_cfg, 1, wx.EXPAND, 5 )


        bSizer_right.Add( sbSizer_joytokey, 1, wx.EXPAND, 5 )

        sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"前景偵測" ), wx.VERTICAL )

        self.m_checkBox2 = wx.CheckBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"只在程式位於前景時啟用", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer8.Add( self.m_checkBox2, 0, wx.ALL, 5 )

        bSizer87 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText44 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText44.Wrap( -1 )

        bSizer87.Add( self.m_staticText44, 0, wx.ALL, 5 )

        self.m_textCtrl60 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer87.Add( self.m_textCtrl60, 0, wx.ALL|wx.EXPAND, 5 )


        sbSizer8.Add( bSizer87, 1, wx.EXPAND, 5 )


        bSizer_right.Add( sbSizer8, 1, wx.EXPAND, 5 )


        bSizer_left.Add( bSizer_right, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer_left )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class SettingFrame
###########################################################################

class SettingFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 710,581 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer89 = wx.BoxSizer( wx.VERTICAL )

        sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.HORIZONTAL )

        bSizer29 = wx.BoxSizer( wx.VERTICAL )

        self.setting_cfg_name_staticText = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Hotkey name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.setting_cfg_name_staticText.Wrap( -1 )

        bSizer29.Add( self.setting_cfg_name_staticText, 0, wx.ALL, 5 )

        self.setting_cfg_name_textCtrl = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer29.Add( self.setting_cfg_name_textCtrl, 0, wx.ALL, 5 )


        sbSizer9.Add( bSizer29, 0, 0, 5 )


        bSizer89.Add( sbSizer9, 0, wx.EXPAND|wx.ALL, 5 )

        bSizer91 = wx.BoxSizer( wx.VERTICAL )

        bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

        self.setting_move_up_button17 = wx.Button( self, wx.ID_ANY, u"Up", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer28.Add( self.setting_move_up_button17, 0, wx.ALL, 5 )

        self.setting_move_down_button17 = wx.Button( self, wx.ID_ANY, u"Down", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer28.Add( self.setting_move_down_button17, 0, wx.ALL, 5 )

        self.setting_add_button = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer28.Add( self.setting_add_button, 0, wx.ALL, 5 )

        self.setting_delete_button17 = wx.Button( self, wx.ID_ANY, u"Delete select", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer28.Add( self.setting_delete_button17, 0, wx.ALL, 5 )


        bSizer91.Add( bSizer28, 0, 0, 5 )

        self.hotkey_listctrl = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_VRULES )
        bSizer91.Add( self.hotkey_listctrl, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer95 = wx.BoxSizer( wx.HORIZONTAL )

        self.setting_save_button = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer95.Add( self.setting_save_button, 0, wx.ALL, 5 )

        self.setting_cancle_button = wx.Button( self, wx.ID_ANY, u"Cancle", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer95.Add( self.setting_cancle_button, 0, wx.ALL, 5 )


        bSizer91.Add( bSizer95, 0, wx.ALIGN_RIGHT, 5 )


        bSizer89.Add( bSizer91, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )


        self.SetSizer( bSizer89 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.__close_frame )
        self.setting_move_up_button17.Bind( wx.EVT_BUTTON, self.item_move_up )
        self.setting_move_down_button17.Bind( wx.EVT_BUTTON, self.item_move_down )
        self.setting_add_button.Bind( wx.EVT_BUTTON, self.add_new_hotkey )
        self.setting_delete_button17.Bind( wx.EVT_BUTTON, self.delete_hotkey )
        self.hotkey_listctrl.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.edit_hotkey )
        self.setting_save_button.Bind( wx.EVT_BUTTON, self.save_to_cfg )
        self.setting_cancle_button.Bind( wx.EVT_BUTTON, self.__close_frame )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def __close_frame( self, event ):
        event.Skip()

    def item_move_up( self, event ):
        event.Skip()

    def item_move_down( self, event ):
        event.Skip()

    def add_new_hotkey( self, event ):
        event.Skip()

    def delete_hotkey( self, event ):
        event.Skip()

    def edit_hotkey( self, event ):
        event.Skip()

    def save_to_cfg( self, event ):
        event.Skip()



###########################################################################
## Class EditFrame
###########################################################################

class EditFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 610,539 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer23 = wx.BoxSizer( wx.VERTICAL )

        sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Editor" ), wx.VERTICAL )

        self.m_staticText9 = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"HotKey", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        sbSizer6.Add( self.m_staticText9, 0, wx.ALL, 5 )

        self.edit_hotkey_textCtrl = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        sbSizer6.Add( self.edit_hotkey_textCtrl, 0, wx.ALL|wx.EXPAND, 5 )

        self.edit_comment_staticText = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Comment", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.edit_comment_staticText.Wrap( -1 )

        sbSizer6.Add( self.edit_comment_staticText, 0, wx.ALL, 5 )

        self.edit_comment_textCtrl = wx.TextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer6.Add( self.edit_comment_textCtrl, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline3 = wx.StaticLine( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        sbSizer6.Add( self.m_staticline3, 0, wx.EXPAND|wx.ALL, 5 )

        sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Inser Macro Key" ), wx.VERTICAL )

        self.m_staticText10 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Macro Key", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        sbSizer8.Add( self.m_staticText10, 0, wx.RIGHT|wx.LEFT, 5 )

        bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

        self.edit_macrokey_textctrl = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        bSizer26.Add( self.edit_macrokey_textctrl, 0, wx.ALL, 5 )

        edit_keytype_choiceChoices = []
        self.edit_keytype_choice = wx.Choice( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, edit_keytype_choiceChoices, 0 )
        self.edit_keytype_choice.SetSelection( 0 )
        bSizer26.Add( self.edit_keytype_choice, 0, wx.ALL, 5 )


        sbSizer8.Add( bSizer26, 1, wx.EXPAND, 5 )

        self.m_staticText12 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Delay tims (Sec.)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        sbSizer8.Add( self.m_staticText12, 0, wx.RIGHT|wx.LEFT, 5 )

        bSizer29 = wx.BoxSizer( wx.VERTICAL )

        self.edit_delaytime_textCtrl = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer29.Add( self.edit_delaytime_textCtrl, 0, wx.ALL, 5 )

        self.m_staticline31 = wx.StaticLine( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer29.Add( self.m_staticline31, 0, wx.EXPAND |wx.ALL, 5 )


        sbSizer8.Add( bSizer29, 1, wx.EXPAND, 5 )

        bSizer251 = wx.BoxSizer( wx.HORIZONTAL )

        self.insert_edit_button = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Insert", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer251.Add( self.insert_edit_button, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

        self.edit_reset_macro_button = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer251.Add( self.edit_reset_macro_button, 0, wx.ALL, 5 )


        sbSizer8.Add( bSizer251, 1, wx.EXPAND, 5 )


        sbSizer6.Add( sbSizer8, 0, wx.EXPAND, 5 )

        bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

        self.edit_save_button = wx.Button( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer28.Add( self.edit_save_button, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.edit_cancel_button = wx.Button( sbSizer6.GetStaticBox(), wx.ID_ANY, u"Cancle", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer28.Add( self.edit_cancel_button, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


        sbSizer6.Add( bSizer28, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer23.Add( sbSizer6, 1, wx.BOTTOM|wx.EXPAND|wx.LEFT, 5 )


        bSizer22.Add( bSizer23, 1, wx.EXPAND, 5 )

        bSizer25 = wx.BoxSizer( wx.VERTICAL )

        sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )

        self.edit_hotkey_listCtrl = wx.ListCtrl( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VRULES )
        sbSizer7.Add( self.edit_hotkey_listCtrl, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

        self.edit_del_listctrl_item_button = wx.Button( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Del selected", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer26.Add( self.edit_del_listctrl_item_button, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )

        self.edit_del_all_listctrl_item_button = wx.Button( sbSizer7.GetStaticBox(), wx.ID_ANY, u"Del All", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer26.Add( self.edit_del_all_listctrl_item_button, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


        sbSizer7.Add( bSizer26, 0, wx.ALIGN_RIGHT, 5 )


        bSizer25.Add( sbSizer7, 1, wx.EXPAND, 5 )


        bSizer22.Add( bSizer25, 1, wx.BOTTOM|wx.EXPAND|wx.RIGHT, 5 )


        self.SetSizer( bSizer22 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.__close_frame )
        self.edit_hotkey_textCtrl.Bind( wx.EVT_KILL_FOCUS, self.stop_edit_hotkey )
        self.edit_hotkey_textCtrl.Bind( wx.EVT_SET_FOCUS, self.edit_hotkey )
        self.edit_macrokey_textctrl.Bind( wx.EVT_KILL_FOCUS, self.stop_edit_macro )
        self.edit_macrokey_textctrl.Bind( wx.EVT_SET_FOCUS, self.edit_macro )
        self.edit_keytype_choice.Bind( wx.EVT_CHOICE, self.arrange_gui_state )
        self.insert_edit_button.Bind( wx.EVT_BUTTON, self.insert_macro_to_listctrl )
        self.edit_reset_macro_button.Bind( wx.EVT_BUTTON, self.reset_macro_edit )
        self.edit_save_button.Bind( wx.EVT_BUTTON, self.close_frame_save_config )
        self.edit_cancel_button.Bind( wx.EVT_BUTTON, self.close_frame_no_save )
        self.edit_del_listctrl_item_button.Bind( wx.EVT_BUTTON, self.del_selected_listctrl )
        self.edit_del_all_listctrl_item_button.Bind( wx.EVT_BUTTON, self.del_all_listctrl )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def __close_frame( self, event ):
        event.Skip()

    def stop_edit_hotkey( self, event ):
        event.Skip()

    def edit_hotkey( self, event ):
        event.Skip()

    def stop_edit_macro( self, event ):
        event.Skip()

    def edit_macro( self, event ):
        event.Skip()

    def arrange_gui_state( self, event ):
        event.Skip()

    def insert_macro_to_listctrl( self, event ):
        event.Skip()

    def reset_macro_edit( self, event ):
        event.Skip()

    def close_frame_save_config( self, event ):
        event.Skip()

    def close_frame_no_save( self, event ):
        event.Skip()

    def del_selected_listctrl( self, event ):
        event.Skip()

    def del_all_listctrl( self, event ):
        event.Skip()


