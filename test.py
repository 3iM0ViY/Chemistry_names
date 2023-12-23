from rdkit import Chem
from rdkit.Chem import Draw

def visualize_chemical_structure(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        image = Draw.MolToImage(mol)
        # image.show()
        return image

# Example usage
smiles_notation = "c1ccccc1C(=O)OCC"  # Replace with your SMILES notation
image = visualize_chemical_structure(smiles_notation)


import PIL

# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "`", ";", ":", ",", ".", " ", " "]

# resize image according to a new width
def resize_image(image, new_width=200):
    width, height = image.size
    ratio = width/height
    new_height = int(new_width * ratio / 3)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

def main(new_width=200):
    
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    # new_image_data = pixels_to_ascii(resize_image(grayify(image)))
    
    # format
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    # print result
    print(ascii_image)
    
    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
 
if __name__ == "__main__":
    main()