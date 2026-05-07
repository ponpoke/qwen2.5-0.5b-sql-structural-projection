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

Detailed raw logs can be found in [reports/failure_cases_qwen05b_alpha16.json](../reports/failure_cases_qwen05b_alpha16.json).
