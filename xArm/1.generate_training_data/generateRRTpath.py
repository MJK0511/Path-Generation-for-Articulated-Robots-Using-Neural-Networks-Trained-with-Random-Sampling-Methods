from operator import ge
from re import T
import sys
import csv
import rospy
import moveit_commander
from datetime import datetime
from randomsg import RandomCoordinatesGenerator
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

default_folder = "/home/nishidalab07/github/Robot_path_planning_with_xArm/simulation"


if not rospy.get_node_uri():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('xArm6')

# Initialize MoveIt Commander
group = moveit_commander.MoveGroupCommander("xarm6")
group.set_planning_time(7.0)
robot = moveit_commander.RobotCommander()

joint_names = group.get_active_joints()

# Create a list to store execute times
times = []
count = 3
# trajectory = JointTrajectory()

# Get the initial joint values
initial_joint_values = group.get_current_joint_values()
group.set_joint_value_target(initial_joint_values)

# 객체 생성
generatorR = RandomCoordinatesGenerator()

# Iterate through all txt files in the specified folder
for i in range(count):
    print("Processing:", i)

    start, goal = generatorR.generate_random_coordinates()
    print("start: ", start)
    print("goal : ", goal)

    # set RRT*
    group.set_planner_id("RRTstar")  

    # go to start
    plan1 = group.plan(joints=start)
    group.go(wait=True)

    # go to goal
    start_time_plan = datetime.now()

    plan2 = group.plan(joints=goal)

    end_time_plan = datetime.now()
    planning_time = 0
    planning_time = (end_time_plan - start_time_plan).total_seconds()
        
    # Record times
    times.append({
        'count': i,
        'planning_time': planning_time
    })

    # Save the plan to a txt file
    path_filename = f'{default_folder}/Configuration/originpath/path_{i}.txt'
    # plan2 변수의 내용을 txt 파일에 저장
    with open(path_filename, 'w') as file:
        file.write(str(plan2))


# Shutdown MoveIt Commander
moveit_commander.roscpp_shutdown()

# Save times to a CSV file
csv_filename = f'{default_folder}/csv/time_RRT_test.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['count', 'planning_time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for entry in times:
        writer.writerow(entry)

print(f"Times saved to {csv_filename}")
