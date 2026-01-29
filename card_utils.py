import re

def normalize_name(name):
    """Normalize card name for matching"""
    return re.sub(r'[^a-z0-9]', '', name.lower())

def extract_card_name(filename):
    """Extract clean card name from filename"""
    # Remove everything from first parenthesis onwards
    name = filename.split('(')[0].strip()
    # Remove square brackets content
    name = re.sub(r'\s*\[.*?\]\s*', '', name).strip()
    # Remove curly brackets content
    name = re.sub(r'\s*\{.*?\}\s*', '', name).strip()
    
    # Exemptions for underscore replacement
    if name not in ["_____ Goblin", "Rowan, Scion of War.png", "Grist, the Plague Swarm"]:
        name = name.replace('_', "'")
    
    # Replace backticks with apostrophes
    name = name.replace('`', "'")
    
    return name