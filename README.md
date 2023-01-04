# Python Antiplagiarism

This script allows you to evaluate the similarity of two Python scripts

Example of running a script:

```bash
python3 compare.py input.txt scores.txt
```

This is what the `input.txt` file should look like:

```text
files/main.py plagiat1/main.py
files/loss.py plagiat2/loss.py
files/loss.py files/loss.py
```

This is roughly what `scores.txt` will look like after the script runs:

```text
0.63
0.84
0.153
```