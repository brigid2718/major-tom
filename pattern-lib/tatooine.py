""" Rain pattern for major-tom

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

def pulsepixel(pattern, beginstep, position, color):
    pulse_duration = 20

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

    for i, step in enumerate(pattern[beginstep+pulse_duration : beginstep+2*pulse_duration]):
        newred = int(red * ((pulse_duration-i)/float(pulse_duration)))
        newgreen = int(green * ((pulse_duration-i)/float(pulse_duration)))
        newblue = int(blue * ((pulse_duration-i)/float(pulse_duration)))

        step[position].color = Color(newred, newgreen, newblue)

def place_droids(step, pos, numPixels):
    """ Place R2 and 3PO on the strip at position 'pos

    """

    r2 = Pixel(Color(0,0,255))
    tpo = Pixel(Color(255,215,0))

    # Place r2 at the location passed to us, place 3PO two pixel ahead
    # (In both cases wrap around if we reach the end)
    step[pos % numPixels()] = r2
    step[pos + 2 % numPixels()] = tpo



def display_pattern(strip):
    print "STARTING PATTERN (stepping through the door loops for 20 seconds)"
    timestep_ms =  60

    pattern = initpattern(strip, 100, Color(255,255,255))
    place_droids(pattern[1], 12, strip.numPixels)

    #import IPython; IPython.embed()
    #sys.exit()

    for step in pattern:
        #print "STEP"
        for position, pixel in enumerate(step):
            strip.setPixelColor(position, pixel.color)
        strip.show()
        time.sleep(timestep_ms/1000.0)
