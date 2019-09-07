class RGB:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def __str__(self):
        return "RGB[%d,%d,%d]" % (self.r, self.g, self.b)

red = RGB(255,0,0)
green = RGB(0,255,0)
blue = RGB(0,0,255)

print(red,green,blue)