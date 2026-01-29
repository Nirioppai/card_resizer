# Card Resizer

Resize MTG and One Piece TCG cards to 1262x1714 for proxy printing.

## MTG Commands

```bash
python decklist.py  # Pull resized cards from decklist.txt to decklist folder
python resize.py    # Resize cards from current directory to 1262x1714
python list.py      # Generate list.txt of all resized cards
```

## One Piece TCG Commands

```bash
python optcg_resize.py    # Resize cards to 1262x1714 with 54px black margin
python optcg_deresize.py  # Remove 54px margin from resized cards
```
