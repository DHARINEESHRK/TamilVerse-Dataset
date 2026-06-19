from datasets import load_dataset
import json
from pathlib import Path


ROOT = Path(__file__).parent.parent


OUTPUT_PATH = (
    ROOT
    / "data"
    / "raw"
    / "naanmanikadigai"
    / "naanmanikadigai_raw.json"
)


def download():

    print("Downloading Naanmanikadigai dataset...")

    dataset = load_dataset(
        "TamilThagaval/Pathinenkeezhkanakku-Naanmanikadikai"
    )

    records = dataset["train"].to_list()


    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )


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


if __name__ == "__main__":
    download()