import os
import pandas as pd
from extract_waypoint import ExtractWaypoint

def restrict_range(df):
    # 조건을 만족하지 않는 행을 삭제합니다.
    df = df[(df['m1a'] > -1.0) & (df['m1a'] < -0.5) &
              (df['m1b'] > 0.5) & (df['m1b'] < 0.0) &
              (df['m1c'] > 1.2) & (df['m1c'] < 0.6) &
              (df['m1d'] > 0.5) & (df['m1d'] < 0.5) &
              (df['m1e'] > 0.0) & (df['m1e'] < 1.2) &
              (df['m1f'] > 0.5) & (df['m1f'] < 0.5)]

    return df

default_folder = '/home/nishidalab07/github/Robot_path_planning_with_xArm/simulation3'

input_path = os.path.join(default_folder, 'Configuration/originpath')
test_path = os.path.join(default_folder, 'test')
output_path = os.path.join(default_folder, 'csv')

extractor = ExtractWaypoint()

# Training Dataset
train = extractor.trainDF(input_path)
train.to_csv(os.path.join(output_path, 'originpath.csv'), index=False)
restrict_range(train)
train.to_csv(os.path.join(output_path, 'traininginput.csv'), index=False)
