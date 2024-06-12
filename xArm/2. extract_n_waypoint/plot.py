import os
import matplotlib.pyplot as plt
import pandas as pd 

class Plot:
    def plot_all_waypoint(self, df, x, y):
        # jointx, jointy : abcdef ... 중 택 2
        # ex) (jointx, jointy) = (a, b)
        n = 2
        
        row = df.iloc[n]  # n번째 행을 선택합니다.

        x_values = row[[f's{x}', f'm8{x}', f'm4{x}', f'm9{x}', f'm2{x}', f'm10{x}', f'm5{x}', f'm11{x}', f'm1{x}', 
                                f'm12{x}', f'm6{x}', f'm13{x}', f'm3{x}', f'm14{x}', f'm7{x}', f'm15{x}', f'g{x}']].values.flatten()

        y_values = row[[f's{y}', f'm8{y}', f'm4{y}', f'm9{y}', f'm2{y}', f'm10{y}', f'm5{y}', f'm11{y}', f'm1{y}', 
                                f'm12{y}', f'm6{y}', f'm13{y}', f'm3{y}', f'm14{y}', f'm7{y}', f'm15{y}', f'g{y}']].values.flatten()
        # plot
        plt.plot(x_values, y_values, marker='o')
        plt.xlabel(f'Joint {x}')
        plt.ylabel(f'Joint {y}')
        plt.title(f"Waypoint Plot ({x},{y}), {n+1}")
        plt.grid(True)
    
    def plot_one_waypoint(self, df, x, y):
        # x,y : sa, sb, ..., m8a, m8b, ..., ga, ..., gf 중에서, s, m, g의 특정 관절을 선택
        # ex) (x, y) = (m1a, m1b)  

        num_rows = len(df)

        x_values = df[f'{x}'].values
        y_values = df[f'{y}'].values

        #plot
        for i in range(num_rows):
            plt.plot(x_values[i], y_values[i], marker='o')
        plt.xlabel(f'Joint {x}')
        plt.ylabel(f'Joint {y}')
        plt.title(f"Waypoint Plot Joint ({x},{y})")
        plt.grid(True)
    
    def plot_all_window(self, df, X):
        if X == 0:
            # 0 : one path, all waypoint
            plt.subplot(1, 3, 1)
            self.plot_all_waypoint(df, 'a', 'b')

            plt.subplot(1, 3, 2)
            plotter.plot_all_waypoint(df, 'c', 'd')

            plt.subplot(1, 3, 3)
            plotter.plot_all_waypoint(df, 'e', 'f')

            # plot
            plt.tight_layout()
            plt.show()

        else:
            # 1 : one waypoint, all path
            plt.subplot(1, 3, 1)
            plotter.plot_one_waypoint(df, 'm1a', 'm1b')

            plt.subplot(1, 3, 2) 
            plotter.plot_one_waypoint(df, 'm1c', 'm1d')

            plt.subplot(1, 3, 3)
            plotter.plot_one_waypoint(df, 'm1e', 'm1f')

            # plot
            plt.tight_layout()
            plt.show()
            


if __name__ == "__main__":
    default_folder = '/home/nishidalab07/github/Robot_path_planning_with_xArm/simulation3'
    input_file_folder = os.path.join(default_folder, 'csv/samplecheck.csv')

    # csv파일을 데이터프레임에 넣기
    df = pd.read_csv(input_file_folder)

    plotter = Plot()

    # plot all window
    # 0 : one path, all waypoint, 1 : one waypoint, all path
    plotter.plot_all_window(df, 1)