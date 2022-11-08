from game.casting.actor import Actor

class Score(Actor):
    """   
    The responsibility of the Score is to provide the score of the game.

    Attributes:
        _score (integer): A score of the game.
    """
    def __init__(self):
        super().__init__()
        self._score = 0
        
    def get_score(self):
        """Gets the game's score.
        
        Returns:
            score (integer): The score.
        """
        return self._score
        
    def print_score(self):
        """Prints the score of the game.

        Return:
            self._text: The text that shows the text.
        """
        self._text = print(f'Score: {self.get_score()}')