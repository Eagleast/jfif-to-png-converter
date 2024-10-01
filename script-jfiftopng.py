import os
import argparse
from PIL import Image

# Function to convert JFIF to PNG
def convert_jfif_to_png(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return
    
    # Create an output folder if it doesn't exist
    output_folder = os.path.join(folder_path, "converted_pngs")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".jfif"):
            jfif_path = os.path.join(folder_path, filename)
            try:
                # Open the JFIF image
                with Image.open(jfif_path) as img:
                    # Convert and save as PNG
                    png_filename = os.path.splitext(filename)[0] + ".png"
                    png_path = os.path.join(output_folder, png_filename)
                    img.save(png_path, "PNG")
                    print(f"Converted: {filename} -> {png_filename}")
                
                # Delete the original JFIF file
                os.remove(jfif_path)
                print(f"Deleted: {filename}")
                
            except Exception as e:
                print(f"Error converting {filename}: {e}")
    
    print("Conversion and deletion complete.")

# Main function to parse command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Convert JFIF images to PNG format and delete the original JFIF files.")
    parser.add_argument("folder", help="Path to the folder containing JFIF images.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Call the conversion function with the specified folder
    convert_jfif_to_png(args.folder)

# Entry point
if __name__ == "__main__":
    main()
