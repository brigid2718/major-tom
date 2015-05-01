def display_pattern(strip):
    pixelcount = strip.numPixels()

    def changeallthepixels(color):
        for pixel in range(pixelcount):
            strip.setPixelColor(pixel, color)

    def makepixelsbrighter(color):
        for brightness in range(16,96,2):
            changeallthepixels(color)
            strip.setBrightness(brightness)
            strip.show()
            time.sleep(.2)

    makepixelsbrighter(Color(0,0,255))
    makepixelsbrighter(Color(0,255,0))
