import os
import re
import ast
import pandas as pd

class ExtractWaypoint:
    def __init__(self):
        self.waypoint = 17
        self.columns_m = ['m8a', 'm8b', 'm8c', 'm8d', 'm8e', 'm8f', 'm4a', 'm4b', 'm4c', 'm4d', 'm4e', 'm4f', 'm9a', 'm9b', 'm9c', 'm9d', 'm9e', 'm9f', 'm2a', 'm2b', 'm2c', 'm2d', 'm2e', 'm2f', 'm10a', 'm10b', 'm10c', 'm10d', 'm10e', 'm10f', 'm5a', 'm5b', 'm5c', 'm5d', 'm5e', 'm5f', 'm11a', 'm11b', 'm11c', 'm11d', 'm11e', 'm11f', 'm1a', 'm1b', 'm1c', 'm1d', 'm1e', 'm1f', 'm12a', 'm12b', 'm12c', 'm12d', 'm12e', 'm12f', 'm6a', 'm6b', 'm6c', 'm6d', 'm6e', 'm6f', 'm13a', 'm13b', 'm13c', 'm13d', 'm13e', 'm13f', 'm3a', 'm3b', 'm3c', 'm3d', 'm3e', 'm3f', 'm14a', 'm14b', 'm14c', 'm14d', 'm14e', 'm14f', 'm7a', 'm7b', 'm7c', 'm7d', 'm7e', 'm7f', 'm15a', 'm15b', 'm15c', 'm15d', 'm15e', 'm15f']
        self.columns_s = ['filename']+['sa', 'sb', 'sc', 'sd', 'se', 'sf']
        # self.columns_s = ['sa', 'sb', 'sc', 'sd', 'se', 'sf']
        self.columns_g = ['ga', 'gb', 'gc', 'gd', 'ge', 'gf']

        self.train_columns = self.columns_s+self.columns_m+self.columns_g
        self.test_colums = self.columns_s+self.columns_g

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

                        # filename을 추가
                        m_lists.insert(0, filename)
                        all_mid.append(tuple(m_lists))
                        m_lists = []

        return all_mid
    
    def trainDF(self, training_path):
        all_mid = self.extract_middle(training_path)
        self.train_df = pd.concat([self.train_df, pd.DataFrame(all_mid, columns=self.train_columns)], ignore_index=True)
        return self.train_df

    def testDF(self, test_path):
        all_mid = self.extract_middle(test_path)
        self.test_df = pd.concat([self.test_df, pd.DataFrame(all_mid, columns=self.train_columns)], ignore_index=True)
        return self.test_df
