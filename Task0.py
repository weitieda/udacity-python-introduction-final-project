import csv
from datetime import datetime
"""
Intro to Python Project 1, Task 0

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
    print(
        f"First record of texts, {texts[0][0]} texts {texts[0][1]} at time {texts[0][2]}")

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    print(
        f"Last record of calls, {calls[-1][0]} calls {calls[-1][1]} at time {calls[-1][2]}")


"""
TASK 0: 
what is the first record of texts and what is the last record of calls
Print messages: 
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
