import random
from sg_range import SGrange 

class RandomCoordinatesGenerator:
    def __init__(self):
        #simulation1
        # start range a~f
        self.a_sr = [-0.4569210738, 0.4467361857]
        self.b_sr = [-0.330376887, 0.1727778313]
        self.c_sr = [-0.6099227446, -0.06732848964]
        self.d_sr = [-0.001551473737, 0.001717763764]
        self.e_sr = [0.3722089367, 0.831491059]
        self.f_sr = [-0.4561402356, 0.4468273788]

        # goal range a~f
        self.a_gr = [-1.9000000000, -1.3000000000]
        self.b_gr = [-0.200000000, 0.1739460607]
        self.c_gr = [-0.6967717359, -0.1090631356]
        self.d_gr = [-0.003813281147, -0.001441490354]
        self.e_gr = [0.3790173902, 1.137436831]
        self.f_gr = [-0.4641266619, 0.3906798661]


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

if __name__ == "__main__":
    # 주어진 범위
    # 객체 생성
    generator = RandomCoordinatesGenerator()

    # 랜덤 좌표 생성
    start, goal = generator.generate_random_coordinates()

    # 출력
    print("start:", start)
    print("goal:", goal)
