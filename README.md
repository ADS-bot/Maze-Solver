# Maze Solver using A* Algorithm

This repository contains Python code to solve a maze using the A* algorithm. The algorithm finds the shortest path from a starting point to an ending point in a given maze image.

## Prerequisites

Before using this code, you need to have the following:

- Python 3.x
- `opencv-python` (`cv2`) library
- `matplotlib` library
- `numpy` library

You can install the required libraries using the following commands:

```bash
pip install opencv-python matplotlib numpy

# Code Explanation
maze_solver.py
This script reads the maze image, defines the source and destination coordinates, and then uses the A* algorithm to find the shortest path. The path is plotted on the image, and the image with the path is displayed.

## Import Libraries
cv2 is the OpenCV library used for image processing.
matplotlib.pyplot is used to display images.
numpy is used to work with arrays.
Read Maze Image
The maze image is read using cv2.imread(). The starting and ending points are defined using pixel coordinates obtained from the provided maze coordinates.

## Define Vertex Class
The Vertex class represents a vertex in the A* algorithm. It contains information about the vertex's coordinates, distance (d) from the source, parent vertex coordinates, and whether it has been processed.

## Define A* Algorithm Functions
heuristic(a, b): Computes the Euclidean distance between two points.
a_star(matrix, source, destination, img): Implements the A* algorithm to find the shortest path from the source to the destination.
get_neighbors(mat, r, c): Returns unprocessed neighboring vertices of a given vertex.
get_distance(img, u, v): Computes the Euclidean distance between two points based on RGB values.
Main Execution
Reads the maze image using cv2.imread().
Sets the source and destination coordinates.
Creates a matrix of Vertex objects for each pixel in the image.
Uses the A* algorithm to find the shortest path.
Plots the path on the image.
Displays the image with the path using matplotlib.pyplot.
## Usage Tips
Ensure the maze image is in the same directory as the script.
Adjust the source and destination coordinates based on the specific maze image.
