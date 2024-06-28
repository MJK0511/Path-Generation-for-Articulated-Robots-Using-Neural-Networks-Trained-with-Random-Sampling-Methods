import os
import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

class MoveOnePoint:
    def __init__(self):
        rospy.init_node('xArm6')

        self.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']

        self.client = actionlib.SimpleActionClient('/xarm/xarm6_traj_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
        self.client.wait_for_server()

    def movetopoint(self, goal_positions):

        # goal point
        
        trajectory = JointTrajectory()
        trajectory.joint_names = self.joint_names

        # 웨이포인트 추가
        num_waypoints = 3  # 원하는 웨이포인트 수로 변경
        duration_per_waypoint = 1.0  # 각 웨이포인트에 도달하는 데 걸리는 시간(초)

        for i in range(num_waypoints):
            point = JointTrajectoryPoint()
            point.positions = goal_positions
            point.time_from_start = rospy.Duration(i * duration_per_waypoint)
            trajectory.points.append(point)

        # ゴールの設定
        goal = FollowJointTrajectoryGoal()
        goal.trajectory = trajectory

        # アクションを実行
        self.client.send_goal(goal)
        self.client.wait_for_result()

        result = self.client.get_result()
        if result.error_code == result.SUCCESSFUL:
            print("successful!")
        else:
            print(f"failed! Error message: {result.error_string}")

goal_positions = [0.038040146298087, -0.0769280764459274, -0.4077942819228193, -0.0001213473923513, 0.4097432863265702, 0.0886203910422125]

moving = MoveOnePoint()
moving.movetopoint(goal_positions)