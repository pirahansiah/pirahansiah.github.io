Supervised fine-tuning means updating a pre-trained language model using labeled data to do a specific task. The data used has been checked earlier. 

LLaVA-13B with 4-bit quantization allows you to run on a GPU with as few as 12GB VRAM! 
QLoRA by Dettmers et al., short for quantized LoRA, is a technique that further reduces memory usage during finetuning. 
Model Size: Large Language Models (LLMs) are massive, with billions of parameters, making them resource-intensive to work with.
Gradients: Storing gradients for a 7-billion-parameter LLM alone requires a whopping 28GB of memory.
Optimizers: Advanced optimizers like AdamW are commonly used in LLM fine-tuning, contributing to memory requirements.
Precision Change: Transitioning from 32-bit floating-point precision to 16-bit can halve memory usage, but it comes with a trade-off of reduced representational capacity.
Quantization: Quantization is a technique that maps continuous values to discrete ones, a strategy employed to reduce memory usage. However, it necessitates a careful balance between memory efficiency and model accuracy.
During training, optimizers also store gradients, and this is what explains that the actual memory usage is 2x - 3x bigger. Additionally, the memory usage will also increase as per the batch size.

16 bytes per param * 1B = 16GB per param. That's 48GB for a 3B param model and 112GB for a 7B
112GB for a 7B gets us to about 20% the 8x A100 memory


Llama-7B model weight is around 12 GB. That means we require ~48 GB+ GPU memory per card to finetune Llama-7B. The typical A-100 GPU card available on AWS has a memory of only 40 GB.
Activations too consume GPU memory. These are dependent on your batch size and sequence length (the easiest knobs to turn).

QLoRA is now the default method for fine-tuning large language models (LLM) on consumer hardware. For instance, with QLoRA, we only need 8 GB of GPU VRAM to fine-tune Mistral 7B and Llama 2 7B while a standard fine-tuning would require at least 24 GB of VRAM.

QLoRA reduces memory consumption thanks to 4-bit quantization. This is usually performed with the bitsandbytes package which optimizes the quantization and QLoRA fine-tuning on GPU.


M1 Max and 32GB of system memory, batch size 1 and LoRA layers 4 
Nvidia RTX 4090 (24GiB)
M2 Ultra with 192GB 

Method	Speed	Memory
Gradient accumulation	No	Yes
Gradient checkpointing	No	Yes
Mixed precision training	Yes	No*
Batch size	Yes	Yes
Optimizer choice	Yes	Yes
DataLoader	Yes	No
DeepSpeed Zero	No	Yes

Fine-tuning large language models (LLMs) that can generate and understand images, such as DALL·E, CLIP, Imagen, or Stable Diffusion, involves substantial computational resources. The exact amount of RAM needed depends on several factors including the model size (number of parameters), the complexity of your fine-tuning dataset, and the specific tasks you're training the model for. However, I can provide some general guidelines based on typical requirements:

Model Size and Parameters: Larger models with billions of parameters require significantly more RAM. Fine-tuning models like GPT-3, DALL·E 2, or Imagen could require tens to hundreds of gigabytes of RAM, often necessitating the use of specialized hardware with high RAM capacities.
Use of GPUs: Fine-tuning these models is usually done on GPUs or TPUs rather than CPUs due to their faster processing capabilities for parallel computations. The RAM in this context refers to GPU memory, which is critical for storing the model, its parameters, and the data being processed. High-end GPUs come with memory ranging from 24 GB (e.g., NVIDIA Tesla V100, A100) to 80 GB (A100 80GB version) or more.
Dataset Size: The size of your dataset for fine-tuning also affects memory usage. Larger datasets require more memory, but techniques like gradient accumulation can help manage memory demands by processing smaller batches of data.
Optimization Techniques: Techniques such as mixed-precision training (using both 16-bit and 32-bit floating-point numbers) can reduce memory usage and computational requirements, allowing for the fine-tuning of larger models on hardware with less GPU memory.
General Guidelines
For Small-Scale Models (tens of millions to a few hundred million parameters): You might be able to fine-tune on consumer-grade GPUs with 8-24 GB of RAM.
For Medium-Scale Models (up to a few billion parameters): Professional or high-end GPUs with 24-48 GB of RAM are often required.
For Large-Scale Models (tens of billions of parameters): You would likely need access to specialized AI hardware or cloud-based solutions with GPUs or TPUs that offer 80 GB or more of RAM per device. It's common to distribute the training process across multiple devices to manage the memory requirements.
Cloud-Based Solutions
For many users, cloud-based platforms like Google Cloud AI, AWS SageMaker, and Microsoft Azure AI provide access to high-end GPUs and TPUs, offering a way to fine-tune large models without the upfront cost of purchasing the hardware. These platforms can dynamically allocate resources based on the task's demands.

