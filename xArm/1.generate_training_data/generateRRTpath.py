import sys
import csv
import rospy
import moveit_commander
from datetime import datetime
from randomsg import RandomCoordinatesGenerator
from moveonepoint import MoveOnePoint

moving = MoveOnePoint()

class GenerateRRT:
    def __init__(self, default_folder, time):
        self.default_folder = default_folder
        self.times = []

        if not rospy.get_node_uri():
            moveit_commander.roscpp_initialize(sys.argv)
            rospy.init_node('xArm6')

        # Initialize MoveIt Commander
        self.group = moveit_commander.MoveGroupCommander("xarm6")
        self.group.set_planning_time(time)
        self.robot = moveit_commander.RobotCommander()
        self.joint_names = self.group.get_active_joints()
        
        # Get the initial joint values
        self.initial_joint_values = self.group.get_current_joint_values()
        self.group.set_joint_value_target(self.initial_joint_values)
        
        # Create an instance of RandomCoordinatesGenerator
        self.generatorR = RandomCoordinatesGenerator()

    def move_to_sg(self, count):
        for i in range(count):
            print("Processing:", i)

            start, goal = self.generatorR.generate_random_coordinates()
            print("start: ", start)
            print("goal : ", goal)

            # go to start
            moving.movetopoint(start)

            # set RRT*
            self.group.set_planner_id("RRTstar")  

            # go to goal
            start_time_plan = datetime.now()
            plan2 = self.group.plan(joints=goal)
            end_time_plan = datetime.now()
            planning_time = (end_time_plan - start_time_plan).total_seconds()
            
            # Record times
            self.times.append({
                'count': i,
                'planning_time': planning_time
            })

            # Save the plan to a txt file
            path_filename = f'{self.default_folder}/Configuration/originpath/path_{i}.txt'
            with open(path_filename, 'w') as file:
                file.write(str(plan2))

        # Shutdown MoveIt Commander
        moveit_commander.roscpp_shutdown()

    def save_times_csv(self):
        csv_filename = f'{self.default_folder}/csv/time_RRT_test.csv'
        with open(csv_filename, 'w', newline='') as csvfile:
            fieldnames = ['count', 'planning_time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for entry in self.times:
                writer.writerow(entry)
        print(f"Times saved to {csv_filename}")

# if __name__ == "__main__":
#     default_folder="/home/nishidalab07/github/Robot_path_planning_with_xArm/simulation2"
#     rrt_generator = GenerateRRT(default_folder, time=5)
#     rrt_generator.move_to_sg(count=3)
#     rrt_generator.save_times_csv()
