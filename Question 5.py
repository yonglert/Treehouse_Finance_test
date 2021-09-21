import os

# Place this python file into the git repo folder
# Get the current work directory path
app_folder = os.getcwd()

### Q5a. Find number of python files ###
'''
    Traverse through the folder to find files ending with '.py'.
    We will not consider .ipynb files in this case. However,
    if you would like to include counting '.ipynb' files, simply
    add "file.endswith('.ipynb')".
'''
totalFiles = 0
for base, dirs, files in os.walk(app_folder):
    for file in files:
        if file.endswith(".py"):
            totalFiles += 1

print(f"Total number of python files: {totalFiles}")

