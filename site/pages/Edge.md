<h1><img src="images/Edge.webp">Action Plans</h1>
# Embedded Engineer Specializing in LLM and Computer Vision
# Unlocking the Future: An Embedded Engineer's Journey into LLM and Computer Vision
# Edge + LLMs
Unlocking the Future: An Embedded Engineer's Journey into LLM and Computer Vision tested on : 
Hardware:
    - Raspberry Pi 3/4/5 (with accelerator support)
    - Google Coral (TPU)
    - Intel® Neural Compute Stick 2
    - NVIDIA Jetson Series (Nano, AGX Xavier, AGX Orin)
    - OpenCV AI Kits (OAK, OAK-D, OAK-D with WiFi, OAK-D-PoE, OAK-D lite)
LLMs:
    - Llamacpp
    - geminicpp


## Generative AI and Edge Computing Overview

Generative AI, including large language models (LLMs) like ChatGPT, is becoming increasingly integrated into edge computing devices such as IoT gadgets, Raspberry Pis, Intel Neural Compute Sticks, and Nvidia Jetson modules. This shift aims to make advanced AI technologies more accessible for real-world applications, notably in computer vision and generative AI tasks.

### Edge Hardware Capabilities

Raspberry Pi 3/4/5 (with accelerator support)
Google Coral (TPU)
Intel® Neural Compute Stick 2
NVIDIA Jetson Series (Nano, AGX Xavier, AGX Orin)
OpenCV AI Kits (OAK, OAK-D, OAK-D with WiFi, OAK-D-PoE, OAK-D lite)


### Tools and Libraries

Intel® Distribution of OpenVINO™ Toolkit enhances AI performance on edge devices.
TensorFlow Lite offers a lightweight, low-latency solution for edge AI with privacy and power efficiency.
OpenVINO™ Toolkit facilitates the use of pre-trained models and optimization for Intel devices.
Edge AI Introduction

Edge computing processes data locally to reduce latency, enhance security, and ensure reliability when cloud connectivity is limited. It supports real-time decision-making for IoT devices and smart applications. Despite the growth of cloud computing, edge computing addresses critical needs for immediate data processing and privacy, crucial for applications like autonomous vehicles and private data handling. The evolution from networked ATMs and the internet to smart devices underscores the rapid expansion of IoT, highlighting the importance of edge computing in modern technology landscapes.

### Key Advantages of Edge AI

Reduced data transmission costs and improved efficiency in remote or disaster-prone areas.
Immediate processing capabilities for critical applications such as autonomous driving.
Enhanced privacy for sensitive data by processing it locally.
Simplified and efficient software deployment tailored to specific edge devices.
This concise overview captures the essence of integrating generative AI into edge computing, emphasizing the hardware, tools, and strategic benefits. The shift towards edge AI not only makes cutting-edge technology accessible for various applications but also ensures efficiency, privacy, and real-time processing, marking a significant step forward in the IoT and smart device ecosystem.









Multi-Camera Multiple Object Tracking (MCMOT) aims to improve upon current limitations in MOT, significantly boosting its effectiveness for various uses.

Hardware-Friendly Frameworks: To solve compatibility problems between deep learning systems and various hardware or operating systems, it's key to develop libraries and frameworks optimized for specific hardware. For example, designing specialized CUDA kernels for devices such as the Jetson Nano could enhance performance and simplify configurations.

Optimized MOT Designs: Creating MOT models that use less computing power can help increase the FPS rate, allowing for real-time tracking to become more practical. Techniques like model quantization, pruning, and knowledge distillation could be used to make models lighter without losing precision.

Parallel Processing & Distributed Systems: Using parallel processing can spread the computing workload over several GPUs or systems. This method could greatly speed up processing and make MOT algorithms more adaptable.

Incorporating Various Modalities: Enhancing MOT by integrating it with other types of sensors, such as thermal or depth sensors, can make the system more reliable, especially under difficult lighting or in crowded areas.

Adaptable Models: Developing MOT models that adjust their complexity based on the scene could use resources more effectively. For example, a model might use fewer resources for simpler scenes and more for complicated ones.

Broad Use of Synthetic Data: To address the issue of limited annotated data, synthetic data could be a solution. With improvements in graphics and simulation, it's now possible to create a vast amount of varied, annotated synthetic data for training MOT models.

Better Evaluation Metrics: Creating more detailed and specific metrics for evaluation could offer deeper insights and precise improvements in MOT models, ensuring performance is accurately measured.

Real-time Performance Tuning: Employing strategies like frame skipping, adaptable frame rates, and dynamic ROI selection can help keep a good balance between precision and real-time performance, ensuring efficient operation.




