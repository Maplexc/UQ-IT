import tkinter as tk
from game_model import *


class PlayGame:
    """ play game """
    def __init__(self, canvas, var):
        """ play game within the canvas """
        self._canvas = canvas
        self.color = ['#CC8686','#DBB18E','#F9FF7D','#A0E57E','#6AB3EE','#8EDBC9','#CFF2BA','#ADBCFF']
        self.var = var

    def get_begin(self):
        """ start a game """
        base = self._canvas.create_rectangle(50,256,650,270, fill = '#A67D26', outline = '#644B17')
        self.rod1 = Rod(1)
        self._canvas.create_rectangle(145,100,155,256, fill = '#A67D26', outline = '#644B17')
        self.rod2 = Rod(2)
        self._canvas.create_rectangle(345,100,355,256, fill = '#A67D26', outline = '#644B17')
        self.rod3 = Rod(3)
        self._canvas.create_rectangle(545,100,555,256, fill = '#A67D26', outline = '#644B17')
        self.disk0 = Disk(0, self.color[0])
        self.disk_draw0 = self._canvas.create_rectangle(60, 240, 240, 255, fill = self.disk0._color, outline = 'azure')
        self._canvas.tag_bind(self.disk_draw0, '<Button-1>', self.press)
        self._canvas.tag_bind(self.disk_draw0, '<B1-Motion>', self.move)
        self._canvas.tag_bind(self.disk_draw0,'<ButtonRelease-1>', self.release)
        self.rod1.add_disk(self.disk0)
        num = self.var.get()
        if num >= 2:
            self.disk1 = Disk(1, self.color[1])
            self.disk_draw1 = self._canvas.create_rectangle(70, 225, 230, 240, fill = self.disk1._color, outline = 'azure')
            self._canvas.tag_bind(self.disk_draw1, '<Button-1>', self.press)
            self._canvas.tag_bind(self.disk_draw1, '<B1-Motion>', self.move)
            self._canvas.tag_bind(self.disk_draw1,'<ButtonRelease-1>', self.release)
            self.rod1.add_disk(self.disk1)
        if num >= 3:
            self.disk2 = Disk(2, self.color[2])
            self.disk_draw2 = self._canvas.create_rectangle(80, 210, 220, 225, fill = self.disk2._color, outline = 'azure')
            self._canvas.tag_bind(self.disk_draw2, '<Button-1>', self.press)
            self._canvas.tag_bind(self.disk_draw2, '<B1-Motion>', self.move)
            self._canvas.tag_bind(self.disk_draw2,'<ButtonRelease-1>', self.release)
            self.rod1.add_disk(self.disk2)
        if num >= 4:
            self.disk3 = Disk(3, self.color[3])
            self.disk_draw3 = self._canvas.create_rectangle(90,195,210,210, fill = self.disk3._color, outline = 'azure')
            self._canvas.tag_bind(self.disk_draw3, '<Button-1>', self.press)
            self._canvas.tag_bind(self.disk_draw3, '<B1-Motion>', self.move)
            self._canvas.tag_bind(self.disk_draw3,'<ButtonRelease-1>', self.release)
            self.rod1.add_disk(self.disk3)
        if num >= 5:
            self.disk4 = Disk(4, self.color[4])
            self.disk_draw4 = self._canvas.create_rectangle(100,180,200,195, fill = self.disk4._color, outline = 'azure')
            self._canvas.tag_bind(self.disk_draw4, '<Button-1>', self.press)
            self._canvas.tag_bind(self.disk_draw4, '<B1-Motion>', self.move)
            self._canvas.tag_bind(self.disk_draw4,'<ButtonRelease-1>', self.release)
            self.rod1.add_disk(self.disk4)
        if num >= 6:
            self.disk5 = Disk(5, self.color[5])
            self.disk_draw5 = self._canvas.create_rectangle(110,165,190,180, fill = self.disk5._color, outline = 'azure')
            self._canvas.tag_bind(self.disk_draw5, '<Button-1>', self.press)
            self._canvas.tag_bind(self.disk_draw5, '<B1-Motion>', self.move)
            self._canvas.tag_bind(self.disk_draw5,'<ButtonRelease-1>', self.release)
            self.rod1.add_disk(self.disk5)
        if num >= 7:
            self.disk6 = Disk(6, self.color[6])
            self.disk_draw6 = self._canvas.create_rectangle(120,150,180,165, fill = self.disk6._color, outline = 'azure')
            self._canvas.tag_bind(self.disk_draw6, '<Button-1>', self.press)
            self._canvas.tag_bind(self.disk_draw6, '<B1-Motion>', self.move)
            self._canvas.tag_bind(self.disk_draw6,'<ButtonRelease-1>', self.release)
            self.rod1.add_disk(self.disk6)
        if num >= 8:
            self.disk7 = Disk(7, self.color[7])
            self.disk_draw7 = self._canvas.create_rectangle(130,135,170,150, fill = self.disk7._color, outline = 'azure')
            self._canvas.tag_bind(self.disk_draw7, '<Button-1>', self.press)
            self._canvas.tag_bind(self.disk_draw7, '<B1-Motion>', self.move)
            self._canvas.tag_bind(self.disk_draw7,'<ButtonRelease-1>', self.release)
            self.rod1.add_disk(self.disk7)

    def press(self, e):
        """ motion when press the disk """
        self.prex = e.x
        self.prey = e.y
        self.lastx = e.x
        self.lasty = e.y
        self.top1 = self.rod1.get_top()
        if self.top1 != None:
            self.rod1.get_top().set_rod(1)
            self.top1.move = False
        self.top2 = self.rod2.get_top()
        if self.top2 != None:
            self.rod2.get_top().set_rod(2)
            self.top2.move = False
        self.top3 = self.rod3.get_top()
        if self.top3 != None:
            self.rod3.get_top().set_rod(3)
            self.top3.move = False

    def move(self, e):
        """ motion when move the disk """
        ## movement of top disk in rod1 
        if self.prex >= 60 and self.prex <= 240 and self.prey <= 255 and self.prey >= 100:
            if self.top1 != None:
                top1_num = self.top1.get_id()
                if top1_num == 0:
                    self._canvas.move(self.disk_draw0,e.x - self.lastx, e.y - self.lasty)
                    self.top1_draw = self.disk_draw0
                elif top1_num == 1:
                    self._canvas.move(self.disk_draw1,e.x - self.lastx, e.y - self.lasty)
                    self.top1_draw = self.disk_draw1        
                elif top1_num == 2:
                    self._canvas.move(self.disk_draw2,e.x - self.lastx, e.y - self.lasty)
                    self.top1_draw = self.disk_draw2
                elif top1_num == 3:
                    self._canvas.move(self.disk_draw3,e.x - self.lastx, e.y - self.lasty)
                    self.top1_draw = self.disk_draw3
                elif top1_num == 4:
                    self._canvas.move(self.disk_draw4,e.x - self.lastx, e.y - self.lasty)
                    self.top1_draw = self.disk_draw4
                elif top1_num == 5:
                    self._canvas.move(self.disk_draw5,e.x - self.lastx, e.y - self.lasty)
                    self.top1_draw = self.disk_draw5
                elif top1_num == 6:
                    self._canvas.move(self.disk_draw6,e.x - self.lastx, e.y - self.lasty)
                    self.top1_draw = self.disk_draw6
                elif top1_num == 7:
                    self._canvas.move(self.disk_draw7,e.x - self.lastx, e.y - self.lasty)
                    self.top1_draw = self.disk_draw7                
                self.lastx = e.x
                self.lasty = e.y
                self.top1.move = True
        ## movement of top disk in rod2
        elif self.prex >= 260 and self.prex <= 440 and self.prey <= 255 and self.prey >= 100:    
            if self.top2 != None:
                top2_num = self.top2.get_id()
                if top2_num == 0:
                    self._canvas.move(self.disk_draw0,e.x - self.lastx, e.y - self.lasty)
                    self.top2_draw = self.disk_draw0
                elif top2_num == 1:
                    self._canvas.move(self.disk_draw1,e.x - self.lastx, e.y - self.lasty)
                    self.top2_draw = self.disk_draw1
                elif top2_num == 2:
                    self._canvas.move(self.disk_draw2,e.x - self.lastx, e.y - self.lasty)
                    self.top2_draw = self.disk_draw2
                elif top2_num == 3:
                    self._canvas.move(self.disk_draw3,e.x - self.lastx, e.y - self.lasty)
                    self.top2_draw = self.disk_draw3
                elif top2_num == 4:
                    self._canvas.move(self.disk_draw4,e.x - self.lastx, e.y - self.lasty)
                    self.top2_draw = self.disk_draw4
                elif top2_num == 5:
                    self._canvas.move(self.disk_draw5,e.x - self.lastx, e.y - self.lasty)
                    self.top2_draw = self.disk_draw5                    
                elif top2_num == 6:
                    self._canvas.move(self.disk_draw6,e.x - self.lastx, e.y - self.lasty)
                    self.top2_draw = self.disk_draw6
                elif top2_num == 7:
                    self._canvas.move(self.disk_draw7,e.x - self.lastx, e.y - self.lasty)
                    self.top2_draw = self.disk_draw7
                self.lastx = e.x
                self.lasty = e.y
                self.top2.move = True
        ## movement of top disk in rod3
        elif self.prex >= 460 and self.prex <= 640 and self.prey <= 255 and self.prey >= 100:    
            if self.top3 != None:
                top3_num = self.top3.get_id()
                if top3_num == 0:
                    self._canvas.move(self.disk_draw0,e.x - self.lastx, e.y - self.lasty)
                    self.top3_draw = self.disk_draw0
                elif top3_num == 1:
                    self._canvas.move(self.disk_draw1,e.x - self.lastx, e.y - self.lasty)
                    self.top3_draw = self.disk_draw1
                elif top3_num == 2:
                    self._canvas.move(self.disk_draw2,e.x - self.lastx, e.y - self.lasty)
                    self.top3_draw = self.disk_draw2
                elif top3_num == 3:
                    self._canvas.move(self.disk_draw3,e.x - self.lastx, e.y - self.lasty)
                    self.top3_draw = self.disk_draw3
                elif top3_num == 4:
                    self._canvas.move(self.disk_draw4,e.x - self.lastx, e.y - self.lasty)
                    self.top3_draw = self.disk_draw4
                elif top3_num == 5:
                    self._canvas.move(self.disk_draw5,e.x - self.lastx, e.y - self.lasty)
                    self.top3_draw = self.disk_draw5
                elif top3_num == 6:
                    self._canvas.move(self.disk_draw6,e.x - self.lastx, e.y - self.lasty)
                    self.top3_draw = self.disk_draw6
                elif top3_num == 7:
                    self._canvas.move(self.disk_draw7,e.x - self.lastx, e.y - self.lasty)
                    self.top3_draw = self.disk_draw7
                self.lastx = e.x
                self.lasty = e.y
                self.top3.move = True
        
    def release(self, e):
        """ motion when release the disk """
        if e.x >= 90 and e.x <= 210 and e.y <= 255 and e.y >= 100:
            ### disk move from rod1 to rod1
            if self.top1 != None and self.top1.move:
                self._canvas.move(self.top1_draw, self.prex - e.x, self.prey - e.y)
            ### disk move from rod2 to rod1
            if self.top2 != None and self.top2.move:
                if self.rod1.add_disk(self.top2) == True:
                    self.rod2.remove_disk(self.top2)
                    disty = ((self.rod2.get_num_of_disks()+1) - (self.rod1.get_num_of_disks())) * 15
                    distx = -200
                    self._canvas.move(self.top2_draw, self.prex - e.x + distx, self.prey - e.y + disty)
                else:
                    self._canvas.move(self.top2_draw, self.prex - e.x, self.prey - e.y)
            ### disk move from rod3 to rod1
            if self.top3 != None and self.top3.move:
                if self.rod1.add_disk(self.top3) == True:
                    self.rod3.remove_disk(self.top3)
                    disty = ((self.rod3.get_num_of_disks()+1) - (self.rod1.get_num_of_disks())) * 15
                    distx = -400
                    self._canvas.move(self.top3_draw, self.prex - e.x + distx, self.prey - e.y + disty)
                else:
                    self._canvas.move(self.top3_draw, self.prex - e.x, self.prey - e.y)
        elif e.x >= 290 and e.x <= 410 and e.y <= 255 and e.y >= 100:
            ### disk move from rod2 to rod2
            if self.top2 != None and self.top2.move:
                self._canvas.move(self.top2_draw, self.prex - e.x, self.prey - e.y)
            ### disk move from rod1 to rod2
            if self.top1 != None and self.top1.move:
                if self.rod2.add_disk(self.top1) == True:
                    self.rod1.remove_disk(self.top1)
                    disty = ((self.rod1.get_num_of_disks()+1) - (self.rod2.get_num_of_disks())) * 15
                    distx = 200
                    self._canvas.move(self.top1_draw, self.prex - e.x + distx, self.prey - e.y + disty)
                else:
                    self._canvas.move(self.top1_draw, self.prex - e.x, self.prey - e.y)
            ### disk move from rod3 to rod2
            if self.top3 != None and self.top3.move:
                if self.rod2.add_disk(self.top3) == True:
                    self.rod3.remove_disk(self.top3)
                    disty = ((self.rod3.get_num_of_disks()+1) - (self.rod2.get_num_of_disks())) * 15
                    distx = -200
                    self._canvas.move(self.top3_draw, self.prex - e.x + distx, self.prey - e.y + disty)
                else:
                    self._canvas.move(self.top3_draw, self.prex - e.x, self.prey - e.y)
        elif e.x >= 490 and e.x <= 610 and e.y <= 255 and e.y >= 100:
            ### disk move from rod3 to rod3
            if self.top3 != None and self.top3.move:
                self._canvas.move(self.top3_draw, self.prex - e.x, self.prey - e.y)    
            ### disk move from rod1 to rod3
            if self.top1 != None and self.top1.move:
                if self.rod3.add_disk(self.top1) == True:
                    self.rod1.remove_disk(self.top1)
                    disty = ((self.rod1.get_num_of_disks()+1) - (self.rod3.get_num_of_disks())) * 15
                    distx = 400
                    self._canvas.move(self.top1_draw, self.prex - e.x + distx, self.prey - e.y + disty)
                else:
                    self._canvas.move(self.top1_draw, self.prex - e.x, self.prey - e.y)
            ### disk move from rod2 to rod3
            if self.top2 != None and self.top2.move:
                if self.rod3.add_disk(self.top2) == True:
                    self.rod2.remove_disk(self.top2)
                    disty = ((self.rod2.get_num_of_disks()+1) - (self.rod3.get_num_of_disks())) * 15
                    distx = 200
                    self._canvas.move(self.top2_draw, self.prex - e.x + distx, self.prey - e.y + disty)
                else:
                    self._canvas.move(self.top2_draw, self.prex - e.x, self.prey - e.y) 
        else:   
            if self.top1 != None and self.top1.move:
                self._canvas.move(self.top1_draw, self.prex - e.x, self.prey - e.y) # if not right place, bounce back
            if self.top2 != None and self.top2.move:
                self._canvas.move(self.top2_draw, self.prex - e.x, self.prey - e.y)
            if self.top3 != None and self.top3.move:
                self._canvas.move(self.top3_draw, self.prex - e.x, self.prey - e.y)
        self.check_win()
                
    def check_win(self):
        """ check whether the player win the game """
        if self.rod1.get_num_of_disks() == 0 and self.rod2.get_num_of_disks() == 0:
            self._canvas.create_text(350,50, text = 'Well Done!', font=('Rockwell', 20, 'bold'), fill = 'red')
            self._canvas.create_text(350,70, text = 'Press new game to start a new game', font=('Rockwell', 15, 'bold'), fill = '#DB8036')
