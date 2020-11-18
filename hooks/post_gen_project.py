# hooks/post_gen_project.py
import os
import shutil


def remove_tailwind_folder():
    theme_dir_path = "theme"
    if os.path.exists(theme_dir_path):
        shutil.rmtree(theme_dir_path)

# ...

def main():
    remove_tailwind_folder()

if __name__ == "__main__":
    main()