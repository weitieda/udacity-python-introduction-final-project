import csv
"""
Intro to Python Lab 1, Task 3

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Lab Preparation page.
"""

"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    called_by_bangalore_numbers = [n[1]
                                   for n in calls if str(n[0]).startswith('(080)')]

    home_phone_numbers = [
        n for n in called_by_bangalore_numbers if n.startswith('(0')]
    unique_home_phone_area_code = set([
        n.split(')')[0][1:] for n in home_phone_numbers])

    unique_mobile_area_code = set([r[:4] for r in called_by_bangalore_numbers if " " in r
                                   and str(r).startswith('7') or str(r).startswith('8') or str(r).startswith('9')])

    unique_telsales_code = set([r for r in called_by_bangalore_numbers if " " not in r
                                and "(" not in r and ")" not in r and str(r).startswith('140')])
    result = set(list(unique_home_phone_area_code) +
                 list(unique_mobile_area_code) + list(unique_telsales_code))
    result_sorted = sorted(list(result))

    print("The numbers called by people in Bangalore have codes:")
    [print(r) for r in result_sorted]

    from_bangalore_to_bangalore = [n for n in calls if str(
        n[0]).startswith('(080)') and str(n[1]).startswith('(080)')]
    ratio = float(len(calls)) / float(len(from_bangalore_to_bangalore))

    print(f"{ratio: .2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore. 
Fixed line numbers include parentheses, so Bangalore numbers 
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. 
 - Fixed lines start with an area code enclosed in brackets. The area 
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
