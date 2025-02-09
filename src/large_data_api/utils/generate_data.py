"""
Utility functions to generate data for testing purposes.
"""

import json
import random
from pathlib import Path
from typing import Any

CURRENT_DIR = Path(__file__).parent


def generate_random_json_data(length: int = 100000) -> list[dict[str, str | int]]:
    length = length + 1  # To include the last item
    return [
        {
            "id": i,
            "name": f"Name {i}",
            "description": f"Description {i} of the data item.",
            "value": random.randint(1, 100),
        }
        for i in range(1, length, 1)
    ]


def save_data_to_file(data: list[dict[str, Any]], filepath: Path) -> None:
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)


def load_data_from_file(filepath: Path) -> list[dict[str, Any]]:
    with open(filepath) as f:
        return json.load(f)


if __name__ == "__main__":
    sample_length = 100000
    data = generate_random_json_data(sample_length)
    save_data_to_file(data, CURRENT_DIR.parent / "data" / "100k_random_data.json")
