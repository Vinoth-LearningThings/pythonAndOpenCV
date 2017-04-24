import numpy

import cv2
from PIL import Image, ImageOps
from hash_utils import Hash

#first_image = Image.open('c.png')
#second_image = Image.open('b.png')

first_image_hasher = Hash('user1576.jpg')
second_image_hasher = Hash('user1575.jpg')

first_image_score = first_image_hasher.ahash()
second_image_score = second_image_hasher.ahash()


s1 =  first_image_hasher.calc_scores()
s2 = second_image_hasher.calc_scores()

vector = []
for h1, h2 in zip(s1, s2):
     vector.append(Hash.calc_difference(h1[1], h2[1]))
#data['is_duplicates'] = Hash.predict(vector)

print Hash.predict(vector)

print int(first_image_score, base=2)

print  int(second_image_score, base=2)

diff = 0
for i in range(len(second_image_score)):
     if first_image_score[i] != second_image_score[i]:
         diff += 1

print diff
