import os
import matplotlib.pyplot as plt
import pandas as pd 

class Plot:
    def __init__(self, default_folder):
        input_path = os.path.join(default_folder, 'csv/before/samplecheck.csv')
        self.df = pd.read_csv(input_path)

    def all_waypoint(self, x, y, k):
        n = k-1
        # jointx, jointy : abcdef ... 중 택 2
        # ex) (jointx, jointy) = (a, b)
        
        row = self.df.iloc[n]  # n번째 행을 선택합니다.

        x_values = row[[f's{x}', f'm8{x}', f'm4{x}', f'm9{x}', f'm2{x}', f'm10{x}', f'm5{x}', f'm11{x}', f'm1{x}', 
                                f'm12{x}', f'm6{x}', f'm13{x}', f'm3{x}', f'm14{x}', f'm7{x}', f'm15{x}', f'g{x}']].values.flatten()

        y_values = row[[f's{y}', f'm8{y}', f'm4{y}', f'm9{y}', f'm2{y}', f'm10{y}', f'm5{y}', f'm11{y}', f'm1{y}', 
                                f'm12{y}', f'm6{y}', f'm13{y}', f'm3{y}', f'm14{y}', f'm7{y}', f'm15{y}', f'g{y}']].values.flatten()
        # plot
        plt.plot(x_values, y_values, marker='o')
        plt.xlabel(f'Joint {x}')
        plt.ylabel(f'Joint {y}')
        plt.title(f"Waypoint Plot ({x},{y}), {k}")
        plt.grid(True)
    
    def one_waypoint(self, x, y):
        # x,y : sa, sb, ..., m8a, m8b, ..., ga, ..., gf 중에서, s, m, g의 특정 관절을 선택
        # ex) (x, y) = (m1a, m1b)  

        num_rows = len(self.df)

        x_values = self.df[f'{x}'].values
        y_values = self.df[f'{y}'].values

        # plot
        for i in range(num_rows):
            plt.plot(x_values[i], y_values[i], marker='o')
        plt.xlabel(f'Joint {x}')
        plt.ylabel(f'Joint {y}')
        plt.title(f"Waypoint Plot Joint ({x},{y})")
        plt.grid(True)

    def plot_one_waypoint(self, n):
        # one path, all waypoint
        plt.subplot(1, 3, 1)
        self.all_waypoint('a', 'b', n)

        plt.subplot(1, 3, 2)
        self.all_waypoint('c', 'd', n)

        plt.subplot(1, 3, 3)
        self.all_waypoint('e', 'f', n)

        # plot
        plt.tight_layout()
        plt.show()

    def plot_all_waypoint(self, m):
        # one waypoint, all path
        plt.subplot(1, 3, 1)
        self.one_waypoint(f'{m}a', f'{m}b')

        plt.subplot(1, 3, 2) 
        self.one_waypoint(f'{m}c', f'{m}d')

        plt.subplot(1, 3, 3)
        self.one_waypoint(f'{m}e', f'{m}f')

        # plot
        plt.tight_layout()
        plt.show()
            

# # if __name__ == "__main__":
#     default_folder = '/home/nishidalab07/github/Robot_path_planning_with_xArm/simulation3'

# #     # csv파일을 데이터프레임에 넣기
#     plotter = Plot(default_folder)

# #     # plot all window
# #     plotter.plot_one_waypoint(5)
#     plotter.plot_all_waypoint('m1')