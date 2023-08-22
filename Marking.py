import cv2
import matplotlib.pyplot as plt

# Read the maze image
img = cv2.imread('maze1.1.png')

# Define the pixel coordinates for the starting and ending points
starting_point = (43, 335)

ending_point = (288, 325)

# Mark the starting and ending points on the image
cv2.circle(img, starting_point, 3, (255, 0, 0), -1)  # Blue circle for starting point
cv2.circle(img, ending_point, 3, (0, 0, 255), -1)    # Red circle for ending point

# Display the image with the marked points
plt.figure(figsize=(7, 7))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
