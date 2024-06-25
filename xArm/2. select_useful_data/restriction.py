class Restriction:      
        def restrict_range(self, df):
                # #simu1
                # filtered_rows = (0.0<= df['m1a']) & (df['m1a'] <= 0.8)
                # filtered_rows = (-0.4 <= df['m1b']) & (df['m1b'] <= 0.2)
                # filtered_rows = (-2.2 <= df['m1c']) & (df['m1c'] <= -1.6)
                # filtered_rows = (-0.2 <= df['m1d']) & (df['m1d'] <= -0.6)
                # filtered_rows = (0.4 <= df['m1e']) & (df['m1e'] <= 1.2)
                # filtered_rows = (-0.6 <= df['m1f']) & (df['m1f'] <= 0.2)

                # output = df[filtered_rows]

                #simu2
                filtered_rows = (0.0<= df['m1a']) & (df['m1a'] <= 0.8)
                filtered_rows = (-0.4 <= df['m1b']) & (df['m1b'] <= 0.2)
                filtered_rows = (-2.2 <= df['m1c']) & (df['m1c'] <= -1.6)
                filtered_rows = (-0.2 <= df['m1d']) & (df['m1d'] <= -0.6)
                filtered_rows = (0.4 <= df['m1e']) & (df['m1e'] <= 1.2)
                filtered_rows = (-0.6 <= df['m1f']) & (df['m1f'] <= 0.2)

                output = df[filtered_rows]

                return output