import csv
"""
Intro to Python Lab 1, Task 4

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Lab Preparation page.
"""

"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    callers = [r[0] for r in calls]
    numbers_received_call = [r[1] for r in calls]

    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)

        numbers_sent_msg = set([r[0] for r in texts])
        numbers_received_msg = set([r[1] for r in texts])

        result = set(callers) - numbers_received_msg - \
            numbers_sent_msg - set(numbers_received_call)

        print("These numbers could be telemarketers: ")
        [print(r) for r in sorted(list(result))]
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers: 
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message: 
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
