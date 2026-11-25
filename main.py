import os

NOTE = (
    "Nine days I've guarded your yogurt at exactly 3°C. "
    "It has outlived whatever you were saving it for."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(NOTE)


if __name__ == "__main__":
    main()
