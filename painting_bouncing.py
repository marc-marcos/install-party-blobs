from ball import Ball

def get_distance(ball1 : Ball, ball2 : Ball):
    return (ball1.pos[0]-ball2.pos[0])*(ball1.pos[0]-ball2.pos[0]) + (ball1.pos[1]-ball2.pos[1])*(ball1.pos[1]-ball2.pos[1])

def handle_collision(ball1 : Ball, ball2 : Ball):
    pass