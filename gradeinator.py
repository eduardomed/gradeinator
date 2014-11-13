import os
import ud304


def input():
	"""
	Obtain input from user
	"""
	student = raw_input("Please enter the student's name: ")
	evaluator = raw_input("Please enter your name: ")
	course = raw_input("Please enter course code: ")
	file1 = raw_input("Please enter first file path: ")
	file2 = raw_input("Please enter second file path: ")
	file3 = raw_input("Please enter third file path: ")

	return student, evaluator, course, file1, file2, file3

def course_router():
	"""
	Redirect to appropriate course code
	"""
	student, evaluator, course, file1, file2, file3 = input()

	if course == "ud304": 
		#TODO - pass on data to ud304.py
		print "Routing to course code"
	else:
		print "Not a supported course"

def display(): 
	"""
	Display results from course code 
	"""
	pass


def main():
	course_router()

main()

