from firebase import firebase
import time
import os
import base64
import cv2
import numpy as np

firebase1 = firebase.FirebaseApplication('https://miniproject-3f7c3.firebaseio.com/', None)
image = cv2.imread(os.path.expanduser('~/Desktop/mini_proj_ppt/mptest_1.png'))
retval,buffer = cv2.imencode(".jpg",image)
string = base64.b64encode(buffer).decode()
dict1 = {'img': string}
#while(1):
#	time.sleep(5)
#
#print(result)
firebase1.post('/picture',data=dict1,params={'mini':'project'})
result = firebase1.get('/picture', None)
print(type(result))
list1 = []
for x in result:
	list1.append(result[x])
var = list1[0]['img']


#ZED cam code