import pyray
from game.shared.point import Point


class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self, cell_size = 1):
        """Constructs a new KeyboardService using the specified cell size.
        
        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._cell_size = cell_size

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        # move to left
        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        # move to right
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1

        '''
        https://electronstudio.github.io/raylib-python-cffi/pyray.html#pyray.GamepadButton.GAMEPAD_BUTTON_MIDDLE_RIGHT 
        # If player is using the number pad to play
        # move to left
        if pyray.is_key_down(pyray.GAMEPAD_BUTTON_LEFT_FACE_LEFT):
            dx = -1
        
        # move to right
        if pyray.is_key_down(pyray.GAMEPAD_BUTTON_RIGHT_FACE_RIGHT):
            dx = 1

        # move to left
        if pyray.is_key_down(pyray.KEY_KP_4):
            dx = -1
        
        # move to right
        if pyray.is_key_down(pyray.KEY_KP_6):
            dx = 1

        # move to left
        if pyray.is_key_down(pyray.MOUSE_BUTTON_LEFT):
            dx = -1
        
        # move to right
        if pyray.is_key_down(pyray.MOUSE_BUTTON_RIGHT):
            dx = 1
        '''

        direction = Point(dx, dy)
        # Multiply by cell size
        direction = direction.scale(self._cell_size)
        
        return direction