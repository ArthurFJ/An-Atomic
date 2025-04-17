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
    for root, dirs, files in os.walk(base_path):
        # If the folder has no subdirectories, it's a final folder
        if not dirs:
            # Create a new file in the folder named README.md
            new_file_name = "README.md"
            new_file_path = os.path.join(root, new_file_name)

            # Only create the file if it doesn't already exist
            if not os.path.exists(new_file_path):
                shutil.copy(template_path, new_file_path)
                print(f"Created: {new_file_path}")

            # Delete name_of_folder.md if it exists
            folder_name = os.path.basename(root)
            folder_md_file = os.path.join(root, f"{folder_name}.md")
            if os.path.exists(folder_md_file):
                os.remove(folder_md_file)
                print(f"Deleted: {folder_md_file}")

if __name__ == "__main__":
    create_files_from_template()
