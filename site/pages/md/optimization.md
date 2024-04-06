# Ensemble learning
- multiple weak models are trained on data and then combined to create a single strong model
- Methods
    - Boosting
        - adaptive boosting, gradient boosting & (XGBoost), 
    - Bagging
        - random forest, 
    - Stacking
        - sklearn.ensemble.StackingClassifier
- compare 
| Ensemble Method | Training Data Sampling | Base Model Bias | Base Model Variance | Train Speed | Predict Speed | Interpretability |
|-----------------|------------------------|-----------------|---------------------|-------------|---------------|------------------|
| Boosting        | Weighted for errors    | High            | Low                 | Slow        | Fast          | Low              |
| Bagging         | Random                 | Low             | High                | Moderate    | Moderate      | Low              |
| Stacking        | None                   | Low             | High                | Moderate    | Moderate      | Low              |


Thank you to my 9,000+ LinkedIn followers! Your support motivates me to share more about AI, machine learning, computer vision, and more. Let's keep exploring technology together. Follow for updates. #AI #ML #ComputerVision #LLM


# LLM (Large Langure Model) & DL ( Deep Learning ) Model Optimization and Tuning for CV (Computer Vision)

### Target *Inference* Deployment Platform:
#### better accuracy: higher model metrics(like F1), avoid variance and bias
#### lower costs: smaller model sizes, minimal inference latency, lower CPU, GPU, memory, and disk requirements

- IoT & Edge Devices: Focus on techniques like quantization, pruning, and model architecture search (NAS) to reduce model size and computational complexity while maintaining accuracy. Utilize libraries like TensorFlow Lite Micro or TFLite for Microcontrollers.
- Cloud Platforms (e.g., AWS): Leverage hardware acceleration (GPUs, TPUs) and efficient data pipelines for faster inference. Explore frameworks like PyTorch or TensorFlow with distributed training capabilities.
- Local Laptop/PC: Balance model size and accuracy based on your hardware specifications. Consider techniques like knowledge distillation to transfer knowledge from a larger model.
Training, Fine-Tuning, and Transfer Learning

### Target Training Environment:training, fine-tuning, transfer learning, ... 
#### lower training time, 
batch normalization
- normalize inputs before each hidden layer to be same scale, center and scale, help with higher accuracies with lower epochs, additional computations and increase inference time
optimizers
    - SGD (stochastic gradient descent)
    - RMSprop
    - Adam
    - Adagrad


#### higher the batch size: better GPU utilization, lower number of training iterations, instability during training progree

- IoT & Edge Devices: Utilize on-device learning techniques or federated learning for privacy-preserving training on distributed devices.
- Cloud Platforms (e.g., AWS): Leverage cloud resources for large-scale datasets and high-performance computing for training complex models. Explore cloud-based training platforms like Amazon SageMaker or Google AI Platform.
- Local Laptop/PC: For smaller datasets or experimentation, train models locally. Consider using libraries like PyTorch or TensorFlow with GPU acceleration if available on your machine.




# RL
- agenent
- action
- environment
- reward
- policy
- goal


---

---


pattern matching





- Hardware-Aware Optimization 
    - Optimizing models for specific hardware platforms by leveraging techniques like hardware co-design and exploiting hardware accelerators.
- Energy-Efficient Training and Inference
    - Developing algorithms and tools that minimize the energy consumption during training and deploying large language models.
- Parameter/Model Pruning
    - This involves removing unnecessary or redundant parameters from a neural network that do not contribute significantly to the output. 
    - It helps reduce the size of the model and its computational complexity.
- Quantization
    - This process reduces the precision of the weights and activations of models from floating-point to lower-bit integers, decreasing the model size and speeding up inference with minimal loss in accuracy.
- Binarized Neural Networks (BNNs)
    - These networks use binary values for activations and weights instead of floating-point numbers, significantly reducing memory usage and computational requirements.
- Low Rank Matrix Factorization (LRMF)
    - This technique decomposes matrices into lower rank approximations, reducing the number of parameters in fully connected layers and thus the computational complexity.
- Compact Convolutional Filters
    - This involves designing or using convolutional filters that require fewer parameters and operations, maintaining performance while reducing computational load.
- Knowledge Distillation
    - A smaller model (student) is trained to mimic a larger, pre-trained model (teacher). This allows the smaller model to achieve high accuracy while being more efficient.
- Adaptive Sparsity
    - This technique dynamically adjusts the level of pruning during training, allowing for a more granular control over the trade-off between model size and accuracy.
- Architecture Search
    - Utilizing reinforcement learning or evolutionary algorithms to automatically search for optimal network architectures that are efficient and accurate for a specific task.
- Code Size Optimizations for Embedded Systems
    - Techniques and strategies to reduce the code size of applications, especially for embedded systems. 
    - This includes compiler optimizations and software engineering techniques to manage the trade-offs between code size and performance, and specific compiler flags to reduce binary size
- Optimizing Machine Learning Models for IoT Applications
    - Approaches to make ML/AI applications more efficient in embedded or constrained environments, focusing on low latency, low bandwidth, and low power consumption. Strategies include structuring code effectively, model size reduction post-training, and ensemble methods for compact model representation
- Optimized Model Deployment
    - Strategies for deploying models efficiently using web frameworks, cloud services, Kubernetes for scalable applications, TensorFlow/PyTorch serving for optimized model serving, and Apache TVM for compiling deep learning systems for improved deployment efficiency