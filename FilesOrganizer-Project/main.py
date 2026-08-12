from pathlib import Path
import shutil


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def ask_again(prompt):
    """Ask the user a yes/no question."""
    while True:
        answer = input(prompt).lower().strip()

        if answer in ("yes", "no"):
            return answer

        print("Please answer yes or no.")


def get_folder():
    """Ask the user for a valid folder path."""
    while True:
        folder_path = input("Enter a folder path: ").strip()
        folder = Path(folder_path)

        if not folder.is_dir():
            print("The folder path does not exist. Please try again.\n")
            continue

        return folder


def get_unique_destination(item, destination):
    """Return a unique destination path for a file."""

    destination_file = destination / item.name

    # Use the original filename if it doesn't already exist.
    if not destination_file.exists():
        return destination_file

    # Otherwise, try _1, _2, _3, etc.
    i = 1

    while True:
        new_name = f"{item.stem}_{i}{item.suffix}"
        new_destination = destination / new_name

        if not new_destination.exists():
            return new_destination

        i += 1


# ============================================================
# FILE ORGANIZER
# ============================================================

def organize_files(folder):
    """Organize files into folders based on their extensions."""

    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Documents": [".pdf", ".txt", ".docx"],
        "Code": [".py", ".cpp", ".js"]
    }

    for item in folder.iterdir():

        # Skip folders and only process files.
        if not item.is_file():
            continue

        extension = item.suffix.lower()
        found = False

        # Check which category the file belongs to.
        for category, extensions in file_categories.items():

            for extension_type in extensions:

                if extension == extension_type:
                    found = True

                    destination = folder / category
                    destination.mkdir(exist_ok=True)

                    new_destination = get_unique_destination(
                        item,
                        destination
                    )

                    shutil.move(item, new_destination)

                    if new_destination.name == item.name:
                        print(
                            f"Moved {item.name} to {destination}"
                        )
                    else:
                        print(
                            f"{item.name} already exists. "
                            f"Renamed to {new_destination.name}"
                        )

                    break

            if found:
                break

        # Move unsupported file types to Others.
        if not found:

            destination = folder / "Others"
            destination.mkdir(exist_ok=True)

            new_destination = get_unique_destination(
                item,
                destination
            )

            shutil.move(item, new_destination)

            if new_destination.name == item.name:
                print(
                    f"Moved {item.name} to {destination}"
                )
            else:
                print(
                    f"{item.name} already exists. "
                    f"Renamed to {new_destination.name}"
                )


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    """Run the File Organizer program."""

    while True:

        print("\n" + "=" * 50)
        print("             FILE ORGANIZER")
        print("=" * 50)

        folder = get_folder()

        organize_files(folder)

        print("\nFiles organized successfully!")

        if ask_again(
            "\nDo you want to organize another folder? (yes/no): "
        ) != "yes":

            print("\nThank you for using File Organizer!")
            break


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