Conclusion
The precise amount of RAM needed for fine-tuning image-generating and understanding LLMs can vary widely. For most practical purposes, especially with the largest models, leveraging cloud computing resources or high-end dedicated AI hardware is the most feasible approach. Always consider your specific project needs and consult with the model's documentation and hardware requirements for more detailed recommendations.






===
The RAM (or more accurately for deep learning, GPU memory) required to fine-tune each image-to-text model varies significantly based on the model's architecture, the size of the model (number of parameters), and the dataset used for fine-tuning. Below are general guidelines on the GPU memory requirements for fine-tuning some of the notable image-to-text models. These are approximations, as the exact requirements can vary based on specific implementation details and optimization techniques used (such as mixed precision training, gradient checkpointing, etc.):

CLIP by OpenAI: Fine-tuning CLIP, given its dual nature of processing both images and text, would ideally require GPUs with at least 16 GB of memory for smaller datasets. For more extensive datasets or to experiment with larger batch sizes, 32 GB GPUs or using multiple GPUs through data parallelism would be beneficial.
Google's Vision API and Microsoft Azure Computer Vision: These are cloud-based services, and fine-tuning (if applicable) or custom model training would depend on the cloud infrastructure. The memory requirements would be managed by the cloud provider, and users can choose their compute resources based on need and budget.
DenseCap: For models like DenseCap that perform dense captioning, a minimum of 12-16 GB of GPU memory is recommended for effective fine-tuning, with more complex models benefiting from 24 GB or more.
Show and Tell: Early models like Show and Tell can be fine-tuned with relatively modest hardware, starting from 8 GB of GPU memory, but for better performance and larger datasets, 16 GB or more is advisable.
Neural Baby Talk, Oscar, VinVL, and BLIP: These more recent and complex models, which include object detection and detailed image analysis, generally require more substantial computational resources. Fine-tuning these models would typically need GPUs with at least 16-24 GB of memory. For larger datasets or to experiment with larger batch sizes, using high-end GPUs with 32 GB of memory or employing strategies like model parallelism across several GPUs would be more appropriate.
General Considerations:
Batch Size: Larger batch sizes require more memory but can lead to faster convergence. Adjusting the batch size is a common way to manage memory constraints.
Optimization Techniques: Techniques like mixed-precision training can reduce memory usage by nearly half, allowing for larger models or batch sizes on the same hardware. Gradient checkpointing is another technique that trades computational overhead for lower memory usage, useful for very large models.
Model Size: The number of parameters in a model is a significant factor in determining its memory requirements. Larger models with billions of parameters necessitate more memory.
Dataset Size: While the dataset size primarily affects storage and potentially CPU memory for preprocessing, it can also influence GPU memory usage based on how data is batched and fed into the model.
Cloud Computing:
When local resources are insufficient, cloud-based GPUs offer scalable solutions. Platforms like Google Colab, AWS, Microsoft Azure, and NVIDIA GPU Cloud provide access to high-end GPUs, allowing users to select the appropriate resources for their projects and only pay for what they use.

===


