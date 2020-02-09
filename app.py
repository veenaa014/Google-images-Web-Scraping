# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:06:13 2020

@author: 17202
"""

from flask_cors import CORS,cross_origin
from flask import Flask, render_template, request,jsonify
from scrapperimage.scrapperimage import ScrapperImage
from businesslayer.businesslayerutil import BusinessLayer
import os


app = Flask(__name__) 


@app.route('/')  
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/showImages')
@cross_origin()
def displayImages():
    list_images=os.listdir('static')
    print(list_images)
    
    try:
        if(len(list_images)>0):
            return render_template('showImage.html',user_images=list_images)
        else:
            return "Images are not present"
    except Exception as e:
        print("No images found",e)
        return "Please try with a different search keyword"
    
@app.route('/searchImages',methods=['Get','POST'])
def searchImage():
    if request.method=="POST":
        search_term=request.form['keyword'] 
        
    else:
        print("Please enter something")
    
    imagescrapperutil=BusinessLayer 
    imagescrapper=ScrapperImage()
    list_images=os.listdir('static')
#    print(list_images)
    imagescrapper.delete_downloaded_images(list_images)
#    
    image_name=search_term.split()
    image_name="+".join(image_name)
#    
#   
    header={
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
            
            }
    lst_images=imagescrapperutil.downloadImages(search_term,header)
    
    return displayImages() 
    


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000) 
   #app.run(debug=True) 