class Restriction:
    def restrict_range(self, df, reference_point, r):
        # set range
        [ab, cd, ef] = r

        # Unpack the reference point values
        m1a, m1b, m1c, m1d, m1e, m1f = reference_point

        # Calculate the Euclidean distance between (m1a, m1b) and each data point in the dataframe
        # D = distance between point
        df['D_ab'] = ((df['m1a'] - m1a) ** 2 + (df['m1b'] - m1b) ** 2) ** 0.5
        df['D_cd'] = ((df['m1c'] - m1c) ** 2 + (df['m1d'] - m1d) ** 2) ** 0.5
        df['D_ef'] = ((df['m1e'] - m1e) ** 2 + (df['m1f'] - m1f) ** 2) ** 0.5

        # Filter the dataframe to include only points within the specified distance from the reference point
        filtered_rows = df['D_ab'] <= ab
        filtered_rows = df['D_cd'] <= cd
        filtered_rows = df['D_ef'] <= ef

        output = df[filtered_rows]
        print(output.shape)

        return output