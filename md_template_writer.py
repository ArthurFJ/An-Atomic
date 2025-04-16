import os
import shutil

def create_files_from_template():
    # Corrected base path
    base_path = "C:/Users/fauge/OneDrive/Escritorio/One_More_ALFJ"
    template_path = os.path.join(base_path, "template.md")

    # Check if the template exists
    if not os.path.exists(template_path):
        print(f"Template file '{template_path}' not found.")
        return

    # Walk through the directory tree
    for root, dirs, _ in os.walk(base_path):
        # If the folder has no subdirectories, it's a final folder
        if not dirs:
            # Create a new file in the folder with the lowercase name of the folder
            folder_name = os.path.basename(root)
            new_file_name = f"{folder_name.lower()}.md"
            new_file_path = os.path.join(root, new_file_name)

            # Only create the file if it doesn't already exist
            if not os.path.exists(new_file_path):
                shutil.copy(template_path, new_file_path)
                print(f"Created: {new_file_path}")

if __name__ == "__main__":
    create_files_from_template()
