# Fe

Utility to fix Arabic bitmap-font text when letters appear disconnected or overly spaced.

## What this fixes

- **Shape**: maps Arabic letters to Presentation Forms (isolated/initial/medial/final).
- **Connection**: applies joining rules and **lam-alef ligatures**.
- **Distance**: removes accidental spaces between Arabic letters so words connect naturally.

## Usage

```bash
python3 arabic_font_fix.py "ا ل خ ي ا ر ا ت"
python3 arabic_font_fix.py "التخصيص"
python3 arabic_font_fix.py "اللعبة"
```

The output is a shaped string you can map directly to your font image / atlas glyphs.
