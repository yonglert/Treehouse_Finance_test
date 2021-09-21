import os
import re
# Place this python file into the git repo folder
# Get the current work directory path
app_folder = os.getcwd()

### Q5a. Find number of python files ###
'''
    Traverse through the folder to find files ending with '.py'.
    We will not consider .ipynb files in this case. However,
    if you would like to include counting '.ipynb' files, simply
    add "file.endswith('.ipynb').
'''
### Q5b. Find number of comments and code in all python files ###
'''
    Each file that we traverse that matches ".py", we will iterate through each line
    Some important things to consider:
        1. Indented Code vd Indented block comments
        2. Empty line ("     ") vs New line (\n)
        3. re.readlines will ignore last line if it is not followed by a newline. Hence we do not use re.readlines
        4. We will consider inline comments after the line of code as a line of code.
            i.e for i in range(10): # iterates 10 times, i takes value [0,9]
        
    Assumption:
        1. We do not count empty/new lines in block comments
        2. We do not count inline comments that are written after the line of code
            i.e print('hello world') #this prints the string "hello world" will be considered as a line of code
'''
totalFiles = 0
linesOfComments = 0
linesOfCode = 0
blockComment = False

for base, dirs, files in os.walk(app_folder):
    for file in files:
        if file.endswith(".py"):
            totalFiles += 1
            with open(file, 'r') as f:
                newlines = [line.rstrip('\n') for line in f]
                for line in newlines:
                    # Block Comments
                    if line.startswith("'''"):
                        if blockComment: # end of block comment
                            # print(f"block comment end: {line}")
                            blockComment = False
                            linesOfComments += 1
                        else: # start of block comment
                            # print(f"block comment start: {line}")
                            blockComment = True
                            linesOfComments += 1

                    #Check whether is indented block comment, indented code or just empty line with spaces
                    elif line.startswith(" "): 
                        if bool(re.search('[a-z0-9]', line)): # find character/integer in line
                            if blockComment: # part of block comment
                                # print(f"block comment: {line}")
                                linesOfComments += 1
                            else: # indented code
                                # print(f"indented code: {line}")
                                linesOfCode += 1
                        else: # just spaces in the line => empty line
                            pass

                    # Inline comments
                    elif line.startswith("#"):
                        # print(f"inline comment: {line}")
                        linesOfComments += 1

                    # unindented code / part of block comment 
                    elif bool(re.match('[a-z]+', line)): 
                        if blockComment:
                            # print(f"block comment: {line}")
                            linesOfComments += 1
                        else:
                            # print(f"code: {line}")
                            linesOfCode += 1
                            
                    # Empty lines    
                    elif line == "":
                        # print(f"empty line: {line}")
                        pass
                            
print(f"Total number of python files: {totalFiles}")
print(f"Number of lines of code: {linesOfCode}")
print(f"Number of lines of comments: {linesOfComments}")

