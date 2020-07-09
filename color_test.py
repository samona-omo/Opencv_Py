import cv2
import numpy as np
import os
#读取工作目录路径
pwd=os.getcwd()

#读取彩色图片
img=cv2.imread(pwd+"/rabbits.jpg")

#设置三维数组，300行*300列*3通道，全部置0

#Blue 蓝色通道设置
img[:,0:100,0]=255
img[:,0:100,1]=0
img[:,0:100,2]=0

#Green 绿色通道设置
img[:,100:200,0]=0
img[:,100:200,1]=255
img[:,100:200,2]=0

#Red 红色通道设置
img[:,200:300,0]=0
img[:,200:300,1]=0
img[:,200:300,2]=255

cv2.imshow("rabbits.jpg",img)

keyword=cv2.waitKey(0)
if keyword=='q':
    cv2.destroyAllWindows()
