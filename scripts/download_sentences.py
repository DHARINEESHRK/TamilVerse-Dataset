from datasets import load_dataset
import json
from pathlib import Path


ROOT = Path(__file__).parent.parent


OUTPUT_PATH = (
    ROOT
    / "data"
    / "raw"
    / "sentences"
    / "sentences_raw.json"
)


def download():

    print("Downloading English-Tamil Parallel Corpus...")

    dataset = load_dataset(
        "NLPC-UOM/English-Tamil-Parallel-Corpus"
    )


    print("\nAvailable splits:")
    print(dataset)


    records = []


    for split in dataset.keys():

        records.extend(
            dataset[split].to_list()
        )


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


    print("\n========== Download Report ==========")
    print(
        f"Total records downloaded: {len(records)}"
    )
    print(
        f"Saved at:\n{OUTPUT_PATH}"
    )


if __name__ == "__main__":
    download()