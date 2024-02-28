# Docker on Jetson Nano

- sudo apt-get update
- sudo apt-get install -y docker.io
- sudo usermod -aG docker $USER
- newgrp docker
- docker --version

# Nvidia Docker
- sudo docker run -it --rm --net=host --runtime nvidia -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix nvcr.io/nvidia/l4t-base:r32.4.3

# update
- distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
- curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
- curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
- sudo apt-get update
- sudo apt-get install -y nvidia-docker2
- sudo systemctl restart docker

get info
- sudo /usr/bin/tegrastats
- pip install jetson-stats
    - or 
        - sudo -H pip install jetson-stats
    - or
        - sudo apt install python3-pip
        - sudo pip3 install -U jetson-stats
        - jtop



# info
- docker images
- docker ps

# docker registries -> docker hub
- dokcer image website
- image versioning -> image tags
    - latest
- docker pull {name}
- docker run --name cv-llm -d -p 9000:80 {name} #detach #run each time create new docker image locally
- docker log {nameID} # get from docker ps
- docker stop/start {nameID} # get from docker ps
- docker ps -a # list of all continers
- docker build -t cv-llm:1.0 .
