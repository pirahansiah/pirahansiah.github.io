KerasCV
JAX backend
CVAT
YOLO
RCNN
CLIP facebook
UNIT TEST
GOOGLE TEST
array in protobuf is repeat

Vision Transformer (ViT) (Doso- vitskiy et al., 2021; Vaswani et al., 2017)
architecture AWS, LLM


Several components in the Genie architecture are based on the Vision Transformer (ViT) (Doso- vitskiy et al., 2021; Vaswani et al., 2017). No- tably, the quadratic memory cost of transformers poses challenges for videos, which can contain up to 𝑂(104) tokens. We thus adopt a memory efficient ST-transformer architecture (inspired by Xu et al. (2020), see Figure 4) across all model components, balancing model capacity with com- putational constraints.

1 × 𝐻 × 𝑊 tokens within each time step, and in the temporal layer attends over 𝑇 × 1 × 1 tokens across the 𝑇 time steps.
1) a latent action model that infers the latent action 𝒂 between each pair of frames and 
2) a video tokenizer that converts raw video frames into discrete tokens 𝒛 and 
3) a dynamics model that, given a latent action and past frame tokens, predicts the next frame of the video. 
VQ-VAE- based objective (van den Oord et al., 2017)
Video Tokenizer Following prior work (Gupta et al., 2023; Villegas et al., 2023; Yan et al., 2023), we compress videos into discrete tokens to re- duce dimensionality and enable higher quality video generation
ST-transformer based tokenizer (ST- ViViT) is much more compute efficient with the dominating factor in its cost increasing linearly with the number of frames.


Training Details Flowchart:

1. Video Tokenizer
   - Parameters: 200M
   - Patch Size: 4
   - Codebook: Embedding Size 32, 1024 Unique Codes
   - Objective: Optimal Trade-off Between Reconstruction Quality and Downstream Performance

2. Latent Action Model
   - Parameters: 300M
   - Patch Size: 16
   - Codebook: Embedding Size 32, 8 Unique Codes (Latent Actions)

3. Common Modelling Components
   - Sequence Length: 16 Frames
   - FPS: 10
   - Training Enhancements: bfloat16, QK Norm
     - Purpose: Stabilize Training at Large Scale
     - References: Dehghani et al., 2023; Henry et al., 2020

4. Inference Time
   - Procedure: 25 MaskGIT Steps per Frame
   - Temperature: 2
   - Sampling Method: Random Sampling

Tokenizer architecture ablations We com- pare the performance of three choices of tokeniz- ers, including 1) (spatial-only) ViT, 2) (spatial- temporal) ST-ViViT and 3) (spatial-temporal) C- ViViT (Table 3). For comparison we use similar number of parameters for all tokenizers, with patch size 10, batch size 128 and sequence length 16. We then train the same dynamics and latent action model on these three different tokenizers, and report their FVD as well as Δ PSNR.
𝑡
Table 3 | Tokenizer architecture ablation: Our ST-ViViT architecture results in the best perform- ing tokenizer.
1B 257.8 1.65 1B 136.4 2.07
ViT
C-ViViT (Villegas et al., 2023) ST-ViViT (ours)
#Params Memory
230M 0.3GB 225M 1.6GB 205M 0.9GB
FVD (↓) 114.5
272.7
81.4
Δ PSNR(↑) 𝑡
1.39 1.37 1.66



Training Agents




spatial attention layer

onnx
spatiotemporal video tokenizer
an autoregressive dynamics model
a simple and scalable latent action model
MaskGIT (Chang et al., 2022)


stable diffusion
transformers
NeRFs
gaussian splatting
vision sensor fusion robotics
fine tune image llm


play countors twise to remove other objects inside big objects
aws
celue? activation dl
MLOPs
transformer

* biyas and variance in DL?
MQTT
OpenVINO
FastAPI
RCNN
COCO
Multi object tracking
LVIS= traine on rare categories
panoptic
pytorch
lamacpp
ggml->gguf
quantizaed
llava
detectron 2
attention
autoencoder
transfer learing= train on a task and adapt to different task
full stack mlops





---
# Exploring the Landscape of Modern Machine Learning: Key Models and Innovative Methods
- Stable Diffusion
    - A text-to-image model generating high-quality images from textual descriptions.
    - Other Methods
        - Latent Diffusion Models, Generative Adversarial Networks (GANs), VQ-VAE-2.
- Transformers
    - A deep learning model architecture known for its effectiveness in handling sequential data.
    - Other Methods
        - BERT, GPT-3, Transformer-XL.
        - mT5 (Multi-Task Tuning Transformers)
            - A model trained on a massive dataset of text and code, allowing it to perform various tasks like translation, question answering, and code generation.
        - Jurassic-1 Jumbo
            - A giant Transformer model pushing the boundaries of capabilities in tasks like summarization, question answering, and few-shot learning. 
- NeRFs (Neural Radiance Fields)
    - A method for constructing 3D scenes from 2D images using deep learning.
    - Other Methods
        - Mip-NeRF, NeRF-W, Instant NGP.
        - NeRF-++
            - A method that addresses the limitations of the original NeRF by introducing a hierarchical structure for more efficient rendering.
