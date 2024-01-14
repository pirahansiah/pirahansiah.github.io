Makefile: Install requirement file using conda with pip fallback  
The provided code is a Makefile with several targets and their descriptions. The "help" target lists all the targets along with their short descriptions. The "create" target creates a requirements.txt file by freezing the currently installed Python packages. The "environment" target installs the required environment for deployment using the packages listed in requirements.txt. The "dev_environment" target installs the required environment for development and document corpus generation using the packages listed in requirements-dev.txt. The "conda" target installs the required packages from requirements_conda.txt using Conda and then installs any remaining packages from requirements.txt using pip.  
Attempts to install the package using conda install --yes. If conda install fails, then the loop tries to install the package using pip install -U.

## MakeFile 
```python

.PHONY: help
.DEFAULT_GOAL := help

conda: ## Install requirement file using conda with pip fallback

	while read line; do \
      echo "$$line" ; \
	  conda install --yes "$$line" || pip install -U "$$line"; \
    done <  requirements.txt 

help: ## get a list of all the targets, and their short descriptions
	@# source for the incantation: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?##"}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'

environment: ## installs required environment for deployment
	pip install -q -r requirements.txt

dev_environment:  ## installs required environment for development & document corpus generation
	python.exe -m pip install --upgrade pip
	pip install -q -r requirements-dev.txt

run:
	python 0000.py
update: ## conda update ; pip update 

	conda update -y -n base -c defaults conda		
	conda config --add channels pytorch
	conda config --add channels conda-forge
	conda config --add channels anaconda

	# Install pip for fallback
	conda install --yes pip

	python -m pip install --upgrade pip
	
info: ## more
	@echo "www.Pirahansiah.com"
```

![[MakeFile.png]]