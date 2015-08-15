from PIL import Image
import stepic
import sys

filename = sys.argv[1]

img = Image.open (filename).convert(mode='RGB')
encoded_img = stepic.encode_inplace(img, 'BLAH BLAH BLAH')

