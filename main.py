from urllib.request import urlopen
import numpy as np
from scipy import misc
from skimage.measure import structural_similarity as ssim

def main():
# Read URL input
	f1 = open('1.jpg', 'wb')
	f2 = open('2.jpg', 'wb')
	#url1 = input('Enter the URL of the first image, please --> ')
	#url2 = input('Enter the URL of the second image, please --> ')
	#f1.write(urlopen(url1).read())
	f1.write(urlopen('http://cdn1.vox-cdn.com/assets/4229567/game-of-thrones-poster_85627-1920x1200.jpg').read())
	print('First Image has downloaded successfully')
	#f2.write(urlopen(url2).read())
	f2.write(urlopen('http://cdn.playbuzz.com/cdn/54e7fe1b-e96c-485e-b13f-a205635e0642/1dd69c6a-8870-4709-b28e-0d0d21a67500.jpg').read())
	print('Second Image has downloaded successfully')

	f1.close()
	f2.close()
	comp()





# http://cdn1.vox-cdn.com/assets/4229567/game-of-thrones-poster_85627-1920x1200.jpg
# http://cdn.playbuzz.com/cdn/54e7fe1b-e96c-485e-b13f-a205635e0642/1dd69c6a-8870-4709-b28e-0d0d21a67500.jpg
# Convert to Grayscale

def comp():
	image1 = misc.imread('1.jpg')
	image2 = misc.imread('2.jpg')
	res1 = image1.shape[0]*image1.shape[1]
	res2 = image2.shape[0]*image2.shape[1]
	if (res1 != res2):
		if(res1 > res2):
			size = (image2.shape[0], image2.shape[1])
			image1 = misc.imresize(image1, size, interp='bicubic', mode=None)
		else:
			size = (image1.shape[0], image1.shape[1])
			image2 = misc.imresize(image2, size, interp='bicubic', mode=None)	
	grey1 = np.zeros((image1.shape[0], image1.shape[1])) # init 2D numpy array
	print('Converting 1st image to greyscale....')
	for rownum in range(len(image1)):
   		for colnum in range(len(image1[rownum])):
      			grey1[rownum][colnum] = average(image1[rownum][colnum])
	misc.imsave('grey1.jpg', grey1)
	print('Converting 2nd image to greyscale.....')
	grey2 = np.zeros((image2.shape[0], image2.shape[1])) # init 2D numpy array
	for rownum in range(len(image2)):
   		for colnum in range(len(image2[rownum])):
      			grey2[rownum][colnum] = average(image2[rownum][colnum])
	misc.imsave('grey2.jpg', grey2)
	print('Completed!')
	print('Comparing images......')
	s = ssim(grey1, grey2)
	print('SSIM: ', s)


#weighted average of image=R*0.299 + G*0.587 + B*0.114 per pixel

def average(pixel):
    return 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]

# Calculate Structural Similarity Index
# Check if SSIM>threshold to determine if they are similar


if __name__ == '__main__':
    main()
