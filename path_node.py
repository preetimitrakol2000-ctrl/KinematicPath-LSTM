class TrajectoryPointNode:
    def __init__(self, time_step, x_pos, y_pos):
        self.t = time_step
        self.x = x_pos
        self.y = y_pos
        self.next = None
        self.prev = None
