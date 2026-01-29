from PIL import Image
import os
import shutil
from card_utils import normalize_name, extract_card_name

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

# Process matched cards
copied = []
not_found = []

for i, card_name in enumerate(card_names, 1):
    print(f"[{i}/{len(card_names)}] Processing: {card_name}")
    normalized = normalize_name(card_name)
    if normalized in all_images:
        src_path = all_images[normalized]
        filename = os.path.basename(src_path)
        dst_path = os.path.join("decklist", filename)
        
        # Crop the 54px margin from all sides (1262x1714 -> 1154x1606)
        image = Image.open(src_path)
        cropped = image.crop((54, 54, 1208, 1660))
        cropped.save(dst_path)
        
        copied.append(card_name)
        print(f"  ✓ Deresized: {filename}")
    else:
        not_found.append(card_name)
        print(f"  ✗ Not found: {card_name}")

# Summary
print(f"Deresized {len(copied)} cards to decklist folder")
if not_found:
    print(f"\nCards not found ({len(not_found)}):")
    for card in not_found:
        print(f"  - {card}")
else:
    print("All cards found and deresized!")