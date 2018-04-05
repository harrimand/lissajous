from __future__ import print_function

def settings():
    fullScreen()
    pass


# set lobes to a positive odd number less than 26
lobes = 23
cycles = 0
colors = [[255, 128, 255], #Magenta
          [255, 100, 120], #Red
          [255, 255, 64], #Yellow
          [137, 255, 60], #Green
          [255, 160, 60],  #Orange
          [131, 220, 255], #Blue
          [255, 255, 255]  #White
          ]
lisRadius = 0

def setup():
    global lisRadius, px, py
    background(0)
    noSmooth()
    stroke(255, 128, 255)
    lisRadius = .85 * displayHeight / 2
    px, py = xy(0, lisRadius, 1) #set starting point for lissajous
    print("Lissajous Radius: ", lisRadius)
    print("Color: ", colors[cycles % len(colors)], end=" ")    
    print("Drawing {0} by {1} Lissajous".format(lobes, lobes + 2))

def xy(angle, lSize, lobes):
    x1 = lSize * sin(lobes * angle)
    y1 = -lSize * cos((lobes + 2) * angle)
    return (x1, y1)    

x, angle = 0, 0
drawLine = True

def draw():
    global x, px, py, angle, lisRadius, drawLine, cycles, colors, lobes
    translate(width/2, height/2) #Set coordinates to center of window
    
    x1, y1 = xy(angle, lisRadius, lobes) #Polar to Rectangular conversion
    line(px, py, x1, y1) #Plot line from previous point to current point

    px = x1 #save current points as previous points for next line
    py = y1

    if x > 1.0: #If current lissajous complete start erasing
        drawLine = not drawLine
        if not drawLine:
            stroke(0, 0, 0)
        else:   #If done erasing, change color and start drawing
            stroke(colors[cycles % len(colors)][0],
                   colors[cycles % len(colors)][1],
                   colors[cycles % len(colors)][2])
            print("Color: ", colors[cycles % len(colors)], end=" ")
            # Limiting max number of side lobes to 27
            # resetting to 1x3 lissagjous after max size drawn
            #    lissajous will be lobes x (lobes + 2)
            lobes = lobes + 2 if lobes < 26 else 1
            print("Drawing {0} by {1} Lissajous".format(lobes, lobes + 2))
        cycles += 1
        x = 0.0

    if cycles > 64: #Program draws and erases (cycles/2) lissajous
        print("DONE")
        noLoop()
                      
    x += .001 #Each lissagous composed of 1000 line segments
    angle = x * TAU