- Gaussian Splatting
    - A technique used in graphics and visualization for smoothing or interpolating data points.
    - Other Methods
        - Kernel Density Estimation, Radial Basis Function Interpolation, Moving Least Squares.
        - Kernel Regression with Splatting
            - This technique combines Gaussian Splatting with kernel regression for improved data fitting and noise reduction.
        - Splatting CNNs
            - Integrating Gaussian Splatting with Convolutional Neural Networks for tasks like point cloud processing and image segmentation.
- Fine-Tune LLM
    - Transfer Learning
        - Leverage the knowledge from a pre-trained model and apply it to a similar but different task. This is the essence of fine-tuning.
    - Few-shot Learning
        - Provide examples of the task within the input to guide the model on how to respond. This is particularly effective with models like GPT-3.
    - Zero-shot Learning
        - Adapt the model to perform tasks without any task-specific data during training, relying on its pre-existing knowledge.
    - Prompt Engineering
        - Developing effective prompts to guide the LLM towards the desired task or output becomes increasingly crucial.
    - Continual Learning
        - Techniques that allow LLMs to learn new tasks without forgetting previously learned ones.



- Vision Sensor Fusion Robotics
    - Combining data from multiple vision sensors in robotics for improved perception.
    - Other Methods
        - Multi-Camera Systems, LiDAR-Camera Fusion, Radar-Vision Fusion.
- Fine Tune Image LLM (Large Language Models)
    - Adapting pre-trained large language models to image-related tasks.
    - Other Methods
        - CLIP, DALL-E, Image GPT.
- AWS (Amazon Web Services)
    - A comprehensive cloud computing platform offering various services.
    - Other Services
        - AWS Lambda, Amazon S3, Amazon EC2.
- CELUE Activation (DL)
    - A misinterpretation or typo; likely meant "ReLU" (Rectified Linear Unit) activation in deep learning.
    - Other Methods
        - Leaky ReLU, Parametric ReLU, ELU (Exponential Linear Unit).
- MLOps (Machine Learning Operations)
    - Practices for collaboration and communication between data scientists and operations professionals.
    - Other Concepts
        - Continuous Integration/Continuous Deployment (CI/CD) for ML, Model Monitoring, Model Versioning.
- Transformer
    - A model architecture using self-attention mechanisms, primarily for natural language processing tasks.
    - Other Methods
        - Vision Transformers, Audio Transformers, Time Series Transformers.
- Bias and Variance in DL (Deep Learning)
    - Bias is an error from erroneous assumptions, variance is an error from sensitivity to small fluctuations.
    - Related Concepts
        - Overfitting, Underfitting, Regularization.
- MQTT (Message Queuing Telemetry Transport)
    - A lightweight messaging protocol for small sensors and mobile devices.
    - Related Technologies
        - AMQP (Advanced Message Queuing Protocol), CoAP (Constrained Application Protocol), WebSockets.
- OpenVINO (Open Visual Inference and Neural Network Optimization)
    - A toolkit from Intel for optimizing deep learning models.
    - Related Technologies
        - TensorFlow Lite, NVIDIA TensorRT, ONNX Runtime.
- FastAPI
    - A modern, fast web framework for building APIs with Python.
    - Related Technologies
        - Flask, Django, Tornado.
- RCNN (Regions with CNN features)
    - A deep learning algorithm for object detection.
    - Evolution
        - Fast RCNN, Faster RCNN, Mask RCNN.
- COCO (Common Objects in Context)
    - A large-scale dataset for object detection, segmentation, and captioning.
    - Related Datasets
        - ImageNet, Pascal VOC, Open Images.
- Multi-Object Tracking
    - Tracking multiple objects as they move across frames in a video.
    - Related Concepts
        - DeepSORT, MOT Challenge, Siamese Networks.
- LVIS (Large Vocabulary Instance Segmentation)
    - A dataset for instance segmentation focusing on long-tail distribution of objects.
    - Related Concepts
        - Few-shot Learning, Zero-shot Learning, Class-balanced Loss.
- Panoptic Segmentation
    - Combines semantic segmentation (classifying pixels) and instance segmentation (identifying object instances).
    - Related Concepts
        - Panoptic FPN, UPSNet, Panoptic DeepLab.
- PyTorch
    - An open-source machine learning library for Python, known for its flexibility and dynamic computation graphs.
    - Related Libraries
        - TensorFlow, JAX, MXNet.
- LamaCPP
    - Likely a typo or specific library/tool not widely recognized without further context.
- General Area
    - Consider exploring libraries related to Llama for large language models, or CPP for C++ based ML implementations.
- GGML->GGUF
    - Not a widely recognized term or transition; possibly specific to a context or a typo.
- Suggestion
    - Review for correct terminology or specific domain applications.
- Quantized
    - Refers to the process of reducing the precision of weights and activations in neural networks to accelerate inference.
- Related Technologies
    - Quantization













---
# To know
- less *.cpp :n :p q
- opencv all functions into cmake, opencv world : yes, buld_shared_libs off, static no need dll, it change 200K to 18MB for statics; c/c++>code generation>runtime library>multi-threaded(/mt)

