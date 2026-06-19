# pyrefly: ignore [missing-import]
from datasets import load_dataset
import json
from pathlib import Path


# =========================
# Paths
# =========================

ROOT = Path(__file__).parent.parent

OUTPUT_PATH = (
    ROOT /
    "data" /
    "raw" /
    "naaladiyar" /
    "naaladiyar_raw.json"
)


# =========================
# Download Dataset
# =========================

def download_naaladiyar():

    print("Downloading Naaladiyar dataset...")

    ds = load_dataset(
        "TamilThagaval/Pathinenkeezhkanakku-Naaladiyar"
    )

    # Convert to Python list
    records = ds["train"].to_list()

    # Create folder if missing
    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save JSON
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

    print("Download complete ✓")
    print(f"Records downloaded: {len(records)}")
    print(f"Saved to: {OUTPUT_PATH}")


# =========================
# Main
# =========================

if __name__ == "__main__":
    download_naaladiyar()
