import os
import csv
import numpy as np

class Distance:
    def calculate_distance(self, point1, point2):
        point1 = np.array(point1[:3])
        point2 = np.array(point2[:3])
        distance = np.linalg.norm(point1 - point2)
        return distance

    def calculate_total_distance(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # 대괄호 및 'E' 대문자로 변환하여 부동 소수점으로 변환
        points = [list(map(lambda x: float(x.replace('[', '').replace(']', '').replace('e', 'E')), line.strip().split(','))) for line in lines]

        distances = [self.calculate_distance(points[i], points[i+1]) for i in range(len(points)-1)]
        # print(distances)
        total_distance = sum(distances)

        return total_distance

    def calculate_total_distances_in_folder(self, folder_path):
        file_list = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        total_distances = []
        for file_name in file_list:
            file_path = os.path.join(folder_path, file_name)
            total_distance = self.calculate_total_distance(file_path)
            total_distances.append((file_name, total_distance))
        return total_distances

    def calculate_mean_and_variance(self, distances):
        mean_distance = np.mean(distances)
        variance_distance = np.var(distances)
        return mean_distance, variance_distance

    def save_to_csv(self, result, csv_file_path):
        with open(csv_file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['File Name', 'Total Distance'])
            csv_writer.writerows(result)
        
        print(f"Results saved to {csv_file_path}")

    def calculate(self,folder_path, csv_file_path):
        result = self.calculate_total_distances_in_folder(folder_path)
        
        # 총 거리 리스트 추출
        total_distances = [distance for _, distance in result]
        
        # 평균 및 분산 계산
        mean_distance, variance_distance = self.calculate_mean_and_variance(total_distances)
        
        # 결과에 평균 및 분산 추가
        result.append(('Average', mean_distance))
        result.append(('Variance', variance_distance))
        
        self.save_to_csv(result, csv_file_path)
        

# 주어진 폴더의 경로
default_folder = '/home/nishidalab07/github/Robot_path_planning_with_xArm/simulation1'
# input_path = os.path.join(default_folder, 'Task/beforesample') # RRT* sample 100 
input_path = os.path.join(default_folder, 'Task/aftertrain/point') # after train 100 # all, point, area
output_path = os.path.join(default_folder, 'csv/evaluation/distance_train.csv')


calculator = Distance()
calculator.calculate(input_path, output_path)

