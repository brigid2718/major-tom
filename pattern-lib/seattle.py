""" Rain pattern for major-tom

"""

import random
import pdb

class Pixel():
    def __init__(self,  color=Color(0,0,0), brightness=1):
        self.color = color
        self.brightness = brightness


def initpattern(strip, numsteps):
    """ Return a blank pattern of numsteps steps.

    """

    pattern = [ [ Pixel(Color(0,0,0)) for pixel in range(strip.numPixels()) ] for step in range(numsteps) ]
    return pattern

def pulsepixel(pattern, beginstep, position, color, pulse_duration = 20):

    # We need to unpack the color into RGB
    blue = color & 255
    green = (color >> 8) & 255
    red = (color >> 16) & 255

    #TODO: Fix this gross type mess. Ew.
    for i, step in enumerate(pattern[beginstep : beginstep+pulse_duration]):
        newred = int(red * ((i+1)/float(pulse_duration)))
        newgreen = int(green * ((i+1)/float(pulse_duration)))
        newblue = int(blue * ((i+1)/float(pulse_duration)))

    for i, step in enumerate(pattern[beginstep+pulse_duration : beginstep+2*pulse_duration]):
        newred = int(red * ((pulse_duration-i)/float(pulse_duration)))
        newgreen = int(green * ((pulse_duration-i)/float(pulse_duration)))
        newblue = int(blue * ((pulse_duration-i)/float(pulse_duration)))

        step[position].color = Color(newred, newgreen, newblue)

def makeraindrop(pattern, strip, step, start_pos, color=Color(0,0,255), fadetime=4):
    drop_pos = [ (start_pos + i) % strip.numPixels() for i in [0,1,-1,2,-2,3,-3,4,-4] ]
    for pos in drop_pos:
       pulsepixel(pattern, step, pos, color, fadetime)
       # TODO: this shouldn't actually wrap around to step 0
       step = (step + 1)  % len(pattern)

def raindrops(pattern, strip, numdrops=80):
    makeraindrop(pattern, strip, 0, strip.numPixels()/2)
    makeraindrop(pattern, strip, 3, strip.numPixels()/4)
    while (numdrops >0):
        step = random.randrange(len(pattern))
        pos = random.randrange(strip.numPixels())
        r,g,b = (random.randrange(20), random.randrange(50),
                 random.randrange(150,255))
        makeraindrop(pattern, strip, step, pos, color=Color(r,g,b))
        numdrops -= 1


def display_pattern(strip):
    random.seed()
    print "STARTING PATTERN (stepping through the door loops for 20 seconds)"
    timestep_ms =  60

    pattern = initpattern(strip, 100)

    raindrops(pattern, strip, 30)
    for step in pattern:
        print "STEP"
        #print [ id(pixel) for pixel in step ]
        for position, pixel in enumerate(step):
            strip.setPixelColor(position, pixel.color)
            if position == 5:
                print "Pixel Color: %s" % pixel.color
        strip.show()
        time.sleep(timestep_ms/1000.0)
