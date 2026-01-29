try:
    from PIL import Image
    import os
    
    input_dir = "optcg_resized_cards"
    output_dir = "optcg_deresized_cards"
    os.makedirs(output_dir, exist_ok=True)
    
    found_images = False
    for file in os.listdir(input_dir):
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            found_images = True
            input_path = f"{input_dir}/{file}"
            output_path = f"{output_dir}/{file}"
            if not os.path.exists(output_path):
                # Crop the 54px margin from all sides (1262x1714 -> 1154x1606)
                image = Image.open(input_path)
                cropped = image.crop((54, 54, 1208, 1660))
                cropped.save(output_path)
                print(f"Deresized: {file}")
            else:
                print(f"Skipped: {file} (already exists)")
    
    if not found_images:
        print("No image files found in optcg_resized_cards directory")
        
except Exception as e:
    print(f"Error: {e}")

input("Press Enter to exit...")