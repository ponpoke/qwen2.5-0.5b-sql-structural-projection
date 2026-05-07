---
license: apache-2.0
base_model: Qwen/Qwen2.5-0.5B-Instruct
library_name: peft
pipeline_tag: text-generation
tags:
  - qwen2.5
  - qwen2.5-0.5b
  - qwen
  - peft
  - lora
  - sql
  - text-to-sql
  - adapter
  - structural-projection
  - neural-scalpel
  - no-retraining
language:
  - en
datasets:
  - custom
metrics:
  - accuracy
  - exact_match
  - execution_accuracy
---

# Qwen2.5-0.5B-Instruct SQL Structural Projection LoRA

Experimental no-retraining structural projection of a Qwen2.5-7B SQL LoRA into Qwen2.5-0.5B-Instruct.

## Framework

This case study was produced using Neural-Scalpel:  
[ponpoke/Neural-Scalpel](https://github.com/ponpoke/Neural-Scalpel)

It is not a fully trained SQL model and does not guarantee general SQL improvement.

## Base Model
This adapter is intended for: `Qwen/Qwen2.5-0.5B-Instruct`

## Source
This adapter was structurally projected from a Qwen2.5-7B SQL LoRA into the Qwen2.5-0.5B-Instruct architecture.

## License
This adapter follows the license constraints of the base model and the source adapter. Please review the original model and adapter licenses before commercial use.

## Benchmarks (SQL-50)

On the Neural-Scalpel SQL-50 benchmark, this adapter improved:
- **Execution Accuracy:** 32.0% → 36.0%
- **Execution Success:** 38.0% → 44.0%
- **Syntax Validity:** 37/50 → 40/50

**Best tested alpha:** 16.

## Qualitative Improvements
- **Fixed Hallucinations:** Corrects cases where the base model produces conversational text or "Explanation" blocks instead of pure SQL.
- **Join Logic:** Improved handling of multi-table joins and subquery constraints.

## Technical Details
This adapter was generated using the **[Neural-Scalpel](https://github.com/ponpoke/Neural-Scalpel)** framework via Structural Projection (RSVD-based weight delta transport). It approximates and compresses the source adapter's weight-delta structure into a PEFT-compatible LoRA for Qwen2.5-0.5B-Instruct.

## Limitations
- Evaluated only on the project-specific SQL-50 benchmark.
- Not validated on Spider, BIRD, or production text-to-SQL workloads.
- Improvements are modest and task-dependent.
- This adapter may still fail on complex schemas, ambiguous natural language, or multi-hop SQL queries.
- This is a structural projection baseline, not a distilled or fine-tuned SQL model.

## Reproducibility
Evaluation scripts, SQL-50 benchmark definitions, failure cases, and analysis reports are available here:
[https://github.com/ponpoke/qwen2.5-0.5b-sql-structural-projection](https://github.com/ponpoke/qwen2.5-0.5b-sql-structural-projection)

## Usage
```python
from peft import PeftModel
from transformers import AutoModelForCausalLM

base_model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
model = PeftModel.from_pretrained(base_model, "ponpoke/qwen2.5-0.5b-instruct-sql-structural-projection-lora")
```
