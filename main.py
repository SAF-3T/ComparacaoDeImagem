from ctypes import resize
from fastapi import FastAPI, Form
import matplotlib.pyplot as plt
from PIL import Image
# import numpy as np
from imgcompare.imgcompare import image_diff_percent
import requests
from io import BytesIO

app = FastAPI()

@app.post('/comparar/img1/img2')
def comparar_imagens(nomeImg1: str = Form(), nomeImg2: str = Form()):
    
    #Pega imagem da URL do swagger em binário
    binario1 = requests.get('https://backend-saf-api.azurewebsites.net/Img/' + nomeImg1)
    binario2 = requests.get('https://backend-saf-api.azurewebsites.net/Img/' + nomeImg2)
    
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