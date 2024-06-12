import re
import csv
import os 

class SGrange:
    def sgrange(default_path):
        data = {"start": [], "goal": []}

        # 입력 경로
        input_path = os.path.join(default_path, "Configuration/startgoal")

        # 출력 경로
        output_path = os.path.join(default_path, "csv")

        # 파일 이름 패턴
        file_pattern = ["start{}.txt", "goal{}.txt"]

        # 열 이름
        columns = ["A", "B", "C", "D", "E", "F"]

        # 파일에서 데이터 추출
        for file_type in file_pattern:
            for i in range(1, 9):
                file_name = file_type.format(i)
                file_path = os.path.join(input_path, file_name)
                last_positions = None  # 마지막으로 찾은 "positions" 값을 저장하기 위한 변수

                with open(file_path, "r") as file:
                    for line in file:
                        match = re.search(r"positions: \[(.*)\]", line)
                        if match:
                            values = match.group(1).split(", ")
                            values = [float(val) for val in values]
                            last_positions = values  # 마지막으로 찾은 "positions" 값 저장

                if last_positions is not None:  # 마지막으로 찾은 "positions" 값이 있는 경우에만 추가
                    if file_type.startswith("start"):
                        data["start"].append(last_positions)
                    elif file_type.startswith("goal"):
                        data["goal"].append(last_positions)

        # 출력 경로 생성
        os.makedirs(output_path, exist_ok=True)

        # CSV 파일 이름
        csv_file = os.path.join(output_path, "sg_range.csv")

        with open(csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            
            # 열 머리글 쓰기
            header = ["type"] + columns
            writer.writerow(header)
            
            # 데이터 쓰기
            for type, values_list in data.items():
                for value_list in values_list:
                    row = [type] + value_list
                    writer.writerow(row)
            
            # 최솟값과 최댓값 행 추가
            for type, values_list in data.items():
                min_values = [min(values) for values in zip(*values_list)]
                max_values = [max(values) for values in zip(*values_list)]
            
            # start와 goal의 최솟값과 최댓값을 변수에 할당
            s_min, s_max = min_values, max_values
            if type == "goal":
                g_min, g_max = min_values, max_values
            
            print(f"success! {csv_file} ")
            print(min_values, max_values)

        # 프로그램을 종료하기 전에 최솟값과 최댓값을 반환
        return s_min, s_max, g_min, g_max

# 기본 경로
default_path = "/home/nishidalab07/github/Robot_path_planning_with_xArm/simulation3/"
s_min, s_max, g_min, g_max = SGrange.sgrange(default_path)
print(f"start_range:{s_min},{s_max}")
print(f"goal_range:{g_min},{g_max}")