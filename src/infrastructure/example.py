import matplotlib.pyplot as plt

northeast_corner = (-3.0688033002683164, -0.00806945668954697)
northwest_corner = (-1.3309217113663154, -0.00806945668954697)
southwest_corner = (-1.3309217113663154, -0.9032005043073981)
southeast_corner = (-3.0688033002683164, -0.9032005043073981)
# It should really be named c1, c2, c3, c4 (directions are relative)
x = [northeast_corner[0], southwest_corner[0], southeast_corner[0], northwest_corner[0]]
y = [northeast_corner[1], southwest_corner[1], southeast_corner[1], northwest_corner[1]]
colors = ["red", "blue", "yellow", "green"]

plt.scatter(x, y, c=colors)
plt.show()
