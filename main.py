import arcade
import os

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Snake Game"

# Sprite paths
SNAKE_PATH = "assets/snakeSection.png"

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WHITE)


    def setup(self):
        # draw part of a snake
        self.snake = arcade.Sprite(SNAKE_PATH)
        self.snake.center_x = SCREEN_WIDTH / 2
        self.snake.center_y = SCREEN_HEIGHT / 2

        # keep the ship sprites in a sprite list which is faster later
        self.snake_list = arcade.SpriteList()
        self.snake_list.append(self.snake)


    def on_draw(self):
        arcade.start_render()

        self.snake_list.draw()
        arcade.finish_render()

    def on_key_press(self, symbol, modifiers):
        if arcade.key.ESCAPE == symbol:
            arcade.close_window()

        if arcade.key.N == symbol:
            self.setup()

    def on_key_release(self, symbol, modifiers):
        pass

    def on_update(self, delta_time: float):
        self.snake_list.update()
    
def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
