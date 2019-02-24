# YOLO-Tools

Useful scripts to prepare a testing dataset.

## Convert to jpg
This script will convert the images in a given folder to jpg and also resize it. 

```
imageSize = (800,600)
imagePath = "Images/001/*.*"
datasetOutput = "dataset"
```

 ``` python3 convert2jpg.py ```

## Annotation

### Annotation Tool
Tool to mark the elements in the image

 ``` python3 annotation.py ```
 


### Convert to Darknet
Take the output from annotation tool and convert to the format expected by darknet

``` python3 convert2darknet.py```

## Split
Split the dataset between training and test

``` python3 split.py```

## Darkflow
Convert the darknet annotation file to 

``` python3 darknet2darkflow.py```