from randomsg_3d import RandomSG
from generateRRTpath import GenerateRRT

default_path = "/home/nishidalab07/github/Robot_path_planning_with_xArm/simulation1/"

randomsg = RandomSG()
rrt_generator = GenerateRRT(default_path, time=3)

# 1. x, y, zの最大・最小領域を定義
s_range = [0.218, 0.415, -0.0767, 0.109, 0.0559, 0.192]
g_range = [-0.105, 0.115, -0.425, -0.231, 0.0151, 0.208]

## RRT*の場合，time(s)を指定して最大生成時間を決める．
rrt_generator = GenerateRRT(default_path, time=5)

## countは生成するパスの個数
rrt_generator.move_to_sg(count=3, start_range=s_range, goal_range=g_range)
rrt_generator.save_times_csv()