from turtle import Screen
import arcade
import os

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Snake Game"

# Sprite paths
SNAKE_PATH = "assets/snakeSection.png"

# velocity contants
DIRECTION_NONE = 0
DIRECTION_LEFT = 1
DIRECTION_RIGHT = 2
DIRECTION_UP = 3
DIRECTION_DOWN = 4

SNAKE_VELOCITY = 10

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.PINK)


    def setup(self):
        # draw part of a snake
        self.snake = arcade.Sprite(SNAKE_PATH)
        self.snake.center_x = SCREEN_WIDTH / 2
        self.snake.center_y = SCREEN_HEIGHT / 2

        # keep the ship sprites in a sprite list which is faster later
        self.snake_list = arcade.SpriteList()
        self.snake_list.append(self.snake)

        self.direction = DIRECTION_NONE

    def on_draw(self):
        arcade.start_render()

        self.snake_list.draw()
        
        arcade.finish_render()

    def on_key_press(self, symbol, modifiers):
        if arcade.key.ESCAPE == symbol:
            arcade.close_window()

        if arcade.key.N == symbol:
            self.setup()
        if arcade.key.W == symbol:
            self.direction = DIRECTION_UP
        if arcade.key.A == symbol:
            self.direction = DIRECTION_LEFT
        if arcade.key.S == symbol:
            self.direction = DIRECTION_DOWN
        if arcade.key.D == symbol:
            self.direction = DIRECTION_RIGHT    
    def on_key_release(self, symbol, modifiers):
        pass

    def on_update(self, delta_time: float):
        #movement
        if self.direction == DIRECTION_UP:
            self.snake.center_y+=10
        if self.direction == DIRECTION_DOWN:
            self.snake.center_y-=10
        if self.direction == DIRECTION_LEFT:
            self.snake.center_x-=10
        if self.direction == DIRECTION_RIGHT: 
            self.snake.center_x+=10
        #collision
        if self.snake.center_y>SCREEN_HEIGHT or self.snake.center_y<0 or self.snake.center_x<0 or self.snake.center_x>SCREEN_WIDTH:
            self.setup()
         


        self.snake_list.update()
        
def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
