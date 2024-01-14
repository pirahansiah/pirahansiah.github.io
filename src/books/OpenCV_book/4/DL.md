# How to use computer vision with deep learning in IoT devices.  Inference machine learning on Edge require some extra steps.

I tested several hardware such as Raspberry pi 3, Raspberry pi 4, Intel® Neural Compute Stick 2, OpenCV AI Kit, Google Coral, NVIDIA Jetson Nano, etc. Different OS: real-time operating system (RTOS), Nasa cFS (core Flight System), Real-Time Executive for Multiprocessor Systems (RTEMS),

anomaly detection, object detection, object tracking, ...

## Use special frameworks or library for edge devices:

- NVIDIA TensorRT
    
- TensorFlow Lite: TensorFlow Lite on Microcontroller Gesture Recognition OpenMV/Tensorflow/ studio.edgeimpulse.com
    
- TensorFlow.js
    
- PyTorch Lightning
    
- PyTorch Mobile
    
- Intel® Distribution of OpenVINO Toolkit
    
- CoreML
    
- ML kit
    
- FRITZ
    
- MediaPipe
    
- Apache TVM
    
- TinyML: enabling ultra-low power machine learning at the edge tiny machine learning with Arduino
    
- Libraries: ffmpeg, GStreamer, celery,
    
- GPU library for python: PyCUDA, NumbaPro, PyOpenCL, CuPy
    

Moreover, think about deep learning model for your specific hardware at first stage.

## In some case you need to enhance model for inference. There are many techniques to use such as,

- Pruning
    
- Quantization
    
- Distillation Techniques
    
- Binarized Neural Networks (BNNs)
    
- Apache TVM (incubating) is a compiler stack for deep learning systems
    
- Distributed machine learning and load balancing strategy
    
- Low rank matrix factorization (LRMF)
    
- Compact convolutional filters (Video/CNN)
    
- Knowledge distillation
    
- Neural Networks Compression Framework (NNCF)
    
- Parallel programming
    

## How

Distributed machine learning and load balancing strategy

Pruning

model pruning: reducing redundant parameters which are not sensitive to the performance. aim: remove all connections with absolute weights below a threshold. 🤔go for bigger size of network with many layers then pruning much better and faster

Quantization

The best way is using Google library which support most comprehensive methods

compresses by reducing the number of bits used to represent the weights quantization effectively constraints the number of different weights we can use inside our kernels per channel quantization for weights, which improves performance by model compression and latency reduction.

training a compact neural network with distilled knowledge of a large model distillation (knowledge transfer) from an ensemble of big networks into a much smaller network which learns directly from the cumbersome model's outputs, that is lighter to deploy

Distillation Techniques

Distill-Net: Application-Specific Distillation of Deep Convolutional Neural Networks for Resource-Constrained IoT Platforms

Binarized Neural Networks (BNNs)

It is not support by GPU hardware such as Jetson Nano. mostly based on CPU

Apache TVM (incubating) is a compiler stack for deep learning systems

challenges with large scale models deep neural networks are: expensive computationally expensive memory intensive hindering their deployment in:devices with low memory resources applications with strict latency requirements other issues:data security: tend to memorize everything including PII bias e.g. profanity: trained on large scale public datas elf discovering: instead of manually configuring conversational flows, automatically discover them from your data self training: let your system train itself with new example s self managing: let your system optimize by itself knowledge distillation

Distributed machine learning and load balancing strategy

run models which use all processing power like CPU,GPU,DSP,AI chip together to enhance inference performance. dynamic pruning of kernels which aims to the parsimonious inference by learning to exploit and dynamically remove the redundant capacity of a CNN architecture. partitioning techniques through convolution layer fusion to dynamically select the optimal partition according to the availability of computational resources and network conditions.

Low rank matrix factorization (LRMF)

there exists latent structures in the data, by uncovering which we can obtain a compressed representation of the dataLRMF factorizes the original matrix into lower rank matrices while preserving latent structures and addressing the issue of sparseness

Compact convolutional filters (Video/CNN)

designing special structural convolutional filters to save parameters replace over parametric filters with compact filters to achieve overall speedup while maintaining comparable accuracy

Knowledge distillation

Neural Networks Compression Framework (NNCF)

AI Edge: How to inference deep learning models on edge/IoT  Enabling efficient high-performance Accelerators/Optimization on Deep Learning

if the object is large and we do not need small anchor

in mobileNet we can remove small part of network which related to small objects. in YOLO reduce number of anchor. decrease size of image input but reduce the accuracy

Parallel programming and clean code, design pattern,


# Recommended ML Optimization and ML solutions and Project Workflow

A) 1. specify the use case 2. specify model interface 3. how would we monitor performance after deployment? 4. how can we approximate post-deployment monitoring before deployment? 5. build a model and iteratively improve it 6. deploy the model 7. monitor performance

B) - input/output -> write down - always answered these two question: - what is your are metric? - How do you split your data? - imbalance - exercise - precision(specificity, sensitivity{recall}, imbalance) - what is use case? - what is your one metric? Auto ML use this one

C)

- Training
    - build a baseline
    - do automated hyper-parameters
    - never randomly data-set split

D) 1. how to program training 2. train and not work know how to 1. debug it and how to fix it 2. experience trick 3. data since 3. train and work but not in developed -> split data 1. post deployment 1. monitoring before deployment 2. where data come from, where will come from, how to collected, how change to time 3. roc/ac = not sensitive with imbalance data 4. persition / recall = sentience because persisting secretive to imbalance data

E)

- How to right way collect data?
    - kaggle
    - Ray

F)

- After Training deep learning model
    - Parameter pruning
        - model pruning: reducing redundant parameters which are not sensitive to the performance.
            - aim: remove all connections with absolute weights below a threshold
- Quantization
    - compresses by reducing the number of bits used to represent the weights quantization effectively constraints the number of different weights we can use inside our kernels per-channel quantization for weights, which improves performance by model compression and latency reduction. Low rank matrix factorization (LRMF) there exists latent structures in the data, by uncovering which we can obtain a compressed representation of the data LRMF factorizes the original matrix into lower rank matrices while preserving latent structures and addressing the issue of sparseness Compact convolutional filters (Video/CNN) designing special structural convolutional filters to save parameters replace over parametric filters with compact filters to achieve overall speedup while maintaining comparable accuracy Knowledge distillation training a compact neural network with distilled knowledge of a large model distillation (knowledge transfer) from an ensemble of big networks into a much smaller network which learns directly from the cumbersome model's outputs, that is lighter to deploy Binarized Neural Networks (BNNs) Apache TVM (incubating) is a compiler stack for deep learning systems Neural Networks Compression Framework (NNCF) Deep learning model in production security: controls access to model(s) through secure packaging and execution Test auto training using parallel processing and library such as GStreamer

G) [https://www.tiziran.com/topics/events/ai-hardware](https://www.tiziran.com/topics/events/ai-hardware) [https://www.tiziran.com/topics/events/openvino-deep-learning](https://www.tiziran.com/topics/events/openvino-deep-learning) [https://www.tiziran.com/topics/hardware](https://www.tiziran.com/topics/hardware)