def display_pattern(strip, wait_ms=20, color=Color(30,30,255)):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
        strip.setPixelColor(i, Color(0,0,0))
        strip.show()
        time.sleep(wait_ms/1000.0)
        strip.setPixelColor(strip.numPixels()-i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
        strip.setPixelColor(strip.numPixels()-i, Color(0,0,0))
        strip.show()
        time.sleep(wait_ms/1000.0)
