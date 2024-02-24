import os
import sys

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='port_name',
                                             default_value='ttyTHS1'),
        launch.actions.DeclareLaunchArgument(name='odom_topic_name',
                                             default_value='odom'),

        launch_ros.actions.Node(
            package='tf2_ros',
            node_executable='static_transform_publisher',
            name='base_link_to_imu',
            arguments="0.0 0.0 0.0 0.0 0.0 0.0 /base_link /imu_link".split(
                ' ')),

        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('limo_base'),
                             'launch/limo_base.launch.py')),
            launch_arguments={
                'port_name':
                launch.substitutions.LaunchConfiguration('port_name'),
                'odom_topic_name':
                launch.substitutions.LaunchConfiguration('odom_topic_name')
            }.items()),

	launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('orbbec_camera'),
                             'launch/dabai.launch.py'))),

	launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('ydlidar_ros2_driver'),
                             'launch/ydlidar_launch.py')))
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
