from datasets import load_dataset
import json
from pathlib import Path


# ==============================
# Paths
# ==============================

ROOT = Path(__file__).parent.parent

OUTPUT_PATH = (
    ROOT
    / "data"
    / "raw"
    / "nalvazhi"
    / "nalvazhi_raw.json"
)


# ==============================
# Download Dataset
# ==============================

def download():

    print("Downloading Nalvazhi dataset...")

    dataset = load_dataset(
        "TamilThagaval/avvaiyar-nalvazhi"
    )

    records = dataset["train"].to_list()

    # Create directory
    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save raw JSON
    with open(
        OUTPUT_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            records,
            file,
            ensure_ascii=False,
            indent=4
        )

    print("\nDownload Complete ✓")
    print(f"Records downloaded : {len(records)}")
    print(f"Saved at:\n{OUTPUT_PATH}")


# ==============================
# Main
# ==============================

if __name__ == "__main__":
    download()