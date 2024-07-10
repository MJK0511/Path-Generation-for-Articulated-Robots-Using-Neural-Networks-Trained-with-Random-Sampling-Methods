import os
import csv
import shutil
import re

class Validation:
    def __init__(self, default_folder):
        self.input_path = os.path.join(default_folder, 'Configuration/originpath')
        self.fail_path = os.path.join(default_folder, 'Configuration/fail')
        self.output_path = os.path.join(default_folder, 'csv/evaluation/results.csv')
        
    def validation(self):
        file_results = []

        # input_folder 内のすべてのファイルに対して行う
        for filename in sorted(os.listdir(self.input_path)):
            # ファイルの名前からパスの番号を抽出
            match = re.match('path_([0-9]+).txt', filename)
            if match:
                number = int(match.group(1))  # 数字は定数型
                
                # 読み込み
                with open(os.path.join(self.input_path, filename), 'r') as infile:
                    lines = infile.readlines()
                    
                    # positionsの個数を数える
                    positions_count = sum(1 for line in lines if 'positions' in line)
                    
                    # 成功化失敗かを決める
                    if 15 <= positions_count <= 30:
                        result = 'success'
                    else:
                        result = 'fail'
                        
                        # 結果を出力
                        print(f'File: {filename}, Positions: {positions_count}, Result: {result}')
                        
                        # ファイル名と結果をリストに追加
                        file_results.append((number, positions_count, result))
                        
                        # 失敗したパスはfailディレクトリに移動
                        if result == 'fail':
                            shutil.move(os.path.join(self.input_path, filename), os.path.join(self.fail_path, filename))

        # csvとして生成
        with open(self.output_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            
            csvwriter.writerow(['filename', 'positions', 'result'])
            
            for number, positions_count, result in sorted(file_results, key=lambda x: x[0]):
                csvwriter.writerow([f'path_{number:04d}.txt', positions_count, result])
