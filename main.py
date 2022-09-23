import os
from time import time
from heic2png import HEIC2PNG
import shutil
from os import path, walk

def main():
        listeFichiers = []
        des="./Images-PNG/"
        for (repertoire, sousRepertoires, fichiers) in walk("./Images-HEIC"):
                listeFichiers.extend(fichiers)
        for e in listeFichiers:         
                url = "./Images-HEIC/"+e
                print(url)
                heic_img = HEIC2PNG(url)
                png = heic_img.save() # it'll show as `test.png`
                print(png)
                src=png
                shutil.copy2(src,des)
                os.remove(url)
                os.remove(png)
        print(listeFichiers)
        print("Fini !!")



if __name__ == '__main__':
        if path.exists("Images-HEIC") & path.exists("Images-PNG") :
                print("Creation Des Dossiers...")
                main()
        else: 
                os.mkdir("./Images-HEIC")
                os.mkdir("./Images-PNG")
                main()
        

