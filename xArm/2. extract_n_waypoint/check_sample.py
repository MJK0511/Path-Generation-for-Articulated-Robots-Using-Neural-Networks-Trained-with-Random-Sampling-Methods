import os
import pandas as pd 
from extract_waypoint import ExtractWaypoint
from plot import Plot

default_folder = '/home/nishidalab07/github/Robot_path_planning_with_xArm/simulation3'

input_path = os.path.join(default_folder, 'Configuration/originpath/sample')
output_path = os.path.join(default_folder, 'csv')

# extract 15 waypint of sample
extractor = ExtractWaypoint()

samplecheck = extractor.trainDF(input_path)
samplecheck.to_csv(os.path.join(output_path, 'samplecheck.csv'), index=False)

df = pd.read_csv(os.path.join(output_path, 'samplecheck.csv'))

plotter = Plot()
# plot all window
# 0 : one path, all waypoint, 1 : one waypoint, all path
plotter.plot_all_window(df, 1)