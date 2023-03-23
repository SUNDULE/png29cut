import face_recognition
from PIL import Image

image = face_recognition.load_image_file("my_picture.jpg")
face_locations = face_recognition.face_locations(image)#     [(1716, 497, 1824, 390)]
#face_locations = tuple(face_locations)                 #     ((1716, 497, 1824, 390),)
chaibao = list((*face_locations[0],))#上 右 下 左
facelocations_pro = tuple([chaibao[-1]] + chaibao[:-1])


img = Image.open("my_picture.jpg")

face = img.crop(facelocations_pro)#左 上 右 下
face.save("face.jpg")

# print(img.size)
# print(image.size)
#
# print(face_locations)
# print(chaibao)

