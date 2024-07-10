import os
import pandas as pd
#　csvの出力をtxtに変える
class CsvtoTxt:
    def csv_to_txt(self, csv_file_path, output_dir):
        df = pd.read_csv(csv_file_path, header=None)
        
        for i in range(1, len(df)):
            file_name = f"path{i}.txt"
            output_file_path = os.path.join(output_dir, file_name)
            
            with open(output_file_path, 'w') as output_file:
                # 데이터 프레임의 열 수만큼 반복
                for j in range(0, len(df.columns), 6):
                    # 각 행을 선택하여 출력
                    row_values = df.iloc[i, j:j+6].values.tolist()
                    formatted_values = f"[{', '.join(map(str, row_values))}]"
                    output_file.write(formatted_values + '\n')

