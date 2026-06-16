from path_node import TrajectoryPointNode

class DoublyLinkedTrajectory:
    def __init__(self):
        self.head = None
        self.tail = None

    def log_coordinate(self, t, x, y):
        new_point = TrajectoryPointNode(t, x, y)
        if not self.head:
            self.head = new_point
            self.tail = new_point
            return
        self.tail.next = new_point
        new_point.prev = self.tail
        self.tail = new_point
