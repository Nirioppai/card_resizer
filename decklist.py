from PIL import Image
import os
import shutil
from card_utils import normalize_name, extract_card_name

def modify_and_copy_image(src_path, dst_path, unique_id):
    """Copy image with unique modification to ensure different hash"""
    img = Image.open(src_path)
    width, height = img.size
    pixels = img.load()
    
    # Modify entire bottom row with rotating color channels
    for i in range(width):
        x, y = i, height - 1
        channel = (unique_id + i) % 3  # Rotate between R, G, B
        if img.mode == 'RGB':
            r, g, b = pixels[x, y]
            if channel == 0:
                pixels[x, y] = ((r + unique_id + i) % 256, g, b)
            elif channel == 1:
                pixels[x, y] = (r, (g + unique_id + i) % 256, b)
            else:
                pixels[x, y] = (r, g, (b + unique_id + i) % 256)
        elif img.mode == 'RGBA':
            r, g, b, a = pixels[x, y]
            if channel == 0:
                pixels[x, y] = ((r + unique_id + i) % 256, g, b, a)
            elif channel == 1:
                pixels[x, y] = (r, (g + unique_id + i) % 256, b, a)
            else:
                pixels[x, y] = (r, g, (b + unique_id + i) % 256, a)
    
    # Modify entire right column with different rotating pattern
    for i in range(height):
        x, y = width - 1, i
        channel = (unique_id * 2 + i) % 3  # Different rotation pattern
        if img.mode == 'RGB':
            r, g, b = pixels[x, y]
            if channel == 0:
                pixels[x, y] = ((r + unique_id * 3 + i) % 256, g, b)
            elif channel == 1:
                pixels[x, y] = (r, (g + unique_id * 3 + i) % 256, b)
            else:
                pixels[x, y] = (r, g, (b + unique_id * 3 + i) % 256)
        elif img.mode == 'RGBA':
            r, g, b, a = pixels[x, y]
            if channel == 0:
                pixels[x, y] = ((r + unique_id * 3 + i) % 256, g, b, a)
            elif channel == 1:
                pixels[x, y] = (r, (g + unique_id * 3 + i) % 256, b, a)
            else:
                pixels[x, y] = (r, g, (b + unique_id * 3 + i) % 256, a)
    
    # Save without EXIF data
    img.save(dst_path)

# Clear decklist folder
if os.path.exists("decklist"):
    shutil.rmtree("decklist")
os.makedirs("decklist")

# Read decklist
with open("decklist.txt", "r") as f:
    lines = f.readlines()

# Parse card names
card_names = []
for line in lines:
    parts = line.strip().split(' ', 1)
    if len(parts) == 2:
        card_names.append(parts[1])

# Scan directories for images
all_images = {}
directories = ["resized_cards/frame_new/framed_cards", "resized_cards/frame_old"]

for directory in directories:
    if os.path.exists(directory):
        for file in os.listdir(directory):
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                card_name = extract_card_name(file)
                normalized = normalize_name(card_name)
                all_images[normalized] = os.path.join(directory, file)

# Copy matched cards
copied = []
not_found = []

for i, card_name in enumerate(card_names, 1):
    print(f"[{i}/{len(card_names)}] Processing: {card_name}")
    normalized = normalize_name(card_name)
    if normalized in all_images:
        src_path = all_images[normalized]
        filename = os.path.basename(src_path)
        dst_path = os.path.join("decklist", filename)
        modify_and_copy_image(src_path, dst_path, i)
        copied.append(card_name)
        print(f"  ✓ Copied: {filename}")
    else:
        not_found.append(card_name)
        print(f"  ✗ Not found: {card_name}")

# Summary
print(f"Copied {len(copied)} cards to decklist folder")
if not_found:
    print(f"\nCards not found ({len(not_found)}):")
    for card in not_found:
        print(f"  - {card}")
else:
    print("All cards found and copied!")