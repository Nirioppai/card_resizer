try:
    from PIL import Image, ImageDraw, ImageFont
    import os
    
    os.makedirs("framed_cards", exist_ok=True)
    
    found_images = False
    for file in os.listdir("."):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            found_images = True
            output_path = f"framed_cards/{file}"
            if not os.path.exists(output_path):
                img = Image.open(file)
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("times.ttf", 28)
                draw.text((738, 1585), "™ & © 2025 Wizards of the Coast", font=font, fill="white")
                img.save(output_path)
                os.remove(file)
                print(f"Framed: {file}")
            else:
                print(f"Skipped: {file} (already exists)")
    
    if not found_images:
        print("No image files found in current directory")
        
except Exception as e:
    print(f"Error: {e}")

input("Press Enter to exit...")