from skimage.metrics import structural_similarity
import imutils
import glob
import cv2
import numpy as np


img=cv2.imread("sample_p/rdj.jpg",cv2.IMREAD_GRAYSCALE)
all_images_to_compare=[]
titles=[]
final={}
for f in glob.glob("sample_p\*"):
    image=cv2.imread(f,cv2.IMREAD_GRAYSCALE)
    if image is None:
        continue
    titles.append(f)
    #print(f)
    all_images_to_compare.append(image)

for image_to_compare,title in zip(all_images_to_compare, titles):
    (score,diff) = structural_similarity(img,image_to_compare,full=True)
    diff=(diff*255).astype("uint8")
    '''print("Title:"+title)
    print("SSIM:{}".format(score))'''
    final.update({title:score})

#print(final)
key_l=list(final.keys())
val_l=list(final.values())
#print(val_l) run kro ..isme problem nai hai humne kia tha value print lrra a th likho tm
m=((max(final.values())))
print(m)
if (m>=0.27):
      
     p=(key_l[val_l.index(m)])
     print("IMAGE WITH HIGHEST MATCH FOUND IS : ",p)
else:
    print("Match not found")     
    

cv2.waitKey(0)
cv2.destroyAllWindows()
