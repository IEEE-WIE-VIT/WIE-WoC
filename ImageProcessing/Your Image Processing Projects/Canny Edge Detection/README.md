# Canny Edge Detection

## Overview

The Canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images. 

## Description

The Canny edge detector is arguably the most well known and the most used edge detector in all of computer vision and image processing.
OpenCV provides method to seamlessly implement Canny edge detection over any images using canny() method.

The Canny edge detection algorithm is composed of 5 steps:

 - Noise reduction
 - Gradient calculation
 - Non-maximum suppression
 - Double threshold
 - Edge Tracking by Hysteresis

## How does it works:
 
- Input any images that you want to apply canny edge operation. <br>
- Reading the input images. <br>
- Displaying original images. <br>
- Applying canny() method of OpenCV to detect edges of the input images. <br>
- Displaying the Output image after applying canny edge detection algorithm. <br>

## Screenshots:
    
Original Image

<img src="Images\flower.jpg" width=300 heigth=300/>
  
Canny Edge Detected Image

<img src="Images\demo1.PNG" width=300 height=300/>
  
Original Image

<img src="Images\flower1.jpg" width=300 heigth=300/>
    
Canny Edge Detected Image
  
<img src="Images\demo2.PNG" width=300 height=300/>

## Author

Prathima Kadari
      
