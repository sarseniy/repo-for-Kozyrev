import pygame
from random import randint
from pygame.draw import *

# colours used for picture
RED = (255, 000, 000)
BLUE = (000, 000, 255)
GREEN = (000, 255, 000)
B_GREEN = (170, 222, 105)
L_GREEN = (112, 200, 55)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 000)
GRAY = (128, 128, 128)
BLACK = (000, 000, 000)
SKY = (185, 211, 238)
PURPLE = (229, 128, 255)


# Array of functions drawing lama
def leg(pos, size, reverse=False):
    """
    Draws lama's leg with given coordinates and size
    :param pos: coordinates tuple of the top left corner of the leg (if reversed than right corner)
    :param size: size of the leg / default size (default height is 79 px)
    :param reverse: if revers is true, draws a leg pointing left; else - pointing right
    """
    if reverse:
        ellipse(screen, WHITE, pygame.Rect(pos[0] - int(15 * size), pos[1], int(15 * size), int(40 * size)))
        ellipse(screen, WHITE, pygame.Rect(pos[0] - int(15 * size), pos[1] + int(33 * size), int(15 * size),
                                           int(40 * size)))
        ellipse(screen, WHITE, pygame.Rect(pos[0] - int(20 * size), pos[1] + int(68 * size), int(20 * size),
                                           int(11 * size)))
    else:
        ellipse(screen, WHITE, pygame.Rect(pos[0], pos[1], int(15 * size), int(40 * size)))
        ellipse(screen, WHITE, pygame.Rect(pos[0], pos[1] + int(33 * size), int(15 * size), int(40 * size)))
        ellipse(screen, WHITE, pygame.Rect(pos[0], pos[1] + int(68 * size), int(20 * size), int(11 * size)))


def legs(pos, size, reverse=False):
    """
    Draws legs of lama with given coordinates and size
    :param pos: coordinates tuple of the top left corner of lama's body (if reversed then top right corner)
    :param size: size of the lama / default size (default size is (217, 134) px)
    :param reverse: if revers is true, draws a lama pointing left; else - pointing right
    """
    if reverse:
        leg((pos[0], pos[1] + int(20 * size)), size, reverse)
        leg((pos[0] - int(25 * size), pos[1] + int(30 * size)), size, reverse)
        leg((pos[0] - int(68 * size), pos[1] + int(20 * size)), size, reverse)
        leg((pos[0] - int(86 * size), pos[1] + int(35 * size)), size, reverse)
    else:
        leg((pos[0], pos[1] + int(20 * size)), size, reverse)
        leg((pos[0] + int(25 * size), pos[1] + int(30 * size)), size, reverse)
        leg((pos[0] + int(68 * size), pos[1] + int(20 * size)), size, reverse)
        leg((pos[0] + int(86 * size), pos[1] + int(35 * size)), size, reverse)


def body(pos, size, reverse=False):
    """
    Draws body of lama with given coordinates and size
    :param pos: coordinates tuple of the top left corner of lama's body (if reversed then top right corner)
    :param size: size of the lama / default size (default size is (217, 134) px)
    :param reverse: if revers is true, draws a lama pointing left; else - pointing right
    """
    if reverse:
        ellipse(screen, WHITE, pygame.Rect(pos[0] - int(117 * size), pos[1], int(117 * size), int(46 * size)))
    else:
        ellipse(screen, WHITE, pygame.Rect(pos[0], pos[1], int(117 * size), int(46 * size)))


def neck(pos, size, reverse=False):
    """
    Draws neck of lama with given coordinates and size
    :param pos: coordinates tuple of the top left corner of the lama (if reversed than right corner)
    :param size: size of the legs / default size (default height is 114 px)
    :param reverse: if revers is true, draws a legs pointing left; else - pointing right
    """
    if reverse:
        ellipse(screen, WHITE, pygame.Rect(pos[0] - int(87 * size) - int(34 * size), pos[1] - int(65 * size),
                                           int(34 * size), int(90 * size)))
        ellipse(screen, WHITE, pygame.Rect(pos[0] - int(93 * size) - int(41 * size), pos[1] - int((83 * size)),
                                           int(41 * size), int(25 * size)))
    else:
        ellipse(screen, WHITE, pygame.Rect(pos[0] + int(87 * size), pos[1] - int(65 * size), int(34 * size),
                                           int(90 * size)))
        ellipse(screen, WHITE, pygame.Rect(pos[0] + int(93 * size), pos[1] - int((83 * size)), int(41 * size),
                                           int(25 * size)))


def eyes(pos, size, reverse=False):
    """
    Draws eyes of lama with given coordinates and size
    :param pos: coordinates tuple of the top left corner of lama's body (if reversed then top right corner)
    :param size: size of the lama / default size (default size is (217, 134) px)
    :param reverse: if revers is true, draws a lama pointing left; else - pointing right
    """
    if reverse:
        circle(screen, PURPLE, (pos[0] - int(112 * size), pos[1] - int(70 * size)), int(8 * size))
        circle(screen, BLACK, (pos[0] - int(115 * size), pos[1] - int(70 * size)), int(4 * size))
        ellipse(screen, WHITE, pygame.Rect(pos[0] - int(106 * size) - int(6 * size), pos[1] - int(75 * size),
                                           int(6 * size), int(4 * size)))
    else:
        circle(screen, PURPLE, (pos[0] + int(112 * size), pos[1] - int(70 * size)), int(8 * size))
        circle(screen, BLACK, (pos[0] + int(115 * size), pos[1] - int(70 * size)), int(4 * size))
        ellipse(screen, WHITE, pygame.Rect(pos[0] + int(106 * size), pos[1] - int(75 * size), int(6 * size),
                                           int(4 * size)))


