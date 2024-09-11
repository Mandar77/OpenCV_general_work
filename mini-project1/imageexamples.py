from simpleimage import SimpleImage

def darker(image):
    for pixel in image:
        pixel.red = pixel.red // 2
        pixel.green = pixel.green // 2
        pixel.blue = pixel.blue // 2

def red_channel(filename):
    image = SimpleImage(filename)
    for pixel in image:
        pixel.green = 0
        pixel.blue = 0
    return image

def right_half_darker(filename):
    image = SimpleImage(filename)
    for pixel in image:
        if pixel.x >= image.width // 2:
            pixel.red *= 0.5
            pixel.green *= 0.5
            pixel.blue *= 0.5
    return image

def compute_luminosity(red, green, blue):
    return (0.299 * red) + (0.587 * green) + (0.114 * blue)

def grayscale(filename):
    image = SimpleImage(filename)
    for pixel in image:
        gray = (pixel.red + pixel.green + pixel.blue) / 3
        pixel.red = gray
        pixel.green = gray
        pixel.blue = gray
    return image

def main():
    flower = SimpleImage('images/flower.png')
    #flower.show()

    #darker(flower)
    #flower.show()

    #red_flower = red_channel('images/flower.png')
    #red_flower.show()

    #right_half_darker_flower = right_half_darker('images/flower.png')
    #right_half_darker_flower.show()

    grayscale_flower_avg = grayscale('images/flower.png')
    grayscale_flower_avg.show()

if __name__ == '__main__':
    main()
