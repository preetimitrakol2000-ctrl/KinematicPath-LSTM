def extract_velocity_features(trajectory_list):
    """Calculates derivatives from spatial metrics via linked list traversals."""
    features = []
    current = trajectory_list.head
    
    while current and current.next:
        dt = current.next.t - current.t
        dx = current.next.x - current.x
        dy = current.next.y - current.y
        
        velocity_x = dx / dt if dt != 0 else 0.0
        velocity_y = dy / dt if dt != 0 else 0.0
        features.append((velocity_x, velocity_y))
        current = current.next
        
    return features
