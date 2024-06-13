from sg_range import SGrange
from randomsg import RandomCoordinatesGenerator
from generateRRTpath import GenerateRRTPath
from moveonepoint import MoveOnePoint

default_path = "/home/nishidalab07/github/Robot_path_planning_with_xArm/simulation3/"

# 1-2 
s_min, s_max, g_min, g_max = SGrange.sgrange(default_path)
print(f"start_range:{s_min},{s_max}")
print(f"goal_range:{g_min},{g_max}")

goal_positions = [-1.3, 0.2, -0.6, -0.003813281147, 1.0790173902, 0.4641266619]

moving = MoveOnePoint()
moving.movetopoint(goal_positions)