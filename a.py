from imgcompare.imgcompare import image_diff_percent, is_equal

percentage = image_diff_percent("./ImagemComMascara.jpg", "./ImagemSemMascara.jpg")

compatibilidade = 100 - percentage

print(f'A semelhança entre as duas imagens é de: {compatibilidade:.2f}%')