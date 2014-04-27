modelList = "../models/model_list.txt"

import sys, os
# append the script's directory to the sys.path
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from common_image import CommonImage

# read model file list from modelList
with open(modelList) as f:
	files = [line.rstrip() for line in f]

manager = CommonImage(
	files = files,
	zoomMin = 17,
	zoomMax = 19,
	blenderFilesDir = "../models",
	gdalDir = "C:/Program Files/GDAL",
	angleX = -45,
	angleY = -45,
	outputImagesDir = "../rasters"
)
manager.render()
