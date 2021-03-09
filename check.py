from skimage.metrics import structural_similarity
import imutils
import glob
import cv2
import numpy as np
from findmatch.models import Found_Item,Lost_Item

obj = Found_Item.objects,get(id=1)
img=cv2.imread(obj.img.path,cv2.IMREAD_GRAYSCALE)
all_images_to_compare=[]
titles=[]
final={}
for f in glob.glob("media\lost_items\*"):
    #print("code worked")  
    image=cv2.imread(f,cv2.IMREAD_GRAYSCALE)
    titles.append(f)
    all_images_to_compare.append(image)


all_images_to_compare=all_images_to_compare[:-1]

for image_to_compare,title in zip(all_images_to_compare, titles):
    (score,diff) = structural_similarity(img,image_to_compare,full=True)
    diff=(diff*255).astype("uint8")
    
    '''print("Title:"+title)
    print("SSIM:{}".format(score))'''
    final.update({title:score})
#print("code worked")    

#print(final)
key_l=list(final.keys())
val_l=list(final.values())
#print(val_l)
m=((sorted(final.values()))[-2])
p=(key_l[val_l.index(m)])
print("IMAGE WITH HIGHEST MATCH FOUND IS : ",p)
    

cv2.waitKey(0)
cv2.destroyAllWindows()
