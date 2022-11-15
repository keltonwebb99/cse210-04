from game.casting.artifact import Artifact

class Gem(Artifact): 
  
    def __init__(self):    
        super().__init__()
        self._text = '*' 
        self.move_next(10,10)
        self.set_position
        self.value = 1