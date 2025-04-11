import os
from PIL import Image
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_gif_from_images(input_dir, output_gif, identifier, duration=500):
    """
    Creates a GIF from images with a specific identifier in the specified directory.

    Args:
        input_dir (str): The directory containing the input images.
        output_gif (str): The path to save the output GIF.
        identifier (str): A unique identifier to filter the images.
        duration (int): The duration (in milliseconds) for each frame in the GIF.
    """
    os.makedirs(os.path.dirname(output_gif), exist_ok=True)
    images = []

    # Collect all image paths with the given identifier
    image_files = [
        file_name for file_name in os.listdir(input_dir)
        if file_name.startswith(identifier) and file_name.endswith(".png")
    ]

    # Sort filenames numerically based on the iteration number
    image_files.sort(key=lambda x: int(x.split("_iteration_")[1].split(".png")[0]))

    # Open images in sorted order
    for file_name in image_files:
        images.append(Image.open(os.path.join(input_dir, file_name)))

    # Create and save the GIF
    if images:
        images[0].save(output_gif, save_all=True, append_images=images[1:], duration=duration, loop=0)


