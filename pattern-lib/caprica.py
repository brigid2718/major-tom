def display_pattern(strip):
    pos = 0 # start at the beginning
    dir = 1 # start with a positive direction

    def set_eye(pos):
        strip.setPixelColor(pos - 2, Color(16,0,0))
        strip.setPixelColor(pos - 1, Color(128,0,0))
        strip.setPixelColor(pos    , Color(255,0,0))
        strip.setPixelColor(pos + 1, Color(128,0,0))
        strip.setPixelColor(pos + 2, Color(16,0,0))

    while True:
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
