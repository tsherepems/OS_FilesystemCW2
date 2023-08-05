import os
import zipfile
import shutil
from cryptography.fernet import Fernet
import hashlib
import sys


filename =None
directory_name=None
# Get the current directory and use it as the location for the config file
CONFIG_FILE = os.path.join(os.getcwd(), "config.txt")
RECYCLE_BIN_DIR = "recycle_bin"



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def ask_password():
    password = input("Please enter the password: ")
    return hash_password(password)

def check_password():
    try:
        with open(CONFIG_FILE, "r") as file:
            stored_hashed_password = file.read().strip()
    except FileNotFoundError:
        stored_hashed_password = None

    if not stored_hashed_password:
        # If the config.txt file doesn't exist or is empty, prompt the user to set a new password
        entered_password = ask_password()
        with open(CONFIG_FILE, "w") as file:
            file.write(entered_password)

        print("Password set successfully.")
    else:
        # Password is already set, prompt the user to enter the password and check it
        entered_password = ask_password()
        if entered_password != stored_hashed_password:
            # Show an error message and exit the program
            print("Invalid password.")
            sys.exit()

def create_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        return True, "File created successfully!"
    except Exception as e:
        return False, str(e)

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return True, content
    except Exception as e:
        return False, str(e)

def update_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        return True, "File updated successfully!"
    except Exception as e:
        return False, str(e)

def create_recycle_bin():
    try:
        os.mkdir(RECYCLE_BIN_DIR)
    except FileExistsError:
        pass

def delete_file(filename):
    try:
        create_recycle_bin()
        # Move the file to the recycle bin directory
        shutil.move(filename, os.path.join(RECYCLE_BIN_DIR, os.path.basename(filename)))
        return True, "File moved to recycle bin successfully!"
    except Exception as e:
        return False, str(e)

def delete_directory(directory_name):
    try:
        create_recycle_bin()
        # Move the directory to the recycle bin directory
        shutil.move(directory_name, os.path.join(RECYCLE_BIN_DIR, os.path.basename(directory_name)))
        return True, "Directory moved to recycle bin successfully!"
    except Exception as e:
        return False, str(e)

def restore_item(item_name):
    try:
        # Restore the item from the recycle bin to its original location
        original_path = os.path.join(RECYCLE_BIN_DIR, item_name)
        if os.path.exists(original_path):
            shutil.move(original_path, item_name)
            return True, "Item restored successfully!"
        else:
            return False, "Item not found in recycle bin."
    except Exception as e:
        return False, str(e)


def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        return True, "Directory created successfully!"
    except Exception as e:
        return False, str(e)

def list_directory(directory_name):
    try:
        items = os.listdir(directory_name)
        return True, items
    except Exception as e:
        return False, str(e)

   

def compress_item(item_path):
    try:
        if os.path.isfile(item_path):
            with zipfile.ZipFile(f"{item_path}.zip", 'w') as zip_file:
                zip_file.write(item_path, os.path.basename(item_path))
        elif os.path.isdir(item_path):
            shutil.make_archive(item_path, 'zip', item_path)
        else:
            return False, "Invalid item path. Please enter a valid file or folder path."

        return True, "Item compressed successfully!"
    except Exception as e:
        return False, str(e)
    
def decompress_item(item_path):
    try:
        if item_path.endswith('.zip'):
            with zipfile.ZipFile(item_path, 'r') as zip_file:
                zip_file.extractall(os.path.dirname(item_path))
        else:
            return False, "Invalid item path. Please enter a valid zip file path."

        return True, "Item decompressed successfully!"
    except Exception as e:
        return False, str(e)

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        return True, "File renamed successfully!"
    except Exception as e:
        return False, str(e)

def rename_directory(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        return True, "Directory renamed successfully!"
    except Exception as e:
        return False, str(e)


def encrypt_file(filename, key):
    try:
        with open(filename, 'rb') as file:
            data = file.read()

        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)

        with open(filename, 'wb') as file:
            file.write(encrypted_data)

        return True, "File encrypted successfully!"
    except Exception as e:
        return False, str(e)
    


def decrypt_file(filename, key):
    try:
        with open(filename, 'rb') as file:
            encrypted_data = file.read()

        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(filename, 'wb') as file:
            file.write(decrypted_data)

        return True, "File decrypted successfully!"
    except Exception as e:
        return False, str(e)
    
def copy_file(source_file, destination_file):
    try:
        shutil.copyfile(source_file, destination_file)
        return True, "File copied successfully!"
    except Exception as e:
        return False, str(e)
    

def move_file(source_file, destination_dir):
    try:
        # Move the file to the specified destination directory
        shutil.move(source_file, os.path.join(destination_dir, os.path.basename(source_file)))
        return True, "File moved successfully!"
    except Exception as e:
        return False, str(e)
    
def change_permissions_octal(filename, permissions):
    try:
        # Convert the octal representation to an integer using the base 8
        mode = int(permissions, 8)
        os.chmod(filename, mode)
        return True, "Permissions changed successfully!"
    except Exception as e:
        return False, str(e)


def main_menu():
    print("\nSelect an option:")
    print("1. Files")
    print("2. Directories")
    print("3. Recycle Bin")
    print("4. Exit")
    return input("Enter the option number: ")

