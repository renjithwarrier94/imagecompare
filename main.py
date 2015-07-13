from urllib.request import urlopen
import numpy as np


def main():
# TODO: Read URL input
	f1 = open('1.jpg', 'wb')
	f2 = open('2.jpg', 'wb')
	url1 = input('Enter the URL of the first image, please --> ')
	url2 = input('Enter the URL of the second image, please --> ')
	f1.write(urlopen(url1).read())
	print('First Image has downloaded successfully')
	f2.write(urlopen(url2).read())
	print('Second Image has downloaded successfully')

	f1.close()
	f2.close()



# http://cdn1.vox-cdn.com/assets/4229567/game-of-thrones-poster_85627-1920x1200.jpg
# http://cdn.playbuzz.com/cdn/54e7fe1b-e96c-485e-b13f-a205635e0642/1dd69c6a-8870-4709-b28e-0d0d21a67500.jpg
# TODO: Convert to Grayscale

#weighted average of image=R*0.299 + G*0.587 + B*0.114 per pixel

def average(pixel):
    return 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]

# TODO: Calculate Structural Similarity Index
# TODO: Check if SSIM>threshold to determine if they are similar


if __name__ == '__main__':
    main()
