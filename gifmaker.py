import os
from PIL import Image  # Import the Image module from the Pillow library

def create_gif_from_images(input_dir, output_gif, identifier, duration=500):
    """Creates a GIF from images with a specific identifier in the specified directory."""
    os.makedirs(os.path.dirname(output_gif), exist_ok=True)
    images = []

    # Collect all image paths with the given identifier and sort them by iteration index
    for file_name in sorted(os.listdir(input_dir)):
        if file_name.startswith(identifier) and file_name.endswith(".png"):
            images.append(Image.open(os.path.join(input_dir, file_name)))

    # Create and save the GIF
    if images:
        images[0].save(output_gif, save_all=True, append_images=images[1:], duration=duration, loop=0)
