"""
Class that contains all view data and methods relating to the rgb_scales widget.
Contains a main method to test the widget.
"""
import math
import tkinter as tk
from helpers import rgb_to_hex888

class rgb_scales(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
    def create_frames(self):
        # Colour viewer.
        self.colour_viewer = tk.Frame(self, bg='#5f5f5f',
                                      width=200, height=150, padx=20, pady=20)
        self.colour_viewer.grid(row=0, column=0, sticky='nsew')
        
        # RGB scales.
        self.frame_scales = tk.Frame(self, width=200, height=200, padx=20, pady=20)
        self.frame_scales.grid(row=1, column=0, sticky='nsew')
        
    def create_rgb_scales(self):
        
        def scaleMove(*args):
            # Scale function
            r = int(self.scale_R.get())
            g = int(self.scale_G.get())
            b = int(self.scale_B.get())
            
            hex888 = rgb_to_hex888(r, g, b)
            self.colour_viewer.configure(bg="#" + hex888)
            self.parent.set_colour("#" + hex888)
        
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
        
    def update_colour_viewer(self, ask_colour):
        rgb, hex = ask_colour
        self.colour_viewer.configure(bg=hex)
        r, g, b = math.floor(rgb[0]), math.floor(rgb[1]), math.floor(rgb[2])
        self.scale_R.set(r)
        self.scale_G.set(g)
        self.scale_B.set(b)
    
    def generate(self):
        self.create_frames()
        self.create_rgb_scales()
        
def main():
    root = tk.Tk()
    x = rgb_scales(root)
    x.generate()
    x.pack(side="top", fill="both", expand=True)
    root.mainloop()

if __name__ == '__main__':
    main() 
        