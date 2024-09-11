from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.6

def redscreen(main_filename, back_filename):
    image = SimpleImage(main_filename)
    back = SimpleImage(back_filename)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red >= average * INTENSITY_THRESHOLD:
            x = pixel.x
            y = pixel.y
            image.set_pixel(x, y, back.get_pixel(x, y))
    return image 

def main():
    original_stop = SimpleImage('images/stop.png')
    original_stop.show()

    original_leaves = SimpleImage('images/leaves.png')
    original_leaves.show()

    stop_leaves_replaced = redscreen('images/stop.png', 'images/leaves.png')
    stop_leaves_replaced.show()

if __name__ == '__main__':
    main()
