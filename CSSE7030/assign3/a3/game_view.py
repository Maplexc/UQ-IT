import tkinter as tk
from game_controller import *

class Game(tk.Frame):
    """ Game of tower of hanoi """
    def __init__(self, master):
        super().__init__(master)
        master.config(bg = 'azure')
        self._master = master
        self._master.geometry('750x450')
        self.var = tk.IntVar()
        self.var.set(3) # spinbox default value
        welcome = tk.Label(self._master, text = 'Welcome to tower of hanoi', fg = '#FF8D14', bg = 'azure',
                           font=('Rockwell', 20, 'bold'))
        welcome.pack(fill = tk.BOTH, expand = 1, pady = (0,70))
        welcome.after(3500, welcome.destroy)
        self.after(4400, self.rule)
        self.after(4400, self.get_canvas)
        self.after(4400, self.get_buttons_spinbox)
        
    def rule(self):
        """ get the rule of the game """
        rule_frame = tk.Frame(self._master, bg = 'azure')
        rule_frame.pack(fill = tk.X, padx = 20, pady = 20)
        rule1 = tk.Label(rule_frame, text = 'How to win the game?   Easy, just moving all the disks from the left to the right',
                         font=('Rockwell', 12, 'bold'), bg = 'azure', fg = '#DB8036')
        rule1.pack(anchor = tk.W)
        rule2 = tk.Label(rule_frame, text = 'Rules:   move only one disk every time & cannot place a larger disk onto a smaller disk',
                           font=('Rockwell', 11, 'bold'), bg = 'azure',fg = '#DB8036')
        rule2.pack(anchor = tk.W,padx = 5,pady = (2,0))

    def get_canvas(self):
        """ create a canvas """
        self._canvas = tk.Canvas(self._master, bg = 'azure', bd = 0, highlightthickness = 0)
        self._canvas.pack(padx = 30,fill = tk.BOTH, expand = 1)
        self.playgame = PlayGame(self._canvas, self.var)
        self.playgame.get_begin()
         
    def get_buttons_spinbox(self):
        """ create a spinbox """
        frame = tk.Frame(self._master, bg = 'azure')
        frame.pack(side = tk.BOTTOM, fill = tk.X, pady = 20, padx = 20)
        label = tk.Label(frame, text = 'Select the number of disks:', bg = 'azure', font=('Rockwell', 11), fg = '#DB8036')
        label.pack(side = tk.LEFT, anchor = tk.W, padx = 10)        
        self.spinbox = tk.Spinbox(frame, from_ = 1, to = 8, width = 2, textvariable = self.var, font=('Rockwell', 12),
                                  command = self.change_disks_num)
        self.spinbox.pack(side = tk.LEFT, padx = 10)
        button_quit = tk.Button(frame, text = 'Quit', font=('Rockwell', 10, 'bold'),fg = '#DB8036', bg = 'azure', command = self._master.destroy)
        button_quit.pack(side = tk.RIGHT, padx = 10)
        button_newgame = tk.Button(frame, text = 'New game',font=('Rockwell', 10, 'bold'), fg = '#DB8036', bg = 'azure', command = self.new_game)
        button_newgame.pack(side = tk.RIGHT, padx = 10)

    def new_game(self):
        """ start a new game """
        self._canvas.delete('all')
        self.playgame.get_begin()

    def change_disks_num(self):
        """ change the total number of disks """
        num = self.var.get()
        self.new_game()
        
