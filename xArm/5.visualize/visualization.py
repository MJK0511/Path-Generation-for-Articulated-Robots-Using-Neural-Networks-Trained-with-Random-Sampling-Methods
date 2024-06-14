import ast
import os
import rospy
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Pose, Point

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

        # Add red sphere for the first coordinate
        first_pose = self.set_pose(positions_list[0])
        first_marker = Marker()
        first_marker.header.frame_id = "world"
        first_marker.header.stamp = rospy.Time.now()
        first_marker.ns = "end_effector_markers"
        first_marker.id = 0
        first_marker.type = Marker.SPHERE
        first_marker.action = Marker.ADD
        first_marker.pose = first_pose
        first_marker.scale.x = 0.1
        first_marker.scale.y = 0.1
        first_marker.scale.z = 0.1
        first_marker.color.a = 1.0
        first_marker.color.r = 1.0
        first_marker.color.g = 0.0
        first_marker.color.b = 0.0
        marker_array.markers.append(first_marker)

        # Add gray spheres for intermediate coordinates
        intermediate_scale = 0.05
        for i, position in enumerate(positions_list[1:-1]):
            intermediate_pose = self.set_pose(position)
            intermediate_marker = Marker()
            intermediate_marker.header.frame_id = "world"
            intermediate_marker.header.stamp = rospy.Time.now()
            intermediate_marker.ns = "intermediate_markers"
            intermediate_marker.id = i + 1
            intermediate_marker.type = Marker.SPHERE
            intermediate_marker.action = Marker.ADD
            intermediate_marker.pose = intermediate_pose
            intermediate_marker.scale.x = intermediate_scale
            intermediate_marker.scale.y = intermediate_scale
            intermediate_marker.scale.z = intermediate_scale
            intermediate_marker.color.a = 1.0
            intermediate_marker.color.r = 0.5
            intermediate_marker.color.g = 0.5
            intermediate_marker.color.b = 0.5
            marker_array.markers.append(intermediate_marker)

        # Add blue sphere for the last coordinate
        last_pose = self.set_pose(positions_list[-1])
        last_marker = Marker()
        last_marker.header.frame_id = "world"
        last_marker.header.stamp = rospy.Time.now()
        last_marker.ns = "end_effector_markers"
        last_marker.id = len(positions_list)
        last_marker.type = Marker.SPHERE
        last_marker.action = Marker.ADD
        last_marker.pose = last_pose
        last_marker.scale.x = 0.1
        last_marker.scale.y = 0.1
        last_marker.scale.z = 0.1
        last_marker.color.a = 1.0
        last_marker.color.r = 0.0
        last_marker.color.g = 0.0
        last_marker.color.b = 1.0
        marker_array.markers.append(last_marker)

        # Add green line for all coordinates
        marker = Marker()
        marker.header.frame_id = "world"
        marker.header.stamp = rospy.Time.now()
        marker.ns = "end_effector_trajectory"
        marker.id = len(positions_list) + 1
        marker.type = Marker.LINE_STRIP
        marker.action = Marker.ADD
        marker.scale.x = 0.01
        marker.color.a = 1.0
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0

        for i, position in enumerate(positions_list):
            pose = self.set_pose(position)
            marker.points.append(pose.position)

        marker_array.markers.append(marker)
        return marker_array

    def visualize_one_path(self, file_path):
        rospy.init_node("visualize_end_effector_trajectory")

        # 파일에서 위치 데이터를 읽어 리스트에 저장
        with open(file_path) as file:
            positions_list = [ast.literal_eval(line) for line in file]

        # 마커 퍼블리셔
        marker_pub = rospy.Publisher("visualization_one_path", MarkerArray, queue_size=10)
        rospy.sleep(1)  # 퍼블리셔의 셋업 대기

        marker_array = self.append_marker_array(positions_list)
        marker_pub.publish(marker_array)

        rospy.spin()
    
    def visualize_all_path(self, directory_path):
        rospy.init_node("visualize_all_path")

        # 디렉토리 내의 모든 txt 파일 읽기
        file_paths = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith(".txt")]
        marker_pub = rospy.Publisher("visualization_all_path", MarkerArray, queue_size=10)

        # 각 파일별로 좌표 데이터 읽기 및 마커 생성
        for file_path in file_paths:
            with open(file_path) as file:
                positions_list = [ast.literal_eval(line) for line in file]
            marker_array = self.append_marker_array(positions_list)
            marker_pub.publish(marker_array)

        rospy.spin()

