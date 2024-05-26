
# Farshid Pirahansiah
## GPU optimization workshop
### Mark Saroufim - facebook meta pythorch
- discord.gg/cudamode
- .cuda()
- pointwise ops
- threading strategy
- memory hierarchy 
- PyTorch profiler
- arithmetric intensity
- autoregressive decoding in LLM
- Torch.compile is a fusion compiler
    - 
- tensor cores
- overhead reduction
    - torch.compile(model,mode="reduce-overhead")
- quantization
    - INT8
    - also helps memory bound workloads
    - less memory bandwidth bound
    - INT8 in gptfast weght only quantization
- Terminology rant
    - int 8 is ambiguous
    - digression: bit packing
- compute bound problems
    - paper: flah attention
    - paper: online softmax
    - programming massively parraler .... book
- tools of the trace: **ncu**
### sharan : nvidia
- high performance llm serving on nvidia gpus
- tensorrt-llm 
- request scheduling
- 
### phil tillet
- why triton
- 










?

__init__(self):
super(xxx,self).__init__()






[Doc](https://docs.google.com/document/d/1TR_5Ax0rPqTj8I2sA7MH-aa4J7TUUt4Ji9272OP8ZJg/edit?usp=sharing)
[Code GitHub](https://github.com/mlops-discord/gpu-optimization-workshop)

