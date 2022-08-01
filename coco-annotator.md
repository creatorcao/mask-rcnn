# The best image annotation tool —— COCO Annotator

![COCO Annotator](https://camo.githubusercontent.com/69ce7a40db8bdee3e2a292950b5d84cd3f60cc8ac32bdce3316e40ca4130a71d/68747470733a2f2f692e696d6775722e636f6d2f414137496462512e706e67)

This post is the instruction for installing [COCO Annotator](https://github.com/jsbroks/coco-annotator) on Macbook M1.


I tried many labelling tools and then chose [Labelme](https://github.com/wkentaro/labelme) because it's friendly to the beginners. Two ways to install Labelme: to install the _app_ in your Macbook or through `conda/pip install` and then started with Python. 

One of the problems in [Labelme](https://github.com/wkentaro/labelme) is that it's not flexible and quite slow to open, I want to be more efficient to annotate image. 

And onetime I saw a blog mentioned using [COCO Annotator](https://github.com/jsbroks/coco-annotator), I was immediately attracted by its multiple functions and quick annotation style. But the install process is struggling. 
Steps are:

1. Firstly I directly downloaded the [Docker.app](https://www.docker.com/products/docker-desktop/) from its official website, registered a new account and then to create a new environment, input the coco-annotator git repo. If I try `docker-compose up` in my laptop Terminal, it showed **Error -> File Sharing** related. Then I try to find out the **File Sharing** set-up, but still nothing changed. 

2. Then I try to install through Terminal. `brew install docker` or `brew install docker-compose` ❌
3. `brew install --cask docker` ✅ # This means to install the app in your laptop.

4. Then `docker -v` to check if installed sucessfully, if no response, manually start your Docker.app in Application
5. `docker-compose up` 
    └> _Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running? 
    _This means a project is ready running in you Docker.app, just restart. 

6. `docker-compose up` 
    └> Worker fail to boot.
    In the same folder, modify the _docker-compose.yml_ file -> **- FILE_WATCHER=** (remove **True**)
    
7. **System Preferences** -> **Sharing** -> - [x] **AirPlay Receiver** (!uncheck this)
    
<!-- Updated on Aug 1, 2022 -->
