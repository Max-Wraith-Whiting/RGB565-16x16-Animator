"""
Quick and dirty class for generating a tkinter UI for frame by frame animation to be exported
as raw csv RGB565 values.
"""
import math
import numpy as np
import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter.constants import *
from helpers import rgb_to_hex

class rgb_animator():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("750x500")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Main variables
        self.colour = '#5f5f5f'
        self.true_colour = '0xffff'
        self.holding_colour = ''
        self.holding_true_colour = ''
        
        self.isErase = False
        self.frame_stack = []
        self.frame_index = -1
        self.view_frame = 1
        
    def create_frames(self):
        # Main.
        self.main = tk.Frame(self.root, highlightbackground='red', highlightthickness=2, padx=20,
                             pady=20)
        self.main.grid_rowconfigure(0, weight=1)
        self.main.grid_columnconfigure(0, weight=1)
        self.main.grid(sticky='nsew')
        
        # Canvas.
        self.canvas = tk.Frame(self.main, highlightbackground='red', highlightthickness=2,
                               width=550, height=500)
        self.canvas.grid(row=0, column=0, sticky='nsew')
        
        # Grid Frame.
        self.frame_grid = tk.Frame(self.canvas, highlightbackground='blue', width=500, height=500,
                                   highlightthickness=2, padx=0, pady=0)
        self.frame_grid.grid(row=0, column=0, sticky='nsew')
        
        # Below Canvas Frame.
        self.frame_b_canvas = tk.Frame(self.canvas, highlightbackground='green',
                                       highlightthickness=2, height=15, padx=0, pady=0)
        self.frame_b_canvas.grid(row=1, column=0, sticky='nsew')
        
        # Toolbar Frame.
        self.frame_toolbar = tk.Frame(self.main, highlightbackground='purple',
                                      highlightthickness=2, width=200)
        self.frame_toolbar.grid(row=0, column=1, sticky='nsew')
        
        # Colour viewer.
        self.colour_viewer = tk.Frame(self.frame_toolbar, bg='#5f5f5f',
                                      highlightbackground='yellow', highlightthickness=2, 
                                      width=200, height=150, padx=20, pady=20)
        self.colour_viewer.grid(row=0, column=0, sticky='nsew')
        
        # RGB scales.
        self.frame_scales = tk.Frame(self.frame_toolbar, highlightbackground='orange', 
                                     highlightthickness=2, width=200, height=200, padx=20, pady=20)
        self.frame_scales.grid(row=1, column=0, sticky='nsew')
        
    def create_buttons(self):
        # -- Buttons below canvas.
        
        # Clear canvas button.
        def clear_canvas():
            for i in range(len(self.cell_values)):
                for j in range(len(self.cell_values[i])):
                    self.cell_values[i][j] = '0xffff'
            for i in self.cell_buttons:
                for j in i:
                    j.configure(bg='#ffffff')
                    
        self.button_clear_canvas = tk.Button(self.frame_b_canvas, bg='purple', text='Clear canvas',
                                             command=clear_canvas)
        self.button_clear_canvas.grid(row=0, column=0)
        
        
        # Delete Frame button.
        def delete_frame():
            if len(self.frame_stack) > 2:
                del self.frame_stack[self.frame_index]
                self.frame_index -=1
                self.update_labels()
                
            elif len(self.frame_stack) == 2:
                del self.frame_stack[self.frame_index]
                self.frame_index -=1
                self.update_labels()
                self.button_delete.configure(state=DISABLED, bg='gray')
            else: # <--- Shouldn't be necessary.
                self.button_delete.configure(state=DISABLED, bg='gray')
        
        self.button_delete = tk.Button(self.frame_b_canvas, bg='gray', text='Delete Frame',
                                             command=delete_frame, state=DISABLED)
        self.button_delete.grid(row=0, column=1)
        
        
        # New Frame button.
        def new_frame():
            self.frame_stack.append(np.array(self.cell_values))
            self.frame_index += 1
            self.update_labels()
            if len(self.frame_stack) >= 2:
                 self.button_delete.configure(state=NORMAL)
            print(len(self.frame_stack))
            clear_canvas()
        
        new_frame() # Initialise the first frame.
        
        self.button_new = tk.Button(self.frame_b_canvas, bg='gray', text='New Frame',
                                             command=new_frame)
        self.button_new.grid(row=0, column=2)
        
        # Check frame availability.
        def check_frame_access():
            #if self.view_frame != 1 and 
            pass
        
        # Left button
        def left_view_frame():
            if self.view_frame != 1:
                self.view_frame -= 1
            else:
                self.button_left.configure(state=DISABLED)
            
        self.button_left = tk.Button(self.frame_b_canvas, bg='gray', text='<', state=DISABLED)
        self.button_left.grid(row=0, column=3)
        
        
        # Right button
        def right_view_frame():
            if self.view_frame != len(self.frame_stack):
                self.view_frame += 1
            else:
                self.button_right.configure(state=DISABLED)
                
        self.button_right = tk.Button(self.frame_b_canvas, bg='gray', text='>', state=DISABLED)
        self.button_right.grid(row=0, column=4)
        
        
        # -- Toolbar buttons.
        
        # Eraser button.
        def eraser():
            self.isErase = not self.isErase
            
            if self.isErase:
                # Store current colours and set to white.
                self.holding_colour = self.colour
                self.colour = '#ffffff'
                self.holding_true_colour = self.true_colour
                self.true_colour = '0xffff'
                self.button_eraser.configure(bg='gray', relief=SUNKEN)
            else:
                # Retrieve held colours.
                self.colour = self.holding_colour
                self.true_colour = self.holding_true_colour
                self.button_eraser.configure(bg='white', relief=RAISED)
        
        self.button_eraser = tk.Button(self.frame_toolbar, bg='pink',text='Eraser', command=eraser)
        self.button_eraser.grid(row=2, column=0, sticky='we')
        
        # Colour picker button.
        
        def colour_pick():
            rgb, hex = askcolor() # New colour selection.
            self.colour = hex
            
            r, g, b = math.floor(rgb[0]), math.floor(rgb[1]), math.floor(rgb[2])
    
            self.true_colour = rgb_to_hex(r, g, b)[0] # Get the RGB565 hex.
            self.colour_viewer.configure(bg=hex)
            
            # Set the RGB scales to selected value.
            self.scale_R.set(r)
            self.scale_G.set(g)
            self.scale_B.set(b)
        
        self.button_colour_picker = tk.Button(self.frame_toolbar, bg='brown', text='Colour pick',
                                              command=colour_pick)
        self.button_colour_picker.grid(row=3, column=0, sticky='we')
        
    def create_grid(self):
        
        def set_cell_colour(button, pos):
            button.configure(bg=self.colour)
            self.cell_values[pos[0]][pos[1]] = self.true_colour
        
        self.cell_values = []
        self.cell_buttons = []
        for i in range(16):
            cell_value_row = []
            cell_row = []
            for j in range(16):
                # Create cell.
                cell = tk.Button(self.frame_grid, bg='white', width=2, height=1)
                cell.configure(command= lambda b=cell, pos=(i,j): set_cell_colour(b, pos))
                cell.grid(row=i, column=j, padx=0, pady=0)
                cell_value_row.append(self.true_colour)
                cell_row.append(cell)
            
            self.cell_buttons.append(cell_row)
            self.cell_values.append(cell_value_row)   
        
    def create_rgb_scales(self):
        
        def scaleMove(*args):
            # Scale function
            r = int(self.scale_R.get())
            g = int(self.scale_G.get())
            b = int(self.scale_B.get())
            
            hex565, hex888 = rgb_to_hex(r, g, b)
            self.colour_viewer.configure(bg="#" + hex888)
            self.colour = "#" + hex888
        
        # Red Label
        label_R = tk.Label(self.frame_scales, text='R', fg='red')
        label_R.grid(row=0, column=0)
        
        # Red Scale
        self.scale_R = tk.Scale(self.frame_scales, from_=0, to=255, length=210, fg='red',
                                orient=tk.HORIZONTAL, command=scaleMove)
        self.scale_R.set(95)
        self.scale_R.grid(row=0, column=1)
        
        # Green Label
        label_G = tk.Label(self.frame_scales, text='G', fg='green')
        label_G.grid(row=1, column=0)
        
        # Green Scale
        self.scale_G = tk.Scale(self.frame_scales, from_=0, to=255, length=210, fg='green',
                                orient=tk.HORIZONTAL, command=scaleMove)
        self.scale_G.set(95)
        self.scale_G.grid(row=1, column=1)
        
        # Blue Label
        label_B = tk.Label(self.frame_scales, text='B', fg='blue')
        label_B.grid(row=2, column=0)
        
        # Blue Scale
        self.scale_B = tk.Scale(self.frame_scales, from_=0, to=255, length=210, fg='blue',
                                orient=tk.HORIZONTAL, command=scaleMove)
        self.scale_B.set(95)
        self.scale_B.grid(row=2, column=1)
        
    def create_labels(self):
        # Frame counter.
        self.label_frame_counter = tk.Label(self.frame_b_canvas, text=f'Frame {self.view_frame} of {len(self.frame_stack)}')
        self.label_frame_counter.grid(row=0, column=5)
        
    def update_labels(self):
        self.label_frame_counter.configure(text=f'Frame {self.view_frame} of {len(self.frame_stack)}')
            
    def refresh_canvas(self):
        pass
    
    def main(self):
        self.create_frames()
        self.create_labels()
        self.create_grid()
        self.create_buttons()
        self.create_rgb_scales()
        self.root.mainloop()

x = rgb_animator()
x.main()