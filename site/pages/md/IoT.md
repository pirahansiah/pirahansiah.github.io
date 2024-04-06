# Computer Vision on Edge
# Generative AI on Edge Computing + Prompt Engineering 
# Edge AI & AI IoT + LLMs
# real time fine tune model on Edge devices 
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
# Tools and libraryes:
[LLAMA C++](https://github.com/ggerganov/llama.cpp)
[OpenVINO GenAI](https://github.com/openvinotoolkit/openvino.genai)

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

# Model Updates and Performance Enhancements

## New Models and Tools
latent consistency models (LCM) and Distil-Whisper, along with an improved LLM chatbot notebook featuring Neural Chat, TinyLlama, ChatGLM, Qwen, Notus, and Youri models.
- **Transformer-based LLM Efficiency:** Enhancements in memory efficiency for transformer-based LLMs on CPUs have been achieved through a stateful model technique, optimizing internal state sharing during inference iterations.
- **Model Serving:** The OpenVINO model server now offers improved LLM serving over KServe v2 gRPC and REST APIs, enhancing flexibility and throughput by handling tokenization server-side.

## Neural Network Compression
- **NNCF Support:** The Neural Network Compression Framework (NNCF) now fully supports int4 weight compression model formats on Intel® Xeon® CPUs, extending to Intel® Core™ processors, enabling more efficient model deployment and execution.

## Utilizing Pre-trained Models and Custom Model Integration

- **Pre-trained Models for Quick Deployment:** Leveraging pre-trained models allows for immediate exploration and application integration without the need for initial training. These models, already in Intermediate Representation (IR) format, can be directly utilized with the Inference Engine for deployment at the edge.
- **Custom Model Integration:** For custom or third-party models not in IR format (e.g., TensorFlow, PyTorch, Caffe, MXNet), the Model Optimizer is the first step. This process converts models into a compatible IR format for the Inference Engine, facilitating seamless integration and deployment in edge applications.
- **Efficient Inference and Output Management:** Post-Inference Engine processing, achieving efficient inference is critical, but equally important is managing the output for edge applications. The final lesson focuses on optimizing output handling for practical edge deployment.


## Overview of Computer Vision Model Types

In the field of computer vision, three primary model types are utilized to interpret and analyze images: Classification, Detection, and Segmentation. Each serves a distinct purpose and applies to various applications.

### Classification
Classification models identify the category or "class" of an object within an image. This process can range from binary (yes/no) decisions to categorizing images among thousands of possible classes. Classification models often provide a probability for each class, highlighting the most likely categories, including the top predictions. This technique is foundational in computer vision, enabling basic sorting and identification tasks.

### Detection
Detection models go a step further by locating objects within an image, typically marking them with bounding boxes. These models combine object localization with classification to not only identify the presence of objects but also determine their types. Detection models apply confidence thresholds to bounding boxes, allowing for the filtering out of detections with low confidence. This capability is crucial for applications requiring precise object localization and identification, such as surveillance or advanced image analysis.

### Segmentation
Segmentation involves a more detailed analysis, classifying each pixel of an image into a category. This model type is instrumental for tasks requiring an understanding of the spatial arrangement and shape of objects within images. Segmentation can be divided into:
- **Semantic Segmentation:** All instances of a class are grouped together, treating them as a single entity.
- **Instance Segmentation:** Each instance of a class is identified as a separate object, enabling the differentiation between individual objects of the same class.

Segmentation models are often post-processed to refine the results and eliminate inaccuracies, such as phantom classes. They are vital for applications needing detailed scene understanding, including autonomous driving and medical imaging.

These computer vision models provide a comprehensive toolkit for analyzing and interpreting images, each with specific strengths suited to different tasks in the field.

## Understanding SSD, ResNet, and MobileNet Architectures

In the exploration of advanced neural network architectures, SSD, ResNet, and MobileNet stand out for their innovative approaches to common challenges in computer vision tasks such as object detection and image classification.

### SSD (Single Shot MultiBox Detector)
SSD is a groundbreaking object detection model that merges the tasks of object localization and classification. By employing default bounding boxes at various levels within the network, SSD can detect multiple objects within an image in a single forward pass. This method enhances efficiency and speed, making SSD suitable for real-time processing applications.

### ResNet (Residual Network)
ResNet addresses the vanishing gradient problem encountered in deep neural networks by introducing residual layers. These layers allow some inputs to "skip" one or more layers, effectively enabling the creation of much deeper networks without a corresponding increase in training difficulty. ResNet's design significantly improves the convergence rate during training compared to traditional deep networks. Additionally, it's worth noting that ResNet tackles not only the vanishing gradient problem but also issues related to the convergence of very deep networks, attributing improved performance to both the architecture's depth and the normalization techniques applied to inputs across layers.

### MobileNet
MobileNet is designed for efficiency, aiming to reduce computational complexity and network size without drastically compromising accuracy. It achieves this through the use of depth-wise separable convolutions, including 1x1 convolutions, which significantly cut down on the computational load. This design makes MobileNet particularly well-suited for mobile devices, where computational resources are limited, and fast inference is critical.

### Additional Insights on ResNet
The ResNet paper further clarifies that very deep networks might struggle with convergence not merely because of the vanishing gradient problem but due to the exponentially lower convergence rates inherent to their depth. The introduction of residual connections and normalization at various layers aids in mitigating these issues, allowing ResNet architectures to achieve faster convergence and improved performance over "plain" networks without residual connections.

These architectures represent significant advancements in neural network design, each addressing specific challenges within the realm of computer vision and enabling more efficient, accurate, and deep models suitable for a wide range of applications.







| Date | Model/Method | Importance | Previous Method | Next Method | Reference |
|------|--------------|------------|-----------------|-------------|-----------|
| Various | SSD (Single Shot MultiBox Detector) | Revolutionizes object detection by merging localization and classification tasks. | N/A | ResNet | [Source](https://paperswithcode.com/method/ssd) |
| Various | ResNet (Residual Network) | Solves the vanishing gradient problem with residual layers, enabling deeper networks. | SSD | MobileNet | [Source](https://paperswithcode.com/method/resnet) |
| Various | MobileNet | Designed for efficiency on mobile devices with depth-wise separable convolutions. | ResNet | GPT | [Source](https://paperswithcode.com/method/mobilenet) |
| Various | GPT (Generative Pre-trained Transformer) | Revolutionized NLP and generation by leveraging deep learning through transformer architecture. | MobileNet | EfficientNet | [Source](https://paperswithcode.com/method/gpt) |
| Various | EfficientNet | Systematic scaling of networks for improved efficiency and accuracy. | GPT | YOLO | [Source](https://paperswithcode.com/method/efficientnet) |
| Various | YOLO (You Only Look Once) | Real-time object detection system that increases speed of detection. | EfficientNet | U-Net | [Source](https://paperswithcode.com/method/yolo) |
| Various | U-Net | Used for biomedical image segmentation, designed to work with fewer training samples. | YOLO | Capsule Networks | [Source](https://paperswithcode.com/method/u-net) |
| Various | Capsule Networks (CapsNets) | Models hierarchical relationships in data for robustness to changes. | U-Net | Graph Neural Networks | [Source](https://paperswithcode.com/method/capsule-network) |
| Various | Graph Neural Networks (GNNs) | Processes data represented in graphs, crucial for understanding relational data. | Capsule Networks | Attention Mechanisms | [Source](https://paperswithcode.com/method/graph-neural-network) |
| Various | Attention Mechanisms | Allows models to focus on specific parts of the input data, improving performance. | GNNs | Generative Adversarial Networks | [Source](https://paperswithcode.com/method/attention-mechanism) |
| Various | Generative Adversarial Networks (GANs) | Enables the generation of highly realistic images, videos, and audio. | Attention Mechanisms | Reinforcement Learning | [Source](https://paperswithcode.com/method/gan) |
| Various | Reinforcement Learning (RL) & Deep RL | Combines machine learning and decision-making for applications in robotics and game playing. | GANs | N/A | [Source](https://paperswithcode.com/method/reinforcement-learning) |











# Example:
## people density: Course Project: People Counter App Deployment

develop and deploy a People Counter Application leveraging edge computing technologies. 

The project encompasses several key steps:
- **Model Conversion:** Transform an AI model into the Intermediate Representation (IR) format suitable for the Inference Engine.
- **Inference Engine Utilization:** Deploy the IR model using the Inference Engine for real-time analysis.
- **Output Processing:** Analyze the model's output to extract meaningful statistics about people within the camera's view.
- **Data Transmission:** Send the processed statistics to a server for further analysis or display.
- **Performance and Use Case Analysis:** Evaluate the deployed model's performance and explore potential applications.

The demonstration showcases the People Counter App in action. It highlights the app's capability to count the number of people present, calculate the average duration of their stay within the frame, and tally the total count over time. These statistics are then transmitted to a web server from the edge device. The demo provides a visual representation of the project's functionality without audio commentary.
