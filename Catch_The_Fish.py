import random
import arcade

# --- Constants ---

SPRITE_SCALING_PENGUIN = .5
SPRITE_SCALING_FISH = .5
SPRITE_SCALING_WHALE = 1
FISH_COUNT = 500
WHALE_COUNT = 15
MOVEMENT_SPEED = 10
SPEED_INCREASE = 0.02

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
OFF_SCREEN_LEFT = -20000
OFF_SCREEN_RIGHT = -1


class Fish(arcade.Sprite):


    def reset_pos(self):

        # Reset the fish to a random spot to the left
        self.center_x = random.randrange(-200,
                                         -1)
        self.center_y = random.randrange(SCREEN_HEIGHT)


    def update(self):
        # see if a fish has crossed the screen and reset it
        if self.left > SCREEN_WIDTH:
            self.reset_pos()
        super().update()


class InstructionView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("The penguin is hungry", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 250,
                         arcade.color.BLACK, font_size= 30, anchor_x="center")
        arcade.draw_text("Help him catch some fish! ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 175,
                         arcade.color.BLACK, font_size= 30, anchor_x="center")

        arcade.draw_text("Watch out for blowfish", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Don't get eaten by the killer whales!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 25,
                         arcade.color.BLACK, font_size=30, anchor_x="center")
        arcade.draw_text("Click anywhere to continue to instructions", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,
                         arcade.color.BLUE, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instruction_view_2 = InstructionView2()
        self.window.show_view(instruction_view_2)

class InstructionView2(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text("How To Play", SCREEN_WIDTH / 2, 525,
                         arcade.color.PURPLE, font_size = 50, anchor_x="center")
        arcade.draw_text("Use the arrow keys to move the penguin", 10, 450,
                         arcade.color.BLACK, font_size= 24)

        arcade.draw_text("Click To Play the Game!", SCREEN_WIDTH / 2 + 100, 50,
                         arcade.color.BLUE, font_size=30, anchor_x="center")

        arcade.draw_text("Fish Point levels:", 100, 400,
                         arcade.color.BLACK, font_size=24)
        arcade.draw_text("Green = 1 point", 150, 350, arcade.color.DARK_GREEN, 20)

        arcade.draw_text("Orange = 2 points", 150, 300, arcade.color.DARK_ORANGE, 20)
        arcade.draw_text("Red = 3 points", 150, 250, arcade.color.DARK_RED, 20)
        arcade.draw_text("Blowfish = lose 1 life", 150, 200, arcade.color.DARK_TAN, 20)
        arcade.draw_text("Killer Whale = GAME OVER", 150, 150, arcade.color.BLACK, 20)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = MyWindow()
        game_view.setup()
        self.window.show_view(game_view)


class MyWindow(arcade.View):

    #Main Game Code
    def __init__(self):

        super().__init__()

        # Variables that will hold sprite lists
        self.all_sprites_list = None
        self.redFish_list = None
        self.orangeFish_list = None
        self.greenFish_list = None
        self.blowFish_list = None
        self.whale_list = None

        # Set up the player info
        self.penguin_sprite = None
        self.score = 0
        self.lives = 3

        # Set up sound
        self.lose_life_sound = arcade.load_sound("Sounds/LoseLife.wav")
        self.game_over_sound = arcade.load_sound("Sounds/GameOver.wav")

        # Hide mouse cursor
        self.window.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)

    def setup(self):

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.redFish_list = arcade.SpriteList()
        self.orangeFish_list = arcade.SpriteList()
        self.greenFish_list = arcade.SpriteList()
        self.blowFish_list = arcade.SpriteList()
        self.whale_list = arcade.SpriteList()

        # Score
        self.score = 0
        self.lives = 3

        # Set up the player
        # Character image from kenney.nl
        self.penguin_sprite = arcade.Sprite("Images/penguin.png", SPRITE_SCALING_PENGUIN)
        self.penguin_sprite.center_x = 750
        self.penguin_sprite.center_y = 50
        self.all_sprites_list.append(self.penguin_sprite)

        # Create the fish
        for i in range(FISH_COUNT):

            # Create the fish instance
            redFish = Fish("Images/redFish.png", SPRITE_SCALING_FISH)
            redFish.change_x = 2
            orangeFish = Fish("Images/orangeFish.png", SPRITE_SCALING_FISH)
            orangeFish.change_x = 2
            greenFish = Fish("Images/greenFish.png", SPRITE_SCALING_FISH)
            greenFish.change_x = 2
            blowFish = Fish("Images/blowFish.png", SPRITE_SCALING_FISH)
            blowFish.change_x = 2

            # Position the fish
            redFish.center_x = random.randrange(OFF_SCREEN_LEFT,OFF_SCREEN_RIGHT)
            redFish.center_y = random.randrange(SCREEN_HEIGHT)

            orangeFish.center_x = random.randrange(OFF_SCREEN_LEFT,OFF_SCREEN_RIGHT)
            orangeFish.center_y = random.randrange(SCREEN_HEIGHT)

            greenFish.center_x = random.randrange(OFF_SCREEN_LEFT,OFF_SCREEN_RIGHT)
            greenFish.center_y = random.randrange(SCREEN_HEIGHT)

            blowFish.center_x = random.randrange(OFF_SCREEN_LEFT,OFF_SCREEN_RIGHT)
            blowFish.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the fish to the lists
            self.all_sprites_list.append(redFish)
            self.redFish_list.append(redFish)

            self.all_sprites_list.append(orangeFish)
            self.orangeFish_list.append(orangeFish)

            self.all_sprites_list.append(greenFish)
            self.greenFish_list.append(greenFish)

            self.all_sprites_list.append(blowFish)
            self.blowFish_list.append(blowFish)

        # create the whales
        for i in range(WHALE_COUNT):
            whale = Fish("Images/whale.png", SPRITE_SCALING_WHALE)
            whale.change_x = 2

            whale.center_x = random.randrange(OFF_SCREEN_LEFT,OFF_SCREEN_RIGHT)
            whale.center_y = random.randrange(SCREEN_HEIGHT)

            self.all_sprites_list.append(whale)
            self.whale_list.append(whale)

    def on_draw(self):

        arcade.start_render()
        self.all_sprites_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 570, arcade.color.WHITE, 14)

        output = f"Lives: {self.lives}"
        arcade.draw_text(output, 700, 570, arcade.color.WHITE, 14)


    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.penguin_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.penguin_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.penguin_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.penguin_sprite.change_x = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.penguin_sprite.change_y = 0

        elif key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.penguin_sprite.change_x = 0

        elif key == arcade.key.ENTER:
            self.current_state = GAME_INSTRUCTIONS

        elif key == arcade.key.SPACE:
            self.current_state = GAME_RUNNING


        # code learned from https://realpython.com/lessons/staying-on-the-screen/
        # keeps the penguin on the screen
        if self.penguin_sprite.left < 0:
            self.penguin_sprite.left = 0
        elif self.penguin_sprite.right > SCREEN_WIDTH:
            self.penguin_sprite.right = SCREEN_WIDTH
        elif self.penguin_sprite.bottom < 0:
            self.penguin_sprite.bottom = 0
        elif self.penguin_sprite.top > SCREEN_HEIGHT:
            self.penguin_sprite.top = SCREEN_HEIGHT


    def update(self, delta_time):
    #Game Logic
        self.all_sprites_list.update()

        # Generate a list of all sprites that collided with the player.
        redFish_hit_list = arcade.check_for_collision_with_list(self.penguin_sprite,
                                                        self.redFish_list)
        orangeFish_hit_list = arcade.check_for_collision_with_list(self.penguin_sprite,
                                                                   self.orangeFish_list)
        greenFish_hit_list = arcade.check_for_collision_with_list(self.penguin_sprite,
                                                                  self.greenFish_list)
        blowFish_hit_list = arcade.check_for_collision_with_list(self.penguin_sprite,
                                                                 self.blowFish_list)
        whale_hit_list = arcade.check_for_collision_with_list(self.penguin_sprite,
                                                              self.whale_list)

        # Loop through each colliding sprite, remove it, and add to the score or remove lives
        for redFish in redFish_hit_list:
            redFish.kill()
            self.score += 3

        for orangeFish in orangeFish_hit_list:
            orangeFish.kill()
            self.score += 2

        for greenFish in greenFish_hit_list:
            greenFish.kill()
            self.score += 1

        for blowFish in blowFish_hit_list:
            blowFish.kill()
            self.lives -= 1
            arcade.play_sound(self.lose_life_sound)

        for whale in whale_hit_list:
            whale.kill()
            self.lives -= 3

        # Change the speed of the fish as the score increases
        if self.score > 100:
            for fish in self.redFish_list:
                fish.change_x = self.score * SPEED_INCREASE
            for fish in self.blowFish_list:
                fish.change_x = self.score * SPEED_INCREASE
            for fish in self.greenFish_list:
                fish.change_x = self.score * SPEED_INCREASE
            for fish in self.orangeFish_list:
                fish.change_x = self.score * SPEED_INCREASE
            for fish in self.whale_list:
                fish.change_x = self.score * SPEED_INCREASE

        # display end game screen if player is out of lives
        if self.lives <= 0:
            arcade.play_sound(self.game_over_sound)
            end_view = EndGame()
            end_view.total_score = self.score
            self.window.show_view(end_view)


class EndGame(arcade.View):
    def __init__(self):
        super().__init__()
        self.total_score = 0

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("GAME OVER", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size= 50, anchor_x="center")

        arcade.draw_text("Total Score = " + str(self.total_score), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,
                         arcade.color.WHITE, font_size=30, anchor_x="center")


def main():
    window = arcade.Window(SCREEN_WIDTH,SCREEN_HEIGHT,"Catch the Fish - Katie Oosterhuis")
    instruction_view = InstructionView()
    window.show_view(instruction_view)
    arcade.run()

if __name__ == "__main__":
    main()


