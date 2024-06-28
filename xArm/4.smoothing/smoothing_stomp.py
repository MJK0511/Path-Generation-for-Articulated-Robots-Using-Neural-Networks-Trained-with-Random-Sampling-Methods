import rospy
import sys
import numpy as np
import moveit_commander
from moveit_commander import RobotCommander,MoveGroupCommander
from moveonepoint import MoveOnePoint

moving = MoveOnePoint()

class Smoothing:
    def __init__(self, default_folder):
        self.default_folder = default_folder
        self.times = []

        if not rospy.get_node_uri():
            moveit_commander.roscpp_initialize(sys.argv)
            rospy.init_node('xArm6', anonymous=True)

        # Initialize MoveIt Commander
        self.group = MoveGroupCommander("xarm6")
        self.robot = RobotCommander()
        self.joint_names = self.group.get_active_joints()

        # Get the initial joint values
        self.initial_joint_values = self.group.get_current_joint_values()
        self.group.set_joint_value_target(self.initial_joint_values)

    def smooth_trajectory(self, initial_trajectory):
        # Convert initial trajectory to Eigen::MatrixXd equivalent in Python
        initial_parameters = np.array(initial_trajectory).T
        print("b")
        # Set the start state
        self.group.set_start_state_to_current_state()
        print("c")
        # Plan and execute the trajectory for each point
        for point in initial_parameters:
            # Set joint values for this point
            self.group.set_joint_value_target(point)
            print("d")
            
            # Plan the trajectory
            success, plan, _, _ = self.group.plan()
            if success:
                # Execute the plan
                self.group.execute(plan, wait=True)
            else:
                rospy.logerr("Failed to plan trajectory for point {}".format(point))
                return None

        rospy.loginfo("Trajectory smoothed successfully")
        return initial_trajectory
    

if __name__ == '__main__':
    # Example initial trajectory
    initial_trajectory = [
        [0.038040146298087, -0.0769280764459274, -0.4077942819228193, -0.0001213473923513, 0.4097432863265702, 0.0886203910422125],
        [0.06729300832524007, -0.07582961120017434, -0.39678327753238807, 0.0009775088199725362, 0.5560371038924818, 0.07821308790580603],
        [-0.029236305663450833, -0.15254181284296398, -0.42184378896224645, 0.0020764167580219067, 0.5821731206675016, 0.01140422939279033],
        [-0.10490652605024811, -0.3214202521956596, -0.3838903365127956, -0.021571003642965936, 0.5977436839616364, -0.06275602714978196],
        [-0.26041216842892934, -0.25018969823132636, -0.5242003404085159, -0.010634859475475447, 0.6096002446705733, -0.08239800573980469],
        [-0.30123904150736225, -0.7464124286127375, -0.4697223398453865, -0.09834147200990107, 0.6985544792935987, -0.07126389547595358],
        [-0.4526608129107494, -0.817622469857486, -0.4916796154403728, -0.0968943755008535, 0.7537135547032676, -0.13035341058192026],
        [-0.5854657031014785, -0.8654179064174978, -0.47681489662488863, -0.07339907766649088, 0.7720937904753132, -0.189443913397136],
        [-0.8430510336854411, -0.3687276165802189, -0.8818291208059997, -0.008451813305786468, 0.7501763400386912, -0.19134772114525922],
        [-1.0311189274566543, -1.0726677393343083, -0.5856820544926647, -0.11798392746439526, 0.8795918881703721, -0.2020739367133202],
        [-1.226523392853715, -1.1148741268062152, -0.5207109000124057, -0.014538122120644072, 0.8924493032948762, -0.33069944218331726],
        [-1.368605023756234, -1.0701046183721226, -0.4861760563281453, -0.014552451136348128, 0.891000971402367, -0.37185005296384405],
        [-1.4414182125859987, -0.7940877763830874, -0.49694747655578175, 0.014292108979788404, 0.9142285389680173, -0.7167083362467589],
        [-1.5541082663367334, -0.6669337861044458, -0.5069365047239021, 0.02090543693700181, 0.9118580201066401, -0.7226735066873221],
        [-1.6140881789046508, -0.4092414811924946, -0.537143848317257, -0.0002885224990439722, 0.939161711554749, -0.5719091433728236],
        [-1.6802056373713765, -0.2411759804953516, -0.49376974243400024, -0.0012376615107359823, 0.9119120786769617, -0.49511819321046974],
        [-1.7644230859141348, -0.1141780849147108, -0.4506123225987279, -0.0027639827913145, 1.0321155262220445, -0.2791528546239711]
    ]

    smoother = Smoothing(default_folder=".")
    smoothed_trajectory = smoother.smooth_trajectory(initial_trajectory)
    if smoothed_trajectory:
        rospy.loginfo("Smoothed trajectory: {}".format(smoothed_trajectory))