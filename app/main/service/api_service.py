from flask import Flask,request
import requests
import base64
import os

class Service(object):
    def __init__(self,app:Flask) -> None:
       self.app=app
       self.imgpath = os.getcwd().replace('\\','/')+'/app/main/images'


    def download_image_from_url(self, image_url):       
        response = requests.get(image_url)   
        filepath = self.imgpath+'/'+str(self.get_start_index()+1)+'.png'    
        with open(filepath, 'wb') as f:       
            f.write(response.content)       
        return filepath

    def download_image_from_base64(self, image_base64:str):       
        base64_string = image_base64.split('base64,')[1]
        format = 'jpeg' if image_base64.split('image/')[1][0:4] == 'jpeg' else 'png'
        index = self.get_start_index()
        imgdata = base64.b64decode(base64_string)
        with open(self.imgpath+'/'+index+'.'+format, 'wb') as f:
            f.write(imgdata)
            f.close()
        return self.imgpath+'/'+index+'.'+format

    def evaluate_image(self, image):
        imgpath = ''
        try:
            imgpath = self.download_img(image)

        except Exception as e:
            print(e)
            return 'Error: Image format not supported'
        return imgpath
        
    def download_img(self, image):
        # if(image.split(';base64,')[0] == 'data:image/png;base64,' or
        #  image.split(';base64,')[0] == 'data:image/jpeg;base64,' or 
        #  image.split(';base64,')[0] == 'data:image/jpg;base64,'):
        if(image[:4] == 'data'):
            return self.download_image_from_base64(image)
        else:
            return self.download_image_from_url(image)
         

    def get_start_index(self)->int:
        #if a directory doesnt exist for this search term, create it
        imgpath = self.imgpath
        if not os.path.exists(imgpath):
            os.makedirs(imgpath)

        images = os.listdir(imgpath)
        nums = []
        for image in images:
            if(image[-4:] == '.png' or image[-4:] == '.jpg'):
                try:
                    nums.append(int(image[:-4]))
                except Exception as e:
                    print(e)
                    pass
        return 0 if len(nums)==0 else max(nums)
                