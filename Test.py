import sys

import pygame


def load_image(name):
    image = pygame.image.load(name)
    return image


class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []

        self.images.append(load_image("frame_00_delay-0.04s.gif"))
        self.images.append(load_image("frame_01_delay-0.04s.gif"))
        self.images.append(load_image("frame_02_delay-0.04s.gif"))
        self.images.append(load_image("frame_03_delay-0.04s.gif"))
        self.images.append(load_image("frame_04_delay-0.04s.gif"))
        self.images.append(load_image("frame_05_delay-0.04s.gif"))
        self.images.append(load_image("frame_06_delay-0.04s.gif"))
        self.images.append(load_image("frame_07_delay-0.04s.gif"))
        self.images.append(load_image("frame_08_delay-0.04s.gif"))
        self.images.append(load_image("frame_09_delay-0.04s.gif"))

        self.counter = 0
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 625, 766)

    def update(self):
        if 60 >= self.counter >= 0:

            self.counter += 0.04
            self.index += 1

        if self.counter >= 60:
            self.counter = 0

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


def main():
    pygame.init()
    size = width, height = 625, 766
    screen = pygame.display.set_mode(size)
    white = 255, 255, 255

    my_sprite = TestSprite()
    my_group = pygame.sprite.Group(my_sprite)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(white)
        my_group.update()
        my_group.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
