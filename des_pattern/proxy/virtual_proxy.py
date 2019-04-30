class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f'Loading image from {filename}')

    def draw(self):
        print(f'Drawing image {self.filename}')


class LazyBitmap:  # proxy
    def __init__(self, filename):
        self.filename = filename
        self.bitmap = None

    def draw(self):
        if not self.bitmap:
            self.bitmap = Bitmap(self.filename)
        self.bitmap.draw()


def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing image')


if __name__ == '__main__':
    # bmp = Bitmap('test.jpg')
    # draw_image(bmp)

    bmp = LazyBitmap('facepalm.jpg')  # Bitmap
    draw_image(bmp)
    draw_image(bmp)

# Loading happens only once !!!
# About to draw image
# Loading image from facepalm.jpg
# Drawing image facepalm.jpg
# Done drawing image
# About to draw image
# Drawing image facepalm.jpg
# Done drawing image
