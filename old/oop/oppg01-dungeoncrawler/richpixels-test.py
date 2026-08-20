from rich_pixels import Pixels
from rich.console import Console

console = Console()
pixels = Pixels.from_image_path("skolebygget.webp")
console.print(pixels)