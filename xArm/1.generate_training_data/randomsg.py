import random

class RandomCoordinatesGenerator:
    def __init__(self):
        # スタートとゴールの範囲の中から乱数を生成
        # simulation1
        # # start range a~f
        self.a_sr = [-0.1658429916135594, 0.437333859097476]
        self.b_sr = [-0.1399699608363802, -0.0399699608363802]
        self.c_sr = [-0.5099227445917747, -0.306977642700576]
        self.d_sr = [-0.0005763882525579187, 0.0017177637637269413]
        self.e_sr = [0.37220893669441873, 0.8513458438709504]
        self.f_sr = [-0.26514396545471225, 0.43615549942072346]

        # goal range a~f
        self.a_gr = [-2.00000000000, -1.550000000000]
        self.b_gr = [-0.20000000000, -0.100000000000]
        self.c_gr = [-0.69677173590, -0.396771735900]
        self.d_gr = [-0.003813281147, -0.001441490354]
        self.e_gr = [0.37901739020, 1.13743683100]
        self.f_gr = [-0.4641266619, 0.39067986610]

        # simulation2
        # # start range a~f
        # self.a_sr = [-0.4215176695097176, 0.3812938592093262]
        # self.b_sr = [0.10000000000, 0.0000000000000]
        # self.c_sr = [-0.9198909197019524, -0.399447544043225]
        # self.d_sr = [-0.0045485141109748, 0.0123715644599728]
        # self.e_sr = [0.70000000000000, 0.9908187325780036]
        # self.f_sr = [-0.6280545377897786, 0.2210017193588722]

        # # goal range a~f
        # self.a_gr = [1.3500000000000, 1.463283131926562]
        # self.b_gr = [0.000000000000, 0.0292634896919041]
        # self.c_gr = [-2.402771587865023, -2.3597397337209944]
        # self.d_gr = [0.00000000000, 0.7692628705393734]
        # self.e_gr = [0.5250859823064351, 1.2527189482187342]
        # self.f_gr = [-0.40000000000, 0.00000000000]


    def generate_random_coordinates(self):
        start =[
            random.uniform(self.a_sr[0], self.a_sr[1]),
            random.uniform(self.b_sr[0], self.b_sr[1]),
            random.uniform(self.c_sr[0], self.c_sr[1]),
            random.uniform(self.d_sr[0], self.d_sr[1]),
            random.uniform(self.e_sr[0], self.e_sr[1]),
            random.uniform(self.f_sr[0], self.f_sr[1]),
        ]
    
        goal = [
            random.uniform(self.a_gr[0], self.a_gr[1]),
            random.uniform(self.b_gr[0], self.b_gr[1]),
            random.uniform(self.c_gr[0], self.c_gr[1]),
            random.uniform(self.d_gr[0], self.d_gr[1]),
            random.uniform(self.e_gr[0], self.e_gr[1]),
            random.uniform(self.f_gr[0], self.f_gr[1])]
        

        return start, goal

# if __name__ == "__main__":
#     generator = RandomCoordinatesGenerator()

#     # 乱数のスタートとゴールを生成
#     start, goal = generator.generate_random_coordinates()

#     # 出力して確認
#     print("start:", start)
#     print("goal:", goal)
