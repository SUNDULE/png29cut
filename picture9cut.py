from PIL import Image
from glob import glob
import os


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



klist = [1,2]
vlist = [1,2,3,4,5,6,7,8]
named = set(names)

for name in named:
    for kk in klist:
        mkdir(f"C:\\Users\\13966\\OneDrive\\桌面\\画图viso\\{name}-{kk}\\")
        for vv in vlist:
            image = Image.open(f"C:\\Users\\13966\\OneDrive\\桌面\\画图viso\\{name}-{kk}-{vv}.png")
            for i in range(3):
                for j in range(3):
                    width, height = image.size
                    tile_width = width // 3
                    tile_height = height // 3

                    left = j * tile_width
                    top = i * tile_height
                    right = (j + 1) * tile_width
                    bottom = (i + 1) * tile_height

                    tile = image.crop((left, top, right, bottom))
                    tile.save(f"C:\\Users\\13966\\OneDrive\\桌面\\画图viso\\{name}-{kk}\\{name}-{kk}-{vv}_{i}_{j}.png")


print("全部图片处理完毕！F**k！TLW")

