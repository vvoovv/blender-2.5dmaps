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
	zoomMin = 17,
	zoomMax = 19,
	blenderFilesDir = "D:/projects/blender/models",
	outputImagesDir = "C:/Users/vvoovv/Documents/MapBox/project/test-2_5dmaps/models",
	angleX = -45,
	angleY = -45,
	csvFile = "D:/projects/blender/models/models.csv"
)
manager.render()
