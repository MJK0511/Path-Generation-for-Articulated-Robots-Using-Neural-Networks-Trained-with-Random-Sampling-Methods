import os
from extract_waypoint import ExtractWaypoint
from validate_result import Validation
from plot import Plot
from restriction import Restriction

default_folder = '/home/nishidalab07/github/Robot_path_planning_with_xArm/simulation2'

validator = Validation(default_folder)
extractor = ExtractWaypoint()
plotter = Plot(default_folder)
restrictor = Restriction()


# 2-2 1.から生成した教師データの中から，100個のサンプルデータから15個のウェイポイントを抽出
def generate_sample(default_folder):
    input_path = os.path.join(default_folder, 'Configuration/sample')
    output_path = os.path.join(default_folder, 'csv/before')

    # Sample Data
    sample = extractor.trainDF(input_path)
    sample.to_csv(os.path.join(output_path, 'samplecheck.csv'), index=False)

    # Training Data : After restriction
    restricted_train = restrictor.restrict_range(sample)
    restricted_train.to_csv(os.path.join(output_path, 'traininginput.csv'), index=False) 


## 2-4 設定した範囲内に存在するパスをすべてcsvとして出力：トレーニングデータの生成
def generate_training_input(default_folder):
    input_path = os.path.join(default_folder, 'Configuration/originpath')
    output_path = os.path.join(default_folder, 'csv/before')

    # original data
    train = extractor.trainDF(input_path)
    # train.to_csv(os.path.join(output_path, 'originpath.csv'), index=False)
    print(train.shape)

    # Training Data : After restriction
    restricted_train = restrictor.restrict_range(train)
    restricted_train.to_csv(os.path.join(output_path, 'traininginput.csv'), index=False) 

## 2-5 テストデータの生成
def generate_test_input(default_folder):
    input_path = os.path.join(default_folder, 'Configuration/sample')
    output_path = os.path.join(default_folder, 'csv/before')

    # TEST Data
    test = extractor.testDF(input_path)
    test.to_csv(os.path.join(output_path, 'testinput.csv'), index=False)

## 2-1 失敗したデータを削除し，csvファイルに入れる
# validator.validation()

## 2-2 1.から生成した教師データの中から，100個のサンプルデータから15個のウェイポイントを抽出
# generate_sample(default_folder)

## 2-3 2次元グラフとしてプロットし，望ましい経路を通るパスの範囲を設定
# one path, all waypoint # n = path name
# plotter.plot_one_waypoint(10)

# one waypoint, all path # m = waypoint name
# plotter.plot_all_waypoint('m1')

## 2-4 設定した範囲内に存在するパスをすべてcsvとして出力：トレーニングデータの生成
generate_training_input(default_folder)

## 2-5 テストデータの生成
# generate_test_input(default_folder)