# Visual-Perception

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.txt)

Visual Perception is a High Level Python Library to performs various task under visual recognition.

Currently, It Provides the Solution for Object Detection.

For Detection with pre-trained models it provides:
  - YOLOv4
  - TinyYOLOv4


### Dependencies:
  - tensorflow >= 2.3.0
  - keras
  - opencv-python
  - numpy
  - pillow
  - matplotlib
  - pandas
  - scikit-learn
  - scikit-image
  - imgaug
  - labelme2coco
  - progressbar2
  - scipy
  - h5py
  - configobj

### **`Image Object Detection` Using `YOLOv4`** 

```python
from visual_perception.Detection import Object_Detection

model = Object_Detection()
model.Det_YOLOv4()
model.Detect_From_Image(input_path='car.jpg',
                        output_path='./output_image.jpg')

from PIL import Image
Image.open('output_image.jpg')
```
