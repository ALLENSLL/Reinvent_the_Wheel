#-*- coding:utf-8 -*-

import os
import wx
from random import randrange, choice 
import copy

class Core(object):
    def __init__(self,rank=4):
        self.rank = rank
        self.score = 0
        self.bestscore = 0
        self.isgameover = False
        self.loadScore()
        self.data = [[0 for i in range(rank)] for k in range(rank)]
        self.spawn()
        self.spawn()
    
    def againCore(self):
        self.score = 0
        self.isgameover = False
        self.data = [[0 for i in range(self.rank)] for k in range(self.rank)]
        self.spawn()
        self.spawn()        
        
    def loadScore(self):
        if os.path.exists('bestscore.ini'):  
            with open('bestscore.ini') as f:
                self.bestscore = int(f.read())            
    def saveScore(self):
        with open('bestscore.ini','w') as f:
            f.write(str(self.bestscore))
    
    def transpose(self):
         self.data = [list(row) for row in zip(*self.data)]
    
    def spawn(self):
        new_element = 2 if randrange(100) < 90 else 4
        try:
            (row,col) = choice([(row,col) for row in range(self.rank) for col in range(self.rank) if self.data[row][col] == 0]) 
            self.data[row][col] = new_element
        except:
            pass
    
    def merge(self,up):
        oldData = copy.deepcopy(self.data)
        for col in range(self.rank):
            nozero = [self.data[row][col] for row in range(self.rank) if self.data[row][col] != 0]
            if len(nozero) >= 2:
                if up:
                    i = 1
                    while i < len(nozero):
                        if nozero[i-1] == nozero[i]:
                            del nozero[i]
                            nozero[i-1] *= 2
                            self.score += nozero[i-1]
                            i += 1
                        i += 1
                else:
                    i = len(nozero)-1
                    while i>0:
                        if nozero[i-1] == nozero[i]:
                            del nozero[i]
                            nozero[i-1] *= 2
                            self.score += nozero[i-1]
                            i -= 1
                        i -= 1
            for i in range(self.rank-len(nozero)):
                if up:
                    nozero.append(0)
                else:
                    nozero.insert(0,0)
            for row in range(self.rank):
                self.data[row][col] = nozero[row]
        if self.score > self.bestscore:
            self.bestscore = self.score
        return oldData!=self.data
        
    def ifGameOver(self):
        temp = copy.deepcopy(self)
        if not temp.merge(True) and not temp.merge(False):
            temp.transpose()
            if not temp.merge(True) and not temp.merge(False):
                self.isgameover = True
 
        
    def upgrade(self,direction):
        if self.isgameover == False:
            if direction == 'UP':
                isMove = self.merge(True)
            elif direction == 'DOWN':
                isMove = self.merge(False)
            else:
                self.transpose()
                if direction == 'LEFT':
                    isMove = self.merge(True)
                elif direction == 'RIGHT':
                    isMove = self.merge(False)
                self.transpose()
            if isMove:
                self.spawn()
            self.ifGameOver()
        
