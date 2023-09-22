# Why self-collected dataset

* Common dataset construction issues
	* Not enough data
	* class imbalances
	* noisy labels
	* train/test from different distributions
	* different camera system/hardware
* resolution & distance: 
	* the size of object will be different  
* number of objects
	* 1 object: SOT
	* 2 or more objects: MOT
	* multiple objects for different. classes: MCMOT
* camera
	* static camera
	* moving camera
	* moving object
	* static object 
* FPS
* different time of day
* out door or indoor
* different light condition
* different camera system
	* cheap camera
	* high quality camera
	* OpeCV AI Kit
	* depth camera
* image or video
* color space
	* RGB
	* HSV
* pre processing 
	* normalization
		* Normalization usually means scaling a variable to have values between 0 and 1
	* Standardizing
		* standardizing data turns it into having a mean of 0 and a standard deviation of 1
	* balance data
	* data augmentation
	* generate data by using GAN
	* Rebuilding missing data
* privacy:
	* federated learning: training a global model from data on local devices, without ever having access to the data
	* differential privacy: aggregating data such that individual points cannot be identified
	* learning on encrypted data
* Data versioning:
	* level 0: filesystem/S3:
	* level 1: snapshot, version deployed
	* level 2: mix of assets and code, JSON, lazydata, git signature
	* level 3: DVC, pachyderm, Quill, delta lake, git large file storage, dolt, lakeFS
* data labeling:
	* training the annotators is crucial
	* CVat
	* Ultimate labeling
	* label studio
* use case OCR
	* Receipt : crinkliness, curvature, alignment with camera, ink fededness, paper glossiness
	* table material
	* camera: flash, location, direction, exposure, focal distance, aperture size
	* environment ambient brightness
	* primary light location
