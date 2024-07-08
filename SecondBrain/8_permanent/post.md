https://www.octomind.dev/blog/why-we-no-longer-use-langchain-for-building-our-ai-agents

# <span style="color:blue;">Why Octomind No Longer Uses LangChain for Building AI Agents</span>

### <span style="color:green;">1. Initial Attraction to LangChain</span>
- Octomind initially adopted LangChain due to its comprehensive list of components and tools, which seemed ideal for quickly transitioning from an idea to working code.
- LangChain's popularity and initial ease of use were significant factors in its adoption.

### <span style="color:green;">2. Growing Frustrations</span>
- As Octomind’s requirements became more complex, LangChain’s rigid high-level abstractions became a source of friction.
- The need to dive into LangChain’s internals to customize lower-level behaviors highlighted its inflexibility.
- LangChain’s abstractions often made the code more difficult to understand and maintain.

### <span style="color:green;">3. Complexity of Abstractions</span>
- LangChain’s use of multiple abstractions (e.g., prompt templates, output parsers, chains) increased the complexity of the code without providing significant benefits.
- Comparisons with simpler implementations using only essential packages showed that LangChain's approach could overcomplicate straightforward tasks.

### <span style="color:green;">4. Impact on Development</span>
- The team found themselves spending as much time debugging LangChain as building new features, which was counterproductive.
- LangChain’s limitations were particularly evident when trying to implement dynamic and complex agent interactions.

### <span style="color:green;">5. Decision to Move Away</span>
- Removing LangChain allowed Octomind to directly code their requirements without translating them into framework-specific solutions.
- The team decided that a modular approach using simple, low-level building blocks was more efficient for their needs.

### <span style="color:green;">6. Adopting a Simpler Approach</span>
- Octomind found that using fundamental components (e.g., LLM communication clients, function calling tools, vector databases) and selected external packages sufficed for most of their application’s needs.
- This approach also facilitated faster innovation and iteration, which is crucial in the rapidly evolving AI field.

### <span style="color:green;">7. Conclusion</span>
- Octomind’s experience suggests that while frameworks like LangChain can be useful for prototyping, they may not be suitable for production-level applications requiring flexibility and simplicity.

For more detailed insights, you can read the full article on [Octomind's blog](https://www.octomind.dev/blog/why-we-no-longer-use-langchain-for-building-our-ai-agents).
