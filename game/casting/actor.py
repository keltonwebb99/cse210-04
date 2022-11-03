from game.shared.point import Point
from game.shared.color import Color

"""    -actor: (Teigen)
      A visible, moveable thing that participates in the game. 
              
              methods:
                -get_color:
                -get_position:
                -get_velocity:
                -move_next:
                -set_color:
                -set_position:
                -set_velocity:        
    
       --gem: child of actor (Teigen)
         will call on Actor's methods through inheritance  
      
       --rock: child of actor (Teigen)
         will call on Actor's methods through inheritance"""

class Actor:
    def __init__(self):
        #Constructs a new Actor
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 10)

    def get_color(self):
        #gets the color in the form of 3 integers
        #returns the color
        return self._color
    
    def set_color(self):
        #updates the color
        self._color = Color
    
    def get_position(self):
        #gets the starting position in x/y format
        #returns the position
        return self._position

    def get_velocity(self):
        #gets the speed and direction
        #returns speed and direction
        return self._velocity
    
    def move_next(self, max_x, max_y):
        #moves the actor to the next position
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)

    def set_position(self, position):
        #updates the postion to the current one
        self._position = position

    def set_velocity(self, velocity):
        #updates velocity
        self._velocity = velocity

class Gem(Actor):
    
    def __init__(self):
        super().__init__()
        super().get_color
        super().set_color
        super().get_position
        super().get_velocity
        super().move_next
        super().set_position
        super().set_velocity

class Rock(Actor):

    def __init__(self):
        super().__init__()
        super().get_color
        super().set_color
        super().get_position
        super().get_velocity
        super().move_next
        super().set_position
        super().set_velocity
