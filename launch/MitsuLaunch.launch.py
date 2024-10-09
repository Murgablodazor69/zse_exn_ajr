from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            namespace='turtle1'
            executable='turtlesim_node',
            name='sim',
        ),
        Node(
            package='zse_exn_arj',
            executable='Mitsu',
            output='screen',
        ),
    ])