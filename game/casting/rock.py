from game.casting.artifact import Artifact

class Rock(Artifact): 
  
    def __init__(self):    
        super().__init__() 
        self._text = 'O' 
        self.move_next(10,5)
        self.value = -1