#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
	print('=========================================')
	print('s1 [0]')
	print msg.ranges[0]

	print('s2 [90]')
	print msg.ranges[90]

	print('s3 [180]')
	print msg.ranges[180]

	print('s4 [270]')
	print msg.ranges[270]

	print('s5 [359]')
	print msg.ranges[359]

	#If obstacle is at least 0.5m in front of the TB3, the TB3 will move forward
	if msg.ranges[0] > 0.5:
		move.linear.x = 0.5
		move.angular.z = 0.0
	else:
		move.linear.x = 0.0
		move.angular.z = 0.0

	pub.publish(move)

rospy.init_node('obstacle_avoidance')			# Initiate a Node called 'obstacle_avoidance'
sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist)
move = Twist()

rospy.spin()
