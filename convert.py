import argparse
import numpy as np


from PIL import Image

def image_to_ascii(image, n_colors=3):
    def to_char(c):
        if c == 0:
            return ' '
        elif c == 1:
            return '-'
        else:
            return 'X'
    """
    PIL image object -> 2d array of values

    """
    quantised = image.quantize(n_colors)

    quantised.show()
    array = np.asarray(quantised.resize((128,64)))

    return [[to_char(k) for k in i] for i in array] 



def convert_file(fn):
    converted = ""
    try:
        image = Image.open(fn)
        converted = image_to_ascii(image)
    except Exception as e:
        print e.message

    return converted



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", 
                        help="Convert this file to ASCII art", 
                        required=True)
    args = parser.parse_args()
    print args
    filename = args.filename
    converted = convert_file(filename)
    print '\n'.join(''.join(i) for i in converted)
