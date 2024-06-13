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
    # 파일 이름과 결과의 쌍을 저장할 리스트
        file_results = []

        # input_folder 내의 모든 파일 순회
        for filename in sorted(os.listdir(self.input_path)):
            # 정규 표현식을 사용하여 파일 이름에서 숫자 추출
            match = re.match('path_([0-9]+).txt', filename)
            if match:
                number = int(match.group(1))  # 숫자를 정수형으로 변환
                
                # 파일 읽기
                with open(os.path.join(self.input_path, filename), 'r') as infile:
                    lines = infile.readlines()
                    
                    # positions 개수 세기
                    positions_count = sum(1 for line in lines if 'positions' in line)
                    
                    # 결과 결정
                    if 2 <= positions_count <= 39:
                        result = 'success'
                    else:
                        result = 'fail'
                        
                        # 결과 출력
                        print(f'File: {filename}, Positions: {positions_count}, Result: {result}')
                        
                        # 파일 이름과 결과를 리스트에 추가
                        file_results.append((number, positions_count, result))
                        
                        # fail인 경우 파일을 fail 폴더로 이동
                        if result == 'fail':
                            shutil.move(os.path.join(self.input_path, filename), os.path.join(self.fail_path, filename))

        # 파일 이름과 결과를 정렬하여 CSV 파일에 쓰기
        with open(self.output_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            
            # 헤더 쓰기
            csvwriter.writerow(['filename', 'positions', 'result'])
            
            # 정렬된 파일 이름과 결과 쓰기
            for number, positions_count, result in sorted(file_results, key=lambda x: x[0]):
                csvwriter.writerow([f'path_{number:04d}.txt', positions_count, result])
