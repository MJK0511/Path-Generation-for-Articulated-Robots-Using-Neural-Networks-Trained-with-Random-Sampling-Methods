import os
import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import csv

rospy.init_node('xArm6')

joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']

client = actionlib.SimpleActionClient('/xarm/xarm6_traj_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
client.wait_for_server()

# goal point
goal_positions = [-1.3, 0.2, -0.6, -0.003813281147, 1.0790173902, 0.4641266619]

trajectory = JointTrajectory()
trajectory.joint_names = joint_names

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
client.send_goal(goal)
client.wait_for_result()

result = client.get_result()
if result.error_code == result.SUCCESSFUL:
    print("successful!")
else:
    print(f"failed! Error message: {result.error_string}")
