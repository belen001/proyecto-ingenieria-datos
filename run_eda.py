import sys
from pathlib import Path

# Add project root to sys.path
project_root = Path(__file__).resolve().parent
sys.path.append(str(project_root))

from utils.eda_helpers import run_full_eda

if __name__ == "__main__":
    results = run_full_eda()
    print("EDA completed. Generated files:")
    for key, path in results.items():
        print(f"{key}: {path}")
