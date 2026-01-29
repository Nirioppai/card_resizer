import os
from card_utils import extract_card_name

directories = ["resized_cards/frame_new/framed_cards", "resized_cards/frame_old"]

with open("list.txt", "w") as f:
    for directory in directories:
        if os.path.exists(directory):
            for file in os.listdir(directory):
                if file.lower().endswith(('.png', '.jpg', '.jpeg')) and file != "Rowan, Scion of War.png":
                    name = extract_card_name(file)
                    f.write(name + "\n")
    
    if not any(os.path.exists(d) for d in directories):
        f.write("Directories not found\n")