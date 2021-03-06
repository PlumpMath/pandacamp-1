from Panda import *
# When you create a triangle or rectangle, you can choose which points in texture space each vertex goes with
# In texture space, the lower left corner is P2(0,0) and the upper right is P2(1,1).



# Here are four points in space.  Build two triangles and texture them with realpanda.jpg
p1 = P3(-1, 0, -1)
p2 = P3(1, 0, -1)
p3 = P3(-1, 0, 1)
p4 = P3(1,0, 1)
# For a triangle, the texture points are P2(0,0), P2(1,0), and P2(0, 1).  You can alter
# these by keyword parameters . Create a slider the more the second triangle to the side.
# Change the texP3 coordinate below and see what happens.
m = triangle(p1, p2, p3, texture = "realpanda.jpg")
n = triangle(p3, p4, p2, texture = "realpanda.jpg", texP1 = P2(0, 1), texP2 = P2(1,1), texP3 = P2(1,0), position = P3(slider(), 0, 0))
start()