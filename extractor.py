import PIL
import os
import colorsys
from PIL import Image


def sort_by_luminance(palette):
    def lum(rgb):
        r, g, b = [x / 255 for x in rgb]
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        return h

    return sorted(palette, key=lum)


def calcLuminance(R, G, B):
    Luminance = 0.2126 * R + 0.7152 * G + 0.0722 * B
    return Luminance

while True:
    file_name = str(input("Enter path to your image file: "))
    if os.path.exists(file_name):
        break
    else:
        print("That file doesn't seem to exists...")

image = None

try:
    image = Image.open(file_name)
except (FileNotFoundError, PIL.UnidentifiedImageError) as e:
    print(f"Failed to load image file with error : {e}")
    os.system("pause")
except Exception as e:
    print(f"Unexpected error : {e}")
    os.system("pause")

print("Processing started...")
width, height = image.size
colors = image.getcolors(maxcolors=width * height)
color_count = len(colors)
color = []
print("Colors found...")

palette_text = "JASC-PAL\n0100\n"
palette_text += str(color_count) + "\n"

if color_count <= 0:
    exit()

# Process Colors array from Pillow to more understandable one :D
for i in colors:
    target_color = i[1]
    temp = []
    for a in range(3):
        temp.append(target_color[a])
    color.append(temp)

# Sort
color = sort_by_luminance(color)

# Process palette text
for i in color:
    target_color = i
    for a in range(3):
        palette_text += f"{target_color[a]} "
    palette_text += "\n"

# Write palette file
file_t = open(f"{file_name}.pal", "w", encoding="utf-8")

try:
    file_t.write(palette_text)
    file_t.close()
except Exception as e:
    print(f"Unexpected error : {e}")
    os.system("pause")
    exit()

image.close()
print("Your color palette is ready!")
os.system("pause")
exit()
