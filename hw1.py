#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np
import re
from collections import Counter
from operator import itemgetter

def histogram_times(filename):
    result = []
    with open (filename) as f:
    	readCSV = csv.reader(f, delimiter = ',')
    	for row in readCSV:
    		hour = re.findall(r'(\d+):\d+', row[1])
    		if (len(hour) != 0):
    			if (hour[0].startswith('0')):
    				result.append(int(hour[0][1]))
    			else:
    				result.append(int(hour[0]))
    result = dict(Counter(result))
    return [result[k] for k in sorted(result)][:24]

def weigh_pokemons(filename, weight):
	result = []
	with open (filename) as f:
		data = json.load(f)

		for info in data['pokemon']:
			cur_weight = float(re.findall(r'\d+\.\d+', info['weight'])[0])
			if (weight == cur_weight):
				result.append(info['name'])
	return result

def single_type_candy_count(filename):
   	result = 0
   	with open (filename) as f:
   		data = json.load(f)
   		for info in data['pokemon']:
   			if len(info['type']) == 1:
   				if 'candy_count' in info:
   					result += info['candy_count']
   	return result

def reflections_and_projections(points):
    #reflect over line y = 1
    points[1] = 2 - points[1]
    #rotate the point pi/2 radian around origin
    points = np.array([[0, -1], [1, 0]]) @ points
    #project the point onto y = 3x
    points = np.array([[1, 3], [3, 9]]) @ points
    return points

def normalize(image):
    min_image, max_image = np.amin(image), np.amax(image)
    return 255/(max_image - min_image)*(image - min_image)

def sigmoid_normalize(image, a):
	return 255*(1 + e**(-a** (-1)*(p-128)))**-1
    
