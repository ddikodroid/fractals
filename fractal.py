""" 
    Draws fractals given in simplified IFS notation
    Program can be started from terminal as follows:
    python fractal.py -i filename -n num_of_iterations -t drawing_type
    filename - file containing IFS with extension e.g. Sierpinski.ifs
    num_of_iterations - when in chaos mode specifies the number of iterations
    (that is points) that will be drawn; when in recursive mode specifies
    the depth of recursion
    drawing_type - specifies mode: r - recursive (draws fractals as rectangles)
    c - chaos game (draws multiple points)
    
    By: Piotr Sliwa
    17 January 2015 
    Programming assignment 2 for Introduction to Computer Science
"""

import turtle
import argparse
import random
import math
import copy

turt = turtle.Turtle()
turt.hideturtle()
turt.tracer(0,0)
turt.speed(0)

global transformations

def read_IFS(file_name):
    """    
        Reads IFS from file and returns list as follows:
        [number, ref_x, ref_y, [[scale_x, scale_y, shift_x, shift_y, rot_left], [...], ...]
    """
        
    answer = list()
    
    with open(file_name, "r") as handle:
        
        answer.extend([float(x) for x in handle.readline().split()])
        transformations = list()
        for line in handle:
            transformations.append([float(x) for x in line.split()])
	answer.append(transformations)

    return answer
    
def draw_rec(A, B, C, D):
    """ Draws rectangle ABCD """
    turt.penup()
    turt.goto(A)
    turt.pendown()
    turt.goto(B)
    turt.goto(C)
    turt.goto(D)
    turt.goto(A)
    
def draw_point(coordinates):
    """ Draws point at given coordinates """ 
    turt.penup()
    turt.goto(coordinates)
    turt.pendown()
    turt.dot(2)

def transform(scale_x, scale_y, shift_x, shift_y, rot_left, x, y):
    """ Transforms point and returns its new coordinates """ 
    x_dash = math.cos(math.radians(rot_left)) * scale_x * x - math.sin(math.radians(rot_left)) * scale_y * y + shift_x
    y_dash = math.sin(math.radians(rot_left)) * scale_x * x + math.cos(math.radians(rot_left)) * scale_y * y + shift_y
    
    return tuple([x_dash, y_dash])
    
def chaos(n, prob_of, X, Y):
    """ Draws fractal using chaos game """
    for i in range(0, n):
        random_choice = random.random() 
        for which_trans in range(1, len(prob_of)):
            if prob_of[which_trans - 1] < random_choice and random_choice < prob_of[which_trans]: 
                random_choice = which_trans - 1
                break
                
        X, Y = transform(transformations[random_choice][0], transformations[random_choice][1], transformations[random_choice][2], transformations[random_choice][3], transformations[random_choice][4], X, Y)
        draw_point(tuple([X, Y]))
        

def recursive(n, r, trans):
    """ Draws fractal using rectangles """
    rec = copy.deepcopy(r)
    if 0 < n:
        for coord in rec:
            coord[0], coord[1] = transform(trans[0], trans[1], trans[2], trans[3], trans[4], coord[0], coord[1]) # transform all coordinates of a rectangle
        if n - 1 == 0:
            draw_rec(tuple(rec[0]), tuple(rec[1]), tuple(rec[2]), tuple(rec[3]))
        for y in range(0, len(transformations)):	# run recursion for all transformations
            recursive(n-1, rec[:], transformations[y])

parser = argparse.ArgumentParser()

parser.add_argument("-i", type = str, help = "file_name", required = False, default = "test.txt")
parser.add_argument("-n", type = int, help = "number of iterations", required = False, default = 3)
parser.add_argument("-t", type = str, help = "type of drawing: [r]ecursive / [c]haos", required = False, default = "r")

args = parser.parse_args()

file_name = args.i
num_it = args.n
drawing_type = args.t

data = read_IFS(file_name)

reference_rectangle = [[0., 0.], [data[1], 0.], [data[1], data[2]], [0., data[2]]]
transformations = list()
transformations.extend(data[3])

if drawing_type == "r":
    if num_it == 0:
		draw_rec(tuple(reference_rectangle[0]), tuple(reference_rectangle[1]), tuple(reference_rectangle[2]), tuple(reference_rectangle[3]))
    else:
        for y in range(0, len(transformations)):
            recursive(num_it, reference_rectangle, transformations[y])
    
elif drawing_type == "c":
    
    areas = list()
    for trans in transformations:
        areas.append(data[1] * trans[0] * data[2] * trans[1])
        
    sum_of_areas = sum(areas)
    probabilities = list()
    for area in areas:
        probabilities.append(area / sum_of_areas)
    prob_of = [0]           # probability intervals
    last = 0
    for prob in probabilities:
        last += prob
        prob_of.append(last)
    
    chaos(num_it, prob_of, random.uniform(0, data[1]), random.uniform(0, data[2]))
    
else:
    print "Wrong input. Please, restart. "
    
print "Press Enter to end"
raw_input()
