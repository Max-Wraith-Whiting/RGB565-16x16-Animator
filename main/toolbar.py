"""
Class that contains all view data and methods relating to the toolbar widget.
Contains a main method to test the widget.
"""

import tkinter as tk
from helpers import rgb_to_hex888
from tkinter.colorchooser import askcolor

class toolbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
    def create_frames(self):
        # Toolbar Frame.
        self.frame_toolbar = tk.Frame(self, highlightbackground='gray',
                                      highlightthickness=2, width=200)
        self.frame_toolbar.grid(row=0, column=1, sticky='nsew')
        
    def create_buttons(self):
        # Eraser
        self.button_eraser = tk.Button(self.frame_toolbar, text='Eraser', width=20,
                                       command=self.parent.toggle_eraser)
        self.button_eraser.grid(row=2, column=0, sticky='we')
        
        # Colour picker
        self.button_colour_picker = tk.Button(self.frame_toolbar, bg='brown', text='Colour pick',
                                              command=self.colour_picker)
        self.button_colour_picker.grid(row=3, column=0, sticky='we')
    
    def colour_picker(self):
        colour = askcolor()
        self.parent.set_colour(colour[1])
        self.parent.update_colour_viewer(colour)
        
    def generate(self):
        self.create_frames()
        self.create_buttons()