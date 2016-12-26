# import numpy as np
# import math

# def rotation_matrix(axis, theta):
#     """
#     Return the rotation matrix associated with counterclockwise rotation about
#     the given axis by theta radians.
#     """
#     axis = np.asarray(axis)
#     axis = axis/math.sqrt(np.dot(axis, axis))
#     a = math.cos(theta/2.0)
#     b, c, d = -axis*math.sin(theta/2.0)
#     aa, bb, cc, dd = a*a, b*b, c*c, d*d
#     bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
#     return np.array([[aa+bb-cc-dd, 2*(bc+ad), 2*(bd-ac)],
#                      [2*(bc-ad), aa+cc-bb-dd, 2*(cd+ab)],
#                      [2*(bd+ac), 2*(cd-ab), aa+dd-bb-cc]])

# v = [0, 1, 0]
# axis = [1, 0, 0]
# theta = 1.2

# print(np.dot(rotation_matrix(axis,theta), v)) 
from __future__ import print_function
import noise

xoff = 0.0
for x in range(10):
    yoff = 0.0
    for y in range(10):
        print(noise.pnoise2(xoff,yoff), end=" ")
        yoff+=.01
    xoff+=.01
    print()
