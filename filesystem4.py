# import os

# def create_file(filename, content):
#     try:
#         with open(filename, 'w') as file:
#             file.write(content)
#         return True, "File created successfully!"
#     except Exception as e:
#         return False, str(e)

# def read_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#         return True, content
#     except Exception as e:
#         return False, str(e)

# def update_file(filename, content):
#     try:
#         with open(filename, 'w') as file:
#             file.write(content)
#         return True, "File updated successfully!"
#     except Exception as e:
#         return False, str(e)

# def delete_file(filename):
#     try:
#         os.remove(filename)
#         return True, "File deleted successfully!"
#     except Exception as e:
#         return False, str(e)

# def create_directory(directory_name):
#     try:
#         os.mkdir(directory_name)
#         return True, "Directory created successfully!"
#     except Exception as e:
#         return False, str(e)

# def list_directory(directory_name):
#     try:
#         items = os.listdir(directory_name)
#         return True, items
#     except Exception as e:
#         return False, str(e)

# def delete_directory(directory_name):
#     try:
#         os.rmdir(directory_name)
#         return True, "Directory deleted successfully!"
#     except Exception as e:
#         return False, str(e)

# def main_menu():
#     print("\nSelect an option:")
#     print("1. Files")
#     print("2. Directories")
#     print("3. Exit")
#     return input("Enter the option number: ")

# def file_options(filename):
#     print("\nFile Options:")
#     print("1. Create a file")
#     print("2. Read a file")
#     print("3. Update a file")
#     print("4. Delete a file")
#     print("5. Back to Main Menu")
#     choice = input("Enter the file operation number: ")
    
#     if choice == '1':
#         content = input("Enter the content to write to the file: ")
#         success, message = create_file(filename, content)
#     elif choice == '2':
#         success, message = read_file(filename)
#         if success:
#             print(f"Content of {filename}: {message}")
#     elif choice == '3':
#         content = input("Enter the new content: ")
#         success, message = update_file(filename, content)
#     elif choice == '4':
#         success, message = delete_file(filename)
#     elif choice == '5':
#         return

#     print(message)
#     file_options(filename)

# def directory_options(directory_name):
#     print("\nDirectory Options:")
#     print("1. Create a directory")
#     print("2. List items in a directory")
#     print("3. Delete a directory")
#     print("4. Back to Main Menu")
#     choice = input("Enter the directory operation number: ")

#     if choice == '1':
#         success, message = create_directory(directory_name)
#     elif choice == '2':
#         success, items = list_directory(directory_name)
#         if success:
#             print(f"Items in {directory_name}:")
#             for item in items:
#                 print(item)
#     elif choice == '3':
#         success, message = delete_directory(directory_name)
#     elif choice == '4':
#         return

#     print(message)
#     directory_options(directory_name)

# def main():
#     print("Welcome to the Simple File System!")

#     while True:
#         choice = main_menu()

#         if choice == '1':
#             filename = input("Enter the filename: ")
#             file_options(filename)
#         elif choice == '2':
#             directory_name = input("Enter the directory name: ")
#             directory_options(directory_name)
#         elif choice == '3':
#             print("Exiting the File System. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

import os
import zipfile
import shutil
from cryptography.fernet import Fernet

filename = None
directory_name=None

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

def delete_file(filename):
    try:
        os.remove(filename)
        return True, "File deleted successfully!"
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

def delete_directory(directory_name):
    try:
        os.rmdir(directory_name)
        return True, "Directory deleted successfully!"
    except Exception as e:
        return False, str(e)
   

def compress_file(filename):
    try:
        with zipfile.ZipFile(f"{filename}.zip", 'w') as zip_file:
            zip_file.write(filename, os.path.basename(filename))
        return True, "File compressed successfully!"
    except Exception as e:
        return False, str(e)

def decompress_file(filename):
    try:
        with zipfile.ZipFile(filename, 'r') as zip_file:
            zip_file.extractall(os.path.dirname(filename))
        return True, "File decompressed successfully!"
    except Exception as e:
        return False, str(e)
    

def compress_folder(foldername):
    try:
        shutil.make_archive(foldername, 'zip', foldername)
        return True, "Folder compressed successfully!"
    except Exception as e:
        return False, str(e)
    
def decompress_folder(zip_filename):
    try:
        folder_path = os.path.splitext(zip_filename)[0]
        with zipfile.ZipFile(zip_filename, 'r') as zip_file:
            zip_file.extractall(folder_path)
        return True, "Folder decompressed successfully!"
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
    


def main_menu():
    print("\nSelect an option:")
    print("1. Files")
    print("2. Directories")
    print("3. Exit")
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
    print("10. Back to Main Menu")
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
        filename = input("Enter the filename to compress: ")
        success, message = compress_file(filename)
    elif choice == '6':
        filename = input("Enter the filename to decompress: ")
        success, message = decompress_file(filename)
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
        key = Fernet.generate_key()
        success, message = encrypt_file(filename, key)
    elif choice == '9':
    # Decrypt a file
      key = input("Enter the encryption key: ")
      success, message = decrypt_file(filename, key)


    print(message)
    file_options()

def directory_options(directory_name=None):
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
        # Compress a folder
        foldername = input("Enter the folder name to compress: ")
        success, message = compress_folder(foldername)
    elif choice == '5':
        # Decompress a folder
        zip_filename = input("Enter the zip filename to decompress: ")
        success, message = decompress_folder(zip_filename)#attention required
    elif choice == '6':
        # Rename a directory
        # Ask for old and new directory names
        old_name = input("Enter the old directory name: ")
        new_name = input("Enter the new directory name: ")
        success, message = rename_directory(old_name, new_name)
        print(message)
        # Call directory_options() recursively with directory_name
        directory_options(directory_name)
      

    print(message)
    directory_options()

def main():
    print("Welcome to the Simple File System!")

    while True:
        choice = main_menu()

        if choice == '1':
            file_options(  )
        elif choice == '2':
            directory_options()
        elif choice == '3':
            print("Exiting the File System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()