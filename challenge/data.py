# coding: utf-8

'''
Author: Danish Jaffer
'''

import math

def calcDistance(x1,y1,x2,y2):
	'''
	Distance from Point A to B
	'''
	x = x2-x1
	y = y2-y1

	return math.sqrt(((x**2) + (y**2)))

def openTextFromFile(filename):
	'''
		Open Text and return array each elem for each line of text
	'''
	File = open(filename,"r") 
	text = File.readlines()
	File.close()
	return text


def parseInfo(text):

	''' 
	Gets the information from the file
	'''
	vehicles = {}

	for l in text:
		l = l.replace("\n","")
		values = l.split(",")

		if (values[1] in vehicles):
			if values[2] in vehicles[values[1]]:
				vehicles[values[1]][values[2]].append([values[0],values[2],float(values[3]),float(values[4]),values[5]])
			else:
				vehicles[values[1]][values[2]] = [[values[0],values[2],float(values[3]),float(values[4]),values[5]]]
			if(values[2] == "END_RIDE") :
				
				if "DIST_RIDE" in vehicles[values[1]]:
					i = len(vehicles[values[1]]["DIST_RIDE"])
					vehicles[values[1]]["DIST_RIDE"].append(calcDistance(vehicles[values[1]]["START_RIDE"][i][2],vehicles[values[1]]["START_RIDE"][i][3],vehicles[values[1]]["END_RIDE"][i][2],vehicles[values[1]]["END_RIDE"][i][3]))
				else:
					i = 0
					vehicles[values[1]]["DIST_RIDE"] = [calcDistance(vehicles[values[1]]["START_RIDE"][i][2],vehicles[values[1]]["START_RIDE"][i][3],vehicles[values[1]]["END_RIDE"][i][2],vehicles[values[1]]["END_RIDE"][i][3])]

				if "DIST_DROP" in vehicles[values[1]]:
					i = len(vehicles[values[1]]["END_RIDE"])-1
					vehicles[values[1]]["DIST_DROP"].append(calcDistance(vehicles[values[1]]["DROP"][0][2],vehicles[values[1]]["DROP"][0][3],vehicles[values[1]]["END_RIDE"][i][2],vehicles[values[1]]["END_RIDE"][i][3]))
				else:
					i = 0
					vehicles[values[1]]["DIST_DROP"] = [calcDistance(vehicles[values[1]]["DROP"][0][2],vehicles[values[1]]["DROP"][0][3],vehicles[values[1]]["END_RIDE"][i][2],vehicles[values[1]]["END_RIDE"][i][3])]

		else:
			vehicles[values[1]]={ values[2]:[[values[0],values[2],float(values[3]),float(values[4]),values[5]]] }
	return vehicles




def calc(vehicles):
	'''
	Gets the total dropped vehicles,
	max distance. max distance from inital drop location
	'''
	count = 0
	maxDist = 0
	maxDistDropToEnd = 0
	maxDistDropKey = ""
	maxDistBird = ""
	for key in vehicles:
		if "DROP" in vehicles[key]:
			count += 1
		totalDist = sum(vehicles[key]["DIST_RIDE"])
		if maxDist < totalDist:
			maxDist = totalDist
			maxDistBird = key

		if maxDistDropToEnd < vehicles[key]["DIST_DROP"][-1]:
			maxDistDropKey = key
			maxDistDropToEnd = vehicles[key]["DIST_DROP"][-1]



	return [count,(maxDistDropKey,maxDistDropToEnd),(maxDistBird,maxDist)]

text = openTextFromFile("events.txt")
vehicles = parseInfo(text)
result = calc(vehicles)

print("What is the total number of Bird vehicles dropped off in the simulation?")
print result[0],"\n"
print("Which Bird ends up the farthest away from its drop location? What is the distance?")
print "Bird: ",result[1][0]," - Dist: ",result[1][1],"\n"
print("Which Bird has traveled the longest distance in total on all of its rides? How far is it?")
print "Bird: ",result[2][0]," - Dist: ",result[2][1],"\n"
