""" Rain pattern for major-tom

"""

class Pixel():
    def __init__(self,  color=Color(0,0,0), brightness=1):
        self.color = color
        self.brightness = brightness


def initpattern(strip, numsteps):
    """ Return a blank pattern of numsteps steps.

    """

    pattern_step = [ [ Pixel(Color(0,0,0)) ] * strip.numPixels() ]
    pattern = [ pattern_step for step in range(numsteps) ]
    return pattern


def display_pattern(strip):
    timestep_ms =  500

    pattern = initpattern(strip, 3)

    # At timestep 2, set pixel at position 5 to white
    pattern[2][5].color=Color(255,255,255)
    for step in pattern:
        for position, pixel in enumerate(step):
            strip.setPixelColor(position, pixel.color)
        strip.show()
        time.sleep(timestep_ms/1000)
