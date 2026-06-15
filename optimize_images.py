"""
Optimiza las imágenes de la landing Canopy GuardIAn.

- Mueve los originales a images/originals/
- Genera versiones .webp (formato moderno, ~70% más liviano) y .jpg (fallback)
- Redimensiona a 1600px de ancho máximo (manteniendo aspect ratio)
- Reporta tamaños antes/después

Uso:
    python optimize_images.py
"""

from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).parent
IMG_DIR = ROOT / "images"
ORIGINALS_DIR = IMG_DIR / "originals"

MAX_WIDTH = 1600
WEBP_QUALITY = 82
JPG_QUALITY = 82

TARGETS = [
    "hardware",
    "bosque-nativo",
    "plantacion",
    "ranger-alerta",
    "ariel-herrera",
    "esteban-donoso",
]


def fmt_size(n_bytes: int) -> str:
    for unit in ("B", "KB", "MB"):
        if n_bytes < 1024:
            return f"{n_bytes:.1f} {unit}"
        n_bytes /= 1024
    return f"{n_bytes:.1f} GB"


def main():
    ORIGINALS_DIR.mkdir(exist_ok=True)
    total_before = 0
    total_after = 0

    print(f"Optimizando imágenes en {IMG_DIR}")
    print("-" * 70)

    for name in TARGETS:
        # Localizar el archivo (puede ser .png, .jpg, .jpeg)
        src = None
        for ext in (".png", ".PNG", ".jpg", ".JPG", ".jpeg"):
            cand = IMG_DIR / f"{name}{ext}"
            if cand.exists():
                src = cand
                break
        if src is None:
            print(f"  - {name}: no encontrado, omitido")
            continue

        size_before = src.stat().st_size
        total_before += size_before

        # Mover original a /originals
        original_path = ORIGINALS_DIR / src.name
        if not original_path.exists():
            src.replace(original_path)
        else:
            src.unlink()  # ya existe el respaldo

        # Abrir + corregir orientación EXIF + convertir a RGB
        img = Image.open(original_path)
        img = ImageOps.exif_transpose(img)
        if img.mode in ("RGBA", "P"):
            background = Image.new("RGB", img.size, (15, 23, 42))  # navy del sitio
            if img.mode == "P":
                img = img.convert("RGBA")
            background.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
            img = background
        elif img.mode != "RGB":
            img = img.convert("RGB")

        # Redimensionar si es muy grande
        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / img.width
            new_size = (MAX_WIDTH, int(img.height * ratio))
            img = img.resize(new_size, Image.LANCZOS)

        # Guardar versiones optimizadas
        webp_out = IMG_DIR / f"{name}.webp"
        jpg_out = IMG_DIR / f"{name}.jpg"

        img.save(webp_out, "WEBP", quality=WEBP_QUALITY, method=6)
        img.save(jpg_out, "JPEG", quality=JPG_QUALITY, optimize=True, progressive=True)

        size_webp = webp_out.stat().st_size
        size_jpg = jpg_out.stat().st_size
        size_after = size_webp  # usaremos webp como principal
        total_after += size_after

        reduction = (1 - size_after / size_before) * 100
        print(f"  {name}")
        print(f"     antes:  {fmt_size(size_before):>10}   ({img.width}px ancho final)")
        print(f"     webp:   {fmt_size(size_webp):>10}   ({reduction:.0f}% menos)")
        print(f"     jpg:    {fmt_size(size_jpg):>10}   (fallback)")
        print()

    print("-" * 70)
    print(f"Total antes:  {fmt_size(total_before)}")
    print(f"Total después (webp): {fmt_size(total_after)}")
    if total_before > 0:
        print(f"Ahorro: {(1 - total_after/total_before)*100:.1f}%")
    print()
    print(f"Originales respaldados en: {ORIGINALS_DIR}")


if __name__ == "__main__":
    main()
