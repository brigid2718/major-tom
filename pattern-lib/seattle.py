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

    #TODO: Fix this gross type mess. Ew.
    for i, step in enumerate(pattern[beginstep : beginstep+pulse_duration]):
        step[position].color.red = int(color.red * ((i+1)/float(pulse_duration)))
        step[position].color.green = int(color.green * ((i+1)/float(pulse_duration)))
        step[position].color.blue = int(color.blue * ((i+1)/float(pulse_duration)))


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
