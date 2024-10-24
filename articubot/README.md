## Robot Package Template

This is a GitHub template. You can make your own copy by clicking the green "Use this template" button.

It is recommended that you keep the repo/package name the same, but if you do change it, ensure you do a "Find all" using your IDE (or the built-in GitHub IDE by hitting the `.` key) and rename all instances of `my_bot` to whatever your project's name is.

Note that each directory currently has at least one file in it to ensure that git tracks the files (and, consequently, that a fresh clone has direcctories present for CMake to find). These example files can be removed if required (and the directories can be removed if `CMakeLists.txt` is adjusted accordingly).

--> ros2 launch articubot robot_gazebo_launch.py world:=./src/articubot/worlds/obstacles.world
--> ros2 run teleop_twist_keyboard teleop_twist_keyboard to move the bot in both gazebo and rviz
#restart the system if required
-->ros2 launch slam_toolbox online_async_launch.py slam_params_file:=/home/invlab/Harsh/ros_ws/src/articubot/config/mapper_params_online_async.yaml  use_sim_time:=True

## AMCL system for localization 

--> ros2 run nav2_map_server map_server --ros-args -p yaml_filename:=/home/invlab/Harsh/ros_ws/my_map_save.yaml -p use_sim_time:=True
--> ros2 run nav2_util lifecycle_bringup map_server

## navigation commands 
--> ros2 run twist_mux twist_mux --ros-args --params-file ./src/articubot/config/twist_mux.yaml -r cmd_vel_out:=diff_cont/cmd_vel_unstamped
--> ros2 launch nav2_bringup navigation_launch.py use_sim_time:=true
--> ros2 launch articubot robot_gazebo_launch.py world:=./src/articubot/worlds/obstacles.world
--> ros2 run teleop_twist_keyboard teleop_twist_keyboard to move the bot in both gazebo and rviz
#restart the system if required
-->ros2 launch slam_toolbox online_async_launch.py slam_params_file:=/home/invlab/Harsh/ros_ws/src/articubot/config/mapper_params_online_async.yaml  use_sim_time:=True

