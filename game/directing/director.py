from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.casting.cast import Cast
from game.shared.point import Point

import random

class Director:
    #A person who directs the game and control sequence of play
    """_keyboard_service (KeyboardService)
       _video_service (VideoService) are attributes"""
    cast = Cast()

    def __init__(self):
        #self._keyboard_service = KeyboardService
        #self._video_service = VideoService
        self._keyboard_service = KeyboardService(15)
        self._video_service = VideoService("Greed", 900, 600, 15, 15)
        self._score = 0
        

    def start_game(self, cast):
        print("TEST5")
        self._video_service.open_window()
        while self._video_service.is_window_open():
            #print("TEST6")
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        #gets keyboard input and applies it to player icon
        player = cast.get_first_actor("cursor")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)


    def _do_updates(self, cast):
        #update player position and update points when colliding with rocks or gems
        banner = cast.get_first_actor("banners")
        player = cast.get_first_actor("cursor")
        artifacts = cast.get_actor("artifacts")
>>>>>>> e5f2f7211a764e6037b14659315f6eb5c8158885

        banner.set_text(f"Score {self._score}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        
        # Update position of robot; in actor
        player.move_next(max_x, max_y)

        for artifact in artifacts: 
            x_compare = abs(player.get_position_x() - artifact.get_position_x())
            y_compare = abs(player.get_position_y() - artifact.get_position_y())
            if x_compare <= 5 and y_compare <=1:
                if artifact.get_text() == "*":
                    self._score += 1
                else:
                    self._score -= 1
                self.to_the_top(artifact)
                banner.set_text(f"Score: {self._score}")
            elif artifact.get_position_y() == 615:
                self.to_the_top(artifact)
            artifact.artifact_fall()

        
                
    def to_the_top(self, artifact):
        x = random.randint(1, 59)
        position = Point(x, 0)
        position = position.scale(15)
        artifact.set_position(position)

    def _do_outputs(self, cast):
        #draws actors on screen
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()




