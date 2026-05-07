# Behavioral Alignment Negative Result

We directly compared Structural Projection against Behavioral Alignment (activation matching) in this Qwen2.5 7B → 0.5B SQL-50 setup.

## Results

| Method | Accuracy | Exec Success | Syntax Valid |
|---|---:|---:|---:|
| **Structural Projection alpha=16** | **36.0%** | **44.0%** | **40/50** |
| Behavioral Alignment (Calibrated) | 32.0% | 38.0% | 37/50 |
| Behavioral Alignment (Standard) | 0.0% | 0.0% | 0/50 |

## Analysis
- **Standard Alignment:** Failed catastrophically (Model Collapse). Forcing the 0.5B activations to mimic the 7B activations destroyed the model's ability to generate coherent tokens.
- **Calibrated Alignment:** Avoided collapse but failed to improve performance over the baseline. The alignment objective appeared too conservative, preserving safety but failing to transfer task-specific specialist logic.

## Interpretation
For extreme cross-scale transplantation (where the student is <10% the size of the teacher), Structural Projection currently provides a more robust and effective transfer path. Behavioral Alignment may require additional distillation or delta-space regularization to be viable in this regime.
