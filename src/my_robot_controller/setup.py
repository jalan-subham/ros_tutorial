from setuptools import find_packages, setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jalan',
    maintainer_email='jalan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "node_name = my_robot_controller.first_node:main",
            "draw_circle = my_robot_controller.draw_circle:main",
            "pose_data = my_robot_controller.get_pose_data:main",
            "turtle_control = my_robot_controller.turtle_controller:main"
        ],
    },
)