class Frame(wx.Frame):
    def __init__(self,title):
        super(Frame,self).__init__(None,-1,title,
                style=wx.DEFAULT_FRAME_STYLE^\
                      wx.MAXIMIZE_BOX^\
                      wx.RESIZE_BORDER)

        self.colors = {
                0:(204,192,179),2:(238, 228, 218),4:(237, 224, 200),
                8:(242, 177, 121),16:(245, 149, 99),32:(246, 124, 95),
                64:(246, 94, 59),128:(237, 207, 114),256:(237, 204, 97),
                512:(237, 200, 80),1024:(237, 197, 63),2048:(237, 194, 46),
                'more':(60,58,50)}
        self.bgFont = wx.Font(50,wx.SWISS,wx.NORMAL,wx.BOLD,face=u"Roboto")
        self.scFont = wx.Font(36,wx.SWISS,wx.NORMAL,wx.BOLD,face=u"Roboto")
        self.smFont = wx.Font(12,wx.SWISS,wx.NORMAL,wx.NORMAL,face=u"Roboto")
                
        self.core = Core()      
        
        self.setIcon()
        
        panel = wx.Panel(self)
        panel.Bind(wx.EVT_KEY_DOWN,self.onKeyDown)
        panel.SetFocus()

        self.initBuffer()
        self.Bind(wx.EVT_SIZE,self.onSize) 
        self.Bind(wx.EVT_PAINT, self.onPaint)
        self.Bind(wx.EVT_CLOSE,self.onClose)
        self.SetClientSize((505,640))
        self.Center()
        self.Show()
        
    def onPaint(self,event):
        dc = wx.BufferedPaintDC(self,self.buffer)
    
    def onClose(self,event):
        self.core.saveScore()
        self.Destroy()

    def setIcon(self):
        icon = wx.Icon("icon.ico",wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        
    def initBuffer(self):
        w,h = self.GetClientSize()
        self.buffer = wx.EmptyBitmap(w,h)

    def onSize(self,event):
        self.initBuffer()
        self.drawAll()
        
    def drawBg(self,dc):
        dc.SetBackground(wx.Brush((250,248,239)))
        dc.Clear()
        dc.SetBrush(wx.Brush((187,173,160)))
        dc.SetPen(wx.Pen((187,173,160)))
        dc.DrawRoundedRectangle(15,150,475,475,5)

    def drawLogo(self,dc):
        dc.SetFont(self.bgFont)
        dc.SetTextForeground((119,110,101))
        dc.DrawText(u"2048",15,26)

    def drawScore(self,dc):            
        dc.SetFont(self.smFont)
        scoreLabelSize = dc.GetTextExtent(u"SCORE")
        bestLabelSize = dc.GetTextExtent(u"BEST")
        curScoreBoardMinW = 15*2+scoreLabelSize[0]
        bstScoreBoardMinW = 15*2+bestLabelSize[0]
        curScoreSize = dc.GetTextExtent(str(self.core.score))
        bstScoreSize = dc.GetTextExtent(str(self.core.bestscore))
        curScoreBoardNedW = 10+curScoreSize[0]
        bstScoreBoardNedW = 10+bstScoreSize[0]
        curScoreBoardW = max(curScoreBoardMinW,curScoreBoardNedW)
        bstScoreBoardW = max(bstScoreBoardMinW,bstScoreBoardNedW)
        dc.SetBrush(wx.Brush((187,173,160)))
        dc.SetPen(wx.Pen((187,173,160)))
        dc.DrawRoundedRectangle(505-15-bstScoreBoardW,40,bstScoreBoardW,50,3)
        dc.DrawRoundedRectangle(505-15-bstScoreBoardW-5-curScoreBoardW,40,curScoreBoardW,50,3)
        dc.SetTextForeground((238,228,218))
        dc.DrawText(u"BEST",505-15-bstScoreBoardW+(bstScoreBoardW-bestLabelSize[0])/2,48)
        dc.DrawText(u"SCORE",505-15-bstScoreBoardW-5-curScoreBoardW+(curScoreBoardW-scoreLabelSize[0])/2,48)
        dc.SetTextForeground((255,255,255))
        dc.DrawText(str(self.core.bestscore),505-15-bstScoreBoardW+(bstScoreBoardW-bstScoreSize[0])/2,68)
        dc.DrawText(str(self.core.score),505-15-bstScoreBoardW-5-curScoreBoardW+(curScoreBoardW-curScoreSize[0])/2,68)
    
    def drawTiles(self,dc):
        dc.SetFont(self.scFont)
        for row in range(self.core.rank):
            for col in range(self.core.rank):
                value = self.core.data[row][col]
                if value < 2048:
                    color = self.colors[value]
                else:
                    color = self.colors['more']
                if value==2 or value==4:
                    dc.SetTextForeground((119,110,101))
                else:
                    dc.SetTextForeground((255,255,255))
                dc.SetBrush(wx.Brush(color))
                dc.SetPen(wx.Pen(color))
                dc.DrawRoundedRectangle(30+col*115,165+row*115,100,100,2)
                size = dc.GetTextExtent(str(value))
                while size[0]>100-15*2:
                    self.scFont = wx.Font(self.scFont.GetPointSize()*4/5,wx.SWISS,wx.NORMAL,wx.BOLD,face=u"Roboto")
                    dc.SetFont(self.scFont)
                    size = dc.GetTextExtent(str(value))
                if value!=0: dc.DrawText(str(value),30+col*115+(100-size[0])/2,165+row*115+(100-size[1])/2)

    def drawAll(self):
        dc = wx.BufferedDC(wx.ClientDC(self),self.buffer)
        self.drawBg(dc)
        self.drawLogo(dc)
        self.drawScore(dc)
        self.drawTiles(dc)

    def drawChange(self):
        dc = wx.BufferedDC(wx.ClientDC(self),self.buffer)
        self.drawScore(dc)
        self.drawTiles(dc)
        
    def onKeyDown(self,event):
        keyCode = event.GetKeyCode()       
        if keyCode == wx.WXK_UP:
            self.core.upgrade('UP')
            self.ctlGame()
        elif keyCode == wx.WXK_DOWN:
            self.core.upgrade('DOWN')
            self.ctlGame()
        elif keyCode == wx.WXK_LEFT:
            self.core.upgrade('LEFT')
            self.ctlGame()
        elif keyCode == wx.WXK_RIGHT:
            self.core.upgrade('RIGHT')
            self.ctlGame()
            
    def ctlGame(self):
        self.drawChange()
        if self.core.isgameover == True:
            if wx.MessageBox(u'Game Over! Try again?',u'2048',
                    wx.YES_NO|wx.ICON_INFORMATION) == wx.YES:
                self.core.againCore()
                self.drawChange()
                
if __name__ == '__main__':
    app = wx.App()
    Frame(u'2048 with help of shiyanlou')
    app.MainLoop()
