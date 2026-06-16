from trajectory_list import DoublyLinkedTrajectory
from sliding_window import extract_velocity_features

if __name__ == "__main__":
    print("📈 Activating KinematicPath-LSTM Trajectory Analyzer...\n")

    robot_path = DoublyLinkedTrajectory()
    
    # Simulate a physics particle sequence tracking movement over time
    robot_path.log_coordinate(t=0.0, x=0.0, y=0.0)
    robot_path.log_coordinate(t=1.0, x=2.5, y=1.0)
    robot_path.log_coordinate(t=2.0, x=6.0, y=4.0)

    print("📥 Ingested Bi-Directional Coordinates Successfully.")
    calculated_kinematics = extract_velocity_features(robot_path)

    print("\n🔮 Calculated Feature Sets for Predictive Input Models:")
    for idx, (vx, vy) in enumerate(calculated_kinematics):
        print(f"   • Step Segment [{idx}] ---> Derived Velocity Vector Components: Vx = {vx:.2f} m/s, Vy = {vy:.2f} m/s")
