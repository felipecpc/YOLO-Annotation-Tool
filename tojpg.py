import glob
from PIL import Image
import os
import cv2

imageSize = (800,600)

imagePaths = "Images/001/*.*"
datasetOutput = "dataset"


imagelist = glob.glob(imagePaths)


def imageResize(im, width = None, height = None, inter = cv2.INTER_AREA):
    image = cv2.imread(im)
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation = inter)
    return resized


def remove(image):

    if os.path.isfile(image):
        os.remove(image)
    else:    ## Show an error ##
        print("Error: %s file not found" % image)

def converImage (image):
    print(">[Converting] %s" %image)
    im = Image.open(image)
    print(">[Converted!] %s" %image)
    rgb_im = im.convert('RGB')
    newName = image.replace(".jpg",".png")
    rgb_im.save(newName)
    
    return newName

count = 0
for image in imagelist:
    if (".jpg" in (image)) == False:
        image = converImage(image)
    print(">[Resizing] %s" %image)
    im = imageResize(image,imageSize[1],imageSize[0])
    cv2.imwrite("%s/%s.jpg"%(datasetOutput,count),im)
    print(">[Resized] %s/%s.jpg" %(datasetOutput,count))
    count = count + 1
    print("--------------------------------")

print("Total: %s images" %(count))
print("Folder: %s\n\n" %(datasetOutput))
    




