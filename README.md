# Gamma Watermark Remover

A high-performance local web utility designed to strip **"Made with Gamma"** branding from PDF and PowerPoint (`.pptx`) documents exported from Gamma's free tier.

The application leverages a **FastAPI** backend to perform heuristic-based document surgery, identifying and removing watermark objects based on metadata and spatial coordinates.

---

## Key Features

### PDF Processing

- **Engine:** PyMuPDF (Fitz)
- **Detection:** Scans page dictionary objects for external links associated with the `gamma.app` domain
- **Action:** Redacts and removes image objects and associated link annotations typically found in the bottom-right quadrant of the page

### PPTX Processing

- **Engine:** python-pptx
- **Detection:** Gamma injects watermarks into **Slide Layouts (Masters)** rather than individual slides
- **Action:**
    - Inspects shapes within layouts
    - If a shape contains a `gamma.app` hyperlink and its position coordinates (`x, y`) exceed `70%` of the slide dimensions, the object is purged from the XML structure

---

## Technical Setup

### Prerequisites

- Python 3.10 or higher

### 1. Initialize Repository

```bash
git clone https://github.com/Aditya-233/Gamma-Watermark-Remover.git
cd Gamma-Watermark-Remover
```

### 2. Environment Configuration

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Launch Application

```bash
python app.py
```

Access the interface at: [http://localhost:8999](http://localhost:8999)

---

## Architecture & Logic

The tool employs a **two-phase pipeline**:

1. **Non-destructive analysis phase**
2. **Destructive removal phase**

### Core Heuristics

- **Coordinate Heuristics:** Watermarks are identified if their bounding box resides in the region where Gamma anchors branding
- **Hyperlink Validation:** Only elements linking to `gamma.app` or containing "Gamma" metadata are targeted to prevent false positives (e.g., user-added images in corners)
- **Layout Cleansing:** Targeting PPTX Master Layouts enables global removal with minimal computational overhead

---

## Dependencies

| Library     | Purpose                         |
| ----------- | ------------------------------- |
| fastapi     | REST API & routing              |
| uvicorn     | ASGI server                     |
| pymupdf     | PDF object manipulation         |
| python-pptx | OpenXML presentation processing |
| jinja2      | Frontend templating             |

---

## Disclaimer

- This software is provided for **educational and personal research purposes only**
- The author is **not affiliated with Gamma**
- Users are responsible for complying with the Terms of Service of the original platform
- If you find Gamma's service valuable, consider supporting the developers by subscribing to their Pro plans

---

**Author:** Aditya-233
