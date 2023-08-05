import os
import zipfile
import shutil
from cryptography.fernet import Fernet
import hashlib
import sys

def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-based systems (Linux, macOS)
        os.system('clear')

class PasswordManager:
    def __init__(self):
        self.CONFIG_FILE = os.path.join(os.getcwd(), "config.txt")

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def ask_password(self):
        password = input("Please enter the password: ")
        return self.hash_password(password)

    def check_password(self):
        try:
            with open(self.CONFIG_FILE, "r") as file:
                stored_hashed_password = file.read().strip()
        except FileNotFoundError:
            stored_hashed_password = None

        if not stored_hashed_password:
            # If the config.txt file doesn't exist or is empty, prompt the user to set a new password
            entered_password = self.ask_password()
            with open(self.CONFIG_FILE, "w") as file:
                file.write(entered_password)

            print("Password set successfully.")
        else:
            # Password is already set, prompt the user to enter the password and check it
            entered_password = self.ask_password()
            if entered_password != stored_hashed_password:
                # Show an error message and exit the program
                print("Invalid password.")
                sys.exit()

class FileSystem:
    def __init__(self):
        self.password_manager = PasswordManager()
        self.filename = None
        self.directory_name = None
        self.CONFIG_FILE = os.path.join(os.getcwd(), "config.txt")
        self.RECYCLE_BIN_DIR = "recycle_bin"

    def create_file(self, filename, content):
        try:
            with open(filename, 'w') as file:
                file.write(content)
            return True, "File created successfully!"
        except Exception as e:
            return False, str(e)

    def read_file(self, filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
            return True, content
        except Exception as e:
            return False, str(e)

    def update_file(self, filename, content):
        try:
            with open(filename, 'w') as file:
                file.write(content)
            return True, "File updated successfully!"
        except Exception as e:
            return False, str(e)
        
    def rename_file(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            return True, "File renamed successfully!"
        except Exception as e:
            return False, str(e)   

   
    def encrypt_file(self, filename, key):
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

    def decrypt_file(self, filename, key):
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

    def copy_file(self, source_file, destination_file):
        try:
            shutil.copyfile(source_file, destination_file)
            return True, "File copied successfully!"
        except Exception as e:
            return False, str(e)

    def move_file(self, source_file, destination_dir):
        try:
            # Move the file to the specified destination directory
            shutil.move(source_file, os.path.join(destination_dir, os.path.basename(source_file)))
            return True, "File moved successfully!"
        except Exception as e:
            return False, str(e)  
    
    def create_recycle_bin(self):
        try:
            os.mkdir(self.RECYCLE_BIN_DIR)
        except FileExistsError:
            pass

    def delete_file(self, filename):
        try:
            self.create_recycle_bin()
            # Move the file to the recycle bin directory
            shutil.move(filename, os.path.join(self.RECYCLE_BIN_DIR, os.path.basename(filename)))
            return True, "File moved to recycle bin successfully!"
        except Exception as e:
            return False, str(e)

    def delete_directory(self, directory_name):
        try:
            self.create_recycle_bin()
            # Move the directory to the recycle bin directory
            shutil.move(directory_name, os.path.join(self.RECYCLE_BIN_DIR, os.path.basename(directory_name)))
            return True, "Directory moved to recycle bin successfully!"
        except Exception as e:
            return False, str(e)
        
    def restore_item(self, item_name):
        try:
            # Get the original name of the item from the recycle bin
            original_name = os.path.basename(item_name)
            original_path = os.path.join(os.getcwd(), original_name)

            # Restore the item from the recycle bin to its original location
            if os.path.exists(item_name):
                shutil.move(item_name, original_path)
                return True, "Item restored successfully!"
            else:
                return False, "Item not found in recycle bin."
        except Exception as e:
            return False, str(e)

    def create_directory(self, directory_name):
        try:
            os.mkdir(directory_name)
            return True, "Directory created successfully!"
        except Exception as e:
            return False, str(e)

    def list_directory(self, directory_name):
        try:
            items = os.listdir(directory_name)
            return True, items
        except Exception as e:
            return False, str(e)

    def compress_item(self, item_path):
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

    def decompress_item(self, item_path):
        try:
            if item_path.endswith('.zip'):
                with zipfile.ZipFile(item_path, 'r') as zip_file:
                    zip_file.extractall(os.path.dirname(item_path))
            else:
                return False, "Invalid item path. Please enter a valid zip file path."

            return True, "Item decompressed successfully!"
        except Exception as e:
            return False, str(e)

    def rename_directory(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            return True, "Directory renamed successfully!"
        except Exception as e:
            return False, str(e)

    def change_permissions_octal(self, filename, permissions):
        try:
            # Convert the octal representation to an integer using the base 8
            mode = int(permissions, 8)
            os.chmod(filename, mode)
            return True, "Permissions changed successfully!"
        except Exception as e:
            return False, str(e)

def main_menu():
    print("\nSelect an option:")
    print("1. File options")
    print("2. Directory options")
    print("3. Recycle Bin options")
    print("4. Exit")

def file_options_menu():
    clear_screen()
    print("\nSelect a file option:")
    print("1. Create a new file")
    print("2. Read a file")
    print("3. Update a file")
    print("4. Delete a file")
    print("5. Rename a file")
    print("6. Copy a file")
    print("7. Move a file")
    print("8. Encrypt a file")
    print("9. Decrypt a file")
    print("10. Compress a file")
    print("11. Decompress a file")
    print("12. Change permissions (Octal)")
    print("13. Return to main menu")

def directory_options_menu():
    clear_screen()
    print("\nSelect a directory option:")
    print("1. Create a new directory")
    print("2. Delete a directory")
    print("3. Rename a directory")
    print("4. Compress a directory")
    print("5. Decompress a directory")
    print("6. List directory")
    print("7. Return to main menu")

def recycle_bin_menu():
    clear_screen()
    print("\nSelect an option for Recycle Bin:")
    print("1. List items in Recycle Bin")
    print("2. Restore an item from Recycle Bin")
    print("3. Empty Recycle Bin")
    print("4. Return to main menu")



def get_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return None

def main():
    print("Welcome to the Simple File System!")
    password_manager = PasswordManager()
    password_manager.check_password()

    file_system = FileSystem()

    while True:
        main_menu()
        option = get_input("Enter the option number: ")

        if option == 1:
            while True:
                file_options_menu()
                file_option = get_input("Enter the file option number: ")

                if file_option == 1:
                    filename = input("Enter the filename: ")
                    content = input("Enter the content: ")
                    success, message = file_system.create_file(filename, content)
                    print(message)

                elif file_option == 2:
                    filename = input("Enter the filename to read: ")
                    success, content = file_system.read_file(filename)
                    if success:
                        print("File content:")
                        print(content)
                    else:
                        print(content)

                elif file_option == 3:
                    filename = input("Enter the filename to update: ")
                    content = input("Enter the new content: ")
                    success, message = file_system.update_file(filename, content)
                    print(message)

                elif file_option == 4:
                    filename = input("Enter the filename to delete: ")
                    success, message = file_system.delete_file(filename)
                    print(message)

                elif file_option == 5:
                    old_name = input("Enter the current filename: ")
                    new_name = input("Enter the new filename: ")
                    success, message = file_system.rename_file(old_name, new_name)
                    print(message)

                elif file_option == 6:
                    source_file = input("Enter the source file path: ")
                    destination_file = input("Enter the destination file path: ")
                    success, message = file_system.copy_file(source_file, destination_file)
                    print(message)

                elif file_option == 7:
                    source_file = input("Enter the source file path: ")
                    destination_dir = input("Enter the destination directory path: ")
                    success, message = file_system.move_file(source_file, destination_dir)
                    print(message)

                elif file_option == 8:
                    filename = input("Enter the filename to encrypt: ")
                    key = input("Enter the encryption key: ")
                    success, message = file_system.encrypt_file(filename, key)
                    print(message)

                elif file_option == 9:
                    filename = input("Enter the filename to decrypt: ")
                    key = input("Enter the decryption key: ")
                    success, message = file_system.decrypt_file(filename, key)
                    print(message)

                elif file_option == 10:
                    item_path = input("Enter the file/folder path to compress: ")
                    success, message = file_system.compress_item(item_path)
                    print(message)

                elif file_option == 11:
                    item_path = input("Enter the zip file path to decompress: ")
                    success, message = file_system.decompress_item(item_path)
                    print(message)

                elif file_option == 12:
                    filename = input("Enter the filename to change permissions: ")
                    permissions = input("Enter the new permissions in octal format (e.g., 755): ")
                    success, message = file_system.change_permissions_octal(filename, permissions)
                    print(message)

                elif file_option == 13:
                    break

                else:
                    print("Invalid option. Please try again.")

        elif option == 2:
            while True:
                directory_options_menu()
                directory_option = get_input("Enter the directory option number: ")

                if directory_option == 1:
                    directory_name = input("Enter the directory name: ")
                    success, message = file_system.create_directory(directory_name)
                    print(message)

                elif directory_option == 2:
                    directory_name = input("Enter the directory name to delete: ")
                    success, message = file_system.delete_directory(directory_name)
                    print(message)
                
                elif directory_option == 3:
                    old_name = input("Enter the current directory name: ")
                    new_name = input("Enter the new directory name: ")
                    success, message = file_system.rename_directory(old_name, new_name)
                    print(message)

                
                elif directory_option == 4:
                    directory_path = input("Enter the directory path to compress: ")
                    success, message = file_system.compress_item(directory_path)
                    print(message)

                elif directory_option == 5:
                    zip_file_path = input("Enter the zip file path to decompress: ")
                    success, message = file_system.decompress_item(zip_file_path)
                    print(message)

                elif directory_option == 6:
                    directory_name = input("Enter the directory name to list items: ")
                    success, items = file_system.list_directory(directory_name)
                    if success:
                        print("Items in the directory:")
                        for item in items:
                            print(item)
                    else:
                        print(items)

                elif directory_option == 7:
                    break

                else:
                    print("Invalid option. Please try again.")

        elif option == 3:
            while True:
                recycle_bin_menu()
                recycle_bin_option = get_input("Enter the Recycle Bin option number: ")

                if recycle_bin_option == 1:
                    # List items in Recycle Bin
                    success, items = file_system.list_directory(file_system.RECYCLE_BIN_DIR)
                    if success:
                        print("Items in Recycle Bin:")
                        for item in items:
                            print(item)
                    else:
                        print(items)

                elif recycle_bin_option == 2:
                    # Restore an item from Recycle Bin
                    item_name = input("Enter the item name to restore from Recycle Bin: ")
                    success, message = file_system.restore_item(os.path.join(file_system.RECYCLE_BIN_DIR, item_name))
                    print(message)

                elif recycle_bin_option == 3:
                    # Empty Recycle Bin
                    success, message = file_system.delete_directory(file_system.RECYCLE_BIN_DIR)
                    print(message)

                elif recycle_bin_option == 4 :
                    #go to main menu
                    break

        elif option == 4:
            print("Goodbye!")
            sys.exit()

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
