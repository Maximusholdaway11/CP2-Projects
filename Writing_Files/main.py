#Max Holdaway writing to text files
"""
r = read
w = write (error if file does not exist / wont create a file)
w+ = read and write (error if file does not exist / wont create a file)
a = append (add but not overwrite) (will create file if one does not exists)
a+ = read and append
x = create a file

"""

with open("Writing_Files/file_to_write", "a") as file:
    file.write("This is now also on my file")

with open("Writing_Files/file_to_write", "r") as file:
    print(file.read())