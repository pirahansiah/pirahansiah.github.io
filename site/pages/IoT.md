# Generative AI on Edge Computing 
# Edge AI & AI IoT + LLMs
chatGPT like in IoT, Raspberry Pi, Intel Neural Compute Stick, Nvidia Jetson. AI at the Edge with LLMs like chatgpt
Making Generative AI More Accessible for Real-World Scenarios  
computer vision, large language models, and generative AI. 

Edges Hardwares:
* Raspberry pi 3 (you need accelerator )
* Raspberry pi 4 (you need accelerator )
* Raspberry pi 5 
* Google Coral (TPU)
* Intel® Neural Compute Stick 2
* NVIDIA Jetson Nano ( 2GB, 4GB , 8GB RAM)
* NVIDIA JETSON AGX XAVIER 
* NVIDIA AGX Orin  
* OpenCV AI Kit
    * OAK
    * OAK—D
    * OAK—D + Wifi
    * OpenCV AI Kit: OAK—D-PoE
    * OAK—D lite
Tools and libraryes:
* Intel® Distribution of OpenVINO™ Toolkit
* Why TensorFlow lite on Edge: Lightweight, low-latency, Privacy, improved power consumption, efficient model ready to used
* I attached to Raspberry pi 4 by USB 3 and work very well for many deep learning models, TensorFlow models
* I test Multi-Class Multi-Object Multi-Camera Tracking (MCMOMCT) under heavy workloads can perform up to 30 minutes
AI at the edge using Intel® OpenVINO™ Toolkit.
Using ready-made models from OpenVINO™ Model Zoo
Model Optimizer. It changes models from TensorFlow, PyTorch, Caffe, etc., into a format (IR) that works well with OpenVINO™ and Intel devices.
handling input streams, processing model outputs, and the lightweight MQTT architecture used to publish data from your edge models to the web.

# Introduction
AI at Edge, edge applications, relevant tools and prerequisites.
Edge computing involves processing data locally or nearby, instead of solely in the cloud. It includes devices like smart appliances or nearby servers to reduce latency and enhance reliability when network availability is inconsistent. This approach supports real-time decision-making across various applications, offering increased security and reduced network strain. While edge AI algorithms are trained in the cloud, they operate locally.
   - Cloud computing is popular, but edge computing is becoming very important too.
   - According to Intel®, the number of IoT devices increased from 2 billion in 2006 to 200 billion expected by 2020.
   - We have seen technology grow from the first network ATMs in the 1970s, the internet in the 1990s, to smart meters in the early 2000s.
   - The use of smart devices, like phones, speakers, fridges, locks, and warehouse tools, is growing fast.
### +:
- Sending data over networks can cost a lot (in terms of data use and power) and might not work in far places or when disasters happen.
- Fast processing is needed for things like self-driving cars to make quick decisions.
- Edge apps might use private information (like health details) which is safer not sent to the cloud.
- Special software for certain devices can make edge AI work better.
   - Karpathy trains a new Llama 2 model using PyTorch. He saves its information in a simple file. Then, he creates a small program, 'run.c', that uses this information to make predictions. This program uses little memory and doesn't need extra tools, making it fast.
Imagine a smartwatch that checks your heart rate. It needs to work fast and keep your health information safe. The smartwatch uses a tiny computer (edge AI) to understand your heart rate without sending data far away. This way, even if you're in a place with no internet, your smartwatch can still help keep you safe by making quick decisions.

Imagine a world where almost everything around us is smart and connected, from the watch on your wrist to the fridge in your kitchen. Back in the day, we started with simple machines like ATMs for getting cash. Then, we got the internet, which let us share information worldwide. Now, we have smart gadgets that help us in daily life, like a fridge that tells you when you're out of milk or a door that locks itself. This is all part of the IoT world, which is getting bigger every day, making our lives easier and more connected.
Imagine you're learning to make a smart camera that can recognize people's faces. In this course, we use special tools from Intel® to make this easier. First, we pick a model that already knows how to recognize faces from a collection of many models. You don't need to teach it from scratch. Next, we'll show you how to make this model work even better and faster on smart devices like your camera. This way, your camera can quickly know

