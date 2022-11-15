import os
import random

from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.artifact import Artifact
from game.casting.gem import Gem 
from game.casting.rock import Rock 

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

print ("TEST1")

FRAME_RATE = 30
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
DATA_PATH = os.path.dirname(os.path.abspath(__file__))
WHITE = Color(255, 255, 255)
default_artifacts = 40

print("Test2")

def main():
    print("Test 3")
    # create the cast
    cast = Cast()
    director = Director()

    # create the banner for Score
    # This is where Score should be set to banner with text of score
    banner = Actor("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the cursor
    x = int(MAX_X / 2)
    y = 575
    position = Point(x, y)

    cursor = Actor("#")
    # Need to have an icon for player/cursor
    cursor.set_text("#")
    cursor.set_font_size(FONT_SIZE)
    cursor.set_color(WHITE)
    cursor.set_position(position)
    cast.add_actor("cursor", cursor)

    # create the actors
    for i in range(default_artifacts):

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        if random.randint(0, 1) > 0: #Played around with values here for the gems and rocks to appear on screen
            actor = Gem()
        else:
            actor = Rock()
        actor_name = "artifacts"
        actor.set_color(color)

        actor.set_position(position)
        actor.set_velocity(Point(random.randint(0, 10), random.randint(0, 10)))
        cast.add_actor(actor_name, actor)


    x = random.randint(1, COLS - 1)
    y = (59)
    position = Point(x, y)
    position = position.scale(CELL_SIZE)

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = Color(r, g, b)   

    gem = Gem()
    #gem.set_color(color)
    #gem.set_position(position)
    cast.add_actor("gems", gem)
    
    rock = Rock()
    #rock.set_color(color)
    #rock.set_position(position)
    cast.add_actor("rocks", rock)

      #if current_actors < 40:
            #continue
        #else: 
            #break
    
    # start the game
   # keyboard_service = KeyboardService(CELL_SIZE)
  #  video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    
    director.start_game(cast)



if __name__ == "__main__":
    main()