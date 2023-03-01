from PIL import Image
import os

# Set the directory containing the PNG images
directory = os.getcwd()

# Set the name of the output GIF file
gif_file = "output.gif"

# Create a list of the PNG files in the directory
png_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".png")]

# Sort the PNG files alphabetically by file name
png_files.sort()

# Open the first PNG file to get the image dimensions
with Image.open(png_files[0]) as im:
    width, height = im.size

# Create a new GIF file
with Image.new("RGB", (width, height)) as gif:

    # Create a list to store each frame of the GIF
    frames = []

    # Iterate over the PNG files and add each frame to the GIF file
    for png_file in png_files:
        with Image.open(png_file) as im:
            frames.append(im.copy())

    # Save the frames as a GIF file
    frames[0].save(gif_file, format="GIF", append_images=frames[1:], save_all=True, duration=10, loop=0)

