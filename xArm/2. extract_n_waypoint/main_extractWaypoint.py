import os

def main(default_folder):
    # RRT로 training data path 생성 직후   
    # 100개의 sample로부터 15개의 positions(configuration 공간의 관절값)를 추출
    extractor = extract_C_all()
    input_folder_path = os.path.join(default_folder, 'Configuration/originpath/sample')
    output_folder_path = os.path.join(default_folder, 'Configuration/extract_angle')
    extractor.process_files_in_directory(input_folder_path, output_folder_path)

default_folder = '/home/nishidalab07/github/6dimension/simulation3'
main(default_folder)