""" Rain pattern for major-tom

"""

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

def pulsepixel(pattern, beginstep, position, color):
    pulse_duration = 10

    # We need to unpack the color into RGB
    blue = color & 255
    green = (color >> 8) & 255
    red = (color >> 16) & 255

    #TODO: Fix this gross type mess. Ew.
    for i, step in enumerate(pattern[beginstep : beginstep+pulse_duration]):
        newred = int(red * ((i+1)/float(pulse_duration)))
        newgreen = int(green * ((i+1)/float(pulse_duration)))
        newblue = int(blue * ((i+1)/float(pulse_duration)))

        step[position].color = Color(newred, newgreen, newblue)


def display_pattern(strip):
    print "STARTING PATTERN (stepping through the door loops for 20 seconds)"
    timestep_ms =  500

    pattern = initpattern(strip, 50)

    # At timestep 2, set pixel at position 5 to white
    pattern[2][5].color=Color(255,255,255)
    pulsepixel(pattern, 1, 6, Color(0,255,0))
    #import IPython; IPython.embed()
    for step in pattern:
        print "STEP"
        print [ id(pixel) for pixel in step ]
        for position, pixel in enumerate(step):
            strip.setPixelColor(position, pixel.color)
            if position == 5:
                print "Pixel Color: %s" % pixel.color
        strip.show()
        time.sleep(timestep_ms/1000.0)
