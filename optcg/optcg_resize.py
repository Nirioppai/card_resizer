try:
    from PIL import Image
    import os
    
    output_dir = "optcg_resized_cards"
    os.makedirs(output_dir, exist_ok=True)
    
    found_images = False
    for file in os.listdir("."):
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            found_images = True
            output_path = f"{output_dir}/{file}"
            if not os.path.exists(output_path):
                # Resize card to fit within 1154x1606 (1262-108, 1714-108 for 54px margin on each side)
                card = Image.open(file).resize((1154, 1606))
                # Create 1262x1714 canvas and paste card centered with 54px margin
                canvas = Image.new('RGB', (1262, 1714), 'black')
                canvas.paste(card, (54, 54))
                canvas.save(output_path)
                os.remove(file)
                print(f"Resized: {file}")
            else:
                print(f"Skipped: {file} (already exists)")
    
    if not found_images:
        print("No image files found in current directory")
        
except Exception as e:
    print(f"Error: {e}")

input("Press Enter to exit...")