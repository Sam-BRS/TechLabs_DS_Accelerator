# importing matplotlib modules
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# Read Images
img1 = mpimg.imread('berlin.jpg')

#print the array
print(img1)

#enhance luminosity
img2 = img1 * 0.75

# show Images
plt.figure(1)
plt.subplot(211)
plt.imshow(img1)

plt.subplot(212)
plt.imshow(img2)
plt.show()
