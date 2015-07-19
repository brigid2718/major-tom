#!/usr/bin/env python

import sys
import time

#class Color():
#    def __init__(self, red, green, blue):
#      self.red, self.green, self.blue = (red, green, blue)
#       
#    def __str__(self):
#        return "[%s %s %s]" % (self.red, self.green, self.blue)

def Color(red, green, blue):
  return (red << 16) | (green << 8) | blue

class Strip():
    def __init__(self, numPixels=30):
      self._numPixels = numPixels
      self.pixels = [ Color(0,0,0) for pixel in range(self._numPixels) ]

    def numPixels(self):
        return self._numPixels

    def setPixelColor(self, n, color):
        self.pixels[n] = color

    def show(self):
        print [ str(p) for p in self.pixels  ]


def testpattern():
    strip = Strip()
    display_pattern(strip)
  
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(1)
    else:
        pattern = sys.argv[1]
        execfile(pattern)
        testpattern()
