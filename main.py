import sys
import pygame

from block_puzzle.game import Game
from block_puzzle.colors import Colors

# NOTE: Basic init stuff, nothing special here.
pygame.init()
title_font = pygame.font.Font(None, 40)
screen = pygame.display.set_mode((500, 620))
score_surface = title_font.render("Score", True, Colors.white)
score_rect = pygame.Rect(320, 55, 170, 60)
next_surface = title_font.render("Next", True, Colors.white)
next_rect = pygame.Rect(320, 215, 170, 180)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

# NOTE: This sets the title of the window.
pygame.display.set_caption("Python Block Puzzle")

# NOTE: The clock controls the framerate of the game.
clock = pygame.time.Clock()

# NOTE: The game loop consists of 3 parts:
# NOTE: event handling, updating positions, and drawing objects.
game = Game()

# NOTE: This little bit of code creates a custom event,
#       called a "userevent" in Pygame.
#       The set_timer() call causes pygame to emit an
#       event of pygame.USEREVENT every 200 milliseconds.
#       By using this event in the event handler,
#       we can cause the current block to move downwards
#       at a reasonable rate (every 200 ms), and not at
#       60 fps.
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
    # NOTE: Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        # NOTE: As described above, this controls the
        #       speed at which the game drops blocks.
        #       Since the GAME_UPDATE event is only emitted
        #       every 200 ms, blocks descend reasonably slowly.
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    # NOTE: Drawing objects
    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(next_surface, (375, 180, 50, 50))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    screen.blit(
        score_value_surface,
        score_value_surface.get_rect(
            centerx=score_rect.centerx,
            centery=score_rect.centery
        )
    )

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    game.draw(screen)

    # NOTE: Updating positions.
    # NOTE: Should the .tick() call always be at the end? 
    pygame.display.update()
    clock.tick(60)
