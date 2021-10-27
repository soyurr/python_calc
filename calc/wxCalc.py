'''
Created on 2021. 7. 21.
계산기 구현하기
@author: pc368
'''
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"계산기", pos = wx.DefaultPosition, size = wx.Size( 360,415 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.txt_res = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
        bSizer1.Add( self.txt_res, 0, wx.ALL, 5 )
        
        gSizer2 = wx.GridSizer( 7, 4, 5, 5 )
        
        self.m_button28 = wx.Button( self, wx.ID_ANY, u"%", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button28.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer2.Add( self.m_button28, 0, wx.ALL, 5 )
        
        self.m_button29 = wx.Button( self, wx.ID_ANY, u"CE", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button29.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer2.Add( self.m_button29, 0, wx.ALL, 5 )
        
        self.m_button30 = wx.Button( self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button30.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer2.Add( self.m_button30, 0, wx.ALL, 5 )
        
        self.m_button31 = wx.Button( self, wx.ID_ANY, u"←", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button31.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer2.Add( self.m_button31, 0, wx.ALL, 5 )
        
        self.m_button32 = wx.Button( self, wx.ID_ANY, u"1/x", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button32.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer2.Add( self.m_button32, 0, wx.ALL, 5 )
        
        self.m_button33 = wx.Button( self, wx.ID_ANY, u"x²", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button33.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer2.Add( self.m_button33, 0, wx.ALL, 5 )
        
        self.m_button34 = wx.Button( self, wx.ID_ANY, u"²√x", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button34.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer2.Add( self.m_button34, 0, wx.ALL, 5 )
        
        self.m_button35 = wx.Button( self, wx.ID_ANY, u"÷", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button35.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer2.Add( self.m_button35, 0, wx.ALL, 5 )
        
        self.m_button36 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button36.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button36.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
        
        gSizer2.Add( self.m_button36, 0, wx.ALL, 5 )
        
        self.m_button37 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button37.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button37.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
        
        gSizer2.Add( self.m_button37, 0, wx.ALL, 5 )
        
        self.m_button38 = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button38.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button38.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
        
        gSizer2.Add( self.m_button38, 0, wx.ALL, 5 )
        
        self.m_button39 = wx.Button( self, wx.ID_ANY, u"×", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button39.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer2.Add( self.m_button39, 0, wx.ALL, 5 )
        
        self.m_button40 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button40.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button40.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
        
        gSizer2.Add( self.m_button40, 0, wx.ALL, 5 )
        
        self.m_button41 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button41.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button41.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
        
        gSizer2.Add( self.m_button41, 0, wx.ALL, 5 )
        
        self.m_button42 = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button42.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button42.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
        
        gSizer2.Add( self.m_button42, 0, wx.ALL, 5 )
        
        self.m_button43 = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button43.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer2.Add( self.m_button43, 0, wx.ALL, 5 )
        
        self.m_button44 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button44.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button44.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
        
        gSizer2.Add( self.m_button44, 0, wx.ALL, 5 )
        
        self.m_button45 = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button45.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button45.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
        
        gSizer2.Add( self.m_button45, 0, wx.ALL, 5 )
        
        self.m_button46 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button46.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button46.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
        
        gSizer2.Add( self.m_button46, 0, wx.ALL, 5 )
        
        self.m_button47 = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button47.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer2.Add( self.m_button47, 0, wx.ALL, 5 )
        
        self.m_button48 = wx.Button( self, wx.ID_ANY, u"+/-", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button48.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer2.Add( self.m_button48, 0, wx.ALL, 5 )
        
        self.m_button49 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button49.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.m_button49.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
        
        gSizer2.Add( self.m_button49, 0, wx.ALL, 5 )
        
        self.m_button50 = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button50.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer2.Add( self.m_button50, 0, wx.ALL, 5 )
        
        self.m_button51 = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button51.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
        
        gSizer2.Add( self.m_button51, 0, wx.ALL, 5 )
        
        self.m_button54 = wx.Button( self, wx.ID_ANY, u"(", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button54.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer2.Add( self.m_button54, 0, wx.ALL, 5 )
        
        self.m_button55 = wx.Button( self, wx.ID_ANY, u")", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button55.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        gSizer2.Add( self.m_button55, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button28.Bind( wx.EVT_BUTTON, self.btnPer )
        self.m_button29.Bind( wx.EVT_BUTTON, self.btnCe )
        self.m_button30.Bind( wx.EVT_BUTTON, self.btnC )
        self.m_button31.Bind( wx.EVT_BUTTON, self.btnDelete )
        self.m_button32.Bind( wx.EVT_BUTTON, self.btnDivX )
        self.m_button33.Bind( wx.EVT_BUTTON, self.btnSqrX )
        self.m_button34.Bind( wx.EVT_BUTTON, self.btnRootX )
        self.m_button35.Bind( wx.EVT_BUTTON, self.btnDiv )
        self.m_button36.Bind( wx.EVT_BUTTON, self.btn7 )
        self.m_button37.Bind( wx.EVT_BUTTON, self.btn8 )
        self.m_button38.Bind( wx.EVT_BUTTON, self.btn9 )
        self.m_button39.Bind( wx.EVT_BUTTON, self.btnMulti )
        self.m_button40.Bind( wx.EVT_BUTTON, self.btn4 )
        self.m_button41.Bind( wx.EVT_BUTTON, self.btn5 )
        self.m_button42.Bind( wx.EVT_BUTTON, self.btn6 )
        self.m_button43.Bind( wx.EVT_BUTTON, self.btnMinus )
        self.m_button44.Bind( wx.EVT_BUTTON, self.btn1 )
        self.m_button45.Bind( wx.EVT_BUTTON, self.btn2 )
        self.m_button46.Bind( wx.EVT_BUTTON, self.btn3 )
        self.m_button47.Bind( wx.EVT_BUTTON, self.btnPlus )
        self.m_button48.Bind( wx.EVT_BUTTON, self.btnPosiNega )
        self.m_button49.Bind( wx.EVT_BUTTON, self.btn0 )
        self.m_button50.Bind( wx.EVT_BUTTON, self.btnDot )
        self.m_button51.Bind( wx.EVT_BUTTON, self.btnEqual )
        self.m_button54.Bind( wx.EVT_BUTTON, self.btnBracket1 )
        self.m_button55.Bind( wx.EVT_BUTTON, self.btnBracket2 )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    
    def OnDisplay( self, event ):
        if self.txt_res.GetLineText(0) == '0':
            self.txt_res.SetValue('')
        self.txt_res.AppendText(event.GetEventObject().GetLabel())
        event.Skip()
        
    def btnPer( self, event ):
        num = eval(self.txt_res.GetValue()+'/100.0')
        self.txt_res.SetValue(str(num))
        event.Skip()
    
    def btnCe( self, event ):
        
        event.Skip()
    
    def btnC( self, event ):
        self.txt_res.Clear()
        event.Skip()
    
    def btnDelete( self, event ):
        formula = self.txt_res.GetValue()
        self.txt_res.Clear()
        #맨오른쪽 값을 뺀 나머지 값을 셋팅함
        self.txt_res.SetValue(formula[:-1])
        event.Skip()
    
    def btnDivX( self, event ):
        num = eval('1/'+self.txt_res.GetValue())
        self.txt_res.SetValue(str(num))
        event.Skip()
    
    def btnSqrX( self, event ):
        num = eval(self.txt_res.GetValue()+'*'+self.txt_res.GetValue())
        self.txt_res.SetValue(str(num))
        event.Skip()
    
    def btnRootX( self, event ):
        num = eval(self.txt_res.GetValue()+'**0.5')
        self.txt_res.SetValue(str(num))
        event.Skip()
    
    def btnDiv( self, event ):
        self.txt_res.AppendText("/")
        event.Skip()
    
    def btn7( self, event ):
        self.txt_res.AppendText("7")
        event.Skip()
    
    def btn8( self, event ):
        self.txt_res.AppendText("8")
        event.Skip()
    
    def btn9( self, event ):
        self.txt_res.AppendText("9")
        event.Skip()
    
    def btnMulti( self, event ):
        self.txt_res.AppendText("*")
        event.Skip()
    
    def btn4( self, event ):
        self.txt_res.AppendText("4")
        event.Skip()
    
    def btn5( self, event ):
        self.txt_res.AppendText("5")
        event.Skip()
    
    def btn6( self, event ):
        self.txt_res.AppendText("6")
        event.Skip()
    
    def btnMinus( self, event ):
        self.txt_res.AppendText("-")
        event.Skip()
    
    def btn1( self, event ):
        self.txt_res.AppendText("1")
        event.Skip()
    
    def btn2( self, event ):
        self.txt_res.AppendText("2")
        event.Skip()
    
    def btn3( self, event ):
        self.txt_res.AppendText("3")
        event.Skip()
    
    def btnPlus( self, event ):
        self.txt_res.AppendText("+")
        event.Skip()
    
    #음수양수 부호
    def btnPosiNega( self, event ):
        try:
            res = -((int)(self.txt_res.GetValue()))
            self.txt_res.SetValue(str(res))
        except:
            res = 'error!'
            self.txt_res.setValue(res)
        event.Skip()
    
    def btn0( self, event ):
        self.txt_res.AppendText("0")
        event.Skip()
    
    def btnDot( self, event ):
        self.txt_res.AppendText(".")
        event.Skip()
    
    def btnEqual( self, event ):
        try:
            res = eval(self.txt_res.GetLineText(0))
            self.txt_res.SetValue(str(res))
        except:
            res = 'error!'
            self.txt_res.SetValue(res)
        event.Skip()
    
    def btnBracket1( self, event ):
        self.txt_res.AppendText("(")
        event.Skip()
    
    def btnBracket2( self, event ): 
        self.txt_res.AppendText(")")
        event.Skip()

    

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame2(parent=None)
    frame.Show()
    app.MainLoop()
