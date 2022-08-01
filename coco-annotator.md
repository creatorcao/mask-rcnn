# The best image annotation tool -- COCO Annotator

![COCO Annotator](https://camo.githubusercontent.com/69ce7a40db8bdee3e2a292950b5d84cd3f60cc8ac32bdce3316e40ca4130a71d/68747470733a2f2f692e696d6775722e636f6d2f414137496462512e706e67)

This post is the instruction for installing COCO Annotator on Mac M1.

I tried many labelling tools and then chose LabelMe before for its eary interface for the beginners 

the data annotation and then train it in Mask-RCNN or Detectron2.
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
2. `brew install docker`
3. `brew install docker-compose`
--------------------------------
3. `brew install --cask docker` ✅
4. `docker-compose up`
└> Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?

6. Privacy -> File Sharing -> uncheck
-------------------------------------
6. docker-compose up -> Worker fail to boot
7. .yml -> remove **True**

<!-- Updated on Aug 1, 2022 -->
