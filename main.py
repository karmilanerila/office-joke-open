"""One original single-line office joke for the make.fun Office Joke Open."""

import os

JOKE = "Our office printer has been 'out of order' for six months, so I printed my resignation on it \u2014 it jammed, and HR said that counts as staying."

OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main():
    text = JOKE + "\n"
    if not JOKE.strip():
        raise SystemExit("joke must not be only whitespace")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry length {len(text)} out of range 1-200")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
