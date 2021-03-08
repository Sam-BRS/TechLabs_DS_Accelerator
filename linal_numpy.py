# importing matplotlib modules
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# Read Images
img = mpimg.imread('samurais.jpg')

#print the array
print(img)



# Output Images
plt.imshow(img)
plt.show()