from __future__ import print_function
from PIL import Image
im = Image.open("lexicon2.jpg")
print(im.format, im.size, im.mode)
width_letter = 212
gap_width = 0
start_pos = 40
letters = []
# letters.append((start_pos, 20,start_pos + width_letter, 400))
# letters.append((start_pos + width_letter ,20,start_pos + width_letter+ width_letter,400))

for i in range(0,3):
	letters.append((start_pos + width_letter*i, 20,start_pos + width_letter*(i+1), 400))

region1 = im.crop(letters[0])
region1.show()
region2 = im.crop(letters[1])
region2.show()
region3 = im.crop(letters[2])
region3.show()
print(1336/6)
print(255-40)
print(letters[0])