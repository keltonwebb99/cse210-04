import random
import os

from game.casting.actor import Actor
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
DATA_PATH = os.path.dirname(os.path.abspath(__file__))
WHITE = Color(255, 255, 255)
default_actors = 40

def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner for Score
    # This is where Score should be set to banner with text of score
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the cursor
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    cursor = Actor()
    # Need to have an icon for player/cursor
    cursor.set_text("#")
    cursor.set_font_size(FONT_SIZE)
    cursor.set_color(WHITE)
    cursor.set_position(position)
    cast.add_actor("cursor", cursor)
    
    # create the actors
    for i in range(default_actors):

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

    #this needs to be somewhere where it is getting run as the program updates constantly
    if default_actors < 40:
        x = random.randint(1, COLS - 1)
        y = (59)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)   
        
#I don't think we need this part because we don't have an artifact class
#but just in case we may need it, I don't want to delete it yet

        #artifact = Artifact()
        #artifact.set_color(color)
        #artifact.set_position(position)
        #cast.add_actor("artifacts", artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()