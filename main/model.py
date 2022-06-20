import math
import numpy as np

class rgb_animator_model():
    def __init__(self, parent):
        # Main variables
        self.parent = parent
        self.colour = '#5f5f5f'
        self.holding_colour = ''
        
        self.isErase = False
        self.frame_stack = [np.array([['#ffffff'] * 16] * 16)]
        self._frame_count = 0
        self.current_view_frame = 0
    
    def get_frame_count(self):
        self._frame_count = len(self.frame_stack) # Safety to avoid index issues with instancing.
        return self._frame_count
    
    def set_frame_count(self, value):
        self._frame_count = value
    
    def get_current_view_frame(self):
        return self.current_view_frame
    
    def set_current_view_frame(self, index):
        if index < self.get_frame_count():
            self.current_view_frame = index
            
    def shift_current_view_left(self):
        """Decrease the current view frame index by one if possible."""
        if self.current_view_frame != 0:
            self.current_view_frame -= 1
            self.parent.set_current_frame_data(self.get_current_frame_data())
            return True
        else:
            return False
            
    def shift_current_view_right(self):
        """Increase the current view frame index by one if possible."""
        if self.current_view_frame + 1 < self.get_frame_count():
            self.current_view_frame += 1
            self.parent.set_current_frame_data(self.get_current_frame_data())
            return True
        else:
            return False
        
    def save_value_to_current_frame(self, x, y, hex):
        """Sets a hex value to a cell within the currently viewed frame.

        Args:
            x (int): X cooridinate in the cell.
            y (int): Y cooridinate in the cell.
            hex (string): RGB888 in the form '#ffffff'
        """
        self.frame_stack[self.current_view_frame][x][y] = hex
        
    def get_current_frame_data(self):
        """Returns 16 x 16 numpy array of the frame_stack hex data."""
        return self.frame_stack[self.current_view_frame]
    
    def clear_current_frame(self):
        print("[MODEL]: Clearing current frame.")
        self.frame_stack[self.current_view_frame] = np.array([['#ffffff'] * 16] * 16)
        return self.get_current_frame_data()
        
    def insert_new_frame(self):
        self.frame_stack.insert(self.current_view_frame + 1, np.array([['#ffffff'] * 16] * 16))
        self.shift_current_view_right()
        
    def delete_current_frame(self):
        if self.get_frame_count() > 1:
            print("[DELETE]: ",self.current_view_frame, self.frame_stack)
            del self.frame_stack[self.current_view_frame]
            
            if self.get_frame_count() == self.current_view_frame: # If mismatch by 1.
                self.shift_current_view_left()

        else:
            print("[MODEL]: Cannot delete only remaining frame.")
            self.clear_current_frame()
        
    def toggle_eraser(self):
        """# Eraser button.
        def eraser():
            self.isErase = not self.isErase
            
            if self.isErase:
                # Store current colours and set to white.
                self.holding_colour = self.colour
                self.colour = '#ffffff'
                
            else:
                # Retrieve held colours.
                self.colour = self.holding_colour
                self.button_eraser.configure(bg='white', relief=RAISED)
        """
        self.isErase = not self.isErase
        
        if self.isErase:
            # Store current colours and set to white.
            self.holding_colour = self.get_colour()
            self.set_colour('#ffffff')
        else:
            # Retrieve held colour.
            self.set_colour(self.holding_colour)

    def get_colour(self):
        return self.colour
    
    def set_colour(self, colour):
        self.colour = colour
        