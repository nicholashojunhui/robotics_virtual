#!/usr/bin/env python
import rospy 		#import the python library for ROS
from open_manipulator_msgs.msg import JointPosition	#import JointPosition message from the open_manipulator_msgs.msg package
from open_manipulator_msgs.srv import SetJointPosition	#import SetJointPosition message from the open_manipulator_msgs.srv package
import math

def talker():
	rospy.init_node('OM_publisher')	#Initiate a Node called 'OM_publisher'

	#Create a Service object to change joint positions
	set_joint_position = rospy.ServiceProxy('/goal_joint_space_path', SetJointPosition) 

	#Create a Service object to change gripper position
        set_gripper_position = rospy.ServiceProxy('/goal_tool_control', SetJointPosition)
	
	# Loop until ^c; comment this line if you want the arm to stop at the last joint set
	#while not rospy.is_shutdown():

	#define joint names to assign value to
	joint_position = JointPosition()
	joint_position.joint_name = ['joint1','joint2','joint3','joint4']

	##### Step 1; OM pointed to the front with gripper fully open #####

	##Assigning Joint Position values
	joint_position.position =  [0, 0, 0, 0]		# in radians

	#Send Service Message to OM to change joint positions based on previously defined values
	resp1 = set_joint_position('planning_group',joint_position, 3)
	
	##Assigning Gripper Position value
	gripper_position = JointPosition()
	gripper_position.joint_name = ['gripper']
	gripper_position.position =  [0.01]	# -0.01 for fully close and 0.01 for fully open

	#Send Service Message to OM to change gripper position based on previously defined value
	respg2 = set_gripper_position('planning_group',gripper_position, 3)

	#Delay in between steps
	rospy.sleep(3)

	##### Step 2; shift OM to its left side, gripper still fully open #####
	
	##Assigning Joint Position values
	### To fill in:
	



	##### Step 3a; shift OM down so that target item is in between open gripper #####
	##Assigning Joint Position values
	### To fill in:

	


	##### Step 3b; close gripper to grab target item #####
	##Assigning Gripper Position value
	### To fill in:



	
	##### Step 4; bring target item up #####
	##Assigning Joint Position values
	### To fill in:
	



	##### Step 5; bring target item to the front #####
	##Assigning Joint Position values
	### To fill in:
	joint_position.position =  [0, 0, 0, 0]		# in radians
	resp1 = set_joint_position('planning_group',joint_position, 3)

	rospy.sleep(3)

	##### Step 6; shift OM to its right side #####
	##Assigning Joint Position values
	### To fill in:




	##### Step 7a; bring OM down #####
	##Assigning Joint Position values
	### To fill in:




	##### Step 7b; open gripper to release item #####
	gripper_position.position =  [0.01]	# -0.01 for fully close and 0.01 for fully open
	respg2 = set_gripper_position('planning_group',gripper_position, 3)

	rospy.sleep(3)

	##### bring arm up #####
	joint_position.position =  [-1.571, 0, 0, 0]		# in radians
	resp1 = set_joint_position('planning_group',joint_position, 3)

	rospy.sleep(3)

	##### initial pose #####
	joint_position.position =  [0, 0, 0, 0]		# in radians
	resp1 = set_joint_position('planning_group',joint_position, 3)


if __name__== '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
