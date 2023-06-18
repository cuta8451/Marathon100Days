import requests
import re
import pandas as pd
from PIL import Image
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt

# [作業重點]
# - 從網頁上讀取連結清單 (In[1], In[2])
# - 從清單網址讀取圖片 (In[6]~In[9], Out[6]~Out[9])


# 把連結填入
target_url = 'https://raw.githubusercontent.com/vashineyu/slides_and_others/master/tutorial/examples/imagenet_urls_examples.txt'
response = requests.get(target_url)
data = response.text
print(data)

# 用正規表達式找出字串中所有網址
httpRegex = re.compile(r'http://.+')
httpdata = httpRegex.findall(data)
print(httpdata)


#讀取前五張照片，若連結失效應不會跳出錯誤訊息
try:
    for pic_ in httpdata[0:5]:
        response = requests.get(pic_)
        img = Image.open(BytesIO(response.content))
        # Convert img to numpy array
        plt.imshow(img)
        plt.show()
except:
    print('圖片連結失效')