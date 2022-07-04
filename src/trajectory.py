#!/usr/bin/env python

import rospy					#import the python library for ROS
from geometry_msgs.msg import Twist		#import the twist message from the std_msgs package

def talker():
	rospy.init_node('vel_publisher')	#Initiate a Node called 'vel_publisher'
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)	#Create a Publisher object
	move = Twist()				#Create a var named move of type Twist
	rate = rospy.Rate(1)			#Set a publish rate of 0.5 Hz
	while not rospy.is_shutdown():
		move.linear.x = 1
		move.angular.z = 1
		pub.publish(move)
		rate.sleep()

if __name__== '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
