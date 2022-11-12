from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        self._score = 0
        
    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message

    def update_score(self, text):
        """ Updates Score if they hit a rock or gem
        
        """
        if text == '*':
            self._score += 1
        if text == 'O':
            self._score -= 1

    def get_score(self):
        """ Returns the score

        """
        return self._score