import cv2
import matplotlib.pyplot as plt
from boxdetect import config
from boxdetect.pipelines import get_boxes
from boxdetect.pipelines import get_checkboxes

file_name = 'test.jpg'

cfg = config.PipelinesConfig()

# important to adjust these values to match the size of boxes on your image
cfg.width_range = (15, 25)
cfg.height_range = (15, 25)
px_threshold = 0.4

# the more scaling factors the more accurate the results but also it takes more time to processing
# too small scaling factor may cause false positives
# too big scaling factor will take a lot of processing time
cfg.scaling_factors = [0.7]

# w/h ratio range for boxes/rectangles filtering
cfg.wh_ratio_range = (0.5, 1.7)

# group_size_range starting from 2 will skip all the groups
# with a single box detected inside (like checkboxes)
cfg.group_size_range = (2, 1)

# num of iterations when running dilation tranformation (to engance the image)
cfg.dilation_iterations = 0

# cfg.autoconfigure_from_vott(vott_dir="E:\dev/vsc_workspace/python/opencv/checkboxdetect/tests/data/autoconfig_simple", class_tags=["box"])

# View boxes
rects, grouping_rects, image, output_image = get_boxes(file_name, cfg=cfg, plot=False)
print(grouping_rects)
plt.figure(figsize=(10, 10))
plt.imshow(output_image)
plt.show()

# View Checkboxes
checkboxes = get_checkboxes(file_name, cfg=cfg, px_threshold=px_threshold, plot=False, verbose=True)
#print("Output object type: ", type(checkboxes))
for checkbox in checkboxes:
    print("Checkbox bounding rectangle (x,y,width,height): ", checkbox[0])
    print("Result of `contains_pixels` for the checkbox: ", checkbox[1])
    if checkbox[1] == True:
        plt.figure(figsize=(3, 3))
        plt.imshow(checkbox[2])
        plt.show()
