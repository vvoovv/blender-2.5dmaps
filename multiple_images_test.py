modelList = "../models/model_list.txt"

import sys, os
# append the script's directory to the sys.path
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from multiple_images import MultipleImages

# read model file list from modelList
with open(modelList) as f:
	files = [line.rstrip() for line in f]

manager = MultipleImages(
	files = files,
	blenderFilesDir = "../models",
	outputImagesDir = "C:/Users/vvoovv/Documents/MapBox/project/test-2_5dmaps/models",
	angleX = -45,
	angleY = -45,
	csvFile = "../models/models.csv"
)
manager.render()
