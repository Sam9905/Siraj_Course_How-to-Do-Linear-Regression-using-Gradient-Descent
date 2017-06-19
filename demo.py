
from numpy import *


def compute_error_for_given_points(b, m, points):
	totalError = 0
	for i in range(0, length(points)):
		x = points[i, 0]
		y = points[i, 1]
		totalError += (y- (m * x + b)) **2
	return totalError / float(len(points))


def step_gradient(b_current, m_current, points, learning_rate)
    #gradient descent
	b_gradient = 0
	m_gradient = 0
	M = float(len(points))
	for i in range(0, len(points)):
		x = points[i,0]
		y = points[i,1]
		b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
		m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
	new_b = b_current - (learning_rate * b_gradient)
	new_m = m_current - (learning_rate * m_gradient)
	return [new_b, new_m]
	

def gradient_descent_runner(points, learning_rate, initial_b, initial_m, num_iterations)
	b = starting_b
	m = starting_m
	
	for i in range(num_iterations):
		b, m = step_gradient(b, m, array(points), learning_rate)
		return [b,m]

def run():
	points = genfromtext('data.csv', delimeter=",")
	#hyperparameters
    learning_rate = 0.0001
	
	#y = mx + b (slope formula)
	initial_b = o
	initial_m = 0
	num_iterations = 1000
	[b, m] = gradient_descent_runner(points, learning_rate, initial_b, initial_m, num_iterations)
	print(b)
	print(m)
	
if__name__ = '__main__':
	run()