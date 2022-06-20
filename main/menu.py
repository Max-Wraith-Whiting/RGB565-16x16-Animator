"""A class for generating all the menu elements for the GUI.
"""

import tkinter as tk

class menu():
    def __init__(self, parent):
        self.parent = parent
        
        self.menu = tk.Menu(self.parent)
        self.parent.parent.config(menu= self.menu)
        
        
    def create_file_menu(self):
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='Save', command=self.parent.save_frame_stack)
        self.file_menu.add_command(label='Quit', command=self.parent.parent.quit)
    
    def create_options_menu(self):
        self.options_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label='Options', menu=self.options_menu)
        self.options_menu.add_command(label='Grid', command=self.parent.disable_grid)
    
    def generate(self):
        self.create_file_menu()
        self.create_options_menu()