import time
import unicornhathd
from sys import exit, argv

unicornhathd.brightness(0.8)

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit('This script requires the pillow module\nInstall with: sudo pip install pillow')


def get_ip():

    my_ip = argv[1]
    print(my_ip)
    return my_ip


def create_image_from_text(in_text):
    colours = (255, 165, 0)
    font_file = '/home/pi/weather/fonts/Herkules.ttf'
    font_size = 16
    font = ImageFont.truetype(font_file, font_size)
    w, h = font.getsize(in_text)

    text_x, text_y = width, 0
    text_width, text_height = width, 0

    text_width += w + width                # add some padding so the ip scrolls off the unicorn hat
    text_height = max(text_height, h, 16)  # no more than the size of the unicorn hat

    image = Image.new('RGB', (text_width, text_height), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.text((text_x, text_y), my_ip, colours, font=font)
    return (image, text_width)


# DISPLAY
def scroll_txt(image, text_width):
    unicornhathd.rotation(0)
    for scroll in range(text_width - width):
        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x + scroll, y))
                r, g, b = [int(n) for n in pixel]
                unicornhathd.set_pixel(width - 1 - x, y, r, g, b)
        unicornhathd.show()
        time.sleep(0.2)
    unicornhathd.off()


# one stop call for scrolling text
def scroll_text(in_txt):
    image, text_width = create_image_from_text(in_txt)
    scroll_txt(image, text_width)


if __name__ == '__main__':
    width, height = unicornhathd.get_shape()  # 16, 16 by default
    my_ip = get_ip()

    scroll_text(my_ip)