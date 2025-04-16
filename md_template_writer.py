import os
import shutil

def create_files_from_template():
    # Paths
    base_path = "OM_Bit/OMB_Course"
    template_path = os.path.join(base_path, "template.md")
    folders_to_scan = [
        os.path.join(base_path, "0_Languages"),
        os.path.join(base_path, "1_Topics")
    ]

    # Check if the template exists
    if not os.path.exists(template_path):
        print(f"Template file '{template_path}' not found.")
        return

    # Process each folder
    for folder in folders_to_scan:
        if not os.path.exists(folder):
            print(f"Folder '{folder}' not found.")
            continue

        for item in os.listdir(folder):
            item_path = os.path.join(folder, item)
            if os.path.isdir(item_path):
                # Create a new file in the subfolder with the lowercase name of the folder
                new_file_name = f"{item.lower()}.md"
                new_file_path = os.path.join(item_path, new_file_name)

                # Copy the template content to the new file
                shutil.copy(template_path, new_file_path)
                print(f"Created: {new_file_path}")

if __name__ == "__main__":
    create_files_from_template()