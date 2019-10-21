##NOTE##
#The code above was run on Google Colab. The main changes done were in the imshow attribute of cv2. 
#Google Colab doesn't necessarily support imshow, hence it has its own module cv2_imshow. 
#If you are running the code on a platform which is not colab, you will have to change cv2_imshow to cv2.imshow
!pip install wand
!apt-get update
!apt-get install libmagickwand-dev
import cv2
from google.colab.patches import cv2_imshow
import numpy as np
from wand.image import Image
def Vignette_eff(img1):
  with Image(filename=img1) as img:
    img.vignette(sigma=3, x=10, y=10)
    img.save(filename="fx-vignette.jpg")
  im = cv2.imread("/content/fx-vignette.jpg")
  cv2_imshow(im)

def grayscale(img1):
  c3 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  cv2_imshow(c3)
  cv2.imwrite("./lol.jpeg", c3)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  return c3

def Tint(img1,c):
  with Image(filename=img1) as img:
    if(c=="yellow"):
      img.colorize(color=c, alpha="rgb(10%, 0%, 20%)")
    if(c=="red"):
      img.colorize(color=c, alpha="rgb(50%,0%,0%)")
    if(c=="green"):
      img.colorize(color=c, alpha="rgb(0%,50%,0%)")
    if(c=="blue"):
      img.colorize(color=c, alpha="rgb(0%,0%,50%)")
    img.save(filename="fx-colorize.jpg")
  im = cv2.imread("/content/fx-colorize.jpg")
  cv2_imshow(im)

def Cartoon(img1):
    c3 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    c3 = cv2.medianBlur(c3, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    color = cv2.bilateralFilter(img, 2, 300, 300) 
    cartoon = cv2.bitwise_and(color, color, mask=edges) #Creating cartoon image with dark egdes detected above
    #cv2.imshow("Cartoonized", cartoon) #Displaying the conventional cartoon image as expected
    c1 = cv2.bilateralFilter(color, 7, 250, 50) #1 #Taking the colorized image
    c2 = cv2.bitwise_and(color, c1,mask=edges) #2 with edges as the mask
    c3 = cv2.bilateralFilter(c2, 5, 250, 200) #Changing values with #2 as input
    c4 = cv2.bitwise_and(c3, c2, c1) #2 with edges as the mask
    cv2_imshow(c4) #Displaying the image
    cv2.imwrite("./lol.jpeg", c4)
    cv2.waitKey(0) #Holds the output
    cv2.destroyAllWindows() #Destroys the process when all result windows are closed

def Swirl_eff(img1):
  with Image(filename=img1) as imgs:
        imgs.swirl(degree=-90)
        imgs.save(filename="fx-wave.jpg")
  im = cv2.imread("/content/fx-wave.jpg")
  cv2_imshow(im)
  
def Charcoal_eff(img1):
  with Image(filename=img1) as img:
    img.charcoal(radius=1.5, sigma=0.5)
    img.save(filename="fx-charcoal.jpg")
  im = cv2.imread("/content/fx-charcoal.jpg")
  cv2_imshow(im)
  
  
fileog = "/content/file_name.jpg" #uploaded filename here  
file =  fileog
img = cv2.imread(file)
n = 1

while(n==1):
  c=int(input("\n1. Grayscale Image\n2. Cartoonize Image\n3. Other Filters\nEnter your choice"))
  if(c==1):
      gray = grayscale(img)
      yn = input("Do you want to add more filters? ")
      file = "/content/lol.jpeg"
      if(yn == "y"):
        ch=int(input("\n1.Swirl\n2.Charcoal\n3.Vignette\nEnter your choice"))
        if(ch==1):
          Swirl_eff(file)
        if(ch==2):
          Charcoal_eff(file)
        if(ch==3):
          Vignette_eff(file)
  if(c==2):
    car = Cartoon(img)
    yn = input("Do you want to add more filters? ")
    file = "/content/lol.jpeg"
    if(yn == "y"):
      ch=int(input("\n1.Swirl\n2.Charcoal\n3.Tint\n4.Vignette\nEnter your choice"))
      if(ch==1):
        Swirl_eff(file)
      if(ch==2):
        Charcoal_eff(file)
      if(ch==3):
        color = int(input("Choose color\n1.yellow\n2.red\n3.blue\n4.green"))
        if(color == 1):
          Tint(file,"yellow")
        if(color == 2):
          Tint(file,"red")
        if(color== 3):
          Tint(file, "blue")
        if(color == 4):
          Tint(file, "green")
      if(ch==4):
        Vignette_eff(file)
         
  if(c==3):
    file = fileog 
    ch=int(input("\n1.Swirl\n2.Charcoal\n3.Tint\n4.Vignette\nEnter your choice"))
    if(ch==1):
      Swirl_eff(file)
    if(ch==2):
      Charcoal_eff(file)
    if(ch==3):
      color = int(input("Choose color\n1.yellow\n2.red\n3.blue\n4.green"))
      if(color == 1):
        Tint(file,"yellow")
      if(color == 2):
        Tint(file,"red")
      if(color== 3):
        Tint(file, "blue")
      if(color == 4):
        Tint(file, "green")
    if(ch==4):
      Vignette_eff(file)
  n = int(input("\nPress 1 to continue"))