def ears(pos, size, reverse=False):
    """
    This function draws ears of lama with given coordinates and size
    :param pos: coordinates tuple of the top left corner of lama's body (if reversed then top right corner)
    :param size: size of the lama / default size (default size is (217, 134) px)
    :param reverse: if revers is true, draws a lama pointing left; else - pointing right
    """
    if reverse:
        ear1 = [pos[0] - int(96 * size), pos[1] - int(75 * size)]
        polygon(screen, WHITE, [ear1, (ear1[0] + int(15 * size), ear1[1] - int(22 * size)),
                                (ear1[0] - int(10 * size), ear1[1])])
        ear2 = [pos[0] - int(108 * size), pos[1] - int(80 * size)]
        polygon(screen, WHITE,
                [ear2, (ear2[0] + int(15 * size), ear2[1] - int(22 * size)), (ear2[0] - int(10 * size), ear2[1])])
    else:
        ear1 = [pos[0] + int(96 * size), pos[1] - int(75 * size)]
        polygon(screen, WHITE, [ear1, (ear1[0] - int(15 * size), ear1[1] - int(22 * size)),
                                (ear1[0] + int(10 * size), ear1[1])])
        ear2 = [pos[0] + int(108 * size), pos[1] - int(80 * size)]
        polygon(screen, WHITE,
                [ear2, (ear2[0] - int(15 * size), ear2[1] - int(22 * size)), (ear2[0] + int(10 * size), ear2[1])])


def draw_lama(pos, size, reverse=False):
    """
    This function draws lama with given coordinates and size
    :param pos: coordinates tuple of the top left corner of lama's body (if reversed then top right corner)
    :param size: size of the lama / default size (default size is (217, 134) px)
    :param reverse: if revers is true, draws a lama pointing left; else - pointing right
    """
    # Resizing the position
    pos[0] = int(pos[0] * size)
    pos[1] = int(pos[1] * size)

    # Drawing the lama
    body(pos, size, reverse)
    legs(pos, size, reverse)
    neck(pos, size, reverse)
    eyes(pos, size, reverse)
    ears(pos, size, reverse)


# Array of functions drawing flowers and bushes
def draw_flower(pos, size):
    """
    Draws random flower with given coordinates and size
    :param pos: coordinates tuple of the top left corner of flower
    :param size: size of the flower / default size (default size is (42, 21) px)
    """
    num = randint(1, 4)
    eval('flower_{}({}, {})'.format(num, pos, size))


