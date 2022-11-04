class Director:
    #A person who directs the game and control sequence of play
    """_keyboard_service (KeyboardService)
       _video_service (VideoService) are attributes"""

    def __init__(self, keyboard_service, video_service):
        self._keyboard_service = keyboard_service
        self._video_service = video_service

    def start_game(self, cast):
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        #gets keyboard input and applies it to player icon
        player = cast.get_first_actor()
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)


    def _do_updates(self, cast):
        #update player position and update points when colliding with rocks or gems
        player = cast.get_first_actor("players")
        gem = cast.get_actors("gems")
        rock = cast.get_actors("rocks")

        max_x = self._video_service.get_width()
        player.move_next(max_x)

        if player.get_position().equals(gem.get_position()):
            #add code that adds a point
            pass
        elif player.get_position().equals(rock.get_position()):
            #add code that subtracts a point
            pass
            


    def _do_outputs(self, cast):
        #draws actors on screen
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()



