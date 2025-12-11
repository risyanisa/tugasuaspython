# Tugas UAS - Product Manager (Simple CLI)

A small Python project for managing products with a minimal UI and a lightweight database module. This repository contains the application entrypoint and organized packages for model, database, and UI logic. Use this README to quickly run the app and add your manual and screenshots.

**Features**
- Basic product model stored using the `database` module
- Console/menu-driven UI in `ui/menu.py`
- Simple, easy-to-extend structure for learning and assignments

**Project Structure**
```
main.py
database/
    __init__.py
    db.py
model/
    __init__.py
    product.py
ui/
    __init__.py
    menu.py
```

**Quick Start**
- Requirements: Python 3.8+ (recommended)
- From the project root run:

```powershell
python main.py
```

(If your environment uses `py` launcher: `py main.py`)

**Where to put a screenshot**
Add a screenshot file to `screenshots/screenshot.png` and it will be displayed here in the README. Example markdown is already included below — replace the file with your actual screenshot.

![Project Screenshot](screenshots/screenshot.png)

**Manual / Documentation**
A manual placeholder is provided at `docs/MANUAL.md`. Open that file and replace the placeholder content with your step-by-step manual, usage examples, and any screenshots or diagrams.

**How to add the manual and screenshot**
- Edit `docs/MANUAL.md` and add your manual text and examples.
- Create a `screenshots/` folder at project root and add `screenshot.png` (recommended resolution: 1280x720 or similar).
- Update this README or the manual as needed.

**Development notes**
- Keep database files (if created) out of git — the provided `.gitignore` covers common Python artifacts and virtual environments.
- Tests are not included; consider adding a `tests/` folder and a `requirements.txt` if you add dependencies.

**Contributing**
- Make small, focused commits.
- Add a descriptive commit message and push to a feature branch.

**License**
Add a license file if you intend to publish this project. For coursework, you may keep the code private or add an appropriate license later.
