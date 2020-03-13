import numpy as np

class RubiksCube:
    """Play Rubik's cube.
    
    Parameters
    ----------
    size : int
        size of the cube, 3 (meaning 3x3x3) by default
    """
    
    ACTIONS = dict(LEFT=0, RIGHT=1, TOP=2, FRONT=3)
    
    def __init__(self, size=3):
        self.size = size
        self.cube = self._init_cube(size)
        
    @staticmethod
    def _init_cube(size, num_sides=9):
        """Initialize cube. """
        cube = np.zeros((num_sides,size,size))
        for i in range(num_sides):
            cube[i] = c * np.ones((size,size))
        return cube
        
    def __call__(self,action):
        assert action in self.ACTIONS.values()
        
        self._check_done()
    
        if self.done:
            return self
        
        self.move(action)
        return self
        
    @staticmethod
    def _move_left(cube,size):
        cube = cube.copy()
        # Rotate left side
        cube[1] = np.rot90(cube[1],1)
        # Store upper left column
        upper = cube[0,:size,size]
        # Shift left columns
        cube[0,:size,size] = cube[2,:size,size]
        cube[2,:size,size] = cube[4,:size,size]
        cube[4,:size,size] = cube[5,:size,size]
        cube[5,:size,size] = upper
        return cube
        
    @staticmethod
    def _move_right(cube,size):
        cube = cube.copy()
        # Rotate right side
        cube[3] = np.rot90(cube[1],-1)
        # Store upper left column
        upper = cube[0,:size,2*size-1]
        # Shift right columns
        cube[0,:size,2*size-1] = cube[2,:size,2*size-1]
        cube[2,:size,2*size-1] = cube[4,:size,2*size-1]
        cube[4,:size,2*size-1] = cube[5,:size,2*size-1]
        cube[5,:size,2*size-1] = upper
        return cube
    
    def move(self,action):
        if action == 0:
            # Move left
            self.cube = self._move_left(self.cube,self.size)
            
        elif action == 1:
            # Move right
            self.cube = self._move_right(self.cube,self.size)
            
        elif action == 2:
            # Move top (rotate cube such that top is to the left)
            cube = self.cube.copy()
            # Rotate 5 upper sides anti-clockwise
            upper5 = cube[:3*self.size,:3*self.size]
            cube[:3*self.size,:3*self.size] = np.rot90(upper5, 1)
            # Rotate lower side clockwise
            lower = cube[3*self.size:,3*self.size:6*self.size]
            cube[3*self.size:,3*self.size:6*self.size] = np.rot90(lower, -1)
            # Move left
            cube = self._move_left(cube,self.size)
            # Rotate 5 upper sides clockwise
            upper5 = cube[:3*self.size,:3*self.size]
            cube[:3*self.size,:3*self.size] = np.rot90(upper5, -1)
            # Rotate lower side anti-clockwise
            lower = cube[3*self.size:,3*self.size:6*self.size]
            cube[3*self.size:,3*self.size:6*self.size] = np.rot90(lower, 1)
            self.cube = cube
            
        elif action == 3:
            # Move front (shift front to the left)
            cube = self.cube.copy()
            # Store right and lower
            right = cube[1*self.size:2*self.size,2*self.size:]
            lower = cube[3*self.size:,3*self.size:6*self.size]
            # Shift to the left
            middleright = cube[1*self.size:2*self.size,1*self.size:]
            cube[1*self.size:2*self.size,:2*self.size] = middleright
            # Swift right and lower
            cube[1*self.size:2*self.size,2*self.size:] = lower
            cube[3*self.size:,3*self.size:6*self.size] = right
            # Rotate sides
            
            
if __name__ == "__main__":
    rubiks_cube = RubiksCube(3)
    rubiks_cube.move("left")
    

