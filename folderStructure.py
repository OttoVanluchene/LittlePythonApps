import os
from pathlib import Path

def generate_tree(path, ignore_folders, full_structure=True, indent=0, is_root=True):
    tree = ""

    for entry in sorted(os.listdir(path)):
        entry_path = os.path.join(path, entry)

        if os.path.isdir(entry_path) and not entry.startswith('.') and (entry not in ignore_folders or not is_root):
            if is_root:
                tree += f"- [[{entry}]]\n"
            else:
                tree += f"{'    ' * indent}- [[{entry}]]\n"
                
            tree += generate_tree(entry_path, ignore_folders, full_structure, indent + 1, is_root=False)

    return tree


def main():
    current_path = os.getcwd()
    output_file = "+ Index.md"
    ignore_folders = ['Inbox', 'Documents', 'Journal', 'Readwise']

    choice = input("Choose folder structure type:\n1. Full folder structure\n2. Main folders only\nYour choice (1/2): ")

    if choice == "1":
        full_structure = True
    elif choice == "2":
        full_structure = False
    else:
        print("Invalid choice, defaulting to full folder structure.")
        full_structure = True

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(generate_tree(current_path, ignore_folders, full_structure))


if __name__ == "__main__":
    main()
