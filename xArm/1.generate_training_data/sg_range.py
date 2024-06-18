import os
import csv
import re

class SGRange:
    def __init__(self, default_path):
        self.start_path = os.path.join(default_path, "Configuration/sg/start")
        self.goal_path = os.path.join(default_path, "Configuration/sg/goal")
        self.output_path = os.path.join(default_path, "csv/before")

        self.columns = 6

    def read_positions(self, file_path):
        positions = []
        pattern = r'positions:\s*(\[.*?\])'

        with open(file_path, 'r') as file:
            for line in file:
                match = re.search(pattern, line)
                if match:
                    position_line = match.group(1)
                    position_line = position_line.strip('[').strip(']')  # 대괄호 제거
                    positions = [float(val.strip()) for val in position_line.split(',')]
                    break

        return positions

    def read_txt_file(self, directory_path):
        # Read all txt files in the directory_path
        list_var = []
        for file_name in os.listdir(directory_path):
            if file_name.endswith('.txt'):
                file_path = os.path.join(directory_path, file_name)
                positions = self.read_positions(file_path)
                list_var.extend(positions)

        # Reshape list_var to have self.columns columns
        list_var = [list_var[i:i + self.columns] for i in range(0, len(list_var), self.columns)]

        # Find the minimum and maximum values in each column of list_var
        min_vals = [min(col) for col in zip(*list_var)]
        max_vals = [max(col) for col in zip(*list_var)]
        
        return list_var, min_vals, max_vals

    def save_to_csv(self, data, filename):
        csv_path = os.path.join(self.output_path, filename)
        with open(csv_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(data)

    def sgrange(self):
        start, s_min, s_max = self.read_txt_file(self.start_path)
        goal, g_min, g_max = self.read_txt_file(self.goal_path)

        # Save data to CSV files
        self.save_to_csv(start, "start.csv")
        self.save_to_csv(goal, "goal.csv")

        print(f"start_range: {s_min}, {s_max}")
        print(f"goal_range: {g_min}, {g_max}")



# # 기본 경로
# default_path = "/home/nishidalab07/github/Robot_path_planning_with_xArm/simulation2/"
# sg_range = SGRange(default_path)
# sg_range.sgrange()
