import os
from csvtotxt import CsvtoTxt
from ex_and_con_cartesian_all import CtoT
from visualization import VisualOnePath

default_folder = '/home/nishidalab07/github/Robot_path_planning_with_xArm/simulation2'

csvtotxt = CsvtoTxt()
cartesian = CtoT()
visualization1 = VisualOnePath()

def Csv_to_Txt(default_folder):
    # before train for check sample
    # input_path = os.path.join(default_folder, 'csv/before/samplecheck.csv')
    # output_path = os.path.join(default_folder, 'Configuration/beforesample')

    # after train # all / point / area
    input_path = os.path.join(default_folder, 'csv/after/after_train.csv')
    output_path = os.path.join(default_folder, 'Configuration/aftertrain')
    
    csvtotxt.csv_to_txt(input_path, output_path)

def Cartesian_to_Task(default_folder):
    # before train for check sample
    # input_path = os.path.join(default_folder, 'Configuration/beforesample')
    # output_path = os.path.join(default_folder, 'Task/beforesample')

    # after train # all / point / area
    input_path = os.path.join(default_folder, 'Configuration/aftertrain')
    output_path = os.path.join(default_folder, 'Task/aftertrain')

    cartesian.process_files(input_path, output_path)

# # 5-1
# Csv_to_Txt(default_folder)

# # 5-2
# Cartesian_to_Task(default_folder)

## 5-3
# before train
# directory_path = os.path.join(default_folder, 'Task/beforesample')

# after train # all, area, point
directory_path = os.path.join(default_folder, 'Task/aftertrain')

visualization1.visualize_one_path(os.path.join(directory_path, 'path2_visual.txt')) # 2
# visualization1.visualize_all_path_1sec(directory_path)
# visualization1.visualize_all_path(directory_path)
