import graphics
import numpy
import settings

from settings import c
from settings import scale
from settings import length
from settings import width

win = graphics.GraphWin("window", width, length)
for num_y in range(0, length + 1):
    
    y = (num_y/(scale)) - ((length/2)/scale) 
    for num_x in range(0, width + 1):
        count = 0
        check = 0
        x = (num_x/(scale)) - ((width/2)/scale) 

        z = complex(x,y)**2 - c
        while count < 100:
            point = graphics.Point(num_x, num_y)

            z = z**2 - c

            if abs(z) > 1000000000000:

                check = count

                count = 100


            count += 1

        if abs(z) <= 1:
            point.setFill("black")

        elif check > 50:
            point.setFill("red")           
            
        elif check > 40:
            point.setFill("purple")           
            
        elif check > 32:
            point.setFill("blue")
            
        elif check > 26:
            point.setFill("white")

        elif check > 18:
            point.setFill("yellow")

        elif check > 15:
            point.setFill("orange")    
            
        elif check > 12:
            point.setFill("red")
            
        elif check > 9:
            point.setFill("orange")
            
        elif check > 7:
            point.setFill("yellow")

        elif check > 6:
            point.setFill("white")
            
        elif check > 4:
            point.setFill("blue")

        else:
            point.setFill("cyan")

        point.draw(win)
win.postscript(file="image.eps", colormode='color')

from PIL import Image as NewImage
img = NewImage.open("image.eps")




