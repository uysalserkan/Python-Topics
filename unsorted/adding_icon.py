import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

fix, ax = plt.subplots()

ax.set_xlim([0, 1000])
ax.set_ylim([0, 1000])

X = np.arange(0, 1000)
Y = np.arange(0, 1000)

img1 = plt.imread("baykar_tb2.png")
imgBox = OffsetImage(img1, zoom=0.01)

xy = [300, 300]

ab_img1 = AnnotationBbox(imgBox, xy, xycoords="data",)
ax.add_artist(ab_img1)

ab_img1 = AnnotationBbox(imgBox, [200, 600], xycoords="data",)
ax.add_artist(ab_img1)
ab_img1.xy = [600, 600]
# ax.draw_artist(ab_img1)
# ab_img1.xy = [200, 600]
# print(ab_img1._get_xy)
plt.show()
