#launch this launch file --> ros2 launch articubot robot_gazebo_launch.py world:=./src/articubot/worlds/obstacles.world
# and then --> ros2 run teleop_twist_keyboard teleop_twist_keyboard to move the bot in both gazebo and rviz
#restart the system if required 

import os
from ament_index_python.packages import get_package_share_directory
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_path


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node


def generate_launch_description():

    package_name='articubot' 

    urdf_file_path = os.path.join(get_package_share_path('articubot'), 'urdf', 'robot.urdf.xacro')

    rviz_config_path = os.path.join(get_package_share_path('articubot'),'config', 'drive_bot.rviz')

    
    robot_description = ParameterValue(Command(['xacro ', urdf_file_path]), value_type=str)

    robot_state_publisher_node =  Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': robot_description }]
        )
    
#     gazebo_params_file = os.path.join(get_package_share_directory(package_name),'config','gazebo_params.yaml')

    # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
                    # launch_arguments={'extra_gazebo_args': '--ros-args --params-file ' + gazebo_params_file}.items()
             )

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot_1'],
                        output='screen')
    
    rviz2_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d', rviz_config_path]
    )


    # Launch them all!
    return LaunchDescription([
        robot_state_publisher_node,
        gazebo,
        spawn_entity,
        rviz2_node
    ])
