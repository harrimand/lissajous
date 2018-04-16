# Lissajous drawing by Darrell Harriman harrimand@gmail.com
# Program developed using Processing3 IDE in Python Mode
# Drawing lissajous patterns fullscreen.
# Hit Esc to stop drawing
# Variable lobes sets number of lobes on sides of patterns
# The number of lobes on top and bottom will be lobes + 2
# Variable segLength sets number of segments plotted between screen updates
# Higher segLength value will increase drawing speed
# Colors are changed on each new lissajous pattern drawn
# List of 10,000 x,y point pairs is generated during setup()
# Line segments are drawn between each point pair and the next point pair

from __future__ import print_function

def settings():
    fullScreen()

lobes = 199
segLength = 25

colors = [[0, 0, 0],       #Black
          [255, 128, 255], #Magenta
          [255, 100, 120], #Red
          [255, 255, 64],  #Yellow
          [137, 255, 60],  #Green
          [255, 160, 60],  #Orange
          [131, 220, 255], #Blue
          [255, 255, 255]  #White
          ]

def lis(lobes):
    radius = .85 * displayHeight / 2
    lisPoint = []
    for t in range(10000):
        angle = float(t) / 10000.0 * TAU
        pX = radius * sin(lobes * angle)
        pY = -radius * cos((lobes + 2) * angle)
        lisPoint.append((pX, pY))
    return lisPoint

segment = 0
cS = 1  #color Selection
erase = False  #select Draw/Erase
lP = []  #lissajous Points

def setup():
    global lobes, lP
    lobes = lobes if lobes % 2 == 1 else lobes * 2
    background(0)
    stroke(colors[3][0], colors[3][1], colors[3][2])
    lP = lis(lobes)

def draw():
    global segment, cS, erase
    translate(width/2, height/2)
    
    if erase:
        stroke(0, 0, 0)
        strokeWeight(2)
    else:
        stroke(colors[cS][0], colors[cS][1], colors[cS][2])
        strokeWeight(1)
    
    for i in range(segment, segment + segLength):
        if i < len(lP):
            line(lP[i][0], lP[i][1], lP[(i + 1)%len(lP)][0], lP[(i + 1)%len(lP)][1])
        else:
            erase = ~erase
            cS = (cS + 1) % (len(colors) - 1) + 1 if erase else cS
            segment = -segLength
            break
    segment += segLength

