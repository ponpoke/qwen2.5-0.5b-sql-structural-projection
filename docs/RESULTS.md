# Results Summary: Qwen2.5 7B -> 0.5B SQL Projection

## SQL-50 Benchmark Performance

On the Neural-Scalpel SQL-50 benchmark, the projected adapter achieved the following results at the optimal balanced setting ($\alpha=16$):

| Metric | Baseline (0.5B) | Projected (0.5B) | Delta |
|---|---|---|---|
| Execution Accuracy | 32.0% | 36.0% | +4.0% |
| Execution Success | 38.0% | 44.0% | +6.0% |
| Syntax Validity | 37/50 | 40/50 | +3 cases |

## Alpha Sensitivity (Alpha Sweep)

We mapped the performance across varying signal intensities:

| Alpha | Accuracy | Success | Syntax |
|---|---:|---:|---:|
| Baseline | 32.0% | 38.0% | 37/50 |
| 8 | 34.0% | 42.0% | 39/50 |
| **16** | **36.0%** | **44.0%** | **40/50** |
| 24 | 36.0% | 44.0% | 40/50 |
| 32 | 34.0% | 46.0% | 41/50 |

## Qualitative Correction
- **Fixed Hallucinations:** Two cases (`joins_004`, `subqueries_001`) that produced conversational text in the baseline were corrected to valid SQL.
- **Zero Regression:** No cases that were correctly answered by the baseline regressed when using the $\alpha=16$ adapter.

## Cross-Size Generalization

We evaluated the same Structural Projection approach across multiple Qwen2.5 target sizes:

| Target Model | Size | Base Acc | Adapter Acc | Delta | Interpretation |
|---|---:|---:|---:|---:|---|
| Qwen2.5-7B-Instruct | Teacher | 62.0% | 56.0% | -6.0% | Source adapter degraded the already-strong teacher baseline |
| Qwen2.5-3B-Instruct | Student | 30.0% | 34.0% | +4.0% | Positive improvement |
| Qwen2.5-1.5B-Instruct | Student | 48.0% | 46.0% | -2.0% | Mild interference |
| Qwen2.5-0.5B-Instruct | Student | 32.0% | 36.0% | +4.0% | Positive improvement |

## Positive Teacher Validation (Qwen2.5-Coder)

To verify the **Source Adapter Quality Gate** hypothesis, we tested a high-quality SQL DPO adapter on the Qwen2.5-Coder family. Unlike the previous experiment, this source adapter significantly improved its own base model.

| Target Model | Role | Base Acc | Adapter Acc | **Delta** | Interpretation |
|---|---|---:|---:|---:|---|
| **Qwen2.5-Coder-7B** | **Teacher** | 62.0% | 78.0% | **+16.0%** | **Positive Teacher** |
| **Qwen2.5-Coder-3B** | Student | 66.0% | 72.0% | **+6.0%** | Consistent Gain |
| **Qwen2.5-Coder-1.5B**| Student | 38.0% | 44.0% | **+6.0%** | Consistent Gain |
| **Qwen2.5-Coder-0.5B**| Student | 24.0% | 28.0% | **+4.0%** | Consistent Gain |

### Key Conclusion

Structural Projection is a **delta transfer mechanism**. Its success is highly dependent on the quality of the source adapter. When the source adapter passes the quality gate, projection yields consistent positive improvements across all tested student scales.

This results support the **Complementarity Hypothesis**: Structural Projection provides the most value when the target model has a clear task deficit.

Detailed raw logs can be found in [reports/failure_cases_qwen05b_alpha16.json](../reports/failure_cases_qwen05b_alpha16.json).
