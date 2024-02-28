# Docker on Jetson Nano

## Installation and Setup
- Update the package list to ensure you have the latest versions of packages and their dependencies.
  ```
  sudo apt-get update
  ```
- Install Docker on your Jetson Nano to start creating and managing containers.
  ```
  sudo apt-get install -y docker.io
  ```
- Add your user to the Docker group to manage Docker as a non-root user.
  ```
  sudo usermod -aG docker $USER
  ```
- Apply the group changes without logging out and back in.
  ```
  newgrp docker
  ```
- Verify the installation by checking the Docker version.
  ```
  docker --version
  ```

## Nvidia Docker Setup
- Run an NVIDIA Docker container with GUI support and access to the host's network.
  ```
  sudo docker run -it --rm --net=host --runtime nvidia -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix nvcr.io/nvidia/l4t-base:r32.4.3
  ```

## Updating Nvidia Docker
- Prepare your system to install the NVIDIA Docker by adding NVIDIA's package repositories.
  ```
  distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
  curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
  curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
  ```
- Update your package list to recognize the newly added repositories.
  ```
  sudo apt-get update
  ```
- Install the NVIDIA Docker package to integrate Docker with NVIDIA GPUs.
  ```
  sudo apt-get install -y nvidia-docker2
  ```
- Restart the Docker service to apply the new NVIDIA Docker installation.
  ```
  sudo systemctl restart docker
  ```

## Monitoring and Management Tools
- Get system information using NVIDIA's tool.
  ```
  sudo /usr/bin/tegrastats
  ```
- Install `jetson-stats` for detailed system statistics.
  - Using pip (choose one method):
    ```
    pip install jetson-stats
    ```
    or
    ```
    sudo -H pip install jetson-stats
    ```
    or
    - If `pip` is not installed:
      ```
      sudo apt install python3-pip
      sudo pip3 install -U jetson-stats
      ```
    - Launch the monitoring tool.
      ```
      jtop
      ```

## Docker Commands and Registry Interaction
- List Docker images available on your system.
  ```
  docker images
  ```
- Show running Docker containers.
  ```
  docker ps
  ```
- Interact with Docker registries, like Docker Hub, to find Docker images.
  - Pull an image from a registry.
    ```
    docker pull {name}
    ```
- Run a Docker container in detached mode and map ports.
  ```
  docker run --name cv-llm -d -p 9000:80 {name}
  ```
- Retrieve logs from a running container.
  ```
  docker log {nameID}
  ```
- Start or stop a container.
  ```
  docker stop/start {nameID}
  ```
- List all Docker containers, including inactive ones.
  ```
  docker ps -a
  ```
- Build a Docker image with a tag.
  ```
  docker build -t cv-llm:1.0 .
  ```