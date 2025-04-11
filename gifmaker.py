import os
from PIL import Image
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_gif_from_images(input_dir, output_gif, identifier, duration=500):
    """
    Vytvoří GIF z obrázků se specifickým identifikátorem v zadaném adresáři.

    Args:
        input_dir (str): Adresář obsahující vstupní obrázky.
        output_gif (str): Cesta pro uložení výstupního GIFu.
        identifier (str): Jedinečný identifikátor pro filtrování obrázků.
        duration (int): Doba trvání (v milisekundách) pro každý snímek v GIFu.
    """
    os.makedirs(os.path.dirname(output_gif), exist_ok=True)
    images = []

    # Sběr všech cest k obrázkům s daným identifikátorem
    image_files = [
        file_name for file_name in os.listdir(input_dir)
        if file_name.startswith(identifier) and file_name.endswith(".png")
    ]

    # Seřazení souborů numericky podle čísla iterace
    image_files.sort(key=lambda x: int(x.split("_iteration_")[1].split(".png")[0]))

    # Otevření obrázků v seřazeném pořadí
    for file_name in image_files:
        images.append(Image.open(os.path.join(input_dir, file_name)))

    # Vytvoření a uložení GIFu
    if images:
        images[0].save(output_gif, save_all=True, append_images=images[1:], duration=duration, loop=0)