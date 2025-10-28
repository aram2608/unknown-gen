# unknown-gen
Generate an excel file of unknown bacteria for teaching labs.

This is a small GUI app built with tkinter for creating an excel file populated
with randomized bacteria. The idea for this project came about during my time as a
TA for a microbiology course at UNH. As a part of the lab, we have our students
attempt to identify an unknown bacteria using a series of biochemical tests.

As you can imagine the setup for this lab can take some time, and I had the idea
of creating this small app to streamline a part of the process.

# Demo
---

The app is quite simple as it includes a couple fields for data input.
The most obvious being the fields for adding Gram positive and negative bacteria

![Demo](embedded/demo.png)

To add a new bacteria simply add the name to the entry and press the add bacteria
button corresponding the bacteria type. Once all your bacteria are ready, add the number
of sections you teach, (ie 8), and the number of students per section (ie 20).
Finally, add a file name for the output file and you are ready to get your
bacteria!

The entries are generated in the following format,
```csv
Section Number Bacteria         GramStain
1       1      E. coli          Gram-negative
1       2      S. aureus        Gram-positive
1       3      P. aeruginosa    Gram-negative
...
8       141    S. agalactiae    Gram-positive
8       142    E. coli          Gram-negative
8       143    S. marscecens    Gram-negative
...
```

With each section getting its own sheet in the excel file.

# Usage
---

```shell
python -m venv venv
source .venv/bin/activate

# Not always needed but sometimes good to run just in case
python3 -m ensurepip

# Install requirements
pip install -r requirements.txt

# Or
python -m pip install requirements.txt

# Then you can run as a module
python3 -m src/
```