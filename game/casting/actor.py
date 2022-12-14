
from game.shared.point import Point
from game.shared.color import Color

class Actor:
#The parent class that defines the methods that rock and gem classes will use

    def __init__(self, text):
        #Constructs a new Actor
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(20, 20)
        self._font_size = 15
        self._text = text

    def get_color(self):
        #gets the color in the form of 3 integers
        #returns the color
        return self._color

    def set_color(self, color):
        #updates the color
        self._color = color

    def get_position(self):
        #gets the starting position in x/y format
        #returns the position
        return self._position

    def get_position_y(self):
        #gets the starting position in x/y format
        #returns the position
        return self._position.get_y()
    def get_position_x(self):
        #gets the starting position in x/y format
        #returns the position
        return self._position.get_x()

    def get_velocity(self):
        #gets the speed and direction
        #returns speed and direction
        return self._velocity

    def move_next(self, max_x, max_y):
        #moves the actor to the next position
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)
        return self._position



    def set_position(self, position):
        #updates the postion to the current one
        self._position = position

    def set_velocity(self, velocity):
        #updates velocity
        self._velocity = velocity

    # For player icon. Need font size and text returns
    def get_font_size(self):
        """Gets the actor's font size.

        Returns:
            Point: The actor's font size.
        """
        return self._font_size

    def get_text(self):
        """Gets the actor's textual representation.

        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def set_font_size(self, font_size):
        """Updates the font size to the given one.

        Args:
            font_size (int): The given font size.
        """
        self._font_size = font_size

    def set_text(self, text):
        """Updates the text to the given value.

        Args:
            text (string): The given value.
        """
        self._text = text  


    
