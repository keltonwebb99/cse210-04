# cse210-04
Here is the README.md to make the design for the project. Enter your name below when you are able to access: 
Kelton Webb: * email: *

 

Josiah Madondo: * email: jmadondo1722@gmail.com*

 

Teigen Barber: * email: barber.teigen@gmail.com *

 

Stacie Abbey: * email: srabbey@byui.edu *

 

Rules
Greed is played according to the following rules.

 

Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
The player (#) can move left or right along the bottom of the screen.
If the player touches a gem they earn a point.
If the player touches a rock they lose a point.
Gems and rocks are removed when the player touches them.
The game continues until the player closes the window.

 

Design
  Casting:
    -actor: (Teigen)
      A visible, moveable thing that participates in the game. 
              
              methods:
                -get_color:
                -get_font_size:
                -get_position:
                -get_velocity:
                -move_next:
                -set_color:
                -set_position:
                -set_velocity:
                  
    
       --gem: child of actor (Teigen)
          Gems and rocks are removed when the player touches them. 
      
       --rock: child of actor (Teigen)
          Gems and rocks are removed when the player touches them.
  
      -cast: Josiah
        A collection of actors.
        
              methods:
                -add_actor(self, group, actor):
                -get_actors(self, group):
                -get_all_actors(self):
                -get_first_actor(self, group):
                -remove_actor(self, group, actor):
        
       -score: Josiah
          If the player touches a gem they earn a point. If the player touches a rock they lose a point.
              
              methods:
                -score: pull from gem and rock
                        display to video_service 
      
  Directing: Kelton
    -director:  
        A person who directs the game. 
        The responsibility of a Director is to control the sequence of play.
            Attributes:
            _keyboard_service (KeyboardService): For getting directional input.
            _video_service (VideoService): For providing video output.
            
            methods:
            start_game(self, cast)
            _get_inputs(self, cast)
            _do_updates(self, cast)
            _do_outputs(self, cast)
            
  
  Services: Stacie
    -keyboard-service:  Stacie
         Detects player input. 
          The responsibility of a KeyboardService is to detect player key presses and translate them into 
          a point representing a direction.
          Attributes:
            cell_size (int): For scaling directional input to a grid.
            -video-service:
            
            methods:
            get_direction(self)
            
    -video_service:  Stacie
          
          methods:
          -close_window(self):
          -clear_buffer(self):
          -draw_actor(self, actor):
          -draw_actors(self, actors):
          -flush_buffer(self):
          -get_cell_size(self):
          -get_height(self):
          -get_width(self):
          -is_window_open(self):
          -open_window(self):
          -_draw_grid(self):
         
  
  Shared:
    -color:
        A color.
        
        methods:
          -to_tuple(self):
          
    -point:
        A distance from a relative origin (0, 0).
        
        methods:
          -add(self, other):
          -equals(self, other):
          -get_x(self):
          -get_y(self):
          -scale(self, factor):
