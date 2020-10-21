from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import AI.settings as config
import numpy  as np
import json
from PIL import Image
from django.db import models
import random
from .models import *
import os
# Create your views here.
def web_hook(request):
    return render(request, 'web_hook.html')

def ranstr(num):
    # 猜猜变量名为啥叫 H
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    salt = ''
    for i in range(num):
        salt += random.choice(H)

    return salt

def web_hook_request(request):
    img_file = request.FILES['image_file']
    img = np.array(Image.open(img_file))
    my_data = json.dumps({'img':img.tolist()})
    response = requests.post('https://m09dpva23e.execute-api.us-east-1.amazonaws.com/default/hello', \
                             data=my_data, \
                            )
                             #files=request.FILES)
    with open('resp.json','w') as file_object:
        json.dump(response.json(),file_object)
    res_json = response.json()
    try:
        after = np.array( res_json['new_data'])
        print("after shape" ,after.shape)
        imagepath = f'./userimage/{ranstr(8)}.jpg'
        final_img = Image.fromarray(np.uint8(after)).save(os.path.join('media',imagepath))
        #image_data = open(imagepath,"rb").read() 
        uploaded_image = photo(img=imagepath)
        uploaded_image.save()
        print(uploaded_image.img.url)
        response_data = {
            'path': uploaded_image.img.url,
        }
 
    except Exception as e:
        print(e)
        return HttpResponse(bytes.decode(response.content), content_type='application/json')
    return JsonResponse(response_data)#,content_type="image/png")