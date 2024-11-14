import argparse
import os
from PIL import Image
from PIL.ExifTags import TAGS
import datetime


def parse_args():
    parser = argparse.ArgumentParser(
        description="Scorpion program to parse image metadata.")
    parser.add_argument("files", nargs='+',
                        help="Image files to parse metadata from")
    return parser.parse_args()


def display_basic_attributes(filepath):
    if os.path.exists(filepath):
        file_size = os.path.getsize(filepath) / 1024  # in Kb
        creation_time = datetime.datetime.fromtimestamp(
            os.path.getctime(filepath)).strftime('%Y-%m-%d %H:%M:%S')
        print(f"File: {filepath}")
        print(f"Size: {file_size:.2f} KB")
        print(f"Created: {creation_time}")
    else:
        print(f"File not found: {filepath}")


def display_exif_data(image):
    """Extracts and displays EXIF metadata if available."""
    try:
        exif_data = image._getexif()
        if exif_data:
            print("EXIF Data:")
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                print(f"{tag_name}: {value}")
        else:
            print("No EXIF data found.")
    except AttributeError:
        print("No EXIF data available for this image.")


def process_image(file_path):
    """Process the image file and extract metadata."""
    try:
        with Image.open(file_path) as img:
            display_basic_attributes(file_path)
            if img.format in ['JPEG', 'JPG']:
                display_exif_data(img)
            print("-" * 40)  # Divider for readability
    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def main():
    args = parse_args()
    for file in args.files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            process_image(file)
        else:
            print(f"Unsupported file format: {file}")


if __name__ == "__main__":
    main()
