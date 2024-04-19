#!/usr/bin/python3
import rospy
from square import find_other_corners
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Bool
from math import sqrt

class Decider:

    def __init__(self):
        rospy.init_node('intersection')

        # Intersection box of intersection (x1, y1, x2, y2)
        self.intersection_box = self.calculate_corners(1,1,1,1)
       
        if(rospy.has_param("/smart_infrastructure/static_positions")):
            rospy.loginfo("Static position config found")

        static_positions = rospy.get_param("/smart_infrastructure/static_positions")
        corners = static_positions["intersection_corners"]

        self.intersection_obstruction = False

        rospy.loginfo("defined corners: %s", corners)
        rospy.loginfo("inferred corners: %s", find_other_corners((corners[0][0], corners[0][1]), (corners[1][0], corners[1][1])))
        rospy.loginfo("defined velodyne position: %s", static_positions["velodyne"])

        # Subsribers: Car Pose, etc.
        rospy.loginfo("Subscribing...")
        rospy.Subscriber('/car/particle_filter/inferred_pose', PoseStamped, self.car_pose_callback)

        # Publisher for car to read

    # Execute when new pose is received
    def car_pose_callback(self, msg: PoseStamped):
        # Print pose information
        rospy.loginfo(f"received message {msg}")

    def calculate_corners(self, x1: float, y1: float, x2: float, y2: float):
        

        return

if __name__ == "__main__":
    try:
        awesomeDecider = Decider()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
