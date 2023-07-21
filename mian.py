
import pygame as pg
import math

pg.init()
clock = pg.time.Clock()

width = 1000
height = 800
screen = pg.display.set_mode((width, height))

cameraX = width/2
cameraY = height/2
cameraZ = -1000

cubeX = cubeY = cubeZ = 0
speed = 4
line_thickness = 2

cube_size = 200
cube_3d_pointlist = []


def update_list():
    global cube_3d_pointlist
    cube_3d_pointlist = [(cameraX - cube_size/2 + cubeX, cameraY - cube_size/2 + cubeY, cubeZ),
                         (cameraX + cube_size/2 + cubeX, cameraY -
                          cube_size/2 + cubeY, cubeZ),
                         (cameraX + cube_size/2 + cubeX, cameraY +
                          cube_size/2 + cubeY, cubeZ),
                         (cameraX - cube_size/2 + cubeX, cameraY +
                          cube_size/2 + cubeY, cubeZ),
                         (cameraX - cube_size/2 + cubeX, cameraY -
                          cube_size/2 + cubeY, cube_size + cubeZ),
                         (cameraX + cube_size/2 + cubeX, cameraY -
                          cube_size/2 + cubeY, cube_size + cubeZ),
                         (cameraX + cube_size/2 + cubeX, cameraY +
                          cube_size/2 + cubeY, cube_size + cubeZ),
                         (cameraX - cube_size/2 + cubeX, cameraY +
                          cube_size/2 + cubeY, cube_size + cubeZ)
                         ]


update_list()
cube_2d_pointlist = []


def keys_move():
    global cubeX, cubeY, cubeZ
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        cubeY -= speed
    if keys[pg.K_DOWN]:
        cubeY += speed
    if keys[pg.K_LEFT]:
        cubeX -= speed
    if keys[pg.K_RIGHT]:
        cubeX += speed
    if keys[pg.K_q]:
        cubeZ += (speed+10)
    if keys[pg.K_a]:
        cubeZ -= (speed+10)
    update_list()


def point_3d_to_2d(x, y, z):
    return (math.floor(((x-cameraX)*cameraZ)/(cameraZ-z)+cameraX)),(math.floor(((y-cameraY)*cameraZ)/(cameraZ-z)+cameraY))


def draw_polygons(screen):
    pg.draw.polygon(screen, (255, 255, 255), [
                    cube_2d_pointlist[0], cube_2d_pointlist[1], cube_2d_pointlist[5], cube_2d_pointlist[4]], line_thickness)
    pg.draw.polygon(screen, (255, 255, 255), [
                    cube_2d_pointlist[1], cube_2d_pointlist[2], cube_2d_pointlist[6], cube_2d_pointlist[5]], line_thickness)
    pg.draw.polygon(screen, (255, 255, 255), [
                    cube_2d_pointlist[2], cube_2d_pointlist[3], cube_2d_pointlist[7], cube_2d_pointlist[6]], line_thickness)
    pg.draw.polygon(screen, (255, 255, 255), [
                    cube_2d_pointlist[3], cube_2d_pointlist[0], cube_2d_pointlist[4], cube_2d_pointlist[7]], line_thickness)


running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys_move()

    cube_2d_pointlist = []
    for x, y, z in cube_3d_pointlist:
        cube_2d_pointlist.append(point_3d_to_2d(x, y, z))

    screen.fill((0, 0, 0))

    draw_polygons(screen)

    text_print = pg.font.SysFont("SFCompact", 12).render(str(cube_3d_pointlist), True, (255, 255, 255))
    text_print2 = pg.font.SysFont("SFCompact", 12).render(str(cube_2d_pointlist), True, (255, 255, 255))
    screen.blit(text_print, (0, 0))
    screen.blit(text_print2, (0, 20))

    clock.tick(60)
    pg.display.flip()

pg.quit()
