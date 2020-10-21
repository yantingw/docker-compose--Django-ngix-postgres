import requests
import json

from PIL import Image
import numpy as np

img = np.array(Image.open('./media/favicon.ico')).tolist()
my_data = json.dumps({'img':img})
r = requests.post("https://m09dpva23e.execute-api.us-east-1.amazonaws.com/default/hello",data=my_data)
print(r.status_code)
print(r.json())