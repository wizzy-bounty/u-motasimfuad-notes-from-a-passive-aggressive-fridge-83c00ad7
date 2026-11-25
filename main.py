import os

NOTE = (
    "Nine days I've guarded your yogurt at exactly 3°C. "
    "It has outlived whatever you were saving it for."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as entry_file:
        entry_file.write(NOTE)


if __name__ == "__main__":
    main()
