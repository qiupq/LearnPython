from Tkinter import *
import random
colors = ['red', 'green', 'blue', 'orange', 'yellow']
lblfont = 5

class Callback:
    def __init__(self, widget):
        self.widget = widget
    def __call__(self):
        global lblfont
        color = self.widget.get()
        lbl.config(font=('courier', lblfont), bg=color)
        lblfont += 5

def dialog():
    popup = Toplevel()
    color = random.choice(colors)
    Label(popup, text='Popup', bg=color, font=('times', 25)).pack()
    
win = Tk()
win.title('GUI1')
lbl = Label(win, text='Spam', fg='white', bg='blue')
lbl.pack(side=TOP, expand=YES, fill=X)
ent = Entry(win)
ent.pack()

btn = Button(win, text='Press', command=Callback(ent))
btn.pack(side=BOTTOM, expand=YES, fill=BOTH)
btn.config(font=('courier', 25, 'italic bold'))

Button(text='Popup', command=dialog).pack(side=BOTTOM, fill=X)
mainloop()

