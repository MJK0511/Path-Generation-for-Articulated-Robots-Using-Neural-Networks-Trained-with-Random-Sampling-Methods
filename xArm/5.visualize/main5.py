import os
from csvtotxt import CsvtoTxt
from ex_and_con_cartesian_all import CtoT
from visual_onepath import VisualOnePath

default_folder = '/home/nishidalab07/github/Robot_path_planning_with_xArm/simulation3'

csvtotxt = CsvtoTxt()
cartesian = CtoT()
visualization1 = VisualOnePath()

def Csv_to_Txt(default_folder):
    input_path = os.path.join(default_folder, 'csv/after/after_train.csv')
    output_path = os.path.join(default_folder, 'Configuration/aftertrain')
    csvtotxt.csv_to_txt(input_path, output_path)

def Cartesian_to_Task(default_folder):
    input_path = os.path.join(default_folder, 'Configuration/aftertrain')
    output_path = os.path.join(default_folder, 'Task/aftertrain')
    cartesian.process_files(input_path, output_path)

## 5-1
# Csv_to_Txt(default_folder)

## 5-2
# Cartesian_to_Task(default_folder)

## 5-3
file_path = os.path.join(default_folder, 'Task/aftertrain/path1_visual.txt')
visualization1.visualize_trajectory_points(file_path)

