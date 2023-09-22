* Why 
	* Autonomous Cars
	* Tracking
	* Video Search/Analysis
* Traditional Object Tracking
	* Advantages:
		- Fast and easy to use
		- Many research papers and codes available
		- Real-time capability
	- Disadvantages:
		- Limited to selected objects
		- Low resolution videos
		- Low accuracy
- OpenCV Object Tracking Algorithms:
	1. BOOSTING Tracker: 
		1. Based on the same algorithm as Haar cascades (AdaBoost), 
		2. but slow and less efficient. Used mainly for legacy purposes and algorithm comparison.
	2. MIL Tracker: Provides better accuracy but suffers from reporting failure.
	3. KCF Tracker (Kernelized Correlation Filters): Faster than BOOSTING and MIL, but less efficient when there are changes in size and position of the object.
	4. TLD Tracker: Suffers from false positives and abnormal behavior. Not recommended for use.
	5. Median Flow Tracker: Good at reporting failures but fails with large motion jumps and fast motion.
	6. MOSSE Tracker: Very fast but less accurate than CSRT or KCF. Suitable for scenarios where speed is prioritized.
	7. CSRT Tracker (Discriminative Correlation Filter with Channel and Spatial Reliability): More accurate but slightly slower than KCF.
	8. Object Detection via template matching & Tracking by Kalman filter.
* Object Tracking Categories:
	* based on number of object
		- Single Object Tracking (SOT)
		- Multi-Object Tracking (MOT) including Multi-Target Tracking (MTT) and Multi-Class Multi-Object Tracking (MCMOT)
		- Multi-Camera Multi-Class Multi-Object Tracking (MCMCMOT)
	- Methods based on the number of stages:
		- One stage
		- Two stages
		- Pruning and merging
			- Pruning : remove hypotheses with small weights (and re-normalize)
			- Merging: approximate a mixture of densities by a single density (often Gaussian)
			- Gating: technique to disregard unreasonable detection 
				- Gaussian densities
				- Nearest neighbor (NN) filter [pruning]
				- Probabilistic data association (PDA) filter [merging]
				- Gaussian mixture densities
				- Gaussian sum filter (GSF) [pruning/merging]
	- 2D, 3D, ...
- Deep Learning Object Tracking:
	- YOLO: One-stage object detection algorithm : v3,4,5,6,7,8
	- Deep SORT: Integrates object detection and tracking, but may face memory issues after some frames
	- JDE (Joint Detection and Embedding): PyTorch implementation for accurate multi-object tracking
	- CenterTrack: Tracks objects as points in real-time
	- YolactEdge: Real-time instance segmentation on the edge using AI coordination
- Other Resources:
	- MediaPipe Objectron: Mobile real-time 3D object detection solution for everyday objects
	- MOTS (Multi-Object Tracking and Segmentation): Benchmark dataset and evaluation metrics for pixel-level tracking and segmentation
	- ROLO, SiamMask, Deep SORT, TrackR-CNN, Tracktor++, JDE: Various object tracking algorithms and implementations
	- Training resources for deep multi-object trackers
- Jetson Nano for DeepSORT:
	- Requires JetPack 4.4.1 and TensorFlow installation with specific versions of numpy and h5py
	- Memory issues can be addressed by disabling the GUI and increasing swap memory
	- DeepSORT's implementation based on TensorFlow version 1 has a speed of less than 1 FPS
	- Resources provided for turning off the GUI, increasing swap memory, and running DeepSORT on Jetson Nano
- Object Tracking Datasets:
	- MOTChallenge, MOT15, MOT16/17, MOT19: Datasets for evaluating object tracking algorithms
	- KITTI: Dataset for object tracking in autonomous driving scenarios
	- UA-DETRAC: Tracking benchmark dataset