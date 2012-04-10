#!/usr/bin/python

########################################################
# NAME: Convolution Matrix
# DATE: 10 Apr 2012 
########################################################

# imports
import sys
import os
from PIL import Image
import numpy
import math
#import copy

def applyConvToImage(img, convMatrix,offset=0):
   #img is an PIL Image object
   #convMatrix is a numpy matrix
   #offset is the value of delta in the formula (in my CN obsv)
   
   #convImg = copy.deepcopy(img)
   #convImg.putpixel((0,0),(255,255,255))
   #print "Succesful"

   sumOfWeights = convMatrix.sum()
   totalPixels = img.size[0] * img.size[1] 
   count = 0

   for x in range(img.size[0]):
	  for y in range(img.size[1]):
		 #pass
		 #apply conv matrix to each pixel - DONE!
		 #handle boundary conditions - DONE!
		 count += 1
		 img.putpixel((x,y),applyConvToNeigh(img, x, y, convMatrix, offset, sumOfWeights))
		 
		 sys.stdout.write(10*" " + 50*"\b")
		 sys.stdout.write("progress: " + str( float(count) / totalPixels * 100) + "%")
		 sys.stdout.flush()
		 
   return img

def applyConvToNeigh(img, x, y, convMatrix, offset,sumOfWeights):
	neighListR = []
	neighListG = []
	neighListB = []
	radius = (convMatrix.shape[0] - 1) / 2
	
	#flatten convolution matrix into an array
	convArr = numpy.array(convMatrix.flatten())[0]
	
	for yDash in range(y - radius, y + radius + 1):
		neighListR.append([])
		neighListG.append([])
		neighListB.append([])
		for xDash in range(x - radius, x + radius + 1):
			pixelVal = img.getpixel((xDash%img.size[0] ,yDash%img.size[1]))
			neighListR[-1].append(pixelVal[0])
			neighListG[-1].append(pixelVal[1])
			neighListB[-1].append(pixelVal[2])
	
	neighRedArray = numpy.array(numpy.matrix(neighListR).flatten())[0]
	newRedPixelVal = numpy.dot(neighRedArray, convArr) / sumOfWeights + offset;
	if newRedPixelVal > 255:
		newRedPixelVal = 255
	if newRedPixelVal < 0:
		newRedPixelVal = 0
	newRedPixelVal = math.floor(newRedPixelVal)
	
	neighGreenArray = numpy.array(numpy.matrix(neighListG).flatten())[0]
	newGreenPixelVal = numpy.dot(neighGreenArray, convArr) / sumOfWeights + offset;
	if newGreenPixelVal > 255:
		newGreenPixelVal = 255
	if newGreenPixelVal < 0:
		newGreenPixelVal = 0
	newGreenPixelVal = math.floor(newGreenPixelVal)
	
	neighBlueArray = numpy.array(numpy.matrix(neighListB).flatten())[0]
	newBluePixelVal = numpy.dot(neighBlueArray, convArr) / sumOfWeights + offset;
	if newBluePixelVal > 255:
		newBluePixelVal = 255
	if newBluePixelVal < 0:
		newBluePixelVal = 0
	newBluePixelVal = math.floor(newBluePixelVal)
	
	return (int(newRedPixelVal), int(newGreenPixelVal), int(newBluePixelVal))

#main function
def main():
   if len(sys.argv) < 3:
	  #insufficient arguments
	  print sys.argv[0] + "usage: " + "$python " + sys.argv[0] + " <input image name> <output image name>"
	  sys.exit(0)

   #the arguments are passed correctly  
   inputFile = sys.argv[1]
   outputFile = sys.argv[2]
   inputImg = Image.open(inputFile)
   convMatrix = numpy.matrix([[2,3,2],[-1,1,-3],[3,-1,2]])
   
   print "Disclaimer: This is an inefficient code. So, it WILL take a relatively long time to run."
   print "Convolution Matrix:"
   print convMatrix
   print "Applying convolution"
   
   outputImg = applyConvToImage(inputImg, convMatrix, 0)
   outputImg.save(outputFile)
   
   print "Image saved as " + outputFile


if __name__ == "__main__":
   main()