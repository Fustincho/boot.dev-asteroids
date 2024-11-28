import constants
import pygame
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for object in updatable:
            object.update(dt)
        screen.fill("black")

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        # 60 FPS. Tick returns ms so we divide by 1000
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
