from colorthief import ColorThief
import matplotlib.pyplot as plt
import webcolors

ct = ColorThief('images.jpg')

# build a color palette
palette = ct.get_palette(color_count=6)
plt.imshow([[palette[i] for i in range(6)]])
plt.show()

# get the dominant color
dominant_color = ct.get_color(quality=1)

#detecting the dominant color name
def closest_color(rgb):
    differences = {}
    for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
        r, g, b = webcolors.hex_to_rgb(color_hex)
        differences[
            sum([(r - rgb[0])**2,
            (g - rgb[1])**2,
            (b - rgb[2])**2,
            ])] = color_name
    return differences[min(differences.keys())]

color = dominant_color

try:
    cname = webcolors.rgb_to_name(color)
    print(f'The Dominant color is exactly {cname}')
except ValueError:
    cname = closest_color(color)
    print(f'The Dominant color is closest to {cname}')

plt.imshow([[color]])
plt.show()
