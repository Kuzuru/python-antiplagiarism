# Python Antiplagiarism

This script allows you to evaluate the similarity of two Python scripts

You can run script like this:
```bash
python3 compare.py [list_of_input_files] [output_scores] [--verbose]
```

Example of running a script:

```bash
python3 compare.py input.txt scores.txt
```

Or in verbose mode:

```bash
python3 compare.py input.txt scores.txt --verbose
```

This is what the `input.txt` file should look like:

```text
files/main.py plagiat1/main.py
files/lossy.py plagiat2/lossy.py
files/lossy.py files/lossy.py
```

This is roughly what `scores.txt` will look like after the script runs:

```text
[ files/main.py || plagiat1/main.py ]
Levenstein: 89
Similarity: 0.9817098232634608

[ files/lossy.py || plagiat2/lossy.py ]
Levenstein: 5469
Similarity: 0.4116824440619621

[ files/lossy.py || files/lossy.py ]
Files are identical
```