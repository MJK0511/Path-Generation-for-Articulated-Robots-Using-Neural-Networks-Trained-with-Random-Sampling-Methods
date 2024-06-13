class Restriction:      
        def restrict_range(self, df):
                # 1. 'm1a' 열의 값이 -1.0 이상인 행 찾기
                filtered_rows = (-1.0 <= df['m1a']) & (df['m1a'] <= -0.5)
                filtered_rows = (0.0 <= df['m1b']) & (df['m1b'] <= 0.5)
                filtered_rows = (-1.2 <= df['m1c']) & (df['m1c'] <= -0.7)
                filtered_rows = (-0.5 <= df['m1d']) & (df['m1d'] <= 0.5)
                filtered_rows = (0.0 <= df['m1e']) & (df['m1e'] <= 1.5)
                filtered_rows = (-0.5 <= df['m1f']) & (df['m1f'] <= 0.5)

                # 전체 행 중에서 필터링된 행만 저장
                output = df[filtered_rows]

                return output