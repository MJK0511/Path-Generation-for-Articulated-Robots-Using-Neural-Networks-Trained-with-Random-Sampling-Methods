import os
import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
# 特定ポイントまで移動するプログラム

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

        # ウェイポイントを追加
        num_waypoints = 3  # 望むウェイポイントの数を設定
        duration_per_waypoint = 1.0  # 各ウェイポイントまで到達する最大時間を設定(s)

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

#移動したいポイントの関節角度を入力
goal_positions = [-0.0757597751047898, -0.0855379354935719, -0.3967935455350373, 0.0007703124332953, 0.4147338313256012, 0.3060854672165192]

moving = MoveOnePoint()
moving.movetopoint(goal_positions)