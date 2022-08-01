# The best image annotation tool —— COCO Annotator

![COCO Annotator](https://camo.githubusercontent.com/69ce7a40db8bdee3e2a292950b5d84cd3f60cc8ac32bdce3316e40ca4130a71d/68747470733a2f2f692e696d6775722e636f6d2f414137496462512e706e67)

This post is the instruction for installing [COCO Annotator](https://github.com/jsbroks/coco-annotator) on Macbook M1.

I tried many labelling tools and then chose [Labelme](https://github.com/wkentaro/labelme) because it's friendly to the beginners. 
I tried two ways to install Labelme: to install the _app_ in your Macbook or through `conda/pip install` and then started with Python. 

One of the problems in LabelMe is it's not flexible and quite slow to open, I want to be more efficient to annotate image. 

And onetime I saw a blog mentioned using [COCO Annotator](https://github.com/jsbroks/coco-annotator), I was immediately attracted by its multiple functions and quick annotation style. But the install process is struggling. 
Below is the problems I encountered when I start to install it. Hope this blog could help you. 

BUT it's not a software, and I never try to use Docker before. 
I followed the official tutorial but worked very slowly.
I downloaded the Desktop Docker.app at first to cut some time implement it in my Terminal.
The app run slowly and then I uninstalled it. 

steps are:
1. Firstly I directly download the [Docker.app](https://www.docker.com/products/docker-desktop/) from its official website, register a new account and then to create a new environment, input the git repo. If I try `docker-compose up` in my laptop Terminal, it showed **Error -> File Sharing**. 

Then I try to find out the File Sharing set-up, but noting changed if I try to use the docker. 
└> -> 
3. 
4. `brew install docker`
5. `brew install docker-compose`
6. `brew install --cask docker` ✅
7. `docker-compose up`
└> Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
6. Privacy -> File Sharing -> uncheck
7. docker-compose up -> Worker fail to boot
8. .yml -> remove **True**

<!-- Updated on Aug 1, 2022 -->
