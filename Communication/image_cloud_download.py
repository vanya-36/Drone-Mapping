from firebase import firebase
import time
import os
import base64
import cv2
import numpy as np

firebase1 = firebase.FirebaseApplication('https://miniproject-3f7c3.firebaseio.com/', None)
result = firebase1.get('/picture', None)
print(type(result))
list1 = []
for x in result:
	list1.append(result[x])
var = list1[0]['img']

jpg_original = base64.b64decode(var)
jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
img = cv2.imdecode(jpg_as_np, flags=1)
print(cv2.imwrite('/Users/vanya/Desktop/mini_proj_ppt/download2.jpg', img))
