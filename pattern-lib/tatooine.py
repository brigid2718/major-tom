""" Tatooine pattern for major-tom

"""

import pdb

class Pixel():
    def __init__(self,  color=Color(0,0,0), brightness=1):
        self.color = color
        self.brightness = brightness

    def __str__(self):
        return '%s %s' % (self.color, self.brightness)

def initpattern(strip, numsteps, color = Color(0,0,0)):
    """ Return a blank pattern of numsteps steps.

    """

    pattern = [ [ Pixel(color) for pixel in range(strip.numPixels()) ] for step in range(numsteps) ]
    return pattern

def place_droids(step, pos, numPixels):
    """ Place R2 and 3PO on the strip at position 'pos

    """

    r2 = Pixel(Color(0,0,255))
    tpo = Pixel(Color(255,215,0))

    # Place r2 at the location passed to us, place 3PO two pixel ahead
    # (In both cases wrap around if we reach the end)
    step[pos % numPixels()] = r2
    step[(pos + 2) % numPixels()] = tpo

def modulate_brightness(pattern,  speed=3.0):

    for i, step in enumerate(pattern):
        multip = i%(speed + 1)/speed
        colorvalue = int(255 * multip)
        color = Color(colorvalue, colorvalue, colorvalue)
        print color
        pattern[i] = [ Pixel(color) for s in range(100) ]



def display_pattern(strip):
    #print "STARTING PATTERN (stepping through the door loops for 20 seconds)"
    timestep_ms =  60
    numsteps = 100

    pattern = initpattern(strip, numsteps , Color(255,255,255))
    modulate_brightness(pattern)
    place_droids(pattern[1], 12, strip.numPixels)
    import IPython; IPython.embed(); sys.exit()

    for pos, step in enumerate(pattern):
        place_droids(step, pos, strip.numPixels)
        modulate_brightness(pattern)
        


    for step in pattern:
        #print "STEP"
        for position, pixel in enumerate(step):
            strip.setPixelColor(position, pixel.color)
        strip.show()
        time.sleep(timestep_ms/1000.0)
