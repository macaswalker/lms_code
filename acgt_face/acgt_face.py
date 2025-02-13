import cv2

print("hello world")


def pixel_to_dna(val):
    if val < 64:
        return "A"
    elif val < 128:
        return "C"
    elif val < 192:
        return "G"
    else:
        return "T"


def image_to_dna_ascii(image_path, output_width):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    h, w = img.shape

    ratio = h/w

    output_height = int(output_width * ratio * 0.55)  # Adjusting for font aspect ratio

    resized_img = cv2.resize(img, (output_width, output_height))

    dna_art = []

    for row in resized_img:

        dna_row = [pixel_to_dna(pixel) for pixel in row]

        dna_art.append("".join(dna_row))

    return "\n".join(dna_art)

image_path = "profile_photo.jpeg"
output_width = 500
dna_ascii = image_to_dna_ascii(image_path, output_width)

# Save the ASCII art to a file
with open("dna_art.txt", "w") as f:
    f.write(dna_ascii)

# Print the ASCII art to the console
print(dna_ascii)
