import pygame

def draw_smooth_track(track,BLACK,LINE_THICKNESS):

    main_rect = pygame.Rect(100, 100, 600, 400)
    pygame.draw.rect(track, BLACK, main_rect, LINE_THICKNESS, border_radius=80)


    inner_rect = pygame.Rect(250, 200, 300, 200)
    pygame.draw.rect(track, BLACK, inner_rect, LINE_THICKNESS, border_radius=40)


    pygame.draw.line(track, BLACK, (400, 100), (400, 200), LINE_THICKNESS)
    pygame.draw.circle(track, BLACK, (400, 200), LINE_THICKNESS // 2)


    zigzag_points = [(250, 500), (300, 560), (350, 500), (400, 560), (450, 500)]
    pygame.draw.lines(track, BLACK, False, zigzag_points, LINE_THICKNESS)
    
    for pt in zigzag_points:
        pygame.draw.circle(track, BLACK, pt, LINE_THICKNESS // 2)


    start_diag = (250, 200)
    end_diag = (550, 400)
    pygame.draw.line(track, BLACK, start_diag, end_diag, LINE_THICKNESS)
    
 
    intersections = [(250, 200), (550, 400), (400, 100)]
    for pos in intersections:
        pygame.draw.circle(track, BLACK, pos, LINE_THICKNESS // 2)
