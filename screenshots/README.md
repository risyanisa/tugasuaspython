# Screenshots folder

Store screenshots that illustrate the app UI and flows.

You can add two or more images. Recommended naming conventions:

- Ordered gallery: `screenshot-1.png`, `screenshot-2.png`, …
- Descriptive names: `list-products.png`, `add-product.png`, `flow-diagram.png`

PowerShell examples:

```powershell
# copy multiple images and give them project-friendly names
mkdir screenshots
cp .\path\to\image1.png .\screenshots\screenshot-1.png
cp .\path\to\image2.png .\screenshots\screenshot-2.png
cp .\path\to\diagram.png .\screenshots\flow-diagram.png
```

Recommended resolution: 1280×720 for main screenshots; smaller thumbnails are fine for gallery grids.

Refer to these images from `README.md` or `docs/MANUAL.md` using relative paths, e.g. `screenshots/screenshot-1.png`.
