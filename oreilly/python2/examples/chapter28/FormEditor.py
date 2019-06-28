from Tkinter import *
import os, pickle

class FormEditor:

    def __init__(self, name, dataclass, storagedir):
        self.storagedir = storagedir      # stash away some references
        self.dataclass = dataclass
        self.row = 0
        self.current = None

        self.root = root = Tk()           # create window and size it
        root.minsize(300,200)

        root.rowconfigure(0, weight=1)    # define how columns and rows scale
        root.columnconfigure(0, weight=1) # when the window is resized
        root.columnconfigure(1, weight=2)
        
        # create the title Label
        Label(root, text=name, font='bold').grid(columnspan=2)
        self.row = self.row + 1 
        # create the main listbox and configure it
        self.listbox = Listbox(root, selectmode=SINGLE)
        self.listbox.grid(columnspan=2, sticky=E+W+N+S)
        self.listbox.bind('<ButtonRelease-1>', self.select)
        self.row = self.row + 1

        # call self.add_variable once per variable in the class's fieldnames var
        for fieldname in dataclass.fieldnames:
            setattr(self, fieldname, self.add_variable(root, fieldname))

        # create a couple of buttons, with assigned commands
        self.add_button(self.root, self.row, 0, 'Delete Entry', self. delentry)
        self.add_button(self.root, self.row, 1, 'Reload', self.load_data)

        self.load_data()

    def add_variable(self, root, varname):
        Label(root, text=varname).grid(row=self.row, column=0, sticky=E)
        value = Label(root, text='', background='gray90',
                      relief=SUNKEN, anchor=W, justify=LEFT)
        value.grid(row=self.row, column=1, sticky=E+W)
        self.row = self.row + 1
        return value

    def add_button(self, root, row, column, text, command):
        button = Button(root, text=text, command=command)
        button.grid(row=row, column=column, sticky=E+W, padx=5, pady=5)

    def load_data(self):
        self.listbox.delete(0,END)
        self.items = []
        for filename in os.listdir(self.storagedir):
            item = pickle.load(open(os.path.join(self.storagedir, filename)))
            item._filename = filename
            self.items.append(item)
            self.listbox.insert('end', repr(item))
        self.listbox.select_set(0)
        self.select(None)

    def select(self, event):
        selection = self.listbox.curselection()
        self.selection = self.items[int(selection[0])]
        for fieldname in self.dataclass.fieldnames:
            label = getattr(self, fieldname)               # GUI field
            labelstr = getattr(self.selection, fieldname)  # instance attribute
            labelstr = string.replace(labelstr,'\r', '')
            label.config(text=labelstr)

    def delentry(self):
        os.remove(os.path.join(self.storagedir,self.selection._filename))
        self.load_data()
