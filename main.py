from turtle import Screen
import arcade
import os
import random
import math

from numpy import append 



# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Snake Game"

# Sprite paths
SNAKE_HEAD_PATH = "assets/snakeHead.png"
SNAKE_PATH = "assets/snakeSection.png"
FOOD_PATH = "assets/food.png"
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
        arcade.set_background_color(arcade.color.BABY_BLUE_EYES)


    def setup(self):
        # draw part of a snake
        self.snake_head = arcade.Sprite(SNAKE_HEAD_PATH)
        self.snake_head.center_x = SCREEN_WIDTH / 2
        self.snake_head.center_y = SCREEN_HEIGHT / 2
        self.score = 0


        self.food = arcade.Sprite(FOOD_PATH)
        self.place_food()

        # keep the ship sprites in a sprite list which is faster later
        self.snake_head_list = arcade.SpriteList()
        self.snake_head_list.append(self.snake_head)

        self.food_list = arcade.SpriteList()
        self.food_list.append(self.food)

        #draw the tail
        self.tail_list = arcade.SpriteList()
        last_x = self.snake_head.center_x
        last_y = self.snake_head.center_y
        for i in range(2):
            element = arcade.Sprite(SNAKE_PATH)
            element.center_x = last_x - element.width 
            element.center_y = last_y
            self.tail_list.append(element)
            last_x = element.center_x

        self.direction = DIRECTION_NONE
        self.stop_game = False

    def on_draw(self):
        arcade.start_render()

        self.snake_head_list.draw()
        self.food_list.draw()
        self.tail_list.draw()

        arcade.draw_text("score = " + str(self.score), SCREEN_WIDTH - 100, SCREEN_HEIGHT - 20, arcade.color.BLACK, 15, font_name="Arial")
        
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
        if self.stop_game:
            return
        #movement
        if self.direction == DIRECTION_UP:
            self.snake_head.center_y+=10
        if self.direction == DIRECTION_DOWN:
            self.snake_head.center_y-=10
        if self.direction == DIRECTION_LEFT:
            self.snake_head.center_x-=10
        if self.direction == DIRECTION_RIGHT: 
            self.snake_head.center_x+=10

        if self.direction != DIRECTION_NONE:
            previous_x = self.snake_head.center_x
            previous_y = self.snake_head.center_y
            for i in range(len(self.tail_list)):
                x_dir = (previous_x - self.tail_list[i].center_x)
                y_dir = (previous_y - self.tail_list[i].center_y)
                dir_len = math.sqrt(x_dir*x_dir + y_dir*y_dir)
                if dir_len > 1:
                    x_dir = 10 * x_dir / dir_len 
                    y_dir = 10 * y_dir / dir_len 
                if dir_len > (self.snake_head.width + 1):
                    self.tail_list[i].center_x += x_dir
                    self.tail_list[i].center_y += y_dir
                previous_x = self.tail_list[i].center_x
                previous_y = self.tail_list[i].center_y

        #collision
        if self.snake_head.center_y>SCREEN_HEIGHT or self.snake_head.center_y<0 or self.snake_head.center_x<0 or self.snake_head.center_x>SCREEN_WIDTH:
            self.setup()

        food_dist_x = abs(self.snake_head.center_x - self.food.center_x)
        food_dist_y = abs(self.snake_head.center_y - self.food.center_y)
        if food_dist_y < self.food.height and food_dist_x < self.food.width:
            self.place_food()
            element = arcade.Sprite(SNAKE_PATH)
            last_tail_index = len(self.tail_list) - 1
            element.center_x = self.tail_list[last_tail_index].center_x
            element.center_y = self.tail_list[last_tail_index].center_y
            self.tail_list.append(element)
            self.score+=1

        # check for collision with the tail
        tail_collisions = arcade.check_for_collision_with_list(self.snake_head, self.tail_list)
        if len(tail_collisions) > 1:
            self.stop_game = True

        self.snake_head_list.update()

    def place_food(self):
        self.food.center_x = random.randint(self.food.width, SCREEN_WIDTH - self.food.width)  
        self.food.center_y = random.randint(self.food.height, SCREEN_HEIGHT - self.food.height)
        

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()
    


if __name__ == "__main__":
    main()
