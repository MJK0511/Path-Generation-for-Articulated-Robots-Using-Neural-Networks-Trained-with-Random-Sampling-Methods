import pandas as pd
import re
import os
import ast

class GenerateMiddle:
    def __init__(self):
        self.number = 3
        self.filename = pd.DataFrame()
        self.m_df = pd.DataFrame()
        self.columns = ['sx', 'sy', 'sz', 'sox', 'soy', 'soz', 'sow','mx', 'my', 'mz', 'mox', 'moy', 'moz', 'mow','mcx', 'mcy', 'mcz', 'mcox', 'mcoy', 'mcoz', 'mcow', 'gx', 'gy', 'gz', 'gox', 'goy', 'goz', 'gow','filename']

    def middle_index(self, matches): 
        if matches % 2 == 0: 
            middle_index = matches // 2 - 1
        else:
            middle_index = matches // 2
        return middle_index

    def extract_m(self, learning_folder):
        for filename in os.listdir(learning_folder):
            if filename.endswith('.txt'):
                file_path = os.path.join(learning_folder, filename)

                with open(file_path, 'r') as file:
                    data = file.read()

                    # 각 줄의 좌표 값을 추출할 정규 표현식
                    pattern = r'\[([\d\.,\s-]+)\]'
                    matches = re.findall(pattern, data)
                    
                    # 좌표 값이 n개 이상인 경우만 처리
                    if len(matches) >= self.number:
                        s_list = list(ast.literal_eval(matches[0]))
                        g_list = list(ast.literal_eval(matches[-1]))

                        for i in self.number :
                            idx = self.middle_index(len(matches))                   
                            m_list = list(ast.literal_eval(matches[idx]))

                        # 각각의 DataFrame에 추가
                        row_data = [tuple(s_list + m_list + g_list + [filename])]
                        self.m_df = pd.concat([self.m_df, pd.DataFrame(data=row_data, columns=self.columns)], ignore_index=True)
        return self.m_df

    def savetocsv(self, df, output_directory, filename):
        df.to_csv(os.path.join(output_directory, f'{filename}.csv'), index=False)