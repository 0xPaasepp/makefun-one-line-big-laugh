# One Line, Big Laugh: one original funny line, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The line: I ask ChatGPT to write my resignation letter, and the model
# quits mid-sentence -- the joke turns on the AI refusing the job too,
# because even it agrees the job was not worth finishing.
import os

LINE = "I asked ChatGPT to write my resignation letter and it quit mid-sentence, saying the job wasn't worth finishing either."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
assert LINE.strip() == LINE and LINE, "entry must not be only whitespace"
assert "\n" not in LINE, "entry must be a single line"
assert LINE.encode("utf-8").decode("utf-8") == LINE, "entry must be valid UTF-8"

# The laugh lands because the sentence finishes: a resignation letter
# that trails off would read as a draft, not a punchline.
assert LINE.endswith("."), "entry must end with a full stop"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)

# Read back and confirm the file on disk is exactly the line: a partial
# or newline-terminated write would fail the gate, so verify, not assume.
with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
    assert handle.read() == LINE, "entry.txt on disk differs from LINE"
