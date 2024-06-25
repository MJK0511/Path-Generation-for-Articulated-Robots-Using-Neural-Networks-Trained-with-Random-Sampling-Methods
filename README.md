# プログラム・コマンドの説明

#gazeboからxArmを実行

roslaunch xarm_gazebo xarm6_beside_table.launch add_gripper:=true

#rviz 実行

roslaunch xarm6_gripper_moveit_config xarm6_gripper_moveit_gazebo.launch

#現在の trajectoryを読み込む

rostopic echo /xarm/xarm6_traj_controller/follow_joint_trajectory/goal > test.txt



## training data(教示データ)の生成

① 障害物、startとgoalの領域設定

② rviz 上でstart、goalの領域 (3次元空間、8つの頂点)のC空間ロボット関節値を抽出

cd /home/nishidalab07/github/Robot_path_planning_with_xArm/simulation[]/Configuration/startgoal

rostopic echo /xarm/xarm6_traj_controller/follow_joint_trajectory/goal > start1.txt

③ 最小値、最大値(範囲)確認  [sg_range.py] # 実行するファイル

④ 範囲が合っているかrvizで視覚化後微調整 [moveonepoint.py]

⑤ 関節値 (A, B, C, D, E, F)の最小値、最大値をstart、goalの領域範囲とし、ランダムな[start, goal]を生成 [randomsg.py] # パラメータ修正必要

⑥ 生成された範囲でRRT*の経路を10000個生成

[generateRRTpath.py] # 実行するファイル

## 1で生成した10000個の経路から希望する経路を通るpath(15waypointで構成)のみ抽出

main.pyで一度に実行可能 

① 失敗したデータを削除し、csvファイルに結果を残す [validate_result.py]

② sample data 100個から15waypointを抽出 [extract_waypoint.py]

ファイルパス : simulation( )/Configuration/originpath/sample

③ 2次元グラフでplotし、希望する経路を通るpathの範囲を設定  [plot.py]

- 15個のwaypointを全て繋いだplot1
- n個のpathの各関節値を表示したplot2

④ 範囲内に存在するpathを全てcsvファイルに保存 : training dataの生成 [restrict_range.py]

⑤ ランダムに100個のテストデータを選択しtest data生成

ファイルパス : simulation( )/Configuration/originpath/sample

## 抽出したpathをMLPで学習 & 学習完了したMLPを利用し3のtest dataでwaypointを推論

[MLP15.py]

活性化関数 : relu

input nodes : 12

hidden nodes : 7 

hidden layers : 5

output nodes : 6

learning rate : 0.001

## waypointのスムージング

## 推論されたwaypointを視覚化

① 4で推論されたwaypointを個別txtファイルに分離 & sg.txt

② Task空間の座標に変換

③ 視覚化

start(red)とgoal(blue)座標を点で表示し、17個の座標を繋ぐ線(green)を表示する。

A. 一つのpathを表示するプログラム

B. 全てのpathを表示するプログラム

## 評価プログラム

評価方法は他の論文を参考にしてもっと考えよう…

[distance.py] 距離を測るプログラム

[time_MLP.py] 時間 : 

# 追加解説

## csvファイルの解説

1. パス /home/nishidalab07/github/Robot_path_planning_with_xArm/simulation3/csv/after

[after_train.csv] : 学習されたMLPから推論されたtest dataのwaypoint結果値 

1. パス /home/nishidalab07/github/Robot_path_planning_with_xArm/simulation3/csv/before

[originpath.csv] : 生成に成功したRRT経路全体のwaypoint値を含む

[samplecheck.csv] : ランダムに選択された100個のsample経路値 (plot後に範囲を限定する際に使用)

[sgrange.csv] : start、goalの座標設定値

[testinput.csv] : 学習完了したMLPを利用し推論するためのtest inputファイル

[traininginput.csv] : MLPを学習するためのtraining input

1. /home/nishidalab07/github/Robot_path_planning_with_xArm/simulation3/csv/evaluation

[result.csv] : 教示データとして生成された10000個のRRT経路の成功、失敗の有無を記録

[time_RRT_test.csv] : 教示データである10000個のRRT経路の生成時間
