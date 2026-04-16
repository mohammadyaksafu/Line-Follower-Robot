import math
import pygame

def get_sensor(angle,robot_x,robot_y,sensor_distance,offset_angle):
    rad = math.radians(angle + offset_angle)
    x = robot_x + sensor_distance * math.cos(rad)
    y = robot_y + sensor_distance * math.sin(rad)
    return int(x), int(y)


def read_sensor(track,WIDTH,HEIGHT,BLACK,pos):
    x, y = pos
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        return track.get_at((x, y)) == BLACK
    return False

def draw_robot(screen,RED,robot_x,robot_y):
    pygame.draw.circle(screen, RED, (int(robot_x), int(robot_y)), 10)

def draw_sensor(screen,left_pos,center_pos,right_pos):
    pygame.draw.circle(screen, (0,255,0), left_pos, 5)
    pygame.draw.circle(screen, (0,0,255), center_pos, 5)
    pygame.draw.circle(screen, (255,255,0), right_pos, 5)