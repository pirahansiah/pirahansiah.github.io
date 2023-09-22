# Step 1: Before Starting Your Machine Learning Project
* What is your inference hardware?
- What is the use case for your model?
- What is the model interface?
- How will you monitor performance after deployment?
- How can you approximate post-deployment monitoring before deployment?


## Tips for building and deploying a successful machine learning project:

- **Select the right model:** There are many different types of machine learning models available, and the best model for your project will depend on the specific requirements of your use case. It is important to do your research and select a model that is well-suited for your needs.
- **Split your data:** It is important to split your data into training and validation sets. The training set will be used to train your model, and the validation set will be used to evaluate the performance of your model.
- **Use a metric:** It is important to use a metric to measure the performance of your model. The most common metric for machine learning is accuracy, but other metrics such as precision and recall may be more appropriate for your use case.
- **Monitor performance:** It is important to monitor the performance of your model after deployment. This will help you to identify any potential problems with your model, and to make necessary adjustments.

## When selecting a CNN model for your project, it is important to consider the following factors:

- **The size of your dataset:** If you have a small dataset, you may want to choose a simpler CNN model. A simpler model will be easier to train, and it may be less likely to overfit your data.
- **The complexity of your task:** If you are working on a complex task, such as object detection or image segmentation, you may want to choose a deeper CNN model. A deeper model will be able to learn more complex features, and it may be able to achieve better performance.
- **The resources you have available:** Training a CNN model can be computationally expensive. If you do not have access to a powerful GPU, you may want to choose a simpler CNN model.


# Step 2: Per processing

## a

## Golden Rules of Deep Learning Performance:

1. **Use the right hardware.** The hardware you use to train and deploy your deep learning models can have a significant impact on their performance.
2. **Choose the right model.** The type of deep learning model you choose can also have a big impact on its performance.
3. **Prepare your data properly.** The quality and preparation of your data can have a major impact on the performance of your deep learning models.
4. **Use the right hyperparameters.** The hyperparameters you use to train your deep learning models can also have a significant impact on their performance.
5. **Regularize your models.** Regularization can help to prevent overfitting and improve the performance of your deep learning models.
6. **Augment your data.** Data augmentation can help to improve the performance of your deep learning models by increasing the size and diversity of your dataset.
7. **Use a distributed training framework.** A distributed training framework can help you to train your deep learning models faster and more efficiently.
8. **Use a cloud computing platform.** A cloud computing platform can provide you with access to the hardware and software you need to train and deploy your deep learning models.
9. **Monitor your models.** It is important to monitor the performance of your deep learning models after they are deployed. This will help you to identify any potential problems and make necessary adjustments.
10. **Keep your models up to date.** As new data becomes available, you should retrain your deep learning models to improve their performance.

# Step 3: Training

## - PyTorch: How to speed up the training by utilizing the multiple process capabilities of the PyTorch DataLoader class [num_workers (int, optional)]. [https://www.linkedin.com/posts/pirahansiah_pytorch-dataloader-numworkers-deep-learning-activity-6819171661846212608-umQR](https://www.linkedin.com/posts/pirahansiah_pytorch-dataloader-numworkers-deep-learning-activity-6819171661846212608-umQR) 
- Common solution for under-fitting or over-fitting: check data-set, error analysis, choose a different model architecture, hyper-parameter tuning [https://www.linkedin.com/feed/update/urn:li:activity:6790011538192273408](https://www.linkedin.com/feed/update/urn:li:activity:6790011538192273408)  
    

- Under-fitting (reducing bias): 

- ⬆ bigger model ⬇reduce regularization 🤔 error analysis 🤔 different model architecture 🤔 tune hyper-parameters ⬆️ add features  
    

- over-fitting (reducing variance):

- ⬆ add more training data ⬆ add normalization (batch norm, layer norm) ⬆add data augmentation ⬆ increase regularization (dropout, L2, weight decay) 🤔 error analysis 🤔 choose a different model architecture 🤔 tune hyper-parameters ⬇ early stopping ⬇ remove features ⬇ reduce model size

- Machine Learning Engineering for Production (MLOps) Specialization by Coursera; COURSE 3 Machine Learning Modeling Pipelines in Production - Week 1: Neural Architecture Search (NAS) - AutoML, Hyperparameter tuning, Cloud AutoML ; [https://www.linkedin.com/posts/pirahansiah_automl-nas-hyperparameter-activity-6823154343190007808-t4Ax](https://www.linkedin.com/posts/pirahansiah_automl-nas-hyperparameter-activity-6823154343190007808-t4Ax)


# Step 4

**Post processing**

- Method for offline 

model compression and acceleration: reducing parameters without significantly decreasing the model performance  
parameter pruning  
aim: remove all connections with absolute weights below a threshold  
quantization  
compresses by reducing the number of bits used to represent the weights  
quantization effectively constraints the number of different weights we can use inside our kernels  
low rank matrix factorization (LRMF)  
there exists latent structures in the data, by uncovering which we can obtain a compressed representation of the data  
LRMF factorizes the original matrix into lower rank matrices while preserving latent structures and addressing the issue of sparseness  
compact convolutional filters (Video/CNN)  
designing special structural convolutional filters to save parameters  
replace over parametric filters with compact filters to achieve overall speedup while maintaining comparable accuracy  
knowledge distillation  
training a compact neural network with distilled knowledge of a large model  
distillation (knowledge transfer) from an ensemble of big networks into a much smaller network which learns directly from the cumbersome model's outputs, that is lighter to deploy  
Binarized Neural Networks (BNNs)  
TVM

- Performance optimization II: several other methods for improve the machine learning performance [https://www.linkedin.com/posts/pirahansiah_computervision-ai-objectdetection-activity-6787871627586625536-OPO5](https://www.linkedin.com/posts/pirahansiah_computervision-ai-objectdetection-activity-6787871627586625536-OPO5) 
- How to Improve Deep Learning Performance [https://www.linkedin.com/posts/pirahansiah_enablingefficient-highabrperformance-accelerators-activity-6781262923420471296-vIH3](https://www.linkedin.com/posts/pirahansiah_enablingefficient-highabrperformance-accelerators-activity-6781262923420471296-vIH3)


# step 5:
**Monitoring performance and adaptation** 

- Update
- Full Stack Deep Learning ([fullstackdeeplearning.com](http://fullstackdeeplearning.com/)) [https://www.linkedin.com/feed/update/urn:li:activity:6792171813267873792](https://www.linkedin.com/feed/update/urn:li:activity:6792171813267873792)  notes for week 1 to week 12 of Full Stack Deep Learning: (April 2021)