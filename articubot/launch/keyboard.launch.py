from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Parameters for the teleop node can be added here if needed
    teleop_params = os.path.join(get_package_share_directory('articubot'), 'config', 'teleop_params.yaml')

    # Keyboard teleop node
    teleop_keyboard_node = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        name='teleop_keyboard',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}],
        remappings=[('/cmd_vel', '/cmd_vel_keyboard')]
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),
        teleop_keyboard_node,
    ])
