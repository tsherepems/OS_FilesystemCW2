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

import os

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


def main_menu():
    print("\nSelect an option:")
    print("1. Files")
    print("2. Directories")
    print("3. Exit")
    return input("Enter the option number: ")

def file_options():
    print("\nFile Options:")
    print("1. Create a file")
    print("2. Read a file")
    print("3. Update a file")
    print("4. Delete a file")
    print("5. Back to Main Menu")
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
        return

    print(message)
    file_options()

def directory_options():
    print("\nDirectory Options:")
    print("1. Create a directory")
    print("2. List items in a directory")
    print("3. Delete a directory")
    print("4. Back to Main Menu")
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
        return

    print(message)
    directory_options()

def main():
    print("Welcome to the Simple File System!")

    while True:
        choice = main_menu()

        if choice == '1':
            file_options()
        elif choice == '2':
            directory_options()
        elif choice == '3':
            print("Exiting the File System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()