## Robot Package Template

This is a GitHub template. You can make your own copy by clicking the green "Use this template" button.

It is recommended that you keep the repo/package name the same, but if you do change it, ensure you do a "Find all" using your IDE (or the built-in GitHub IDE by hitting the `.` key) and rename all instances of `my_bot` to whatever your project's name is.

Note that each directory currently has at least one file in it to ensure that git tracks the files (and, consequently, that a fresh clone has direcctories present for CMake to find). These example files can be removed if required (and the directories can be removed if `CMakeLists.txt` is adjusted accordingly).


--> sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-gazebo-ros2-control
--> 
--> ros2 launch articubot robot_gazebo_launch.py world:=/home/invlab/Harsh/ros_ws/src/articubot/worlds/obstacles.world
--> ros2 run teleop_twist_keyboard teleop_twist_keyboard


## ros2_control check commnds 
--> ros2 control list_hardware_interfaces 

## ros2_control commands
--> ros2 launch articubot robot_gazebo_launch.py world:=/home/invlab/Harsh/ros_ws/src/articubot/worlds/obstacles.world
--> ros2 run controller_manager spawner diff_cont
--> ros2 run controller_manager spawner joint_broad
--> ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped
# OR --> after adding spwaner in the launch file 
--> ros2 launch articubot robot_gazebo_launch.py world:=/home/invlab/Harsh/ros_ws/src/articubot/worlds/obstacles.world
--> ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped

## run the bot using gazebo_control 
--> ros2 launch articubot robot_gazebo_launch.py world:=/home/invlab/Harsh/ros_ws/src/articubot/worlds/obstacles.world use_ros2_control:=false
--> ros2 run teleop_twist_keyboard teleop_twist_keyboard
