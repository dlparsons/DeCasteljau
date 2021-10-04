Written By:		Darryl Parsons
Last Updated: 	Mar. 20th 2021
Language: Python 3.8
--------------------------------------------------------------------------------------------------------------------------------------

Functionallity:
	This program's purpose is to take three or more points and de casteljau's algorithm to form a bezier curve between these points.
The first output is two graphs that presents the bezier curve as its original order of points, and then in the order from least to 
greatest x value. The second output is the solution to problem two for the given four points.
	On the graph the original points are marked with a red x, and the bezier curve is the blue line with each iterated point inidcated
with a blue circle. 
--------------------------------------------------------------------------------------------------------------------------------------

How to use:
	Must install matplotlib.pyplot in Python Interpreter if your IDE doesn't automatically do that. The program runs by itself
but certain elements can be changed:
	rows = 3  # Determines how many points there are
	iterations = 51  # Determines how many iterations are used
	
	After running the program the user has to input the x and y value of three points (by default) seperated by a space.
Thereafter the rest of the program automatcally runs and forms the bezier curves.
--------------------------------------------------------------------------------------------------------------------------------------