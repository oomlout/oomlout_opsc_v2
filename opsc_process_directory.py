import os
import opsc

def process_file_all(file_path, overwrite):
    """
    A function that processes a single file.

    Args:
        file_path (str): The path to the file to process.
        overwrite (bool): Whether to overwrite existing files.

    Returns:
        None
    """
    file_name, file_ext = os.path.splitext(file_path)
    png_file_path = file_name + ".png"
    if not overwrite and os.path.exists(png_file_path):
        # A PNG file with the same name already exists, do not process the file.
        return
    opsc.saveToAll(file_path)
    
def process_file_stl(file_path, overwrite):
    """
    A function that processes a single file.

    Args:
        file_path (str): The path to the file to process.
        overwrite (bool): Whether to overwrite existing files.

    Returns:
        None
    """
    file_name, file_ext = os.path.splitext(file_path)
    png_file_path = file_name + ".png"
    if not overwrite and os.path.exists(png_file_path):
        # A PNG file with the same name already exists, do not process the file.
        return
    opsc.saveToStl(file_path)
    
def process_file_the_rest(file_path, overwrite):
    """
    A function that processes a single file.

    Args:
        file_path (str): The path to the file to process.
        overwrite (bool): Whether to overwrite existing files.

    Returns:
        None
    """
    file_name, file_ext = os.path.splitext(file_path)
    png_file_path = file_name + ".png"
    if not overwrite and os.path.exists(png_file_path):
        # A PNG file with the same name already exists, do not process the file.
        return
    opsc.saveToTheRest(file_path)

def process_directory(directory_path, overwrite):
    """
    A function that processes all the .scad files in a directory and its subdirectories.

    Args:
        directory_path (str): The path to the directory to process.
        overwrite (bool): Whether to overwrite existing files.

    Returns:
        None
    """
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".scad"):
                file_path = os.path.join(root, file)
                process_file_all(file_path, overwrite)
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".scad"):
                file_path = os.path.join(root, file)
                process_file_stl(file_path, overwrite)
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".scad"):
                file_path = os.path.join(root, file)
                process_file_the_rest(file_path, overwrite)

def do_now(file_path):
    """
    A function that does something with a file.

    Args:
        file_path (str): The path to the file to process.

    Returns:
        None
    """
    # Replace this with the code that you want to run on each .scad file.
    print(f"Processing file: {file_path}")

if __name__ == "__main__":
    import argparse    
    parser = argparse.ArgumentParser(description="Recursively process all .scad files in a directory.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files.")
    args = parser.parse_args()
    # process_directory(".", args.overwrite)
    process_directory(r"C:\GH\oomlout_oobb_v3\things", args.overwrite)
