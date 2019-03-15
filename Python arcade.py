import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "NEGERS ETEN POEP OMDAT ZE DAT LEKKER VINDEN alpha0.001"


class Game(arcade.Window):
    """
   The game class
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        # If you have sprite lists, you should create them here,
        # and set them to None
  
    pos_x = 420
    pos_y = 100
    momentum_x = 0
    momentum_y = 0
    kogel_pos_x = 99
    kogel_pos_y = pos_y
    bool_kogel = False
    kogel_update_x = True

    def setup(self):
        # Create your sprites and sprite lists here
        rondje1 = None
        kogel1 = None

    def resetkogel(self):
        self.kogel_pos_y = self.pos_y
        self.bool_kogel = False
        self.kogel_update_x = True

    def rondje(self, x,y,radius,color):
        arcade.draw_circle_filled(x,y,radius,color)

    def on_draw(self):
        """
        Rendering function
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        rondje1 = self.rondje(self.pos_x,self.pos_y,30,arcade.color.WHITE)
        if self.bool_kogel == True:
            kogel1 = self.rondje(self.kogel_pos_x, self.kogel_pos_y, 10, arcade.color.RED)

        # Call draw() on all your sprite lists below

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        if self.momentum_y == 1:
            self.pos_y += 5
        if self.momentum_y == -1:
            self.pos_y += -5
        if self.momentum_x == 1:
            self.pos_x += -5
        if self.momentum_x == -1:
            self.pos_x += 5
       
       
        if self.pos_x > SCREEN_WIDTH:
            self.pos_x = 0
        if self.pos_x < -10:
            self.pos_x = 799
        if self.pos_y > SCREEN_HEIGHT:
            self.pos_y = 0
        if self.pos_y < -10:
            self.pos_y = 0

        if self.bool_kogel == True:
          self.kogel_pos_y += 10
        if self.kogel_pos_y > SCREEN_HEIGHT:
            self.resetkogel()
        if self.kogel_pos_x > SCREEN_WIDTH:
            self.resetkogel()
            
        
        

        
        

    def on_key_press(self, key, key_modifiers):
        if key == 119:
            self.momentum_y = 1
        if key == 115:
            self.momentum_y = -1
        if key == 97:
            self.momentum_x = 1
        if key == 100:
            self.momentum_x = -1
        if key == 32:
            self.bool_kogel = True
            if self.kogel_update_x == True:
                self.kogel_pos_x = self.pos_x
                self.kogel_update_x = False

            

    def on_key_release(self, key, key_modifiers):
        if key == 119:
            self.momentum_y = 0
        if key == 115:
            self.momentum_y = 0
        if key == 97:
            self.momentum_x = 0
        if key == 100:
            self.momentum_x = 0
 


def main():
    """ Main method """
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()