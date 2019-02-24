import glob
from xml_util import createXMLAnnotation
import cv2 


annotationPath = "dataset/*.txt"
annotationOutput = "dataset"


labelFiles = glob.glob(annotationPath)


def get_rectangles(boxes,image):
    rects = []
    for box in boxes:

        w=int(float(box['width'])*image.shape[1])
        h=int(float(box['height'])*image.shape[0])
        x=int(int(float(box['x'])*image.shape[1])-w/2)
        y=int(int(float(box['y'])*image.shape[0])-h/2)
        r = (y,x,int(y+h),int(x+w))
        rects.append(r)
    return rects


def load_boxes(filename):
    boxes=[]
    with open(filename.split(".")[0]+".txt") as fp:
        line = fp.readline()
        cnt = 1
        while line:
            l = line.strip().split(" ")
            box={
                "class":l[0],
                "x":l[1],
                "y":l[2],
                "width":l[3],
                "height":l[4]
            }
            boxes.append(box)
            line = fp.readline()
            cnt += 1
    return boxes


for label in labelFiles:
    print(label)
    filename = label.replace(".txt",".jpg")
    image = cv2.imread(label.replace(".txt",".jpg"))
    boxes =get_rectangles(load_boxes(label),image)
    createXMLAnnotation(filename,boxes,image.shape,"voc")







