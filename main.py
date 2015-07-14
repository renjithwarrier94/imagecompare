from urllib.request import urlopen
import numpy as np
from scipy import misc
from skimage.measure import structural_similarity as ssim
import time
import sys


def main():
    # Read URL input
    file1 = open('Image1.jpg', 'wb')
    file2 = open('Image2.jpg', 'wb')
    url1 = input('Enter the URL of the first image, please --> ')
    url2 = input('Enter the URL of the second image, please --> ')
    file1.write(urlopen(url1).read())
    print('First Image has downloaded successfully.')
    file2.write(urlopen(url2).read())
    print('Second Image has downloaded successfully.')
    file1.close()
    file2.close()
    comp()


# Convert to Grayscale
# def greyscale(image)


# Comaprison
def comp():
    image1 = misc.imread('Image1.jpg')
    image2 = misc.imread('Image2.jpg')
    resolution1 = image1.shape[0] * image1.shape[1]
    resolution2 = image2.shape[0] * image2.shape[1]
    if (len(image1.shape) == 3):
        greyscale1 = 0
    else:
        greyscale1 = 1
    if (len(image2.shape) == 3):
        greyscale2 = 0
    else:
        greyscale2 = 1
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

    grey1 = np.zeros((image1.shape[0], image1.shape[1]))  # init 2D numpy array
    print('Converting 1st image to greyscale....')
    #	grey1 = greyscale(image1)
    #	grey2 = greyscale(image2)

    if (greyscale1 == 0):
        count = 0
        for row in range(len(image1)):
            for column in range(len(image1[row])):
                grey1[row][column] = average(image1[row][column])
                count = count + 1
                progress = (count / resolution) * 100
                sys.stdout.write("\r%d%%" % progress)
        misc.imsave('Greyscale1.jpg', grey1)
        sys.stdout.flush()
        grey1 = grey1.astype(np.uint8)
    else:
        print('Image1 is already in Greyscale Format')
        grey1 = image1
        misc.imsave('Greyscale1.jpg', grey1)

    grey2 = np.zeros((image2.shape[0], image2.shape[1]))
    if (greyscale2 == 0):
        print('\n\nConverting 2nd image to greyscale.....')
        count = 0
        for row in range(len(image2)):
            for col in range(len(image2[row])):
                grey2[row][col] = average(image2[row][col])
                count += 1
                progress = (count / resolution) * 100
                sys.stdout.write("\r%d%%" % progress)

        misc.imsave('Greyscale2.jpg', grey2)
        grey2 = grey2.astype(np.uint8)
        print('Conversion Completed!')
    else:
        print('Image2 is already in Greyscale Format')
        grey2 = image2
        misc.imsave('Greyscale2.jpg', grey2)

    print('Comparing images......')
    similarity = ssim(grey1, grey2)
    if(similarity < 0):
        print("\nSecond Image maybe an Inverted version of the first")
    similarity= math.fabs(similarity)
    similarity = similarity * 100
    print('Similarity: ', similarity, '%')
    if (similarity >= 90 and similarity <= 100):
        print("\nImages are very similar")
    elif (similarity >= 75 and similarity < 90):
        print("\nImages are quite similar")
    elif (similarity >= 50 and similarity < 75):
        print("\nImages are vaguely similar")
    elif (similarity >= 25 and similarity < 50):
        print("\nImages have low similarity ")
    elif (similarity >= 1 and similarity < 25):
        print("\nImages have very low similarity")
    else:
        print("\n Images are Different")


# weighted average of image=R*0.299 + G*0.587 + B*0.114 per pixel

def average(pixel):
    return 0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2]


# Calculate Structural Similarity Index
# Check if SSIM>threshold to determine if they are similar


if __name__ == '__main__':
    main()