def flower_1(pos, size):
    """
    Draws 9 petals flower with given coordinates and size
    :param pos: coordinates tuple of the top left corner of flower
    :param size: size of the flower / default size (default size is (42, 21) px)
    """
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    param = [15, 7]
    param[0] = int(param[0] * size)
    param[1] = int(param[1] * size)
    ellipse(screen, YELLOW,
            pygame.Rect(pos[0] + int(15 * size), pos[1] + int(6 * size), int(18 * size), int(9 * size)))
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(5 * size), pos[1] + int(2 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(5 * size), pos[1] + int(2 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(1 * size), pos[1] + int(6 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(1 * size), pos[1] + int(6 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(5 * size), pos[1] + int(10 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(5 * size), pos[1] + int(10 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(10 * size), pos[1] + int(12 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(10 * size), pos[1] + int(12 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(15 * size), pos[1] + int(0 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(15 * size), pos[1] + int(0 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(23 * size), pos[1] + int(3 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(23 * size), pos[1] + int(3 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(28 * size), pos[1] + int(5 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(28 * size), pos[1] + int(5 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(25 * size), pos[1] + int(9 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(25 * size), pos[1] + int(9 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(20 * size), pos[1] + int(13 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(20 * size), pos[1] + int(13 * size), param[0], param[1]), 1)


def flower_2(pos, size):
    """
    Draws 8 petals flower with given coordinates and size
    :param pos: coordinates tuple of the top left corner of flower
    :param size: size of the flower / default size (default size is (42, 21) px)
    """
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    param = [15, 7]
    param[0] = int(param[0] * size)
    param[1] = int(param[1] * size)
    ellipse(screen, YELLOW,
            pygame.Rect(pos[0] + int(15 * size), pos[1] + int(6 * size), int(18 * size), int(9 * size)))
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(5 * size), pos[1] + int(2 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(5 * size), pos[1] + int(2 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(1 * size), pos[1] + int(6 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(1 * size), pos[1] + int(6 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(5 * size), pos[1] + int(10 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(5 * size), pos[1] + int(10 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(15 * size), pos[1] + int(12 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(15 * size), pos[1] + int(12 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(15 * size), pos[1] + int(0 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(15 * size), pos[1] + int(0 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(23 * size), pos[1] + int(3 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(23 * size), pos[1] + int(3 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(28 * size), pos[1] + int(7 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(28 * size), pos[1] + int(7 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(25 * size), pos[1] + int(11 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(25 * size), pos[1] + int(11 * size), param[0], param[1]), 1)


def flower_3(pos, size):
    """
    Draws 7 petals flower with given coordinates and size
    :param pos: coordinates tuple of the top left corner of flower
    :param size: size of the flower / default size (default size is (42, 21) px)
    """
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    param = [15.5, 7.5]
    param[0] = int(param[0] * size)
    param[1] = int(param[1] * size)
    ellipse(screen, YELLOW,
            pygame.Rect(pos[0] + int(15 * size), pos[1] + int(6 * size), int(18 * size), int(9 * size)))
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(5 * size), pos[1] + int(2 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(5 * size), pos[1] + int(2 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(2 * size), pos[1] + int(8 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(2 * size), pos[1] + int(8 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(10 * size), pos[1] + int(13 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(10 * size), pos[1] + int(13 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(20 * size), pos[1] + int(12 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(20 * size), pos[1] + int(12 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(15 * size), pos[1] + int(0 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(15 * size), pos[1] + int(0 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(23 * size), pos[1] + int(3 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(23 * size), pos[1] + int(3 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(28 * size), pos[1] + int(7 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(28 * size), pos[1] + int(7 * size), param[0], param[1]), 1)


def flower_4(pos, size):
    """
    Draws 6 petals flower with given coordinates and size
    :param pos: coordinates tuple of the top left corner of flower
    :param size: size of the flower / default size (default size is (42, 21) px)
    """
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    param = [17, 8]
    param[0] = int(param[0] * size)
    param[1] = int(param[1] * size)
    ellipse(screen, YELLOW,
            pygame.Rect(pos[0] + int(15 * size), pos[1] + int(6 * size), int(18 * size), int(9 * size)))
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(5 * size), pos[1] + int(2 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(5 * size), pos[1] + int(2 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(2 * size), pos[1] + int(8 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(2 * size), pos[1] + int(8 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(10 * size), pos[1] + int(13 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(10 * size), pos[1] + int(13 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(20 * size), pos[1] + int(12 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(20 * size), pos[1] + int(12 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(17 * size), pos[1] + int(1 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(17 * size), pos[1] + int(1 * size), param[0], param[1]), 1)
    ellipse(screen, random_color, pygame.Rect(pos[0] + int(25 * size), pos[1] + int(6 * size), param[0], param[1]))
    ellipse(screen, BLACK, pygame.Rect(pos[0] + int(25 * size), pos[1] + int(6 * size), param[0], param[1]), 1)


def bush(pos, size):
    """
    Draws round bush with given coordinates and size
    :param pos: coordinates tuple of the top left corner of bush
    :param size: size of the flower / default size (default size is (200, 200) px)
    """
    # Setting a bush
    radius = 100
    circle(screen, L_GREEN, pos, int(radius * size))
    # Scattering 5 flowers on the bush
    draw_flower((pos[0] - int(5 * size), pos[1] + int(35 * size)), 1.6 * size)
    draw_flower((pos[0] - int(70 * size), pos[1] - int(45 * size)), 1.4 * size)
    draw_flower((pos[0] - int(30 * size), pos[1] - int(20 * size)), 1.2 * size)
    draw_flower((pos[0] + int(10 * size), pos[1] - int(55 * size)), 1.8 * size)
    draw_flower((pos[0] - int(75 * size), pos[1] + int(25 * size)), 1.8 * size)


pygame.init()

# Screen settings
FPS = 30
screen = pygame.display.set_mode((900, 706))

# Sky and mountains drawing
rect(screen, SKY, (0, 0, 900, 706))

mountains_contour = [(0, 216), (60, 73), (104, 172), (172, 93), (297, 282), (389, 88), (419, 122),
                     (490, 130), (570, 250), (750, 140), (900, 300), (900, 706), (0, 706)]
polygon(screen, GRAY, mountains_contour)
polygon(screen, BLACK, mountains_contour, 1)

field_contour = [(0, 373), (38, 362), (75, 359), (114, 352), (271, 355),
                 (280, 414), (294, 418), (900, 419), (900, 706), (0, 706)]
polygon(screen, B_GREEN, field_contour)
polygon(screen, BLACK, field_contour, 1)

# Creating bushes
bush([420, 581], 0.7)
bush([650, 530], 0.5)
bush([110, 625], 0.8)
bush([110, 625], 1.4)
bush([440, 400], 0.7)
bush([850, 450], 0.7)

# Drawing lamas
draw_lama([500, 800], 0.7, True)
draw_lama([600, 1000], 0.4, True)
draw_lama([600, 800], 0.5)
draw_lama([-80, 190], 3)
draw_lama([600, 350], 1.5, True)
draw_lama([800, 550], 0.7)
draw_lama([900, 850], 0.7, True)

# FPS settings
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
