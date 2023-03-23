'''
将输入的png格式图片进行9宫格切分并拼接
    可以识别选取图中人脸部分进行操作
'''
from PIL import Image, ImageOps
import os.path
from pathlib import Path
from glob import glob
import os
import face_recognition



def mkdir(path):
    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)
        print("---  new folder...  ---")
        print("---  OK  ---")
    else:
        print("---  There is this folder!  ---")


folder_path = "C:\\Users\\13966\\OneDrive\\桌面\\画图viso\\"
filename_pattern = '*-*-*.png'

file_paths = glob(os.path.join(folder_path,filename_pattern))
names =[]

for file_path in file_paths:
    origionfilename = os.path.basename(file_path)
    filename = origionfilename[:2]
    partnames =filename

    names.append(partnames)

named = set(names)

klist = [1,2]
vlist = [1,2,3,4,5,6,7,8]


for name in named:
    for kk in klist:
        mkdir(f"C:\\Users\\13966\\OneDrive\\桌面\\画图viso\\BIG-{name}-{kk}\\")
        mkdir(f"C:\\Users\\13966\\OneDrive\\桌面\\画图viso\\FACE-{name}-{kk}\\")
        for vv in vlist:
            origionimage = face_recognition.load_image_file(f"C:\\Users\\13966\\OneDrive\\桌面\\画图viso\\{name}-{kk}-{vv}.png")
            face_locations = face_recognition.face_locations(origionimage)
            chaibao = list((*face_locations[0],))#拆包
            facelocations_pro = tuple([chaibao[-1]] + chaibao[:-1])

            image = Image.open(f"C:\\Users\\13966\\OneDrive\\桌面\\画图viso\\{name}-{kk}-{vv}.png")
            face = image.crop(facelocations_pro)
            face.save(f'C:\\Users\\13966\\OneDrive\\桌面\\画图viso\\FACE-{name}-{kk}\\FACE-{name}-{kk}-{vv}.png')

            width, height = face.size
            cell_width, cell_height = width // 3, height // 3


            #搞个空白大图顺便再扩大2倍大小
            big_image_width = (cell_width * 3 + 2) * 2
            big_image_height = (cell_height *3 + 2) * 2
            big_image = Image.new('RGBA', (big_image_width, big_image_height), 'white')

            #切分处理然后合并
            for row in range(3):
                for col in range(3):
                    # 计算子图滴位置
                    x0, y0 = col * cell_width, row * cell_height
                    x1, y1 = x0 + cell_width, y0 + cell_height

                    # 获取子图然后添加边框
                    cell = face.crop((x0, y0, x1, y1))
                    cell = cell.resize((cell_width * 2 - 2, cell_height * 2 - 2))#这里乘以2是要放大2倍
                    cell = ImageOps.expand(cell, border=2, fill='white')

                    #cell_image = cell
                    # 将子图拼合到大图上
                    big_image.paste(cell, (col * cell_width * 2 + 1, row * cell_height * 2 + 1))


            big_image = ImageOps.crop(big_image, 3)#ID无边框，不想要可以删掉
            #cell_image.save('cell_image.png')
            big_image.save(f'C:\\Users\\13966\\OneDrive\\桌面\\画图viso\\BIG-{name}-{kk}\\BIG-{name}-{kk}-{vv}.png')


print("图片已保存，全部搞完了！")


