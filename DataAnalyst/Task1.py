import csv
"""
Intro to Python Project 1, Task 1

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Project Preparation page.
"""


"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    text_numbers = sum([[r[0], r[1]] for r in texts], [])

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
        call_numbers = sum([[r[0], r[1]] for r in calls], [])
        print(
            f"There are {len(set(call_numbers + text_numbers))} different telephone numbers in the records.")


"""
TASK 1: 
How many different telephone numbers are there in the records? 
Print a message: 
"There are <count> different telephone numbers in the records."
"""
