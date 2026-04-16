import pygame
import sys
import math 
from track import draw_smooth_track
from car import draw_robot,get_sensor,read_sensor,draw_sensor
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Line Follower Robot -Safu ")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LINE_THICKNESS = 20


track = pygame.Surface((WIDTH, HEIGHT))
track.fill(WHITE)


draw_smooth_track(track,BLACK,LINE_THICKNESS)


robot_x, robot_y = 60, 300
angle = 0
speed = 2

sensor_distance = 20



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw track
    screen.blit(track, (0, 0))

    # Sensors
    left_pos = get_sensor(angle,robot_x,robot_y,sensor_distance,-30)
    center_pos = get_sensor(angle,robot_x,robot_y,sensor_distance,0)
    right_pos = get_sensor(angle,robot_x,robot_y,sensor_distance,30)

    left = read_sensor(track,WIDTH,HEIGHT,BLACK,left_pos)
    center = read_sensor(track,WIDTH,HEIGHT,BLACK,center_pos)
    right = read_sensor(track,WIDTH,HEIGHT,BLACK,right_pos)


    draw_sensor(screen,left_pos,center_pos,right_pos)


    if center:
        turn = 2
    elif left:
        turn = -4   
    elif right:
        turn = 4    
    else:
        turn = -4   

    angle += turn

    robot_x += speed * math.cos(math.radians(angle))
    robot_y += speed * math.sin(math.radians(angle))

    draw_robot(screen,RED,robot_x,robot_y)

    pygame.display.update()
    clock.tick(60)