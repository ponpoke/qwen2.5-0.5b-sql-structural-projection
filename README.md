# Qwen2.5-0.5B SQL Structural Projection Case Study

This repository documents a Neural-Scalpel case study:
projecting a Qwen2.5-7B SQL LoRA into Qwen2.5-0.5B-Instruct without gradient-based retraining.

## Released Adapter

Hugging Face:  
[ponpoke/qwen2.5-0.5b-instruct-sql-structural-projection-lora](https://huggingface.co/ponpoke/qwen2.5-0.5b-instruct-sql-structural-projection-lora)

## Framework

This case study was produced using Neural-Scalpel:  
[ponpoke/Neural-Scalpel](https://github.com/ponpoke/Neural-Scalpel)

## Summary

- **Source:** Qwen2.5-7B SQL LoRA source adapter
- **Target:** Qwen/Qwen2.5-0.5B-Instruct
- **Method:** Structural Projection (RSVD-based)
- **Fine-tuning:** None
- **Best tested alpha:** 16
- **Benchmark:** Neural-Scalpel SQL-50

## Main Result

| Method | Accuracy | Exec Success | Syntax Valid |
|---|---:|---:|---:|
| Baseline 0.5B | 32.0% | 38.0% | 37/50 |
| **Structural Projection alpha=16** | **36.0%** | **44.0%** | **40/50** |

## Key Findings

1. **Reproducibility:** The +4.0% accuracy improvement at alpha=16 was confirmed stable across multiple greedy-decoding evaluation runs.
2. **Structural vs Behavioral:** Structural Projection outperformed the tested Behavioral Alignment variants in this cross-scale setup. The tested Behavioral Alignment adapters either failed to improve or collapsed.
3. **No Observed Regression:** No baseline-correct cases were broken by the projected adapter at the best tested alpha setting.

## Reproduce

Install dependencies:

```bash
pip install -r requirements.txt
```

Run SQL-50 evaluation:

```bash
python scripts/run_sql50_eval.py \
  --base_model Qwen/Qwen2.5-0.5B-Instruct \
  --adapter_path ponpoke/qwen2.5-0.5b-instruct-sql-structural-projection-lora
```

Summarize alpha sweep:

```bash
python scripts/summarize_alpha_sweep.py
```

Classify failures:

```bash
python scripts/classify_failures.py
```

## Reports

* [SQL-50 alpha=16 result](reports/sql_eval_results_qwen05b_alpha16.json)
* [Failure cases](reports/failure_cases_qwen05b_alpha16.json)
* [Alpha sweep summary](reports/alpha_sweep_summary.json)
* [Structural vs Behavioral comparison](reports/structural_vs_behavioral_comparison.json)

## Documentation

* [Method](docs/METHOD.md)
* [Results](docs/RESULTS.md)
* [Limitations](docs/LIMITATIONS.md)
* [Reproducibility](docs/REPRODUCIBILITY.md)
* [Behavioral Alignment Negative Result](docs/BEHAVIORAL_ALIGNMENT_NEGATIVE_RESULT.md)

## Important Disclaimer

This is an experimental structural projection case study.

It is not a fully trained SQL model and does not guarantee general SQL improvement. The reported results are specific to the Neural-Scalpel SQL-50 benchmark and the Qwen2.5 7B → 0.5B projection setup.
