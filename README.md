# Smart Fontimage

A professional, feature-rich **Font Atlas (bitmap font) editor** with full Unicode mapping, advanced glyph controls, and real-time preview.

This repository is prepared for public Git hosting so developers and modders can **run, build, and extend** the tool بسهولة.

---

## ✨ Features

### 🧩 Grid & Atlas Management

* Manual grid setup (cell size, rows, columns, padding)
* Automatic grid detection
* Detect grid by character count
* Load grid configuration from metadata files (JSON, YAML, etc.)
* Interactive visual grid with live scaling

### 🔤 Unicode & Glyph Mapping

* Assign Unicode to each cell (hex or direct character input)
* Load Unicode mappings from metadata
* Overlay character preview on atlas cells
* Multi-cell selection and batch editing

### 🖼️ Glyph Editing

* Import glyphs from PNG images

  * Auto-fit to cell
  * Smart centering
  * Alpha preservation
* Batch replace glyphs from a folder (Unicode-based filenames)

### 🔠 Font Import (TTF/OTF)

* Import glyphs directly from font files
* Adjustable font size
* Custom font color (RGBA hex support)
* Arabic shaping support
* RTL rendering via BiDi

### ✏️ Advanced Glyph Controls

* Per-glyph **Advance (spacing)** with global fallback
* Per-glyph **X Offset** (horizontal shift)
* Per-glyph **Y Offset** (vertical shift)
* Fine positioning and multi-selection editing

### 👁️ Preview System

* Real-time text preview rendered from the atlas
* RTL / LTR toggle
* Mixed-language support (Arabic + Latin)
* Accurate spacing using glyph advance + offsets

### 🖱️ Interaction & UX

* Click to select cells
* Ctrl+Click for multi-selection
* Drag to resize rows/columns
* Drag & drop atlas images
* Live overlay visualization

### 📦 Export

* Export modified atlas (PNG)
* Export metadata (JSON) including:

  * Unicode
  * Cell index
  * Position (x, y)
  * Dimensions
  * Advance
  * X/Y offsets

---

## 📦 Included

* `editor.py` — main application
* `utils.py` — helper functions
* `run_my_tool.py` — Python launcher
* `run.bat` — one-click local run script (Windows)
* `build.bat` — one-click EXE build script (Windows)
* `font_editor.spec` — PyInstaller build configuration
* `requirements.txt` — dependencies
* `smart_fontimage.ico` — application icon

---

## 🚀 Run (Development)

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python run_my_tool.py
```

---

## 🏗️ Build EXE (Windows)

```bash
.\build.bat
```

**Output:**

```
dist/Smart Fontimage.exe
```

---

## 🧰 Requirements

* Python 3.10+
* pip
* Dependencies listed in `requirements.txt`

---

## 📂 Workflow Example

1. Load your atlas PNG
2. Detect or configure the grid
3. Assign Unicode values to cells
4. Import or replace glyphs (PNG or TTF)
5. Adjust spacing and offsets
6. Preview your text
7. Export atlas + metadata

---

## 🌍 Arabic Support

Built-in support for Arabic:

* Proper glyph shaping
* Right-to-left rendering
* Compatibility normalization
* Accurate atlas-based preview

---

## 📌 Notes

* Glyph filenames for batch import must be Unicode (e.g., `0627.png` or `U+0627.png`)
* Advance controls character spacing during rendering
* Offsets allow fine-tuning glyph alignment inside cells
* Make sure Python is added to PATH
* First build may take longer due to packaging (PyInstaller)

---

## 🤝 Contributing

Contributions, improvements, and ideas are welcome.

---

## ⭐ Support

If you find this tool useful, consider giving the repository a star ⭐
