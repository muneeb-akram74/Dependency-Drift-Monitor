import json
from config import baseline_file_path

def load_baseline(baseline_file=baseline_file_path):
    with open(baseline_file, 'r') as file:
        return json.load(file)

def compare_versions(current_versions, baseline):
    drift = {}

    for module, baseline_info in baseline.items():
        # Get the current version from current_versions
        current_version = current_versions.get(module, {}).get('current')
        expected_version = baseline_info['expected']
        
        # Check if the current version does not match the expected version
        if current_version != expected_version:
            drift[module] = {
                'current': current_version,
                'expected': expected_version
            }
    
    return drift
