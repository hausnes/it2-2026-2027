# Viser et bilde i terminalen ved hjelp av "pixels" laget av tekst.
# Installer først: pip install rich-pixels
# Dokumentasjon: https://pypi.org/project/rich-pixels/

from pathlib import Path

from rich.console import Console
from rich_pixels import Pixels

# Finner bildet i samme mappe som denne fila, uansett hvor du kjører programmet fra.
bildefil = "skolebygget.webp"

console = Console()
pixels = Pixels.from_image_path(bildefil)
console.print(pixels)
