# resizer ・・・ 画像ファイルを一括でリサイズ！
# 2017/10/8 開発スタート
# 2018/2/4 ver1.1 フォルダが存在してもエラーが出ないように修正

import os
from PIL import Image

FOLDER = r"F:\PORTRAIT\20190421FavoritePictures桜庭まゆさん" # PC側のフォルダ名。ドライブ名から始まる。ウィンドウからコピペ推奨
# FOLDER = FOLDER.replace('\\', '/')
# FOLDER = FOLDER.replace('\x81', '/201')
# FOLDER = FOLDER.replace('\t', '/t')

os.chdir(FOLDER)
# 所定フォルダ内のファイル名をリスト化
files = os.listdir(".")
# フォルダ「mid」と「small」を作成、存在する場合はそのまま使用
if os.path.exists("./mid") == False:
    os.mkdir("mid")
    print("ディレクトリ「mid」作成")
else:
    print("ディレクトリ「mid」は存在するのでそのまま使用")
if os.path.exists("./small") == False:
    os.mkdir("small")
    print("ディレクトリ「small」作成")
else:
    print("ディレクトリ「small」は存在するのでそのまま使用")
# 各ファイルをリサイズして所定フォルダに保存
for file in files:
    if file[-4:] == ".JPG":
        if len(file) < 13:
            # 画像ファイルオープン
            img = Image.open(file,"r")
            exif = img.info['exif']
            # 長辺2400と800へのリサイズ
            mid_img = img.resize((2400,1600), Image.ANTIALIAS)
            small_img = img.resize((1200,800), Image.ANTIALIAS)
            # リサイズファイルの保存
            mid_img.save("mid/" + file[0:8] + "_mid" + file[8:], "JPEG", quality=100, optimize=True, exif=exif)
            print("mid/" + file[0:8] + "_mid" + file[8:] + " save complete!")
            small_img.save("small/" + file[0:8] + "_small" + file[8:], quality=100, optimize=True, exif=exif)
            print("small/" + file[0:8] + "_small" + file[8:] + " save complete!")
        else:
            print(file + " has been passed.")
    else:
        print("{0}はJPEGではないのでスルーしました" .format(file))
