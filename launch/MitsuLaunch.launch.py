from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction

def generate_launch_description():
    return LaunchDescription([
        # Launch Mitsu node first
        Node(
            package='zse_exn_ajr',
            executable='Mitsu',
            output='screen',
        ),

            Node(
                package='turtlesim',
                executable='turtlesim_node',
                name='turtlesim'
            ),
    ])
