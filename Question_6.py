'''
In a text file, give me total number of appearance of “date” within the text file The date
format can appears in either one (or multiple) formats shown below:
    a. YYYY/MM/DD
    b. MM/DD/YYYY
    c. DD/MM/YYYY
    d. DD (Jan/Feb/Mar/Apr/May/Jun/Jul/Aug/Sept/Oct/Nov/Dec) YYYY
'''
'''
    Method 1: using datefinder
    Input txtfile into function findDates
    datefinder will be able to find all occurrences of dates with different
    date formats in a text.

    Problem: 
        Misread fractions as dates i.e 1/4, 3/4, 5/8 as 1st april 2021, 3rd april 2021, 5th august 2021
        Other characters that are very similar to date formats like 1st, 2nd, 3rd etc.
    Solution: 
        Pre-process textfile to remove all fractions
'''

# pip install datefinder
import datefinder
import re 

def findDates(txtfile_path):
    # Read txtfile and call readlines to get a list of strings
    with open(txtfile_path) as f:
        lines = f.readlines()

    processed = ''
    result = 0
    # Iterate through each line, tokenize to remove fractions and ordinal numbers (1st, 2nd, 3rd...)
    # append into processed as one long string
    for line in lines:
        for split in line.split(" "):
            split = re.sub(r'^[0-9]+/0*[1-9][0-9]*$',"FRACTION", split)
            split = re.sub(r'^\d+(?=st|nd|rd|th)',"ORDINAL", split)
            processed = " ".join([processed, split])

    # call datefinder on the processed string to get the number of dates
    dates = datefinder.find_dates(processed)
    # datefinder.find_dates returns a generator, iterate through and count to get occurences
    for d in dates:
        result += 1

    return result

print(f"There is a total of {findDates('Question_6.txt')} occurences of all date formats")
