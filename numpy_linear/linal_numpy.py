# importing matplotlib modules
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# Read Images
img1 = mpimg.imread('berlin.jpg')
img1 = img1 / np.array([255,255,255])
#print info of the array
print(img1)
print(img1.shape)

#enhance luminosity
coef = np.array([0.8, 0.8, 0.8])
img2 = img1 / coef
print(img2)
print(img2.shape)

#make less redish
coef_red = np.array([0.75, 1, 1])
img3 = img2 * coef_red

#add some blue to make it more cold
coef_blue = np.array([1, 1, 1.2])
img4 = img3 * coef_blue

# show Images
plt.figure(1)
plt.subplot(221)
plt.imshow(img1)

plt.subplot(222)
plt.imshow(img2)

plt.subplot(223)
plt.imshow(img3)

plt.subplot(224)
plt.imshow(img4)

plt.show()
