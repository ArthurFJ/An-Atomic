import os
import shutil

def write_readme_in_final_dirs(base_path, template_path):
    """
    Writes a README.md file in all final directories of the given base path
    using the specified template file.
    """
    for root, dirs, files in os.walk(base_path):
        # A final directory has no subdirectories
        if not dirs:
            readme_path = os.path.join(root, "README.md")
            if not os.path.exists(readme_path):  # Avoid overwriting existing README.md
                shutil.copy(template_path, readme_path)
                print(f"README.md written in: {root}")
            else:
                print(f"README.md already exists in: {root}")

def main():
    # Define paths for courses and projects
    courses_base_path = "OM_Bit/Courses"
    projects_base_path = "OM_Bit/Projects"
    course_template_path = os.path.join(courses_base_path, "course_template.md")
    project_template_path = os.path.join(projects_base_path, "project_template.md")

    # Ensure template files exist
    if not os.path.exists(course_template_path):
        print(f"Course template not found: {course_template_path}")
        return
    if not os.path.exists(project_template_path):
        print(f"Project template not found: {project_template_path}")
        return

    # Write README.md in final directories
    write_readme_in_final_dirs(courses_base_path, course_template_path)
    write_readme_in_final_dirs(projects_base_path, project_template_path)

if __name__ == "__main__":
    main()