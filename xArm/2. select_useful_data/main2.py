import os
from extract_waypoint import ExtractWaypoint
from validate_result import Validation
from plot import Plot
from restriction import Restriction

default_folder = '/home/nishidalab07/github/Robot_path_planning_with_xArm/simulation3'

validator = Validation(default_folder)
extractor = ExtractWaypoint()
plotter = Plot(default_folder)
restrictor = Restriction()

## 2-1 실패한 데이터를 삭제, csv 파일로 결과를 남긴다.
## 2-2 1에서 생성한 10000개의 경로 중, 랜덤하게 선택한 100개의 샘플 데이터로부터 15개의 waypoint를 추출
def generate_sample(default_folder):
    input_path = os.path.join(default_folder, 'Configuration/sample')
    output_path = os.path.join(default_folder, 'csv/before')

    # Sample Data
    sample = extractor.trainDF(input_path)
    sample.to_csv(os.path.join(output_path, 'samplecheck.csv'), index=False)

## 2-3 2차원 그래프로 plot하여 원하는 경로를 통과하는 path의 범위를 설정
# plot all window
# 0 : one path, all waypoint, 1 : one waypoint, all path

## 2-4 설정한 범위 내에 존재하는 path를 모두 csv 파일로 저장 : training data의 생성 
def generate_training_input(default_folder):
    input_path = os.path.join(default_folder, 'Configuration/originpath')
    output_path = os.path.join(default_folder, 'csv/before')

    # original data
    train = extractor.trainDF(input_path)
    train.to_csv(os.path.join(output_path, 'originpath.csv'), index=False)

    # Training Data : After restriction
    restricted_train = restrictor.restrict_range(train)
    restricted_train.to_csv(os.path.join(output_path, 'traininginput.csv'), index=False)

## 2-5 test data를 생성 
def generate_test_input(default_folder):
    input_path = os.path.join(default_folder, 'Configuration/sample')
    output_path = os.path.join(default_folder, 'csv/before')

    # TEST Data
    test = extractor.testDF(input_path)
    test.to_csv(os.path.join(output_path, 'testinput.csv'), index=False)

## 2-1 
# validator.validation()

## 2-2 
# generate_sample(default_folder)

## 2-3.
# 0 : one path, all waypoint, 1 : one waypoint, all path
# plotter.plot_all_window(1)

## 2-4. 
# generate_training_input(default_folder)

##
generate_test_input(default_folder)