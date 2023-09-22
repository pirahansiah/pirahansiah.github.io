<p>MLOps</p><p>Coursera</p><p>TensorFlow</p>

- C1,2,3  
    - Scoping
        - Define project  
            - -  
                key metrics: accuracy, latency, throughput  
                estimate resources and timeline  
                
        - scoping process  
            - business problems  
                - things you wish were working better?  
                    
            - AI solutions  
                
            - Dilligence: assess the feasibility and value of potential solution  
                - use external benchmark  
                    
                - Un/Structured in new or existing  
                    - HLP; HLP (history of project);predictive feature avaible;&nbsp;  
                        
                - do we have features that are predictive?  
                    
                - history of project  
                    
                - value
            -   
                
            - determine milestones  
                
            - budget for resources  
                
        - modern software development  
            - scalability
            - extensibility
            - configuration
            - consistency &amp; reproducibility  
                
            - safety &amp; security  
                
            - modularity
            - testability
            - monitoring
            -   
                
    - data
        - define data and establish baseline  
            - is the data labeled consistently?  
                normalization  
                
            - data quality  
                - maximize predictive content  
                    
                - remove non-informative data  
                    
                - feature space coverage  
                    
                - inconsistent formatting, ...  
                    
                - fair; accountable; transparent; explainable  
                    
            - data pipeline: data collection, ingestion and preparation  
                
            - data collection and monitoring  
                - data and scope changes  
                    
                - ground truth changes slowly/faster/very fast  
                    
                - process feedback and human labeling  
                    
        - preprocessing
            - feature engineering  
                - operations
                    - data cleansing  
                        
                    - feature tuning  
                        
                    - representation transformation  
                        
                    - feature extraction  
                        
                    - feature construction  
                        
                    - Text: stemming, lemmatiozation, TF-IDF,n-grams,embedding lookup  
                        
                    - Images: clipping,resizing,cropping,blur,Canny filters, sobel filters,photometric distortions  
                        
                - techniques
                    - numerical range  
                        - scaling
                            - helps NN converge faster  
                                
                            - do away with NaN errors during training  
                                
                            - for each feature, the model learns the right weights  
                                
                        - normalization
                        - standardizing
                            - Z-score
                    - grouping
                        - bucketizing/binning
                        - bag of words  
                            
                    - dimensionality reduction in embeddings  
                        - PCA: principal component analysis  
                            
                        - t-SNE:t-Distributed stochastic neghbor embedding  
                            
                        - UMAP: uniform manifold approximation and projection  
                            
                        - TensorFlow embedding projector  
                            
                - feature crosses  
                    - combines multiple features together into a new feature  
                        
                    - encodes nonlinearity in the feature space , or encodes the same information in fewer features  
                        
                    - encoding features  
                        
                - preprocessing data at scale  
                    - TensorFlow extended  
                        - example gen  
                            
                        - statistics gen  
                            
                        - schema gen  
                            
                        - example validator  
                            
                        - transform
                    - instance level transformation  
                        - clipping
                        - multiplying
                        - expanding features  
                            
                    - TensorFlow Transform  
                        - tf.Transform
                        - tensorflow extended  
                            
                        - trainer  
                            
                        - evaluator
                        - pusher
                            - tensorflow serving  
                                
                            - tensorflow JS  
                                
                            - tensorflow LITE  
                                
                        - tf.transform analyzers  
                            - scaling
                            - bucketizing
                            - vocabulary
                            - dimensionality reduction  
                                
                            - hello world with tf.transform *  
                                
                        - tf.graph
                    - feature spaces/selection/  
                        - unsupervised feature selection  
                            
                        - supervised feature selection  
                            - filter methods  
                                - correlation
                                    - correlation matrix  
                                        
                                    - mendall tau rank correlation coefficien  
                                        
                                    - spearman's rank correlation coefficient  
                                        
                                    - mutual information  
                                        
                                    - f-test
                                    - chi-squared test  
                                        
                                - univariate feature selection  
                                    
                            - wrapper methods  
                                - forward elimination  
                                    
                                - backward elimination  
                                    
                                - recursive feature elimination  
                                    
                            - embedded methods  
                                - L1 regularization  
                                    
                                - feature importance  
                                    
        - validating data  
            - drift
                - change over time  
                    
                - model decay  
                    
                - concept drift  
                    
            - skew
                - different sources  
                    
                - requires continuous evaluation  
                    
                - features/distribution skew  
                    
            - batch processing/ real-time processing  
                
            - TensorFlow data validation (TFDV)  
                - Generates data statistics and browser visulizations  
                    
                - infers the data schema  
                    
                - performs validity checks against schema  
                    
                - detects training/serving skew  
                    
        - Data Journey and Data Storage
            - data versioning  
                - DVC
                    - <a href="https://dvc.org">https://dvc.org</a>/  
                        
                - Git-LFS
                - data pipeline management  
                    
                - reproducibility
                - code versioning: GitHub  
                    
                - environment versioning: Docker, Terraform, ...  
                    
            - ML metadata  
                
            - schema development  
                - schema  
                    - feature name  
                        
                    - type: int,...  
                        
                    - required or optional  
                        
                    - valency (features with multiple values)  
                        
                    - domain: range,categories  
                        
                    - default values  
                        
                - environments
            - data storage  
                - feature stores  
                    - share, discover, use  
                        
                - data warehouse  
                    - subject oriented  
                        
                    - integrated
                    - non volatile  
                        
                    - time variant  
                        
                    - advantages
                        - enhanced ability to analyze data  
                            
                        - timely access to daya  
                            
                        - enhanced data quality and consistency  
                            
                        - high return on investment  
                            
                        - increased query and system performance  
                            
                    - comparison with databases  
                        - data warehouse  
                            - online analytical processing (OLAP)  
                                
                            - data is refreshed from source systems  
                                
                            - stores historical and current data  
                                
                            - data size can scale to &gt;= terabytes  
                                
                            - queries are complex, used for analysis  
                                
                            - queries are long running jobs  
                                
                        - database
                            - online transactional processing (OLPT)  
                                
                            - data is available real-time  
                                
                            - stores only current data  
                                
                            - data size can scale to gigabytes  
                                
                            - queries are simple,used for transactions  
                                
                            - queries executed almost in real-time  
                                
                - data lakes  
                    - aggregates raw data from one or more sources  
                        
                    - data can be structured or unstructured  
                        
                    - doesn't involve any processing before writing data  
                        
                    - comparison with data warehouse  
                        - data warehouses  
                            - data structure  
                                - processed
                            - purpose of data  
                                - currently in use  
                                    
                            - users
                                - business professionals  
                                    
                            - accessibility
                                - more complicated and costly to make changes  
                                    
                        - data lakes  
                            - data structure  
                                - raw
                            - purpose of data  
                                - not yet determined  
                                    
                            - users
                                - data scientists  
                                    
                            - accessibility
                                - highly accessible and quick to update  
                                    
        - label and organize data  
            - data definition  
                - obtaining data  
                    - how long it would take to obtain m examples?  
                        
                    - inventory data  
                        - owned
                        - crowdsourced
                        - pay for labels  
                            
                        - purchase data  
                            
                        - data quality, privacy, regulatory constraints  
                            
                - data pipeline  
                    - data cleaning  
                        
                    - pre-processing  
                        - replicable
                            - tensorFlow transform, apache beam, airflow,...  
                                
                - meta-data,data provenance and lineage  
                    
                - balanced train/dev/test splits  
                    
            - label ambiguity  
                - user ID merge  
                    
            - unstructured/structured | small/big  
                - data augmentation/clean labels/  
                    
            - small data and label clean consistency  
                - standardize labels  
                    
                - merge classes  
                    
                - have a class/label to capture uncertainty  
                    
                - HLP: human level performance  
                    
            - long tail of rare events  
                
        - advanced  
            - semi-supervised learning  
                
            - active learning  
                - a family of algorithms for intelligently sampling data  
                    
                    select the points to be labeled that would be most informative for model training  
                    
                    -&gt;unlabeled pool-&gt;active learning sampler-&gt;human annotator-&gt;labeled training set-&gt;ML model-&gt;  
                    
                    margin sampling (most uncertain point); label points the current model is least confident in  
                    
                    cluster-based sampling: sample from well-formed clusters to "cover"the entire space  
                    
                    query-by-committee: train an ensemble of models and sample points that generate disagreement  
                    
                    region-base sampling: runs several active learning algorithms in different partitions of the space  
                    
            - weak supervision with Snorkel  
                - is about leveraging higher-level and/or noisier input from subject matter experts(SMEs)  
                    
                    <a href="https://www.snorkel.org/blog/weak-supervision">https://www.snorkel.org/blog/weak-supervision</a>  
                    
                    stanford 2016  
                    
                    programmatically building and managing training dataset without manual labeling  
                    
                    automatically: models,cleans, and integrates the resulting training data  
                    
                    offers data augmentation and slicing  
                    
            - data augmentation  
                - improves coverage of feature space  
                    
                - semi-supervised data augmentation: UDA, semi-supervised learning with GANs  
                    
                - policy-based data augmentation: AutoAugment  
                    
                - provides means to improves accuracy, generalization, and avoiding overfitting  
                    
            - time series  
                - human activity recognition (HAR)  
                    
        - data-centric AI development  
            - data augmentation  
                - data+noise
                - realistic/x-&gt;y map clear/the algorithm currently doing poorly on it  
                    
            - big data to good data  
                
            - adding features  
                - cold start: collaborative filtering/content based filtering  
                    
            - experiment tracking  
                - algorithm/code versioning  
                    - github
                - dataset used  
                    - <a href="https://dvc.org">https://dvc.org</a>/  
                        
                - hyperparameters
                    - AutoML
                - results
        - ML modeling vs production ML  
            - Academic/Research ML  
                - Data: Static  
                    
                - priority for design: highest overall accuracy  
                    
                - model training: optimal tuning and training  
                    
                - fairness: very important  
                    
                - challenge: high accuracy algorithm  
                    
            - Production ML  
                - Data: dynamic-shifting  
                    
                - priority for design: fast inference, good interpretability  
                    
                - model training: continuously assess and retrain  
                    
                - fairness: crucial  
                    
                - challenge: entire system  
                    
        - managing the entire life cycle of data  
            - labeling
            - feature space coverage  
                
            - minimal dimensionality  
                
            - maximum predictive data  
                
            - fairness
            - rare conditions  
                
    - modeling
        - select and train model  
            - code(algorithm/model)  
                hyperparameters  
                data  
                
            - key challenges  
                - doing well on training set  
                    
                - doing well on dev/test sets  
                    
                - doing well on business metrics/project goals  
                    
                - performance on disproportionately important examples  
                    
                - performance on key slices of the dataset  
                    
                - rare classes: skewed data distribution  
                    
            - establish a baseline  
                - HLP/open source/quick and dirty implementation/ performance of older system  
                    
                - unstructured
                    - image; audio; text  
                        
                - structured
                    - table, database  
                        
            - tips
                - open source/literature/blogs/courses  
                    
                - sanity check for code and algorithm  
                    
        - perform error analysis  
            - useful metrics for each tag  
                
            - prioritizing what to work on  
                
            - skewed dataset  
                - confusion matrix: precision and recall / F1 score  
                    
            - performance audition  
                - performance on subsets of data  
                    
                - how common are certain errors  
                    
                - performance on rare classes  
                    
                - establish metrics to assess performance against these issues on appropriate slices of data  
                    
        - ML metadata  
            - tracking artifacts and pipeline changes  
                
            - data validation-&gt;data transformation  
                - metadata store  
                    
            - TFX component architecture  
                - driver
                    - supplies required metadata to executor  
                        
                - executor
                    - place to code the functionality of component  
                        
                - publisher
                    - stores result into metadata  
                        
            - ML metadata terminology  
                - units
                    - artifact
                    - execution
                    - context
                - types
                    - artifactType
                    - executionType
                    - contextType
                - relationships
                    - event
                    - attribution
                    - association
            - !pip install ml-metadata  
                
        - C3-W1
            - NAS
                - technique for automating the design of artificial neural networks  
                    
                - find optimal architecture  
                    
                - search over huge space  
                    
            - AutoML
                - search space  
                    - architecture is picked from this space by search strategy  
                        
                    - macro
                    - micro
                - search strategy  
                    - gird search  
                        
                    - random search  
                        
                    - bayesian optimization  
                        
                    - evolutionary algorithms  
                        
                    - reinforcement learning  
                        - agents goal is to maximize a reward  
                            
                        - the available options are selected from the search space  
                            
                        - the performance estimation strategy determines the reward  
                            
                - performance estimation strategy  
                    - performance (latency, accuracy)  
                        
                    - performance estimation strategy  
                        - validation accuracy  
                            - computationally heavy, time consuming+high GPU demand, expensive  
                                
                            - strategies to reduce the cost  
                                - lower fidelity estimates  
                                    
                                - learning curve extrapolation  
                                    
                                - weight inheritance/network morphisms  
                                    
                - cloud
                    - amazon sagemaker autopilot  
                        - raw tabular data in S3 bucket  
                            
                        - select prediction target  
                            
                        - automated model selection, training,and tuning  
                            
                        - notebooks for visibility and control  
                            
                        - select best model  
                            
                    - microsoft azure automated machine learning  
                        - automated feature selection  
                            
                        - automated model selection  
                            
                        - hyperparameter tuning  
                            
                        - optimized model  
                            
                    - google cloud autoML  
                        - Qwiklabs
                            - <a href="https://googlecoursera.qwiklabs.com">https://googlecoursera.qwiklabs.com</a>
            - hyperparameters
                - Keras tuner  
                    
            - trainable parameters  
                
        - C3-W2
            - Model resource management techniques  
                - dimensionality effect on performance  
                    
                - curse of dimensionality  
                    
                - manual dimensionality reduction  
                    
                - algorithm
                    - linear  
                        - linear discriminant analysis (LDA)  
                            
                        - partial least squares (PLS)  
                            
                        - principal component analysis (PCA)  
                            - +
                                - a versatile techinique  
                                    
                                - fast and simple  
                                    
                                - offers several variations and extenstion (e.g., kernel/sparse PCA)  
                                    
                            - -
                                - result is not interapretable  
                                    
                                - requires setting threshold for cumulative explained variance  
                                    
                    - unsupervised
                        - latent semantic indexing/analysis (LSI and LSA) (SVD)  
                            - removes redundant features from the dataset  
                                
                        - independent component analysis (ICA)  
                            - addresses higher order dependence  
                                
                    - matrix factorization  
                        - non-negative matrix factorization (NMF)  
                            
                    - latent methods  
                        - latent dirichlet allocation (LDA)  
                            
            - Quantization  
                - ML kit, Core ML, TensorFlow Lite (TFX)  
                    
                - shrining model file size  
                    
                - reduce computational resources  
                    
                - make models run faster and use less power with low-precision  
                    
                - affected
                    - static values (parameters)  
                        
                    - dynamic values (activations)  
                        
                    - computation (transformations)  
                        
                - post training quantization  
                    - dynamic range quantization  
                        - 4x smaller, 2x-3x speedup  
                            
                    - full integer quantization  
                        - 4x smaller, 3x+ speedup  
                            
                    - float16 quantization  
                        - 2x smaller, GPU acceleration  
                            
                - quantization aware training (QAT)  
                    - reduces the loss of accuracy due to quantization  
                        
            - pruning
                - model sparsity  
                    - sparse models-&gt;less memory-&gt;more efficient  
                        
        - C3-W3
            - distributed training  
                - data parallelism  
                    - synchronous tratining  
                        - all workers train and complete updates in sync  
                            
                        - supported via all reduce architecture  
                            
                    - asynchronous training  
                        - each worker trains and completes updates separately  
                            
                        - supported via parameter server architecture  
                            
                        - more efficient, but can result in lower accuracy and slower convergence  
                            
                - strategies
                    - one device  
                        
                    - mirrored
                        - one machine with multiple GPUs  
                            
                    - parameter server  
                        - workers/parameter servers  
                            
                    - multi-worker
                    - central storage  
                        
                    - TPU
                - model parallelism  
                    
                - high performance ingestion  
                    - input pipeline  
                        - local (HDD/SSD)  
                            remote(GCS/HDFS)  
                            - shuffling&amp;batching (decompression/augmentation/vectorization)  
                                - load transformed data to an accelerator  
                                    
                    - how
                        - prefetching
                            - buffer data from the input dataset ahead of requested. number of elements should greater than the number of batches  
                                
                        - parallelize data extraction and transformation  
                            
                        - caching
                        - reduce memory  
                            
                - overcoming memory constraints  
                    - strategy #1: gradient accumulation  
                        - split batches into mini-batches and only perform backprop after whole batch  
                            
                    - strategy #2: memory swap  
                        - copy activations between CPU and memory, back and forth  
                            
                    - parallelism
                        - data parallelism  
                            
                        - model parallelism  
                            
                        - Gpipe
                            - Open-source tensorflow library (using lingvo)  
                                
                            - inserts communication primitives at the partition boundaries  
                                
                            - automatic parallelism to reduce memory consumption  
                                
                            - gradient accumulation across micro-batches, so that model quality is preserved  
                                
                            - partitioning is heuristic-based  
                                
                - teacher and student networks  
                    - knowledge distillation  
                        - duplicate the performance of a complex model in a simpler model  
                            
                        - idea: create a simple ;student; model that learns from a complex ;teacher; model  
                            
                        - improve softness of the teacher's distribution with 'softmax temperature'(T)  
                            
                        - techniques
                            - approach #1: weigh objectives (student and teacher) and combine during backprop  
                                
                            - approach #2: compare distributions of the predictions (student and teacher) using KL divergence  
                                
                        - make efficientNets robust to noise with distillation  
                            
        - C3-W4
            - model performance analysis  
                - black box evaluation  
                    - models can be tested for metrics like accuracy and losses like test error without knowing internal details  
                        
                - model introspection  
                    - for finer evaluation, models can be inspected part by part  
                        
                    - model introspection  
                        
                - performance metrics  
                    - based on task like regression, classification, ...  
                        
                    - within a type of task, based on the end-goal, your performance metrics may be different  
                        
                    - performance is measured after a round of optimization  
                        
                - optimization objectives  
                    - machine learning formulates the problem statement into an objective function  
                        
                    - learning algorithms find optimum values for each variable to converge into local / global minima  
                        
                - TFMAL: TensorFlow Model Analysis  
                    - read inputs  
                        
                    - extract and evaluate  
                        
                    - evaluators
                    - write results  
                        
                - model robustness  
                    - model debugging  
                        - benchmark models  
                            
                        - sensitivity analysis  
                            - What-if tool for sensitivity analysis  
                                
                            - random attacks  
                                
                            - partial dependence plots  
                                - PDPbox, PyCEbox  
                                    
                            - Foolbox, Cleverhans tools  
                                
                        - residual analysis  
                            - measures the difference between model's predictions and ground truth  
                                
                - model remediation  
                    - remediation techniques  
                        - data augmentation  
                            
                        - interpretable and explainable ML  
                            
                        - model edition  
                            
                        - model assertions  
                            
                        - discrimination remediation  
                            
                - fairness
                - continuous evaluation and monitoring  
                    - data drift and shift  
                        
                    - statistical process control  
                        
                    - squential analysis  
                        
                    - error distribution monitoring  
                        
                    - unsupervised techniques  
                        - clustering/novelty detection  
                            
                        - feature distribution monitoring  
                            
                        - model dependent monitoring  
                            
        - C3-W5
            - Interpretability  
                - explainable AI  
                    
                - model interpretation methods  
                    - intrinsic or post-hoc  
                        
                    - results
                        - feature summary statistics  
                            
                        - feature summary visualization  
                            
                        - model internals  
                            
                        - data point  
                            
                        - model specific or model agnostic  
                            
                        - local or global?  
                            
                    - intrinsically interpretable models  
                        - monotonicity improves interpretability  
                            
                        - interpretation from weights  
                            
                        - feature importance  
                            
                        - TensorFlow Lattice  
                            - inject domain knowledge  
                                
                - understanding model predictions  
                    - model agnostic methods  
                        - PDP: partial dependence plots  
                            
                        - permutation feature importance  
                            
                    - shapley values  
                        - efficiency, symmetry, dummy , additivity properties  
                            
                        - SHAP: SHapley Additive exPlanation  
                            
                    - TCAV: testing concept activation vectors  
                        - CAVs: concept activation vectors  
                            
                        - LIME: local interpretable model agnostic explanations  
                            
                    - Google cloud AI explanations for AI platform  
                        - feature attributions  
                            - integrated gradients  
                                
                            - sampled shapley  
                                
                            - XRAI: eXplanation with Ranked Area Integrals  
                                
    - deployment
        - deploy in production  
            - key challenges  
                - concept drift and data drift  
                    
                    software engineering: realtime or batch; cloud vs. Edge/Browser; compute resources(CPU/GPU/memory); latency, throughput (QPS); logging; security and privacy  
                    
            - deployment patterns  
                - new product/capability  
                    
                - automate/assist with manual task  
                    
                - replace previous ML system  
                    - shadow mode  
                        
                    - canary deployment  
                        
                    - blue green deployment  
                        
                    - degrees of automation  
                        - human only-&gt;shadow mode-&gt;AI assistance-&gt;partial automation-&gt;full automation  
                            
            - ML pipelines  
                - CD foundation MLOps reference architecture  
                    
                - directed acyclic graphs (DAG)  
                    
                - pipeline orchestration frameworks  
                    - Airflow, Argo,Celery,Luigi,Kubeflow  
                        
                - TensorFlow Extended (TFX)  
                    
        - monitor &amp; maintain system  
            - monitoring dashboard  
                - server load  
                    
                - fraction of non-null outputs  
                    
                - fraction of missing input values  
                    
                - set thresholds for alarms  
                    
                - adapt metrics and thresholds over time  
                    
            - metrics to track  
                - software metrics  
                    - memory,compute,latency,throughput,server load  
                        
                - input metrics  
                    - avg input length  
                        
                    - avg input volume  
                        
                    - num missing values  
                        
                    - avg image brightness  
                        
                - output metrics  
                    - # times return ""(null)  
                        
                    - #times user redoes search  
                        
                    - CTR
            - pipeline monitoring  
                
        - C4:W1+W2
            - balance cost, latency and throughput  
                
            - latency
                - google cloud memorystore  
                    
                - google cloud firestore  
                    
                - google cloud bigtable  
                    
                - amazon DynamoDB  
                    
            - improving prediction latency and reducing resource costs  
                
            - tools  
                - Clipper tools  
                    
                - tensorflow serving  
                    
            - on prem / on cloud  
                
            - model servers  
                - tesnsorflow serving  
                    - batch and real time inference  
                        
                    - multi model serving  
                        
                    - exposes gRPC and REST endpoints  
                        
                - torchserve
                - KF serving  
                    
                - triton inference server  
                    
            - scaling infrastructure  
                - why horizontal over vertical scaling  
                    
                - containers  
                    - docker
                - container orchestration  
                    - kubernetes
                    - docker swarm  
                        
                    - kubeflow
            - online inference  
                - inference optimization  
                    - infrastructure
                    - model architecture  
                        
                    - model compilation  
                        
                - NoSQL databases caching and feature lookup  
                    
            - data preprocessing  
                - pre processing operations needed before inference  
                    - data cleansing  
                        
                    - feature tuning  
                        
                    - feature construction  
                        
                    - representation transformation  
                        
                    - feature selection  
                        
                - post processing ; processing after obtaining predictions  
                    
            - model performance  
                - batch inference  
                    
                - batch processing with ETL  
                    - data processing - batch and streaming  
                        
                    - ETL: extract , transform, load  
                        
                    - distributed processing  
                        
                    - kafka, pub sub, cloud dataflow, beam, spark streaming  
                        
        - C4:W3: Model Management and Delivery  
            - tools for experiment tracking  
                - notebooks
                    - nbconvert (.ipynb -&gt; .py)  
                        
                    - nbdime (diffing)  
                        
                    - jupytext ( conversion + versioning)  
                        
                    - neptune-notebooks (versioning+diffing+sharing)  
                        
                - config files/command line  
                    
                - data versioning  
                    - Neptune
                    - Pachyderm
                    - Delta Lake  
                        
                    - Git LFS  
                        
                    - DoIt
                    - LakeFS
                    - DVC
                    - ML-Metadata
                - Logging metrics using TensorBoard  
                    
                - vertex tensorboard  
                    
            - MLOps
                - automation
                    - level 0  
                        - manual process  
                            
                        - script-driven
                        - interactive
                    - level 1  
                        - rapid experimentation  
                            
                        - reusable, composable, and shareable components  
                            
                        - metadata DB  
                            
                        - feature store  
                            
                        - model validation  
                            
                        - data validation  
                            
                    - level 2  
                        - CI/CD pipeline automation  
                            
                        - continuous training  
                            
                        - model deployment CI/CD  
                            
                        - serving and monitoring  
                            
            - orchestrate your ML workflows with FTX
            - managing model versions  
                - <a href="MAJOR.MINOR.PIPELINE">MAJOR.MINOR.PIPELINE</a>
                - model registry  
                    - azure ML model registry  
                        
                    - SAS model manager  
                        
                    - MLflow model registry  
                        
                    - google AI platform  
                        
                    - algorithmia
            - CD: continuous delivery  
                
            - CI: continuous integration  
                
            - CI/CD
                - unit testing in CI  
                    - unit testing input data  
                        
                    - unit testing model performance  
                        
                    - ML unit testing considerations  
                        - mocking
                        - data coverage  
                            
                        - code coverage  
                            
                    - infrastructure validation  
                        
                    - TFX infra validator  
                        
            - progressive delivery  
                - blue/green deployment  
                    
                - canary deployment  
                    
                - live experimentation  
                    - A/B testing  
                        
                    - multi-armed bandit (MAB)  
                        
                    - contextual bandit  
                        
        - C4:W4
            - Monitoring and observability  
                - why
                    - immediate data skews  
                        
                    - model staleness  
                        
                    - negative feedback loops  
                        
                - compare
                    - ML monitoring  
                        - predictive performance  
                            
                        - changes in serving data  
                            
                        - metrics used during training  
                            
                        - characteristics of features  
                            
                    - system monitoring  
                        - system performance  
                            
                        - system status  
                            
                        - system reliability  
                            
                - observability
                    - TFMA: tensorflow model analysis  
                        
                    - supervised/unsupervised
                - logging for ML monitoring  
                    - google cloud monitoring  
                        
                    - amazon cloud watch  
                        
                    - azure monitor  
                        
                - for supervised learning, labels are required  
                    - direct labeling  
                        
                    - manual labeling  
                        
                    - active learning  
                        
                    - weak supervision  
                        
                - tracing for ML systems  
                    - distributed tracing  
                        - dapper
                        - zipkin
                        - jaeger
            - model decay  
                - log predictions (full requests and responses)  
                    
                - tensorflow data validation (TFDV)  
                    
                - scikit-multiflow library  
                    
                - continuous evaluation and labelling in vertex prediction  
                    
                - mitigating model decay  
                    - fine tune or start over  
                        
                    - model re training policy  
                        
            - GDPR, CCPA, anonymization, pseudonymisation, ...