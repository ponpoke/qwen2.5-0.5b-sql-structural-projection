# Reproducibility Guide

Follow these steps to reproduce the Qwen2.5 7B -> 0.5B SQL projection results.

## 1. Prerequisites
- Python 3.10+
- NVIDIA GPU (Recommended: 16GB VRAM for 7B/0.5B operations)

## 2. Installation
```bash
git clone https://github.com/ponpoke/qwen2.5-0.5b-sql-structural-projection
cd qwen2.5-0.5b-sql-structural-projection
pip install -r requirements.txt
```

## 3. Evaluation
To run the SQL-50 evaluation using the pre-projected adapter from Hugging Face:

```bash
python scripts/run_sql50_eval.py \
  --base_model Qwen/Qwen2.5-0.5B-Instruct \
  --adapter_path ponpoke/qwen2.5-0.5b-instruct-sql-structural-projection-lora
```

## 4. Verification
After the evaluation finishes, run the following scripts to verify the reported metrics:

**Aggregate Sweep Results:**
```bash
python scripts/summarize_alpha_sweep.py
```

**Analyze Failure/Fix Patterns:**
```bash
python scripts/classify_failures.py
```

## 5. Metadata Check
The mathematical parameters used for the projection (RSVD rank, layer mapping, etc.) are recorded in [hf/projection_metadata.json](../hf/projection_metadata.json).
