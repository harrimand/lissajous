from __future__ import print_function

def settings():
    fullScreen()
    pass

# set lobes to a positive odd number less than 26
lobes = 1

# Display Diagonal Size used to calculate line length
diagInches = 24
# PPI on my monitor is 91.7878

ppi = 0 #Pixels Per Inch calculated in setup
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
    global lisRadius, px, py, ppi
    ppi = sqrt(displayWidth**2 + displayHeight**2) / diagInches
    print("Display Pixels per Inch: {0:.3f}".format(ppi))
    background(0)
    noSmooth()
    stroke(255, 128, 255)
    lisRadius = .85 * displayHeight / 2
    px, py = xy(0, lisRadius, 1) #set starting point for lissajous
    print("Lissajous Radius: {0} pixels. {1:.2f} inches".format(lisRadius, lisRadius/ppi))
    print("Color: ", colors[cycles % len(colors)], end=" ")    
    print("Drawing {0} by {1} Lissajous".format(lobes, lobes + 2), end=" ")

def xy(angle, lSize, lobes):
    x1 = lSize * sin(lobes * angle)
    y1 = -lSize * cos((lobes + 2) * angle)
    return (x1, y1)    

x, angle = 0, 0
drawLine = True
pix = 0

def draw():
    global x, px, py, angle, lisRadius, drawLine, cycles, colors, lobes, pix
    translate(width/2, height/2) #Set coordinates to center of window
    
    x1, y1 = xy(angle, lisRadius, lobes) #Polar to Rectangular conversion
    line(px, py, x1, y1) #Plot line from previous point to current point

    pix += sqrt((x1 - px)**2 + (y1 - py)**2)

    px = x1 #save current points as previous points for next line
    py = y1

    if x > 1.0: #If current lissajous complete start erasing
        drawLine = not drawLine
        if not drawLine:
            stroke(0, 0, 0)
            print("Length: {0:.2f} inches".format(pix / ppi / 2))
            pix = 0
        else:   #If done erasing, change color and start drawing
            stroke(colors[cycles % len(colors)][0],
                   colors[cycles % len(colors)][1],
                   colors[cycles % len(colors)][2])
            print("Color: ", colors[cycles % len(colors)], end=" ")
            # Limiting max number of side lobes to 27
            # resetting to 1x3 lissagjous after max size drawn
            #    lissajous will be lobes x (lobes + 2)
            pix = 0 if lobes > 26 else pix
            lobes = lobes + 2 if lobes < 26 else 1
            print("Drawing {0} by {1} Lissajous".format(lobes, lobes + 2), end=" ")
        cycles += 1
        x = 0.0

    if cycles > 64: #Program draws and erases (cycles/2) lissajous
        print("DONE")
        noLoop()
                      
    x += .001 #Each lissagous composed of 1000 line segments
    angle = x * TAU
