import numpy as np
from sklearn.neighbors import NearestNeighbors
import pandas as pd
#　トレーニングデータの範囲設定：データクレンジング
class Restriction:
    def __init__(self):
        self.ma = []
        self.mb = []
        self.mc = []
        self.md = []
        self.me = []
        self.mf = []

    def find_point(self, x, y, radius):
        points = np.vstack((x, y)).T
        nbrs = NearestNeighbors(n_neighbors=5804).fit(points)
        distances, indices = nbrs.kneighbors(points)

        # 가장 밀집된 지점을 찾기 위해, n_neighbors번째 최근접 이웃의 거리가 가장 작은 점을 찾음
        densest_point_index = np.argmin(distances[:, -1])
        densest_point = points[densest_point_index]

        # 반경 내의 점들을 추출
        radius_indices = nbrs.radius_neighbors([densest_point], radius=radius, return_distance=False)[0]
        return radius_indices
    # ab_indices = self.find_point(self.ma[i-1], self.mb[i-1], radius=0.2) # find_point

    def find_circle(self, x, y, x_r, y_r, radius):
        return (x - x_r) ** 2 + (y - y_r) ** 2 <= radius ** 2

    def restrict_range(self, df):
        combined_filenames_list = []
        
        r = [
            # simulation1
            # [-1.03, -0.52, -0.89, 0.11, 0.53, -0.14], #m1
            # [-0.29, -0.33, -0.69, 0.05, 0.53, -0.19], #m2
            # [-1.53, -0.43, -0.75, 0.08, 0.73, -0.09], #m3
            # [0.06, -0.23, -0.59, 0.03, 0.53, -0.21], #m4
            # [-0.66, -0.42, -0.79, 0.08, 0.53, -0.17], #m5
            # [-1.44, -0.55, -0.91, 0.12, 0.60, -0.11], #m6
            # [-1.62, -0.30, -0.59, 0.03, 0.86, -0.08] #m7

            # simulation2
            [0.37, -0.34, -1.84, 0.45, 1.46, 0.04], #m1
            [0.04, -0.17, -1.12, 0.21, 1.17, 0.09], #m2
            [0.78, -0.25, -2.18, 0.47, 1.34, -0.07], #m3
            [-0.03, -0.10, -0.88, 0.12, 1.04, 0.09], #m4
            [0.20, -0.26, -1.48, 0.33, 1.32, 0.07], #m5
            [0.59, -0.34, -2.12, 0.51, 1.48, 0.00], #m6
            [1.08, -0.11, -2.28, 0.42, 1.13, -0.18] #m7
        ]
        
        for i in range(1, 8): # i = 1, 2, 3
            # Unpack the reference point values
            self.ma.append(df[f'm{i}a'])
            self.mb.append(df[f'm{i}b'])
            self.mc.append(df[f'm{i}c'])
            self.md.append(df[f'm{i}d'])
            self.me.append(df[f'm{i}e'])
            self.mf.append(df[f'm{i}f'])


            # Calculate the Euclidean distance between (m1a, m1b) and each data point in the dataframe
            ab_mask = self.find_circle(self.ma[i-1], self.mb[i-1], r[i-1][0], r[i-1][1], radius=0.3)
            cd_mask = self.find_circle(self.mc[i-1], self.md[i-1], r[i-1][2], r[i-1][3], radius=0.4)
            ef_mask = self.find_circle(self.me[i-1], self.mf[i-1], r[i-1][4], r[i-1][5], radius=0.6)

            # Get the corresponding filenames
            ab_filenames = set(df[ab_mask]['filename'])
            cd_filenames = set(df[cd_mask]['filename'])
            ef_filenames = set(df[ef_mask]['filename'])

            # Combine the filtered filenames that are present in all three sets
            common_filenames = ab_filenames & cd_filenames & ef_filenames
            combined_filenames_list.append(common_filenames)

        # Find the intersection of all combined_filenames
        if combined_filenames_list:
            final_filenames = set.intersection(*combined_filenames_list)
        else:
            final_filenames = set()

        # Filter the dataframe to include only points with the specified filenames
        filtered_rows = df[df['filename'].isin(final_filenames)]
        print(filtered_rows.shape)

        return filtered_rows


# Usage example:
# restriction = Restriction()
# filtered_df = restriction.restrict_range(df)


# if __name__ == "__main__":
#     restrictor = Restriction()
#     restrictor.restrict_range()
