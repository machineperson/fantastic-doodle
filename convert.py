import argparse
import numpy as np


from PIL import Image

lookup = " .:-=+*#%@"


def image_to_ascii(image, width=128):
    """
    PIL image object -> 2d array of values

    """
    def scale_height(h, w, new_width):
        print "original height: {}".format(h)
        print "original width: {}".format(w)
        print "new width: {}".format(new_width)
        conversion_factor = float(1.0 * new_width / w)
        print "conversion factor {}".format(conversion_factor)
        new_height = (h * conversion_factor) / 2.0
        print "new height: {}".format(new_height)
        return int(new_height)


    quantised = image.quantize(len(lookup))

    #quantised.show()
    array = np.asarray(quantised.resize((width, scale_height(image.height, image.width, width))))

    return array_to_ascii(array) 


def array_to_ascii(array):
    return [[lookup[k] for k in i] for i in array] 


def convert_file(fn, width):
    converted = ""
    try:
        image = Image.open(fn)
        converted = image_to_ascii(image, width)
    except Exception as e:
        print e.message

    return converted



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", 
                        help="Convert this file to ASCII art", 
                        required=True)
    parser.add_argument("-w", "--width", 
                        help="Width of the new image (default 128)", 
                        type=int,
                        default=128)
    args = parser.parse_args()
    print args
    filename = args.filename
    converted = convert_file(filename, args.width)
    print '\n'.join(''.join(i) for i in converted)