def file_options(filename):
    print("\nFile Options:")
    print("1. Create a file")
    print("2. Read a file")
    print("3. Update a file")
    print("4. Delete a file")
    print("5. Compress a file")
    print("6. Decompress a file")
    print("7. Rename a file")
    print("8. Encrypt file ")
    print("9. Decrypt file")
    print("10. Copy file")
    print("11. move file")
    print("12. change permissions linux")
    print("13. Back to Main Menu")
    choice = input("Enter the file operation number: ")
    
    if choice == '1':
        filename = input("Enter the filename: ")
        content = input("Enter the content to write to the file: ")
        success, message = create_file(filename, content)
    elif choice == '2':
        filename = input("Enter the filename: ")
        success, message = read_file(filename)
        if success:
            print(f"Content of {filename}: {message}")
    elif choice == '3':
        filename = input("Enter the filename: ")
        content = input("Enter the new content: ")
        success, message = update_file(filename, content)
    elif choice == '4':
        filename = input("Enter the filename: ")
        success, message = delete_file(filename)
    elif choice == '5':
         # Compress a file or folder
        item_path = input("Enter the file or folder path to compress: ")
        success, message = compress_item(item_path)

    elif choice == '6':
         # Decompress a file or folder
        item_path = input("Enter the zip file path to decompress: ")
        success, message = decompress_item(item_path)

    elif choice == '7':
        # Rename a file
        # Ask for old and new directory names
        old_name = input("Enter the old file name: ")
        new_name = input("Enter the new file name: ")
        success, message = rename_file(old_name, new_name)
        print(message)
        # Call file_options() recursively with file_name
        file_options(filename)
    elif choice == '8':
        # Encrypt a file
        filename = input("Enter the filename to encrypt: ")
        key = input("Enter the encryption key: ")
        success, message = encrypt_file(filename, key)
        print(message)
        file_options(filename)
    elif choice == '9':
      # Decrypt a file
        filename = input("Enter the filename to decrypt: ")
        key = input("Enter the decryption key: ")
        success, message = decrypt_file(filename, key)
        print(message)
        file_options(filename)
    elif choice == '10':
         # Copy a file
        source_file = input("Enter the source file path: ")
        destination_file = input("Enter the destination file path: ")
        success, message = copy_file(source_file, destination_file)
    elif choice == '11':
         # Move a file to a different directory
         source_file = input("Enter the path of the file to move: ")
         destination_dir = input("Enter the destination directory path: ")
         success, message = move_file(source_file, destination_dir)
         print(message)
    elif choice == '12':
          filename = input("enter the filename")
          permissions = input("enter pem like user1:(F)")  # Replace this with the desired permission string
          print(message)
          success, message = change_permissions_octal(filename, permissions)
    elif choice == '13':
      return#back to main menu
    else:
         print("Invalid choice. Please try again.")

   

    #print(message)
    file_options(filename)

def directory_options(directory_name):
    print("\nDirectory Options:")
    print("1. Create a directory")
    print("2. List items in a directory")
    print("3. Delete a directory")
    print("4. Compress a directory")
    print("5. Decompress a directory")
    print("6. Rename a directory")
    
    print("7. Back to Main Menu")
    choice = input("Enter the directory operation number: ")

    if choice == '1':
        directory_name = input("Enter the directory name: ")
        success, message = create_directory(directory_name)
    elif choice == '2':
        directory_name = input("Enter the directory name: ")
        success, items = list_directory(directory_name)
        if success:
            print(f"Items in {directory_name}:")
            for item in items:
                print(item)
    elif choice == '3':
        directory_name = input("Enter the directory name: ")
        success, message = delete_directory(directory_name)
    elif choice == '4':
           # Compress a file or folder
        item_path = input("Enter the folder path with name to compress: ")
        success, message = compress_item(item_path)

    elif choice == '5':
        # Decompress a folder
        item_path = input("Enter the zip file path with name to decompress: ")
        success, message = decompress_item(item_path)

    elif choice == '6':
        # Rename a directory
        # Ask for old and new directory names
        old_name = input("Enter the old directory name: ")
        new_name = input("Enter the new directory name: ")
        success, message = rename_directory(old_name, new_name)
        print(message)
        # Call directory_options() recursively with directory_name
        directory_options(directory_name)
    elif choice == '7':
        return
    else:
        print("Invalid option")
        
        
      
    directory_options(directory_name)

def main():
    print("Welcome to the Simple File System!")
    check_password()


    while True:
        choice = main_menu()

        if choice == '1':
            file_options(filename)
        elif choice == '2':
            directory_options(directory_name)
        elif choice == '3':
             # Recycle Bin
             print("\nRecycle Bin Options:")
             print("1. Restore an item from the recycle bin")
             print("2. Empty the recycle bin")
             print("3. Back to Main Menu")
             bin_choice = input("Enter the recycle bin operation number: ")
  
             if bin_choice == '1':
                 item_name = input("Enter the name of the item to restore: ")
                 success, message = restore_item(item_name)
                 print(message)
             elif bin_choice == '2':
                 # Empty the recycle bin
                 shutil.rmtree(RECYCLE_BIN_DIR)
                 create_recycle_bin()
                 print("Recycle bin emptied successfully!")
             elif bin_choice == '3':
                 continue
             else:
                 print("Invalid choice.")
        elif choice == '4':
            print("Exiting the File System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


       

if __name__ == "__main__":
    main()



