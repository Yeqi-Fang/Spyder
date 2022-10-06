from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import cv2

i = 1
# image = Image.open(f'images/{i}.png')
image = cv2.imread(f'images/{i}.png')
print(np.count_nonzero(np.mean(image[0], axis=1) == 14) / 2)
# sns.histplot(np.mean(image[500], axis=1))
# plt.show()
img = image[:, 735:-735, :]
cv2.imwrite('test2.png', img)
