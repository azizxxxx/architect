from pathlib import Path
from PIL import Image

root = Path('/home/ubuntu/forma-studio/client/public/assets')
for path in root.glob('*.jpg'):
    image = Image.open(path).convert('RGB')
    image.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
    image.save(path, 'JPEG', quality=72, optimize=True, progressive=True)

logo = root / 'forma-mark.png'
if logo.exists():
    image = Image.open(logo).convert('RGBA')
    image.thumbnail((512, 512), Image.Resampling.LANCZOS)
    image.save(logo, 'PNG', optimize=True)
