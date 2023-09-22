# LLMBC 2023 - LLM Bootcamp
0 Launch an LLM App in One Hour 
1 LLM Foundations 
2 Learn to Spell: Prompt Engineering 
3 Augmented Language Models 
4 Project Walkthrough: askFSDL
5 UX for Language User Interfaces
6 LLMOps
7 What's Next?


## 0 
Launch an LLM App in One Hour (LLM Bootcamp)
* Prototyping & Iteration
	* “Foundation models” have unblocked a lot of applications
	* Prototype with a high-capability hosted model in chat first
	* Tinker with prompts and build on open source frameworks
* Deploying an MVP
	* Cloud tooling makes it easy to get started
	* Find a simple UI and start getting feedback from users ASAP
* Zero-Shot prompting 
* Code
	* pip install -qqq  (quiet mode)
		* getpass
		* langchain openai
		* arxiv
		* pypdf
		* faiss-cpu tiktoken
	* code
		* getpass.getpass
		* from IPython.display import Markdown
		* paper=next(arxiv.Search(id_list=["2205.11916:]).results())
		* Markdown(paper.summary)
		* paper_path=paper.download_pdf()
		* from langchain.document_loaders import PyPDFLoader
## 1
* [Andrej Karpathy](https://www.youtube.com/@AndrejKarpathy)
* Model Hub: Hugging Face
* Transformers
	* attention is all you need (2017)
		* Transformer Decoder 
			* 1 inputs: 
				* vectors of numbers
				* turn into a sequence of tokens
				* turn into vocabulary IDs				* 
				* input embedding
					* learn an embedding matrix
						* the simplest NN layer type
			* 1.2 positional encoding
				* position-encoding vectors to embedding vectors 
			* 2 transformer architecture
				* 2.1
					* project inputs into query, key, value roles
					* attention
						* masked multi-head 
					* masking attention
				* 2.2
					* skip connections / residual blocks
						* output=module(input) + input
				* 2.3
					* layer Normalization
				* 2.4 
					* feed forward layer 
			* 3 
		* simultaneously
			* expressive in the forward pass
			* optimizable via back-propagation + gradient descent
			* efficient hight parallelism compute graph 
	* RASP 2021
		* programming language of transformer-implementable operations
* LLMs
	* BERT 2019 - 110M params
		* bidirectional encoder representations from transformers
		* encoder-only (no attention masking)
		* 15% of all words masked out
	* T5 2020 - 11B params
		* Text-to-Text Transfer Transformer
		* Encoder-Decoder architecture
		* T5 training data C4 - 160B tokens
	* GPT / GPT 2 - 2019 - 1.5B params
		* byte pair encoding
	* GPT-3 - 2020 - 175B params
		* exhibited unprecedented few-shot and zero-shot learning
		* 500B tokens
		* but trained on only 300B
	* GPT-4 - 2023 - 
	* Chinchilla 2022
		* optimal model and training set size
	* LLaMA 2023
* Instruction Tuning
	* at the time GPT-3 (2020) 
		* mindset few-shot
			* text completion
	* at the time ChatGPT (2022)
		* mindset zero-shot
			* instruction-following
	* supervised fine-tuning
	* instructGPT/GPT-3.5
	* ChatGPT
		* RLHF on conversations
		* ChatML format (messages from system, assistant, user roles)
* Retrieval-enhanced transformer (2021)
## 2
* Prompt Engineering
	* learn the genie's rules
	* a golem is a magical artificial agent
* tricks
	* few-show learning is not a great model
	* dealing with tokenization
* models don't see characters, they see tokens
* add spaces between the letters in the following word: "      " 
	* GPT-3 see the letters separately and each letter becomes its own token
* a playbook is emerging
	* structured text 
		* pseudocode  
	* decomposition and reasoning
		* breakdown tasks: paper "decomposed prompting"
		* try and automate it
		* reasoning by few-shot prompting with CoT (chain-of-thought)
			* **let's think step by step**
	* self-criticism
		* **review your previous answer and find problems with your answer**
		* **based on the problems you found, improve your answer** 
	* ensembling 
		* paper: self-consistency improves chain of thought
		* Tip: inject randomness for greater heterogeneity. 
	* compose these tricks for the best accuracy.
## 3
* how to make the most of a limited context by augmenting the language model 
* retrieval: augment with a bigger corpus
	* traditional 
		* query, object, relevance, ranking
		* document ingestion, document processing, transaction handling, scaling via shards, ranking & relevance, ...
	* AI
		* vectors are a compact, universal representation of data
		* embedding
			* word2vec
			* a solid baseline: sentence transformers
			* a multimodal option: CLIP
			* OpenAI embedding: text-embedding-ada-002
			* **instructor**
	* ANN index
	* embedding database
	* llamaindex 	 
* chains: augment with more LLM calls
	* if you want reliability
	* building chains of LLM calls
		* QA pattern
		* HyDE
		* summarization 
	* tools
		* **LangChain** 
* tools: augment with outside sources
	* if you want more flexible way
	* ChatGPT plugins 
		* if you want interactivity/ flexibility
## 4
Project Walkthrough
* ask-fsdl
	* make
	* .pre-commit-config.yaml 
		* for code cleanliness 
		* black for python : autoformatting
		* **ruff-pre-commit**
			* flake 8 for linting
		* shellcheck-py
		* pre-commit run --all-files
	* ETL
		* data processing 
			* for improvement **spending time with data**
			* PDF ?
				* its like image format
				* code
					* 
					* 
			* preserve structure: links, paragraph, ...
				* pip: mistune, slugify, 
			* get YouTube captions
				* pip: youtube_transcript_api
		* data storage			
			* MongoDB
	* tool: modalport
		* vm in modos cloud for each task
		* https://modal.com/
		* example
			* pyenv shell 3.10.9
			* pyenv activate ask-fsdl
			* make debugger
	* pip: gradio
		* @modal.asgi_app
		* insted javascript use LLM to create page by text
	* async with
	* fastAPI
	* challenges
		* improving the retrieval
			* information retrieval 
		* improving the quality of the model outputs
			* https://logit.io/blog/post/distributed-tracing-tools/ 
			* log: datadog, sentry, honeycomb, 
			* pip: **gantry** 
		* identifying a like solid user base 
## 5
* UI principles
	* book: the design of everyday things (Don Norman)
		* human-centered design
		* \affordances and signifiers
		* mapping and feedback
		* have empathy for the user
	* book: don't make me think (Steve Krug)
		* design for scanning, not reading
		* make actionable things unambiguous, instinctive, and conventional 
		* less is more
		* testing with real users is crucial
* LUI patterns
* Case studies
## 6
* Choosing your base model
	* T5, Flan-T5: google ai, 12B,2K, apache 2.0
* Iteration and prompt management
	* level 3
		* track prompts in a specialized tool
		* for running parallel evals, decoupling prompt changes from deploys, 
		* or involving non-technical stakeholder
		* tools
			* W&B
			* comet
			* mlflow
* Testing
	* what metric?
	* 1. start incrementally
		* save interesting: hard, different
	* 2. use your LLM to help
		* auto-evaluator 
	* 3. add more data as you roll out
		* hard data
		* different data
	* 4. toward "test coverage" for AI?	
	* evaluation metrics for LLMs 
* Deployment
	* https://blog.replit.com/llm-training
	* self-critique : guardrails.ai
	* sample many times
		* choose the best option
		* ensemble
* Monitoring 
* Continual improvement and fine-tuning
	* user feedback 
	* Supervised fine-tuning of LLMs: https://magazine.sebastianraschka.com/p/finetuning-large-language-models
		* 1) Feature-Based Approach
		* 2) Finetuning I – Updating The Output Layers
		* 3) Finetuning II – Updating All Layers
* conclusion
	* test-driven development for LLMs
## 7
* Transformers can be used for vision
* PaLM-E is scarily capable
* RWKV: RNNs strike back
* www.pirahansiah.com 



```
import json
with open(json_path) as f:
	pdf_infos=json.load(f)
pdf_urls = [pdf[ürl"] for pdf in pdf_infos]
results = list(extract_pdf.map(pdf_urls, return_exceptions=True))
add_to_document_db.call(results)
