# share my experience of using coco-annotator in mac m1

I used LabelMe before for the data annotation and then train it in Mask-RCNN or Detectron2.
But I realize that LabelMe is only beginner friendly and actually not efficient at all. 
I need a more fast and effective label tool to annotate large data.
I read a blog using coco-annotator, the interface looked nice and convinient. 
So I started to install it in my macbook.

BUT it's not a software, and I never try to use Docker before. 
I followed the official tutorial but worked very slowly.
I downloaded the Desktop Docker.app at first to cut some time implement it in my Terminal.
The app run slowly and then I uninstalled it. 

Try to use brew install also failed. 

steps are:
1. Docker.app -> create new env -> git repo -> Error, File Sharing
---------------------------------
2. brew install docker
3. brew install docker-compose
--------------------------------
3. brew install --cask docker✅
4. docker-compose up -> is running? 
5. Privacy -> File Sharing -> uncheck
-------------------------------------
6. docker-compose up -> Worker fail to boot
7. .yml -> remove **True**
