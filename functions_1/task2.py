import os

def find_folder(name):
    try:
        if not os.path.isdir(name):
            print("The folder does not exist")
            return
        files = os.listdir(name)
        if len(files) == 0:
            print("The folder is empty")
            return

        print("\nFiles in", name)
        
        for file in files:
            file_path = os.path.join(name, file)
            if os.path.isfile(file_path):
                print(file)

    except PermissionError:
        print("Permission denied. You cannot access this folder.")

    except OSError as error:
        print("Error:", error)

def change_name(name, new_name):
    try:
        folder = os.path.dirname(name)
        if folder:
            new_path = os.path.join(folder, new_name)
        else:
            new_path = new_name
        os.rename(name, new_path)

        print("Updated file name:", new_path)

    except FileNotFoundError:
        print("The file was not found")

    except FileExistsError:
        print("A file with that name already exists")

    except PermissionError:
        print("Permission denied. The file cannot be renamed.")

    except OSError as error:
        print("An error occurred:", error)

def main():
    print("Task A - List Folder Files")
    folder_name = input("Enter the name or path of a folder: ")
    find_folder(folder_name)

    print("\nTask B - Change File Name")
    file_name = input("Enter the file name or path: ")
    new_file_name = input("Enter the new file name: ")

    change_name(file_name, new_file_name)

if __name__ == "__main__":
    main()