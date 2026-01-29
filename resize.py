try:
    from PIL import Image
    import os
    
    new_frames = input("Are all cards to be resized new frames? (Y/n): ").lower()
    
    if new_frames in ["", "y"]:
        output_dir = "resized_cards/frame_new"
    else:
        output_dir = "resized_cards"
    
    os.makedirs(output_dir, exist_ok=True)
    
    framed_cards = set()
    if os.path.exists("resized_cards/frame_new/framed_cards/"):
        framed_cards = set(os.listdir("resized_cards/frame_new/framed_cards/"))
    
    found_images = False
    for file in os.listdir("."):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            found_images = True
            if file in framed_cards:
                os.remove(file)
                print(f"Deleted: {file} (already framed)")
                continue
            output_path = f"{output_dir}/{file}"
            if not os.path.exists(output_path):
                Image.open(file).resize((1262, 1714)).save(output_path)
                os.remove(file)
                print(f"Resized: {file}")
            else:
                print(f"Skipped: {file} (already exists)")
    
    if not found_images:
        print("No image files found in current directory")
        
except Exception as e:
    print(f"Error: {e}")

input("Press Enter to exit...")