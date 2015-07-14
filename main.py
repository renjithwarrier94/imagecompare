from urllib.request import urlopen
import numpy as np
from scipy import misc
from skimage.measure import structural_similarity as ssim
import sys
import math

def main():
	# Reading URL inputs separately
	file1 = open('Image1.jpg', 'wb')
	file2 = open('Image2.jpg', 'wb')
	url1 = input('\nEnter the URL of the first image -->')
	print('\nDownloading First Image...')
	file1.write(urlopen(url1).read())
	print('\nDownload has Completed Successfuly.')
	url2 = input('\nEnter the URL of the second image --> ')
	print('\nDownloading Second Image...')
	file2.write(urlopen(url2).read())
	print('\nDownload has Completed Successfully.')
	file1.close()
	file2.close()

	compare()


# Convert to Grayscale

def greyscale(image, resolution):
	if (len(image.shape) == 3):
		greyscale = 0
	else:
		greyscale = 1

	grey = np.zeros((image.shape[0], image.shape[1]))  # init 2D numpy array
	if (greyscale == 0):
		count = 0
		for row in range(len(image)):
			for column in range(len(image[row])):
				grey[row][column] = average(image[row][column])
				count = count + 1
				progress = (count / resolution) * 100
				sys.stdout.write('\r%d%%' % progress)
		sys.stdout.flush()
		grey = grey.astype(np.uint8)
	else:
		grey = image
		print('100%')
	return grey


# Comaprison Function
def compare():
	image1 = misc.imread('Image1.jpg')
	image2 = misc.imread('Image2.jpg')
	resolution1 = image1.shape[0] * image1.shape[1]
	resolution2 = image2.shape[0] * image2.shape[1]
	if (resolution1 != resolution2):
		if (resolution1 > resolution2):
			size = (image2.shape[0], image2.shape[1])
			image1 = misc.imresize(image1, size, interp='bicubic', mode=None)
		else:
			size = (image1.shape[0], image1.shape[1])
			image2 = misc.imresize(image2, size, interp='bicubic', mode=None)
	if (resolution1 < resolution2):
		resolution = resolution1
	else:
		resolution = resolution2

	print('\nProcessing First Image...\n')
	grey1 = greyscale(image1, resolution)
	print('\n\nProcessing Complete.')
	misc.imsave('Greyscale1.jpg', grey1)
	print('\nProcessing Second Image...\n')
	grey2 = greyscale(image2, resolution)
	misc.imsave('Greyscale2.jpg', grey2)
	print('\n\nProcessing Complete.')

	print('\nComparing Images...')
	similarity = ssim(grey1, grey2)
	if(similarity < 0):
		print("\nSecond Image maybe an Inverted version of the first")
		similarity *= -1
	similarity = similarity * 100
	print('\nSimilarity --> ', similarity, '%')
	if (similarity == 100):
		print('\nThe Images are Same.')
	elif (similarity >= 90):
		print('\nThe Images are Identical.')
	elif (similarity >= 75):
		print('\nThe Images are Similar.')
	elif (similarity >= 50):
		print('\nThe Images are Vaguely Similar.')
	elif (similarity >= 25):
		print('\nThe Images are Slightly Different.')
	elif (similarity >= 1):
		print('\nThe Images are Dissimilar.')
	else:
		print('\nThe Images are Distinct.')


def average(pixel):
	return 0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2]


# Calculate Structural Similarity Index
# Check if SSIM>threshold to determine if they are similar


if __name__ == '__main__':
	main()
