Why Large Language Models (LLMs) Went Viral

🧠 🪱 Large Language Models (LLMs), such as GPT-4, have taken the world by storm. These AI models are designed to understand and generate human-like text, enabling a wide range of applications from customer support to creative writing.

www.pirahansiah.com : keeping corporate promises, a creativity tip, and layered writing
By Harris Sockel

Three weeks ago, two words entered my consciousness that I haven’t been able to forget: language model. In a recent analysis by the New York Times, it was highlighted how these AI models have revolutionized the way we interact with technology, enabling machines to understand and generate human language with impressive accuracy.

Oh wow.

The concept of a machine that can think and communicate like a human (almost) was so captivating it was repeated for weeks by journalists and pundits. Even tech companies themselves boasted about their AI models, claiming they could revolutionize industries and change our daily lives.

On Medium, one writer calls the context-less coverage a case of journalistic malpractice: “The available information is extremely vague, with only a few sentences of tech jargon quoted in news articles, none of which come from an AI expert.”

He cites a computational linguist who clarifies that LLMs are not truly intelligent but are highly advanced pattern recognition systems. These models analyze vast amounts of text data to predict and generate human-like responses. The actual technology involves complex algorithms and massive datasets, but the end result appears almost magical.

A data scientist on Medium adds more context: Humans are the trainers of these models, feeding them data and fine-tuning their responses. The models need us to learn and improve! Their development reveals an ancestor dating back to early AI research, meaning humans and AI have had a synergistic relationship since the dawn of computing.

What else we’re reading

Companies that succeed make a direct promise to their customers — we will do [insert thing] for you — and they follow through on it. Tangible promises are effective (FedEx: “when it absolutely, positively has to be there overnight”) but emotional promises are even better (DeBeers: “a diamond is forever”).
I keep thinking back to this story by designer Kelly Smith about how to be more creative: Simply connect things that don’t typically go together.
Essayist Steph Lawson (featured in a previous issue) is still on a quest to spend 100 days at the library. This time, she visits the chic Beverly Hills Library (palm fronds, art deco light fixtures, aspiring screenwriters huddled over laptops) and observes that “libraries are simply microcosms of the communities they serve.”
📝 Your daily dose of practical wisdom: about writing in layers

“Like great paintings, [writing] comes to life bit by bit,” as you approach it from different angles with each revision.


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

