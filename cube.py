import numpy as np

class RubiksCube:
    """Play Rubik's cube.
    
    Parameters
    ----------
    size : int
        size of the cube, 3 (meaning 3x3x3) by default
    """
    
    def __init__(self, size=3):
        self.size = size
        self.cube = self._init_cube(size)
        
    @staticmethod
    def _init_cube(size):
        """Initialize cube. """
        cube = np.zeros((4 * size, 3 * size))
        coords = [[0,1], [1,0], [1,1], [1,2], [2,1], [3,1]]
        for c, coord in enumerate(coords):
            [i, j] = coord
            cube[i*size:(i+1)*size, j*size:(j+1)*size] = c * np.ones((size, size))
            
        cube[4,0] = 9
        return cube
        
    
    def move(self, action):
        if action == "left":
            upper = self.cube[-self.size:,self.size].copy()
            self.cube[self.size:,self.size] = self.cube[:-self.size,self.size]
            self.cube[:self.size,self.size] = upper
            edge = self.cube[self.size:2*self.size,0*self.size:1*self.size]
            self.cube[self.size:2*self.size,0*self.size:1*self.size] = np.rot90(edge)

if __name__ == "__main__":
    rubiks_cube = RubiksCube(3)
    rubiks_cube.move("left")
    

