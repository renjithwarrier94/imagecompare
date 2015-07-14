# Image Compare (Python 3.x)

   This script is meant to take two urls as input and produce a similarity value. The similarity will be given as a value between 0 and 100, whre 0 represent not similar at all, and 100 represents exactly similar.
   This script is based on the Structural Similarity Index(SSIM), provided by the python library, scikit-image.
   
# Usage
## Pre-requsites
   1. Python 3.x
   2. Scipy
   3. Scikit-image
   4. Numpy

## Installation
   1. Clone the Git Repo or download and extract into a folder
   2. Create a virtualenv if needed.
   3. Use pip or similar to install the dependencies from *requirements.txt.*
   4. Run main.py from command line.

# Known Issues
* Cannot handle GIF files
* Solid images does not work always
