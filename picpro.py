# 依赖
# pip install baidu-aip
# pip install numpy
# pip install opencv-python

from aip import AipImageProcess
import base64
import numpy as np
import cv2

# 你的 APPID API_KEY SECRET_KEY
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
client = AipImageProcess(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# base64图片解码
def base64_to_image(base64_code):
    # base64解码
    img_data = base64.b64decode(base64_code)
    # 转换为np数组
    img_array = np.frombuffer(img_data, np.uint8)
    # 转换成opencv可用格式
    img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)
    return img

# 图片路径(改成自己的)
img_path = r'E:\Desktop\img.jpg'

ori_img = cv2.imread(img_path)
image = get_file_content(img_path)

# 调用图像无损放大
# img = client.imageQualityEnhance(image)
# 调用黑白图像上色
# img = client.colourize(image)
# 调用图像对比度增强
# img = client.contrastEnhance(image)
# 调用图像清晰度增强
img = client.imageDefinitionEnhance(image)

img = img['image']
show_img = base64_to_image(img)
# imgs = np.hstack([ori_img,show_img])

# 预览
# cv2.imshow('img',imgs)
# 输出
cv2.imwrite('%s.jpg'%(img_path.split('.')[0]+'2'),show_img,[cv2.IMWRITE_JPEG_QUALITY, 100])
