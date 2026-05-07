# Method: Structural Projection

This case study demonstrates **Structural Projection**, a method for transporting learned weight deltas (LoRAs) between heterogeneous architectures without traditional distillation or fine-tuning.

## Core Concept
Instead of matching model activations (Behavioral Alignment), we treat the LoRA as a geometric object in the weight space. We project the high-dimensional delta of the source model (Qwen2.5-7B) into the lower-dimensional manifold of the target model (Qwen2.5-0.5B).

## Workflow
1. **Delta Extraction:** Extract the LoRA weight matrices from the source adapter.
2. **Structural Mapping:** Map source layers to target layers using interpolation or CKA-based correspondence.
3. **Dimensionality Reduction:** Use Randomized Singular Value Decomposition (RSVD) to compress the source matrices into the target rank/dimension.
4. **Scale Calibration:** Systematically sweep the scaling factor ($\alpha$) to find the optimal signal intensity for the target architecture.

## Why Structural Projection?
In our experiments, Structural Projection provided a more stable task-vector carrier than Behavioral Alignment. It preserved the target model's native generation coherence while introducing a bounded source-derived task-vector signal.
