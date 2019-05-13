# Simple image display GUI
#
# Requires the Pillow (PIL) module 
#   available at http://pillow.readthedocs.org/en/latest/installation.html


from tkinter import *
#import ImageTk
from PIL import Image, ImageTk


class StatusBar(Frame):
    """The status bar."""

    def __init__(self, master, label_var):
        super().__init__(master)
        self.label = Label(self, bd=2, relief=SUNKEN, textvariable=label_var)
        self.label.pack(side=RIGHT)
        
class ImageDisplayCanvas(Frame):
    """A canvas widget with scroll bars to hold image."""

    def __init__(self, master, img, status_string):
        super().__init__(master, bd = 2, relief=SUNKEN)
        self.im = img
        self.data = img.getdata()
        self.status_string = status_string
        self.imwidth, self.imheight = self.im.size
        # frame for canvas and vertical scrollbar
        canvas_frame = Frame(self)
        canvas_frame.pack(fill=BOTH, expand=1)
        xscrollbar = Scrollbar(self, orient=HORIZONTAL)
        xscrollbar.pack(fill=X)
        yscrollbar = Scrollbar(canvas_frame)
        self.canvas = Canvas(canvas_frame, bd=0,
                             scrollregion=(0, 0, self.imwidth, self.imheight),
                             xscrollcommand=xscrollbar.set,
                             yscrollcommand=yscrollbar.set)
        self.canvas.pack(side=LEFT, expand=1,fill=BOTH)
        yscrollbar.pack(side=LEFT,fill=Y)
        xscrollbar.config(command=self.canvas.xview)
        yscrollbar.config(command=self.canvas.yview)    
        self.pi = ImageTk.PhotoImage(self.im)
        self.canvas.create_image(0, 0, image = self.pi, anchor = 'nw')
        self.canvas.bind("<Button-1>", self.mousePosAndColour)
        self.canvas.bind("<B1-Motion>", self.motion)
        # Change geometry of toplevel
        geom = "{0}x{1}".format(min(800, self.imwidth+25), 
                                min(600, self.imheight+50))
        self.canvas.winfo_toplevel().geometry(geom)


    def mousePosAndColour(self, event):
        """Callback for Button-1 event."""
        
        self.oldx = event.x
        self.oldy = event.y
        self.oldcx = self.canvas.canvasx(0)
        self.oldcy = self.canvas.canvasy(0)
        x = int(self.canvas.canvasx(event.x))
        y = int(self.canvas.canvasy(event.y))
        red, green,blue = self.data[x + y*self.imwidth]
        self.status_string.set("({0} {1} {2})  ({3}, {4})".format(red,green,blue,x,y))       

    def motion(self, event):
        """Callback for Button-1 motion event."""
        
        dx = event.x - self.oldx
        dy = event.y - self.oldy
        self.canvas.xview('moveto', (self.oldcx - dx)/self.imwidth)
        self.canvas.yview('moveto', (self.oldcy - dy)/self.imheight)
        

class ImageApp():
    """The image display application."""
    
    def __init__(self, img, master=None):
        master.title("Images")
        self.status_string = StringVar()
        self.status_string.set('OK')
        self.img_canvas = ImageDisplayCanvas(master, img, self.status_string)
        self.img_canvas.pack(fill=BOTH,expand=1)
        self.status = StatusBar(master, self.status_string)
        self.status.pack(fill=X)
        master.protocol("WM_DELETE_WINDOW", self.close)
        self._master = master
    def close(self):
        """Exit the application."""
        self._master.destroy()

def display_image(img):
    """Create a window and display the supplied image."""

    root = Tk()
    app = ImageApp(img, root)
    root.mainloop()

    
