# Create a program that reads a file and writes a modified version to a new file. Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read. Outcomes
# - File handling
try:
    filename = input("Please enter the name of the file you want to read: ")
    with open(filename, 'r') as file:
        data = file.read()

    data = data.replace("old text", "new text")
        
    new_filename = input("Please enter the name of the file you want to write to: ")

    with open(new_filename, 'w') as file:
        file.write(data)

    print("File has been written successfully")

except FileNotFoundError:
    print("The file you entered does not exist")

except PermissionError:
    print("You do not have permission to read the file")

except Exception as e:
    print("An error occurred: ", e)

finally:
    print("Program has ended")
    
