# Arkham Horror LCG dividers PDF

This is just a quick script
to allow PDF generation
for the card dividers
from [Arkham Starter](https://arkham-starter.com/divider).

Required fpdf to be installed:

```sh
python -m pip install fpdf
```

This tool was used
with the old 3mm Divider repo
which provided the images.

Now it is required
to download the images
from the webpage
mentioned above.

Put the images into a directory
and create a file `dividers.py`
containing the list of images:

```python
dividers = [
    "dividers/Extra x8/de_Extra_01_Deck 1.png",
    "dividers/Extra x8/de_Extra_02_Deck 2.png",
    "dividers/Extra x8/de_Extra_03_Deck 3.png",
    "dividers/Extra x8/de_Extra_04_Deck 4.png",
    # ...
]
```

Running the script
will create a pdf file
which can be printed.
