from sg_range import SGRange
from moveonepoint import MoveOnePoint
from generateRRTpath import GenerateRRT

default_path = "/home/nishidalab07/github/Robot_path_planning_with_xArm/simulation2/"

sg_range = SGRange(default_path) 
moving = MoveOnePoint()
rrt_generator = GenerateRRT(default_path, time=7)

## 1-2 
# sg_range.sgrange()

## 1-3
# s_min
# goal_positions = [-0.4, -0.3, -0.5, -6.226610678172761e-05, 8.343721795662674e-05, -0.6]
# s_max
# goal_positions = [0.0, -1.00, 3.860126045296397e-05, 0.00011172202384379659, 1.0407782478617102, 0.266168281893874]

# g_min
# goal_positions = [-1.2498537471727624, -0.4, -3.0, -3.0, 0.8, -0.5]
# g_max
# goal_positions = [1.6066508572625366, -0.1, -2.0, 2.06, 1.7, 0.6438224568308124]

# test
# goal_positions = [0.8973413136497992, 0.1, -2.763500692087306, -0.7059470270819488, 1.1236277576136253, 0.3956714078908573]
# moving.movetopoint(goal_positions)

## 1-4
rrt_generator.move_to_sg(count=10000)
rrt_generator.save_times_csv()