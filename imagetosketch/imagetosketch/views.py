from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import cv2 as cv
import os


def makesketch(image):
    image_path = os.path.join(settings.MEDIA_ROOT, image)
    img=cv.imread(image_path)
    gimg=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    iimg=cv.bitwise_not(gimg)
    bimg=cv.GaussianBlur(iimg,(111,111),0)
    bimg=cv.bitwise_not(bimg)
    sketch=cv.divide(gimg,bimg,scale=256.0)
    cv.imwrite(f'static/images/{image}.jpg',sketch)
    return f'static/images/{image}.jpg'

def home(request):
    return render(request,'home.html')

def tool(request):
    return render(request,'tool.html')

def sketch(request):
    if request.method=='POST':
        if 'image' in request.FILES:
            file=request.FILES['image']
            fss=FileSystemStorage()
            temp=fss.save(file.name,file)
            global sketchimg
            sketchimg=makesketch(temp)  
            return render(request,'sketch.html',{'image':f'/{sketchimg}'})
        else:
            return redirect('/tool/')