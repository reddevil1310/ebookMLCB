"""
This is a demo of creating a pdf file with several pages,
as well as adding metadata and annotations to pdf files.
"""

import datetime
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

# Create the PdfPages object to which we will save the pages:
# The with statement makes sure that the PdfPages object is closed properly at
# the end of the block, even if an Exception occurs.



delta = 0.025

xmin = -5
xmax = 5 
ymin = -5 
ymax = 5 

x = np.arange(xmin, xmax, delta)
y = np.arange(ymin, ymax, delta)
X, Y = np.meshgrid(x, y)
# Z = (X**2 + Y - 7)**2 + (X-Y + 1)**2

# Z = X**2  + Y**2
Z = X**2 - Y**2
# CS = plt.contour(X, Y, Z, np.arange(0.1, 3, .5), colors='k')
# plt.axis('equal')
# plt.xlim(-3, 3)
# plt.ylim(-3, 3)
# plt.axes
# plt.xticks([], [])
# plt.yticks([], [])

# plt.show()

fig, ax = plt.subplots()
# ax.plot(range(10))

# fig.patch.set_visible(False)
ax.axis('off')

frame1 = plt.gca()


filename = 'hyper_2d_2.pdf'
with PdfPages(filename) as pdf:
# with PdfPages('multipage_pdf.pdf') as pdf:
    plt.figure(figsize=(3, 3))
    # plt.plot(range(7), [3, 1, 4, 1, 5, 9, 2], 'r-o')

    # CS = plt.contour(X, Y, Z, np.arange(0.1, 3, .5), colors='k')
    CS = plt.contour(X, Y, Z, np.arange(-5, 5, 1))
    plt.axis('equal')
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.xticks([], [])
    plt.yticks([], [])

    plt.title('$f(x, y) =  x^2 - y^2$ (nonconvex)')
    # plt.axes.get_xaxis().set_visible(False)
    # plt.axes.get_yaxis().set_visible(False)
    plt.axis('off')
    # 
    pdf.savefig(bbox_inches='tight') # saves the current figure into a pdf page
    plt.close()