Reference:
[Models Memory](https://huggingface.co/docs/transformers/v4.20.1/en/perf_train_gpu_one#anatomy-of-models-memory)






https://www.linkedin.com/groups/10320678/
Active Group in LinkedIn, "Computer Vision ..." now boasting over 33,000 members! Dive into the world of Computer Vision, Generative AI, Edge Computing, Fine-tune Multimodal LLMs, Robotics, IoT, AR/VR, Medical Computer Vision, and much more.
Explore cutting-edge topics: From Generative AI, Vision Fusion AI, Inception, GPT, and Stable Diffusion to the intricacies of Fine-tuning LLMs and LangChain. Edge Computing & IoT, Multimodal LLMs, Robotics, Video Understanding, and beyond.
#ComputerVision
https://www.linkedin.com/groups/10320678/

# Computer Vision,Generative AI,Edge Computing,Fine-tune Multimodal LLMs,Robotics,IoT,AR/VR,Medical
Computer Vision, OpenCV
Generative AI, Vision Fusion AI, Inception, Generative Pretrained Transformer (GPT),Stable Diffusion,Fine-tune LLMs, LangChain
Edge Computing & IoT, 
Multimodal LLMs (Large Language Models)
Robotics
Video Understanding, Video Analysis, Video Tracking, Automated Human Behavior Recognition, Event Recognition in Video, Video Content Analytics, Time Series Features
https://www.linkedin.com/groups/10320678/


Group Guidelines: Avoid Sending Ads, Job Listings, or Event Notices



Computer Vision,Generative AI,Edge Computing,Multimodal LLMs,Robotics,IoT,AR/VR,Medical Imaging,Stable Diffusion,Fine-tune LLMs,LangChain,OpenCV

Computer Vision, AR/VR, Generative AI, Edge Computing, Multimodal Large Language Model; Robotics, IoT, Medical Image Processing; Stable Diffusion, fine-tune LLMs, ,LLaVA; LangChain, llama.cpp, OpenCV




Computer Vision, AR/VR, Generative AI, Edge Computing, Multimodal Large Language Model; Robotics, IoT, Medical Image Processing; Stable Diffusion, fine-tune LLMs, ,LLaVA; LangChain, llama.cpp


Computer Vision, AR/VR, mixed reality, Vision Fusion AI, #VisionAI #Transformers #MultimodalLearning, LangChain Building AI Agents, #llama.cpp
Apple Shakes Up Open-Source AI With MGIE Image Editor
MLX: Stable Diffusion for Local Image Generation on Apple Silicon
Vision Fusion AI: From Pixels to Perception #VisionAI #Transformers #MultimodalLearning
Computer Vision, Multi-Modal AI, Reinforcement Learning,OpenCV,TensorFlow,PyTorch,ChatGPT,Bard,AWS
Vision-Centric Applications: Learn about the latest in object detection, segmentation, and visual reasoning, leveraging large language models for improved contextual understanding.
Embodied AI: Explore how AI is bridging the gap with the physical world through robotics, understanding human motion, and providing personalized assistance.

Computer Vision, Deep Learning, OpenCV , ChatGPT
Hardware: PC, Mac, Server, Raspberry pi 3,4,5 with Camera Module V1, V2, V2.1
Deep learning chips: Intel® Neural Compute Stick 2 and Google Coral
Software: Linux (Ubuntu, Raspberry OS, ...), Mac OS,Windows, 
OpenCV , TensorFlow Lite, Google Coral SDK, Intel® Neural Compute Stick 2 SDK (OpenVINO)
C++, Image Processing, Machine Vision, Artificial Intelligence 
,Theano,
Automatically Caption Images, Inception, Convolutional Neural Network (CNN), Caffe, TensorFlow, Theano, Torch, DIGITS: LeNet, AlexNet, GoogLeNet; Solver type: Stochastic Gradient Descent (SGD),Nesterov’s Accelerated Gradient (NAG),Adaptive Gradient (AdaGrad),RMSprop,AdaDelta,Adam



# Edge + LLMs

## Generative AI and Edge Computing Overview

Generative AI, including large language models (LLMs) like ChatGPT, is becoming increasingly integrated into edge computing devices such as IoT gadgets, Raspberry Pis, Intel Neural Compute Sticks, and Nvidia Jetson modules. This shift aims to make advanced AI technologies more accessible for real-world applications, notably in computer vision and generative AI tasks.

### Edge Hardware Capabilities

Raspberry Pi 3/4 (with accelerator support)
Raspberry Pi 5
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







============
The basics for the calculation come down to the precision of model weights and the fine tuning method you’re using. Let’s assume for simplicity that you want to do a full model fine tune for a 7B parameter LLM in float 16bit precision. The calculation is as follows:

Bytes per parameter: 16 bits = 2 bytes

Total memory for model weights: 2 bytes * 7B parameters = 14B bytes = 14 GB

Now that’s just the memory to load the model weights onto the GPU. To do full model fine tuning you will also need to store optimizer states, gradients and other stuff on the GPU. Let’s continue breaking it down:

AdamW optimizer states: 2 per parameter = 28 GB

Gradients: 4 bytes * number of parameters = 28 GB

So excluding the data being used to train the model, we’re already looking at 70 GB which is more than single GPUs contain on the market.

So it’s pretty much impossible to do full model fine tuning of a LLM on a single GPU unless you’re leveraging every trick possible like 4 bit quantization, gradient accumulation/check pointing, etc. Instead, most people opt for LoRA fine tuning, in which case you can repeat this calculation but substitute in the number of parameters you will be fine tuning in the place of 7B.
he amount of RAM needed to fine-tune an LLM depends heavily on several factors:

 1. Size of the LLM: Larger models with more parameters naturally require more memory. For example, fine-tuning a 150B parameter model like Megatron-Turing NLG would require significantly more RAM than a 1.5B parameter model like Bard.

 2. Fine-tuning technique:

Full fine-tuning: This approach updates all model parameters, and typically requires the most RAM, often exceeding the capacity of single GPUs. Even smaller models like Bard might struggle with this on standard consumer hardware.
Adapter-based fine-tuning: Techniques like LoRA (Low-Rank Adaptation) utilize smaller "adapters" on top of the pre-trained model, significantly reducing memory requirements. For smaller models like Bard, LoRA can enable fine-tuning on a single GPU with 16GB RAM.
Knowledge distillation: While not yet widely successful, transferring knowledge from a larger model to a smaller one may require comparable RAM to the larger model for processing.
 3. Batch size: In a training batch, multiple data points are processed simultaneously. Larger batch sizes improve training efficiency but consume more memory. Finding a balance between efficiency and available RAM is crucial.

 4. Optimizations: Techniques like Automatic Mixed Precision (AMP) and gradient checkpointing can reduce memory footprint but might require specific hardware support or come with performance trade-offs.

 General RAM requirements:

Small models (under 1 billion parameters): LoRA-based fine-tuning might be achievable on 16GB RAM with optimizations.
Medium models (1-10 billion parameters): Full fine-tuning might require multiple GPUs or specialized hardware, even with optimizations. Adapter-based methods offer better possibilities on single high-end GPUs.
Large models (over 10 billion parameters): Full fine-tuning typically pushes beyond single machines, requiring distributed training setups across multiple GPUs or specialized AI accelerators. Even adapter-based methods might involve significant RAM on individual machines.
 Remember: It's more than just a "minimum RAM" requirement. Consider potential bottlenecks, optimization strategies, and trade-offs between efficiency and performance when planning your fine-tuning process.

 LLaVA-13B with 4-bit quantization allows you to run on a GPU with as few as 12GB VRAM! 
QLoRA by Dettmers et al., short for quantized LoRA, is a technique that further reduces memory usage during finetuning. 
Model Size: Large Language Models (LLMs) are massive, with billions of parameters, making them resource-intensive to work with.
Gradients: Storing gradients for a 7-billion-parameter LLM alone requires a whopping 28GB of memory.
Optimizers: Advanced optimizers like AdamW are commonly used in LLM fine-tuning, contributing to memory requirements.
Precision Change: Transitioning from 32-bit floating-point precision to 16-bit can halve memory usage, but it comes with a trade-off of reduced representational capacity.
Quantization: Quantization is a technique that maps continuous values to discrete ones, a strategy employed to reduce memory usage. However, it necessitates a careful balance between memory efficiency and model accuracy.
During training, optimizers also store gradients, and this is what explains that the actual memory usage is 2x - 3x bigger. Additionally, the memory usage will also increase as per the batch size.

16 bytes per param * 1B = 16GB per param. That's 48GB for a 3B param model and 112GB for a 7B
112GB for a 7B gets us to about 20% the 8x A100 memory


Llama-7B model weight is around 12 GB. That means we require ~48 GB+ GPU memory per card to finetune Llama-7B. The typical A-100 GPU card available on AWS has a memory of only 40 GB.
Activations too consume GPU memory. These are dependent on your batch size and sequence length (the easiest knobs to turn).

QLoRA is now the default method for fine-tuning large language models (LLM) on consumer hardware. For instance, with QLoRA, we only need 8 GB of GPU VRAM to fine-tune Mistral 7B and Llama 2 7B while a standard fine-tuning would require at least 24 GB of VRAM.

QLoRA reduces memory consumption thanks to 4-bit quantization. This is usually performed with the bitsandbytes package which optimizes the quantization and QLoRA fine-tuning on GPU.
