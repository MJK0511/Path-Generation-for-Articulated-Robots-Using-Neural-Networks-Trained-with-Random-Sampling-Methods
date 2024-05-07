#!/usr/bin/env python3
import os
import re
import ast
import pandas as pd

class extract_middle:
    def __init__(self):
        self.waypoint = 17
        # self.columns_m = []
        # for i in range(1, 16):
        #     self.columns_m.extend([f'm{i}{j}' for j in 'abcdef'])

        self.columns_m = ['m8a', 'm8b', 'm8c', 'm8d', 'm8e', 'm8f', 'm4a', 'm4b', 'm4c', 'm4d', 'm4e', 'm4f', 'm9a', 'm9b', 'm9c', 'm9d', 'm9e', 'm9f', 'm2a', 'm2b', 'm2c', 'm2d', 'm2e', 'm2f', 'm10a', 'm10b', 'm10c', 'm10d', 'm10e', 'm10f', 'm5a', 'm5b', 'm5c', 'm5d', 'm5e', 'm5f', 'm11a', 'm11b', 'm11c', 'm11d', 'm11e', 'm11f', 'm1a', 'm1b', 'm1c', 'm1d', 'm1e', 'm1f', 'm12a', 'm12b', 'm12c', 'm12d', 'm12e', 'm12f', 'm6a', 'm6b', 'm6c', 'm6d', 'm6e', 'm6f', 'm13a', 'm13b', 'm13c', 'm13d', 'm13e', 'm13f', 'm3a', 'm3b', 'm3c', 'm3d', 'm3e', 'm3f', 'm14a', 'm14b', 'm14c', 'm14d', 'm14e', 'm14f', 'm7a', 'm7b', 'm7c', 'm7d', 'm7e', 'm7f', 'm15a', 'm15b', 'm15c', 'm15d', 'm15e', 'm15f']
        self.columns_s = ['sa', 'sb', 'sc', 'sd', 'se', 'sf']
        self.columns_g = ['ga', 'gb', 'gc', 'gd', 'ge', 'gf']

        self.train_columns = self.columns_s+self.columns_m+self.columns_g

        # Training dataset
        self.train_df = pd.DataFrame()
        
        # Test dataset
        self.test_df = pd.DataFrame()

    def middle_index(self, matches) : 
        if matches % 2 == 0: 
            middle_index = matches // 2 - 1
        else:
            middle_index = matches // 2
        return middle_index

    def extract_middle(self, learning_folder):
        m_lists = []
        all_mid = []

        for filename in os.listdir(learning_folder):
            if filename.endswith('.txt'):
                file_path = os.path.join(learning_folder, filename)

                with open(file_path, 'r') as file:
                    data = file.read()
                        
                    # positions 값을 추출할 정규 표현식
                    pattern = r'positions:\s*(\[.*?\])'
                    matches = re.findall(pattern, data)
                    n = len(matches)
                    
                    # positions 값이 waypoint개 이상인 경우만 처리
                    if n >= self.waypoint:
                        m_indices = [round(n * i / (self.waypoint)) for i in range(0, (self.waypoint-1))] + [n-1]

                        for index in m_indices:
                            m_lists.extend(list(ast.literal_eval(matches[index])))

                        # print(m_lists)

                        all_mid.append(tuple(m_lists))
                        m_lists = []

        # After the loop, concatenate all rows to the DataFrame
        self.train_df = pd.concat([self.train_df, pd.DataFrame(all_mid, columns=self.train_columns)], ignore_index=True)

    def test_sg(self, learning_folder):
        all_sg = []
            
        for filename in os.listdir(learning_folder):
            if filename.endswith('.txt'):
                file_path = os.path.join(learning_folder, filename)

                with open(file_path, 'r') as file: 
                    data = file.read()
                            
                    # positions 값을 추출할 정규 표현식
                    pattern = r'positions:\s*(\[.*?\])'
                    matches = re.findall(pattern, data)
                        
                    # positions 값이 3개 이상인 경우만 처리
                    if len(matches) >= 3:                           
                        s_list = list(ast.literal_eval(matches[0]))
                        g_list = list(ast.literal_eval(matches[-1]))

                        sg_data = [tuple(s_list+g_list)]
                        all_sg.extend(sg_data)

        # After the loop, concatenate all rows to the DataFrame
        self.test_df = pd.concat([self.test_df, pd.DataFrame(all_sg, columns=self.columns_s+self.columns_g)])

    def save_to_csv(self, learning_folder, test_folder, output_path):
        # Training Dataset
        self.extract_middle(learning_folder)
        self.train_df.to_csv(os.path.join(output_path, 'traininginput.csv'), index=False)

        # TEST Dataset
        # self.test_sg(test_folder)
        self.test_df.to_csv(os.path.join(output_path, 'testinput.csv'), index=False)

# angle 폴더 내의 모든 파일에 대해 반복
# default_folder = '/home/nishidalab07/github/6dimension/simulation2'
default_folder = "C:\\Users\\minje\\github\\simulation1"

# input_folder_path = os.path.join(default_folder, 'Configuration/selected_op')
input_folder_path = os.path.join(default_folder, 'Configuration\\selected_op')
# input_folder_path = os.path.join(default_folder, 'test')
test_folder_path = os.path.join(default_folder, 'Configuration\\test')
output_folder_path = os.path.join(default_folder, 'csv\\test') 

extractor = extract_middle()
extractor.save_to_csv(input_folder_path, test_folder_path, output_folder_path)
