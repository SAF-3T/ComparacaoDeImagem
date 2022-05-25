from ctypes import resize
from fastapi import FastAPI, Form, File, UploadFile
import matplotlib.pyplot as plt
from PIL import Image
# import numpy as np
from imgcompare.imgcompare import image_diff_percent
import requests
from io import BytesIO

app = FastAPI()

#img1 = ('./image1.jpg')
# imga = Image.fromarray(np.ones((100, 100, 3), dtype=np.uint8))
# imgb = Image.fromarray(np.ones((100, 100, 3), dtype=np.uint8))
#img2 = ('./image1.jpg')
# img1 = resize(imga, (51, 50))
# img2 = resize(imgb, (50, 50))

@app.post('/comparar/img1/img2')
def comparar_imagens():
    
    #Pega imagem da URL do swagger em binário
    binario1 = requests.get('https://backend-saf-api.azurewebsites.net/Img/imagem1.jpg')
    binario2 = requests.get('https://backend-saf-api.azurewebsites.net/Img/imagem2.jpg')
    
    #Converte a imagem de binário para as propriedades da imagem
    img1 = Image.open(BytesIO(binario1.content))
    img2 = Image.open(BytesIO(binario2.content))
    
    #Formata as duas imagens para o mesmo tamanho 
    rzImg1 = img1.resize((50,50))
    rzImg2 = img2.resize((50,50))
    
    #Percentual de difença entre as duas imagens
    percentage = image_diff_percent(rzImg1, rzImg2)
    
    #Formatação para semelhança das imagens em percentual 
    compatibilidade = 100 - percentage
    
    return {f'{compatibilidade:.2f}%'}
    

    
    
    
# # Opens a image in RGB mode
# im = Image.open(r"C:\Users\System-Pc\Desktop\ybear.jpg")

# # Size of the image in pixels (size of original image)
# # (This is not mandatory)
# width, height = im.size

# # Setting the points for cropped image
# left = 4
# top = height / 5
# right = 154
# bottom = 3 * height / 5

# # Cropped image of above dimension
# # (It will not change original image)
# im1 = im.crop((left, top, right, bottom))
# newsize = (300, 300)
# im1 = im1.resize(newsize)
# # Shows the image in image viewer
# im1.show()
