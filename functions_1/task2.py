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
        print("\n Files in ", name)
        
        for file in files:
            file_path = os.path.join(name, file)
            
            if os.path.isfile(file_path):
                print(file)
                
    except PermissionError:
        print("Permission denied. You cannot access this folder.")
    
    except OSError as error:
        print("Error: ", error)