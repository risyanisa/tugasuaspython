git clone <your-repo-url>
# 📚 Project Manual

This manual provides step-by-step instructions for using the Tugas UAS Product Manager project.

## 🔎 1. Overview

Simple CLI product manager for learning and assignments. Use it to add, list and manage products via a console menu.

## ⚙️ 2. Requirements

- Python 3.8+
- (Optional) `requirements.txt` if third-party libraries are added

## 🛠️ 3. Installation

1. Clone the repository:

```powershell
git clone <your-repo-url>
cd tugas_uas
```

2. (Optional) Create and activate a virtual environment:

```powershell
python -m venv venv; .\venv\Scripts\Activate.ps1
```

3. Install dependencies (if present):

```powershell
pip install -r requirements.txt
```

## ▶️ 4. Running the app

Run from project root:

```powershell
python main.py
```

## ✍️ 5. Usage Examples

- Add product: follow menu prompt to add product name, price, and stock.
- List products: select "List" or similar option in the menu.

Fill these steps with exact menu option names after you inspect `ui/menu.py`.

## 🖼️ 6. Screenshots

You can include multiple screenshots to illustrate different parts of the application (list view, add form, error states, diagrams).

Place images in the `screenshots/` folder and name them logically (for example: `screenshot-1.png`, `add-product.png`, `flow-diagram.png`).

Example Markdown references:

```markdown
![List view](../screenshots/screenshot-1.png)
![Add product](../screenshots/add-product.png)
![Flow diagram](../screenshots/flow-diagram.png)
```

PowerShell example to copy multiple screenshots into the project:

```powershell
mkdir screenshots; cp .\path\to\image1.png .\screenshots\screenshot-1.png; cp .\path\to\image2.png .\screenshots\screenshot-2.png
```

Tips

- Keep filenames descriptive for easier referencing in the manual.
- Use a consistent naming pattern for ordered images (e.g., `screenshot-1.png`, `screenshot-2.png`).
- Use lower-case names and hyphens to avoid cross-platform path issues.

## 🧭 7. Troubleshooting

- Missing dependencies: run `pip install -r requirements.txt`.
- Python path issues: ensure `python` in PATH or use the `py` launcher.

## ✉️ 8. Contact / Author

Add your name and contact details here.

---

Replace placeholder sections above with detailed steps and examples specific to your implementation.
