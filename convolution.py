#!/usr/bin/python

########################################################
# NAME: Convolution Matrix
# DATE: 09 Apr 2012 
########################################################

# imports
import sys
import os
from PIL import Image
import numpy

def applyConvToImage(img, convMatrix,offset=0):
   #img is an PIL Image object
   #convMatrix is a numpy matrix
   #offset is the value of delta in the formula (in my CN obsv)
   convImg = copy.deepCopy(img)
   sumOfWeights = convMatrix.sum()

   for x in range(img.size[0]):
	  for y in range(img.size[1]):
		 pass
		 #apply conv matrix to 
		 #each pixel
		 #handle boundry conditions
		 convImg.putpixel((x,y),applyConvToNeigh(x, y, convMatrix, offset, sumOfWeights))
		 
   return convImg

def applyConvToNeigh(x, y, convMatrix, offset,sumOfWeights):
   neighList = []
   radius = (convMatrix.shape[0] - 1) / 2
   #find neighbourhood
   #apply weighted convolution

   return newPixelVal


#main function
def main():
   if len(argv) < 3:

	  #insufficient arguments
	  
	  print sys.argv[0] + "usage: " + "$python " + sys.argv[0] + " <input image> <output image>"
	  sys.exit(0)

   #the arguments are passed correctly  
   inputFile = sys.argv[1]
   outputFile = sys.argv[2]
   inputImg = Image.open(inputFile)




if __name__ == "__main__":
   main()
