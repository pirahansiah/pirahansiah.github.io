

# need to know # Feb 2024
1. use python 3.10
    conda install python=3.10 -y
    sudo ln -s /usr/bin/python3 /usr/bin/python
    pip install cuda-python
2. use CUDA 11
    only install last version of current CUDA
3. use ubuntu 22 



# install ubuntu GPU
sudo apt update
sudo apt upgrade -y
sudo apt install nvidia-cuda-toolkit build-essential cmake git libgtk-3-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libjpeg-dev libpng-dev libtiff-dev gfortran openexr libatlas-base-dev python3-dev python3-numpy python3-pip unzip libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev libopenexr-dev libwebp-dev -y


# check
nvcc --version
nvidia-smi 
cat /usr/local/cuda/version.txt
dpkg -l | grep cuda-toolkit


# linux

mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh

~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh

conda install -c conda-forge cudatoolkit cudnn -y
conda install -c nvidia cuda-python -y
conda install -c anaconda cudatoolkit numba mxnet-gpu py-xgboost-gpu cupy chainer caffe-gpu pytorch tensorflow-gpu -y


# MacOS
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh

# Windows 
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
start /wait "" miniconda.exe /S
del miniconda.exe


# CUDA
conda install cudatoolkit
conda install numba 
conda install mxnet-gpu
conda install py-xgboost-gpu
conda install cupy
conda install chainer
conda install caffe-gpu
conda install pytorch
conda install tensorflow-gpu


pip install cuda-python
conda install -c nvidia cuda-python
conda install -c conda-forge cudatoolkit cudnn


# compile
sudo apt install cmake
sudo apt install gcc g++
sudo apt install python3 python3-dev python3-numpy
sudo apt install libavcodec-dev libavformat-dev libswscale-dev
sudo apt install libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
sudo apt install libgtk-3-dev
sudo apt install libpng-dev libjpeg-dev libopenexr-dev libtiff-dev libwebp-dev


sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential cmake unzip pkg-config
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install libv4l-dev libxvidcore-dev libx264-dev
sudo apt-get install libgtk-3-dev
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install python3-dev

