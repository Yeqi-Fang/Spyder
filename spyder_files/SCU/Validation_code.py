import cv2
import numpy as np

a = cv2.imread(r"D:\multi_media\DeskTop\captcha.jpg", 1)
a = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
b = a[:, :, 0] - a[:, :, 1]
b = np.where(b < 0, 0, b)
cv2.imshow('b', b)
cv2.waitKey(0)
cv2.destroyAllWindows()
