# LLMs are pivotal for businesses, especially startups, as the future of AI leans heavily towards inference applications.
### speed up & scale up
- Speed, Scale, Local Inference, AI Acceleration 
  - **What is Model Inference?**
    - Training gets attention.
    - Inference is the main work.
  - **Inference Example**
    - Computer vision for animals.
    - From training to real-world use.
- How AI Inference Works
  - **Steps**
    - Preprocess data.
    - Run the model.
    - Create output.
    - Post-process if needed.
  - **Performance**
    - Must be fast.
    - Uses optimized workloads.
- Challenges of Model Inference
  - **Issues to Handle**
    - Speed and time.
    - Use fewer resources.
    - Manage models well.
    - Keep data safe.
    - Make AI clear to understand.
- AI at the Network's Edge
  - **Benefits**
    - Faster responses.
    - Uses less data.
    - Protects privacy.
- AI Infrastructure Choices
  - **Build or Buy?**
    - In-House: Control and customize.
    - External: Quick and managed.
  - **Cost Factors**
    - Scale and need.
    - Skills and tech.
    - Service options.
- Looking Ahead
  - **Trends**
    - Growth of inference demand.
    - Costs may remain high.
    - Big players vs new ones.
    - Open-source as a game-changer.





### On-Device Training: Efficient training on the edge with ONNX Runtime
On-Device Training, a new capability in ONNX Runtime (ORT) which enables training models on edge devices without the data ever leaving the device. The edge devices can be any compute-enabled devices like laptops, smartphones, gaming consoles, or other embedded devices. This capability opens new opportunities for application developers, as they can now personalize experiences for users without compromising privacy. 
###### ONNX Runtime at a glance
ORT is a high-performance cross-platform inference and training engine that can run a variety of machine learning models. ORT provides an easy-to-use experience for the AI developers to run models on multiple hardware and software platforms. Beyond accelerating server-side inference and training, ORT is also available for inferencing on mobile devices and on web browsers.
The new On-Device Training capability extends the ORT-Mobile inference offering to enable training on the edge devices. The goal is to make it easy for developers to take an inference model and train it locally on-device—with data present on-device—to provide an improved user experience for end customers.
###### On-Device Training with ONNX Runtime
As opposed to traditional deep learning (DL) model training, On-Device Training requires efficient use of compute and memory resources. Additionally, edge devices vary greatly in compute and memory configurations. To support these unique needs of edge device training, we created On-Device Training capability that is framework agnostic and builds on top of the existing C++ ORT core functionality.
With On-Device Training, application developers can now infer and train using the same binaries. At the end of a training session, the runtime produces optimized inference ready models which can then be used for a more personalized experience on the device. For scenarios like federated learning, the runtime provides model differences since the aggregation happens on the server side.
###### Key benefits
- Memory and performance efficient local trainer for lower resource consumption on device (battery life, power usage, and multiple app training).
- Optimized binary size which fits strict constraints on edge devices.
- Simple APIs and multiple language bindings make it easy to scale across multiple platform targets (Now available – C, C++, Python, C###, Java. Upcoming – JS, Objective-C, and Swift).
- Developers can extend their existing ORT Inference solutions to enable training on the edge.
- Same ONNX model and runtime optimizations can run across desktop, edge, and mobile devices, without having to re-design training solution across platforms.
###### Applications of On-Device Training
The applications of On-Device Training fall into two broad categories:
######### Federated learning
This technique can be used to train global models based on decentralized data without sacrificing user privacy. Federated learning involves updating a global model based on training that happens on edge devices. The edge devices train their version of the global model based on data local to the devices and return the model difference to the server. The server then aggregates these model differences from various devices to update the global model. This process is repeated until the desired outcome from the model is achieved. On-Device Training provides the local trainer which will run on individual devices. Federated learning infrastructure will provide the orchestration of managing the output of the local trainers, across a large number of devices, to update the global model.
For instance, healthcare industries can use federated learning to train models based on data from different hospitals with the data always staying on location, to provide better predictions for health conditions. Privacy for the patients is maintained because user data never leaves the devices or hospitals. The model improves the quality because it is updated based on model changes suggested from individual hospitals. This should lead to a comprehensive global model with an overall better performance for the end customer.
######### Personalized learning
This technique involves fine-tuning models on-device to create new personalized models. The training is based on data on-device, which produces a model personalized for the end user locally. On-Device Training again acts as a local trainer, which will update the model present on-device. This personalized model will then be used for inference to provide
###### Other way
- TensorFlow Lite:
    - Description: TensorFlow Lite is an open-source deep learning framework designed for on-device inference but also supports some training capabilities directly on devices. It's optimized for mobile and embedded devices.
    - Use Cases: It's commonly used for fine-tuning pre-trained models with user data on smartphones and IoT devices to enhance personalization and performance without compromising user privacy.
- PyTorch Mobile:
    - Description: PyTorch Mobile brings the power of PyTorch to mobile devices. It supports both inference and training directly on devices, enabling applications to learn from new data in real-time.
    - Use Cases: Suitable for applications requiring real-time model updates based on user interactions or environmental changes, such as personalizing user experiences or adaptive UIs.
- Core ML:
    - Description: A framework by Apple that integrates machine learning models into iOS applications. Core ML supports on-device model training with user data, ensuring privacy and customization.
    - Use Cases: Ideal for iOS applications that need to adapt to user behaviors, preferences, or changing environments, like recommendation systems or adaptive text recognition.
- ML Kit:
    - Description: Provided by Google for Android and iOS app developers, ML Kit facilitates deploying custom ML models on mobile devices. It offers limited on-device model retraining capabilities.
    - Use Cases: Primarily used for enhancing user experiences through personalization features in apps, such as user engagement optimization or content recommendation based on user interaction.
- Federated Learning Frameworks:
    - Description: Google’s Federated Learning (FL) is a technique that allows models to be trained across many devices while keeping the data localized. TensorFlow Federated is an open-source framework developed to make this possible.
    - Use Cases: Federated learning is used in scenarios where data privacy is paramount, such as in healthcare or finance applications, allowing for model improvement without compromising user data.
- Edge AI Platforms:
    - Description: Several platforms, such as NVIDIA Jetson for AI at the edge, provide comprehensive support for on-device training. These platforms offer specialized hardware and software optimized for high-performance AI computations on edge devices.
    - Use Cases: Suitable for robotics, drones, cameras, and other edge devices requiring immediate data processing and decision-making without the latency of cloud computing.
- Custom Solutions with Embedded Libraries:
    - Description: For ultra-low-power devices or specific use cases, custom solutions using embedded ML libraries like TensorFlow Micro, uTensor, or Cube.AI can be developed.
    - Use Cases: These are typically used in wearable technology, smart sensors, and other IoT devices where computing resources are limited, and operations need to be highly efficient.

### For LLMs 
###### on-device training or adaptation of LLMs:
- Model Pruning and Distillation: Techniques like pruning (removing less important neurons) and distillation (training a smaller model to mimic a larger one) can significantly reduce the size of LLMs without a substantial loss in performance. Tools like Hugging Face's transformers library provide functionalities for these techniques, making it easier to prepare models for on-device deployment.
- Quantization: Quantization reduces the precision of the model's parameters from floating-point to integers, which can drastically decrease the model size and speed up inference and training. TensorFlow Lite and PyTorch Mobile support quantization, allowing for the conversion of models into formats suitable for on-device operations.
- Federated Learning: Instead of training a model on a single device, federated learning allows for training across many devices while keeping the data localized. This approach is beneficial for privacy-preserving applications. TensorFlow Federated is a framework designed to facilitate federated learning experiments in simulation and in real-world scenarios.
- Transfer Learning and Fine-tuning: In many cases, retraining the entire LLM on-device might not be necessary. Instead, fine-tuning or transfer learning techniques can be used to adapt pre-trained models to new tasks with a relatively small amount of new data. This approach requires less computational power and can often be done on-device with limited resources. Libraries like TensorFlow Lite and PyTorch Mobile support these operations.
- Split Computing: This method involves splitting the model between the edge device and the cloud. Initial layers of the model run on the device, and the intermediate representations are sent to the cloud for processing by the remaining layers. This approach can reduce the computational load on the device.
- Edge-specific Frameworks and Libraries: Some frameworks are specifically designed for edge computing and on-device model training, such as TensorFlow Lite, PyTorch Mobile, and ONNX Runtime. These frameworks provide tools for optimizing, converting, and running machine learning models on edge devices.
- Adaptive Computation: Techniques that adjust the computational graph of a model in response to the available resources or the complexity of the input. For example, early exiting or conditional computation allows parts of a network to be bypassed for simpler inputs, reducing the computational burden.
- CoreML: For iOS devices, Apple's CoreML provides a framework that supports on-device training for models. CoreML models can be optimized for various tasks, including language understanding, and can be updated with new data directly on the device.
- Custom Hardware and NPUs: Some devices come equipped with Neural Processing Units (NPUs) or custom hardware designed to accelerate machine learning tasks. Leveraging these can significantly improve the efficiency of on-device training and inference tasks.

### Large Language Model Inference with ONNX Runtime

- **ONNX vs. ONNX Runtime**
  - ONNX: Open-source format for ML models.
  - ONNX Runtime: Cross-platform ML inferencing and training accelerator.

- **Optimization for Efficient Inference**
  - **Operator Fusion**
    - Merges operators to reduce GPU memory transfers.
  - **Removal of Unnecessary Nodes**
    - Eliminates cast nodes and simplifies layer norms.

- **Key Concepts**
  - **Root Mean Square Norm (RMS Norm)**
    - Mathematical concept for normalization.
  - **Rotary Embeddings**
    - Projects embeddings into a new space.

- **Optimization Strategies**
  - Simplifies ONNX graph for attention operators.
  - Implements performance optimizations for large models.

- **Performance Comparison**
  - Compares ONNX Runtime with PyTorch.
  - Highlights speed and efficiency of ONNX Runtime.

- **Technical Implementations**
  - **Kernel Creation and Custom Cuda CUTLAS**
    - Discusses GPU implementation and integration with CUTLAS.

- **Ecosystem Integration**
  - Emphasizes the importance of end-to-end integration within ONNX Runtime.

- **Tools for Optimization and Quantization**
  - **Transformer Optimizer Script**
    - Automates optimization process.
  - **Torch Dynamo Exporter**
    - Simplifies pattern matching.
  - **Onyx Rewriter**
    - Converts functions for optimization.



### Prompt Caching
- **User**
  - Gives a prompt.
- **Cache**
  - Has it? Give old answer.
  - No? Get new, save it.
- **LLM (Large Language Model)**
  - Makes answers.

### RAG Knowledge
- **Get Data**
  - From many places.
  - Make it clean.
- **Use Data**
  - Make one format.
  - Make numbers.
  - Build knowledge.

### Seq2Seq Models
- **Use**
  - Take data.
  - Make new data.
- **Attention**
  - Works better.
  - Looks at key parts.

### AI Vision for Companies
- **Do**
  - Build solutions.
  - Deploy them.
  - Grow them.
- **Use**
  - Special LVMs.
- **Fast**
  - Make tasks quick.
  - Move fast to use.










<h1><img src="images/Edge.webp">Action Plans</h1>
### Embedded Engineer Specializing in LLM and Computer Vision
### Unlocking the Future: An Embedded Engineer's Journey into LLM and Computer Vision
### Edge + LLMs
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


###### Generative AI and Edge Computing Overview

Generative AI, including large language models (LLMs) like ChatGPT, is becoming increasingly integrated into edge computing devices such as IoT gadgets, Raspberry Pis, Intel Neural Compute Sticks, and Nvidia Jetson modules. This shift aims to make advanced AI technologies more accessible for real-world applications, notably in computer vision and generative AI tasks.

######### Edge Hardware Capabilities

Raspberry Pi 3/4/5 (with accelerator support)
Google Coral (TPU)
Intel® Neural Compute Stick 2
NVIDIA Jetson Series (Nano, AGX Xavier, AGX Orin)
OpenCV AI Kits (OAK, OAK-D, OAK-D with WiFi, OAK-D-PoE, OAK-D lite)


######### Tools and Libraries

Intel® Distribution of OpenVINO™ Toolkit enhances AI performance on edge devices.
TensorFlow Lite offers a lightweight, low-latency solution for edge AI with privacy and power efficiency.
OpenVINO™ Toolkit facilitates the use of pre-trained models and optimization for Intel devices.
Edge AI Introduction

Edge computing processes data locally to reduce latency, enhance security, and ensure reliability when cloud connectivity is limited. It supports real-time decision-making for IoT devices and smart applications. Despite the growth of cloud computing, edge computing addresses critical needs for immediate data processing and privacy, crucial for applications like autonomous vehicles and private data handling. The evolution from networked ATMs and the internet to smart devices underscores the rapid expansion of IoT, highlighting the importance of edge computing in modern technology landscapes.

######### Key Advantages of Edge AI

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




