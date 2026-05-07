import json

def classify_failures():
    path = "reports/failure_cases_qwen05b_alpha16.json"
    print(f"Classifying failures from {path}...")
    with open(path, "r") as f:
        data = json.load(f)
    
    af = {x['id'] for x in data['adapter_failures']}
    bf = {x['id'] for x in data['baseline_failures']}
    
    fixed = bf - af
    regressed = af - bf
    
    print(f"Fixed: {len(fixed)}")
    print(f"Regressed: {len(regressed)}")
    print(f"Both failed: {len(af & bf)}")
    print(f"Both succeeded: {50 - len(af | bf)}")

if __name__ == "__main__":
    classify_failures()
