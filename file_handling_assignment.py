# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is line 1.\n")
        file.write("This is line 2 with a number: 123.\n")
        file.write("Line 3: Python is fun!\n")
    print("File created and initial lines written successfully.")
except Exception as e:
    print(f"An error occurred during file creation: {e}")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
    print("File content after initial write:")
    print(content)
except FileNotFoundError:
    print("File not found. Please ensure the file exists.")
except PermissionError:
    print("Permission denied. Please check your file permissions.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending line 4.\n")
        file.write("Appending line 5 with a number: 456.\n")
        file.write("Appending line 6: Keep learning!\n")
    print("Additional lines appended successfully.")
except Exception as e:
    print(f"An error occurred during file appending: {e}")

# File Reading and Display after Appending
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
    print("File content after appending:")
    print(content)
except FileNotFoundError:
    print("File not found. Please ensure the file exists.")
except PermissionError:
    print("Permission denied. Please check your file permissions.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
finally:
    print("File handling operations completed.")
