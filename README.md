# Image Compare (Python 3.x)

   This script is meant to take two urls as input and produce a similarity value. The similarity will be given as a value between 0 and 100, where 0 represents distinct images, and 100 represents identical images.
   This script is based on the Structural Similarity Index(SSIM), provided by the python library, scikit-image.
   
# Usage
## Pre-requsites
   1. Python 3.x
   2. Scipy
   3. Scikit-image
   4. Numpy

## Installation
   1. Clone the Git Repo. Alternatively, download and extract into a folder.
   2. Create a virtualenv if required.
   3. Use pip or similar applications to install the dependencies from *requirements.txt.*
   4. Run main.py from command line.
   
# Example
* Example 1
  1. [Black Colour] - http://cdn3.howtogeek.com/wp-content/uploads/2012/12/Plain-Black-Wallpaper.png
  2. [White Colour] - http://mobcup.co/content/jwt/944522

  SSIM = 0.00%
* Example 2
  1. https://lh5.googleusercontent.com/-otxXaCcmkqU/AAAAAAAAAAI/AAAAAAAAAEA/3Ey8OYmb_Ig/photo.jpg
  2. https://lh3.googleusercontent.com/-otxXaCcmkqU/AAAAAAAAAAI/AAAAAAAAAEA/3Ey8OYmb_Ig/s120-c/photo.jpg
  
  SSIM = 97.88%

# Known Issues
* Cannot handle GIF files.
* Solid images does not always work.

