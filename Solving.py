import cv2
import matplotlib.pyplot as plt
import numpy as np
import heapq

class Vertex:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.d = float('inf')
        self.parent_x = None
        self.parent_y = None
        self.processed = False

def heuristic(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def a_star(matrix, source, destination, img):
    pq = []
    source_x, source_y = source
    destination_x, destination_y = destination
    heapq.heappush(pq, (0, (source_x, source_y)))
    matrix[source_y][source_x].d = 0

    while pq:
        _, u = heapq.heappop(pq)
        u_x, u_y = u

        if u_x == destination_x and u_y == destination_y:
            break

        u_vertex = matrix[u_y][u_x]
        u_vertex.processed = True

        neighbors = get_neighbors(matrix, u_y, u_x)
        for v in neighbors:
            if not v.processed:
                dist = get_distance(img, (u_x, u_y), (v.x, v.y))
                new_d = u_vertex.d + dist

                if new_d < v.d:
                    v.d = new_d
                    v.parent_x = u_x
                    v.parent_y = u_y
                    heapq.heappush(pq, (new_d + heuristic((u_x, u_y), destination), (v.x, v.y)))

    path = []
    curr_x, curr_y = destination_x, destination_y
    while curr_x is not None and curr_y is not None:
        path.append((curr_x, curr_y))
        curr_x, curr_y = matrix[curr_y][curr_x].parent_x, matrix[curr_y][curr_x].parent_y

    return path[::-1]

def get_neighbors(mat, r, c):
    shape = mat.shape
    neighbors = []

    # Check if neighboring cells are within bounds and unprocessed
    if r > 0 and not mat[r - 1][c].processed:
        neighbors.append(mat[r - 1][c])
    if r < shape[0] - 1 and not mat[r + 1][c].processed:
        neighbors.append(mat[r + 1][c])
    if c > 0 and not mat[r][c - 1].processed:
        neighbors.append(mat[r][c - 1])
    if c < shape[1] - 1 and not mat[r][c + 1].processed:
        neighbors.append(mat[r][c + 1])

    return neighbors

def get_distance(img, u, v):
    # Calculate the Euclidean distance between u and v based on RGB values
    return np.sqrt(
        (float(img[v[1]][v[0]][0]) - float(img[u[1]][u[0]][0])) ** 2 +
        (float(img[v[1]][v[0]][1]) - float(img[u[1]][u[0]][1])) ** 2 +
        (float(img[v[1]][v[0]][2]) - float(img[u[1]][u[0]][2])) ** 2
    )


# Read the maze image
img = cv2.imread('maze1.1.png')

# Set source and destination coordinates
source = (43, 335)
destination = (288, 325)

# Create a matrix of Vertex objects
imagerows, imagecols = img.shape[0], img.shape[1]
matrix = np.full((imagerows, imagecols), None)
for r in range(imagerows):
    for c in range(imagecols):
        matrix[r][c] = Vertex(c, r)

# Find the path using A*
path = a_star(matrix, source, destination, img)

# Plot the path on the image
for point in path:
    cv2.circle(img, point, 3, (0, 255, 0), -1)

# Display the image with the path
plt.figure(figsize=(7, 7))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
