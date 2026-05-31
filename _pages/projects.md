---
layout: page
title: Projects
permalink: /projects
---

# Projects

## Core Projects

### [EdgeVision Pipeline](https://github.com/pirahansiah/PKM)
End-to-end machine learning pipeline for computer vision:
- **Capture**: Webcam image collection with auto-labeling via SAM2
- **Label**: Automated YOLO annotation pipeline
- **Train**: YOLO training with QAT (quantization-aware training)
- **Export**: ONNX model export (opset 17+)
- **Quantize**: INT8 QDQ quantization with calibration
- **Build**: Compilation for hardware accelerators

### Model Optimization
- INT8 QDQ quantization for ONNX models
- Per-channel weight quantization
- Calibration dataset preparation (200-500 images)
- FP32 vs INT8 benchmarking

### Hardware Deployment
Compilation & deployment targets:
- **Axelera Metis** - via voyager CLI
- **Hailo-8** - ONNX → HAR → HEF pipeline
- **NVIDIA TensorRT** - `trtexec` optimization
- **OpenVINO** - Intel deployment toolkit
- **Google Coral / TFLite** - Edge device deployment

---

## Maintained Repositories

- **[PKM](https://github.com/pirahansiah/PKM.git)** - Main project source (private)
- **[pirahansiah.github.io](https://github.com/pirahansiah/pirahansiah.github.io)** - This website

---

For details on setup, see my [GitHub](https://github.com/pirahansiah) or contact me directly.
