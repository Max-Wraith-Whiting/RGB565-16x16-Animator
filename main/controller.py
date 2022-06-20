"""
Class that contains all GUI widgets and acts as the controller
interfacing the model and the widget views.
"""
import tkinter as tk
from helpers import rgb_to_hex888, rgb_to_hex565
import model
from grid_canvas import grid_canvas
from rgb_scales import rgb_scales
from toolbar import toolbar
from menu import menu

class controller(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.winfo_toplevel().title("RGB-565 Animator")
        self.parent.resizable(width=0, height=0)
        
        self.model = model.rgb_animator_model(self)
        
        self.grid_canvas = grid_canvas(self)
        self.rgb_scales = rgb_scales(self)
        self.toolbar = toolbar(self)
        self.menu = menu(self)
        
        self.grid_canvas.generate()
        self.rgb_scales.generate()
        self.toolbar.generate()
        self.menu.generate()
        
        self.grid_canvas.grid(row=0, column=0, columnspan=5, rowspan=5, sticky='nesw')
        self.rgb_scales.grid(row=0, column=6, sticky='nesw')
        self.toolbar.grid(row=1, column=6)
        
    def get_colour(self):
        return self.model.get_colour()
    
    def set_colour(self, colour):
        self.model.set_colour(colour)
    
    def save_value_to_current_frame(self, x, y, hex):
        self.model.save_value_to_current_frame(x, y, hex)
        
    def clear_current_frame(self):
        print("[CONTROLLER]: Clearing current frame.")
        self.model.clear_current_frame()
        
        to_set = self.grid_canvas.cell_buttons
        for row in to_set:
            for button in row:
                button.configure(bg='#ffffff')
    
    def insert_new_frame(self):
        self.model.insert_new_frame()
        self.grid_canvas.update_label()
        
    def set_current_frame_data(self, data):
        to_set = self.grid_canvas.cell_buttons
        for x, row in enumerate(to_set):
            for y, button in enumerate(row):
                button.configure(bg=data[x][y])
                
    def delete_current_frame(self):
        self.model.delete_current_frame()
        self.grid_canvas.update_label()
     
    def shift_current_view_right(self):
        self.model.shift_current_view_right()
        self.grid_canvas.update_label()
    
    def shift_current_view_left(self):
        self.model.shift_current_view_left()
        self.grid_canvas.update_label()
    
    def get_frame_count(self):
        return self.model.get_frame_count()
    
    def get_current_view_frame(self):
        return self.model.get_current_view_frame()
    
    def toggle_eraser(self):
        self.model.toggle_eraser()
        if self.model.isErase:
            self.toolbar.button_eraser.configure(bg='gray', relief=tk.constants.SUNKEN)
        else:
            self.toolbar.button_eraser.configure(bg='gray', relief=tk.constants.RAISED)

    def update_colour_viewer(self, colour):
        self.rgb_scales.update_colour_viewer(colour)
     
    def save_frame_stack(self):
        self.model.save_frame_stack()
        
    def disable_grid(self):
        self.grid_canvas.disable_grid()
        
def main():
    root = tk.Tk()
    x = controller(root)
    x.pack(side="top", fill="both", expand=True)
    root.mainloop()

if __name__ == '__main__':
    main() 