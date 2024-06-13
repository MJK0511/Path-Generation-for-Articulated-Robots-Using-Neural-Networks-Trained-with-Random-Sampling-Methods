import os
import ast
import rospy
import random
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Pose

class VisualOnePath:
    def set_pose(self, pose_tuple):
        pose = Pose()
        pose.position.x = pose_tuple[0]
        pose.position.y = pose_tuple[1]
        pose.position.z = pose_tuple[2]
        pose.orientation.x = pose_tuple[3]
        pose.orientation.y = pose_tuple[4]
        pose.orientation.z = pose_tuple[5]
        pose.orientation.w = pose_tuple[6]
        return pose

    def append_marker_array(self, positions_list):
        marker_array = MarkerArray()

        for i, position in enumerate(positions_list):
            end_effector_pose = self.set_pose(position)

            marker = Marker()
            marker.header.frame_id = "world"
            marker.header.stamp = rospy.Time.now()
            marker.ns = "end_effector_markers"
            marker.id = i
            marker.type = Marker.SPHERE
            marker.action = Marker.ADD
            marker.pose = end_effector_pose
            marker.scale.x = 0.05
            marker.scale.y = 0.05
            marker.scale.z = 0.05

            # # ランダムな色を生成
            marker.color.a = 1.0
            marker.color.r, marker.color.g, marker.color.b = 1.0, 0.0, 0.0

            marker_array.markers.append(marker)

        return marker_array

    def visualize_trajectory_points(self, file_path):
        while not rospy.is_shutdown():
            rospy.init_node("visualize_end_effector_trajectory")

            # 파일에서 위치 데이터를 읽어 리스트에 저장
            with open(file_path) as file:
                positions_list = [ast.literal_eval(line) for line in file]

            # 마커 퍼블리셔
            marker_pub = rospy.Publisher("visualization_marker_array", MarkerArray, queue_size=10)
            rospy.sleep(1)  # 퍼블리셔의 셋업 대기

            marker_array = self.append_marker_array(positions_list)
            marker_pub.publish(marker_array)

            rospy.spin()
