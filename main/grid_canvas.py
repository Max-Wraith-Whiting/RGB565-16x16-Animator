"""
Class that contains all view data and methods relating to the grid_canvas widget.
"""
import tkinter as tk

class grid_canvas(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.isDisabled = False
        
        self.cell_buttons = []
        
    def create_frames(self):
        # Canvas.
        self.canvas = tk.Frame(self, width=550, height=500)
        self.canvas.grid(row=0, column=0, sticky='nsew')
        
        # Grid Frame.
        self.frame_grid = tk.Frame(self.canvas, highlightbackground='gray', width=500, height=500,
                                   highlightthickness=2, padx=0, pady=0)
        self.frame_grid.grid(row=0, column=0, sticky='nsew')
        
        # Below Canvas Frame.
        self.frame_b_canvas = tk.Frame(self.canvas, height=35, padx=0, pady=0)
        self.frame_b_canvas.grid(row=1, column=0, sticky='nsew')
           
    def create_buttons(self):
        # Clear Canvas button
        self.button_clear_canvas = tk.Button(self.frame_b_canvas, bg='gray', text='Clear canvas',
                                             command=self.parent.clear_current_frame)
        self.button_clear_canvas.grid(row=0, column=0)
        
        # Delete Frame button.
        self.button_delete = tk.Button(self.frame_b_canvas, bg='gray', text='-',
                                       command=self.parent.delete_current_frame)
        self.button_delete.grid(row=0, column=1)
        
        # New Frame button.
        self.button_new = tk.Button(self.frame_b_canvas, bg='gray', text='+', command=self.parent.insert_new_frame)
        self.button_new.grid(row=0, column=2)
        
        # Left button.
        self.button_left = tk.Button(self.frame_b_canvas, bg='gray', text='<',
                                     command=self.parent.shift_current_view_left)
        self.button_left.grid(row=0, column=3)
        
        # Right button.
        self.button_right = tk.Button(self.frame_b_canvas, bg='gray', text='>',
                                      command=self.parent.shift_current_view_right)
        self.button_right.grid(row=0, column=4)
        
    def get_current_frame(self):
        """Request the current frame from the controller, returns 16 x 16 numpy array."""
        return self.parent.get_current_frame()
        
    def create_grid(self):
        for i in range(16):
            cell_row = []
            for j in range(16):
                # Create cell.
                cell = tk.Button(self.frame_grid, bg='white', width=2, height=1)
                cell.configure(command= lambda b=cell, x=i, y=j: self.set_cell_colour(b, x, y))
                cell.grid(row=i, column=j, padx=0, pady=0)
                cell_row.append(cell)
            self.cell_buttons.append(cell_row)
    
    def create_label(self):
        self.frame_label = tk.Label(self.frame_b_canvas, 
                                    text= f'Frame {self.parent.get_current_view_frame() + 1} of {self.parent.get_frame_count()}')
        self.frame_label.grid(row=0, column=5)
    
    def update_label(self):
        self.frame_label.configure(text= f'Frame {self.parent.get_current_view_frame() + 1} of {self.parent.get_frame_count()}')
    
    def set_cell_colour(self, button, x, y):
        colour = self.parent.get_colour()
        button.configure(bg=colour)
        self.parent.save_value_to_current_frame(x, y, colour)    
        
    def generate(self):
        self.create_frames()
        self.create_grid()
        self.create_buttons()
        self.create_label()
        
    def disable_grid(self):
        self.isDisabled = not self.isDisabled
        if self.isDisabled:
            for row in self.cell_buttons:
                for button in row:
                    button.configure(relief=tk.constants.FLAT)
        else:
            for row in self.cell_buttons:
                for button in row:
                    button.configure(relief=tk.constants.RAISED)
                    
def main():
    root = tk.Tk()
    x = grid_canvas(root)
    x.generate()
    x.pack(side="top", fill="both", expand=True)
    root.mainloop()

if __name__ == '__main__':
    main() 