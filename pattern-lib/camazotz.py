def display_pattern(strip):
    import time
    pixelcount = strip.numPixels()

    def changeallthepixels(color):
        for pixel in range(pixelcount):
            strip.setPixelColor(pixel, color)

    def makepixelsbrighter(color):
        for brightness in range(0,96,2):
            changeallthepixels(color)
            strip.setBrightness(brightness)
            strip.show()
            time.sleep(.05)

    def makepixelsdimmer(color):
        for dimness in range(96,0,-2):
            changeallthepixels(color)
            strip.setBrightness(dimness)
            strip.show()
            time.sleep(.05)

    makepixelsbrighter(Color(0,0,255))
    makepixelsdimmer(Color(0,0,255))
    makepixelsbrighter(Color(0,255,0))
    makepixelsdimmer(Color(0,255,0))
    strip.setBrightness(255)

    pos = 0 # start at the beginning
    dir = 1 # start with a positive direction

    def set_eye(pos):
        strip.setPixelColor(pos - 2, Color(16,0,0))
        strip.setPixelColor(pos - 1, Color(128,0,0))
        strip.setPixelColor(pos    , Color(255,0,0))
        strip.setPixelColor(pos + 1, Color(128,0,0))
        strip.setPixelColor(pos + 2, Color(16,0,0))
    now=time.time()
    timeelapse=0
    while timeelapse <5:
        set_eye(pos)
        strip.show()
        time.sleep(0.05)

            #turn the pixels off
        [strip.setPixelColor(j, Color(0,0,0)) for j in range(pos-2,pos+3,1)]
        strip.show()

        pos += dir

        if pos < 0:
            break
        elif pos >= strip.numPixels():
            pos = strip.numPixels() - 2
            dir = -dir
        timeelapse=int(time.time()-now)

    makepixelsbrighter(Color(0,0,255))
    makepixelsdimmer(Color(0,0,255))
    makepixelsbrighter(Color(0,255,0))
    makepixelsdimmer(Color(0,255,0))
    strip.setBrightness(255)
