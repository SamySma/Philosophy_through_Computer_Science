# (6)_Image_Manipulation

from graphics import *

window = GraphWin ('Image Manipulation', 1000,1000)

# new_img = Image(Point(500,500), 500, 500)
# # new_img.draw(window)

# img = Image(Point(500,500),'testPic.png')
# # img.draw(window)

# # r, g, b = img.getPixel(250,400)
# # print(r,g,b)

# # for x in range(10):
# #     for y in range(10):
# #         print(img.getPixel(x,y))

# for x in range(500):
#     for y in range(500):
#         new_img.setPixel(x,y,color_rgb(255,0,0))

# new_img.draw(window)
# # new_img.save('testPic2.png')

#new_img = Image(Point(500,250), 250,250)
#inc = 256/250
# for x in range(500):
#     R = int(255-inc*x)
#     G = int(inc*x)
#     B = 0
#     for y in range(500):
#         new_img.setPixel(x, y, color_rgb(R, G, B))

# new_img.save('red-green-gradient.png')

# for y in range(250):
#     R = 0
#     G = int(255-inc*y)
#     B = int(inc*y)
#     for x in range(250):
#         new_img.setPixel(x,y,color_rgb(R,G,B))

# new_img.draw(window)

existin_img = Image(Point(500,500), 'testPic.png')
width = existin_img.getWidth()
height = existin_img.getHeight()
new_img = Image(Point(500,500),width,height)

for x in range(width):
    for y in range(height):
        R,G,B = existin_img.getPixel(x,y)
        average = int((R+G+B)/3)
        new_img.setPixel(x,y, color_rgb(average,average,average))

#new_img.draw(window)

new_img.save('test-bw.png')

window.getMouse()
window.close()

