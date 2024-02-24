# LLM Fine-Tuning: Memory Needs 
- Factors
    - Model Size
        - Bigger models (more parameters) need more memory.
- Fine-tuning Technique
    - Full: Updates all, most RAM (exceeds single GPUs)
    - LoRA: Smaller "adapters," reduces needs
    - Knowledge Distillation: Similar RAM to larger model (depending on implementation)
    - Batch Size: More data = more memory, balance efficiency and RAM.
    - Optimizations: Reduce memory (trade-offs in speed/accuracy)
    - Gradients
    - Optimizers (e.g., AdamW): Add to memory requirements.
    - Precision reduction (e.g., 32-bit to 16-bit): Reduces memory, impacts accuracy.
    - Quantization: Reduces memory, needs careful tuning for balance.
    - Activations: Consume memory (depend on batch size/sequence length).

- Estimation of general RAM Requirements
    - Small Models (<1B): LoRA + optimizations might work on 16GB.
    - Medium Models (1-10B): Full needs multiple GPUs, LoRA better on high-end GPUs.
    - Large Models (>10B): Full usually impossible on single machines, needs distributed training.
