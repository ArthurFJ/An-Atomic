import os
import shutil

def write_readme_in_final_folders(base_dir, template_path):
    # Read the content of the template.md file
    if not os.path.exists(template_path):
        print(f"Template file '{template_path}' not found.")
        return
    
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()

    # Walk through the directory tree
    for root, dirs, files in os.walk(base_dir):
        # Check if the current folder is a final folder (no subdirectories)
        if not dirs:
            readme_path = os.path.join(root, 'README.md')
            # Write the README.md file
            with open(readme_path, 'w', encoding='utf-8') as readme_file:
                readme_file.write(template_content)
            print(f"README.md written in: {root}")

if __name__ == "__main__":
    # Define the base directory and template file path
    base_directory = os.path.join(os.getcwd(), "OM_Bit")
    template_file_path = os.path.join(os.getcwd(), "template.md")
    
    # Call the function
    write_readme_in_final_folders(base_directory, template_file_path)