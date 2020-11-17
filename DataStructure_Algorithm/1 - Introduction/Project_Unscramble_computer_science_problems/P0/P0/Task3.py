"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

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

def get_prefixes(calls):
    bangalore_calls = {}
    for call in calls:
        if call[0][0:5] == '(080)':
            called_number = call[1]

            if called_number[0:2] == '(0':
                area_code = called_number[called_number.find("(")+1 : called_number.find(")")]
                if area_code not in bangalore_calls:
                    bangalore_calls[area_code] = 0
                bangalore_calls[area_code] += 1

            elif called_number[0] in ['7','8','9']:
                cellphone_prefix = called_number[:4]
                if cellphone_prefix not in bangalore_calls:
                    bangalore_calls[cellphone_prefix] = 0
                bangalore_calls[cellphone_prefix] += 1

            #last time I treated this as else, however my reviewer said I was wrong. The result is the same, but i am adressing the 140 number directly
            elif called_number[0:3] == '140':
                telemarketing = called_number[0:3]
                if telemarketing not in bangalore_calls:
                    bangalore_calls[telemarketing] = 0
                bangalore_calls[telemarketing] += 1
    return bangalore_calls


def answer_A(bangalore_calls):
    print('The numbers called by people in Bangalore have codes')
    for key,value in sorted(bangalore_calls.items()):
        print(key)

def answer_B(bangalore_calls):
    total = 0
    bangalore = 0

    for key, value in bangalore_calls.items():
        total += value

        if key == '080':
            bangalore += value

    return f"{((bangalore/total)*100):.2f}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."


bangalore_calls = get_prefixes(calls)

answer_A(bangalore_calls)
print(answer_B(bangalore_calls))

'''The function of get_prefixes loops all the calls, inside each iteration will loop inside all of the bangalore_call 
dictionary at worst. So it would be O(n*n) at worst

Both functions answer_A and answer_B will loop throught the dictionary bangalore_call once, making both O(n) at worst

The function would be then n*n + 2n = O(n²) at worst

'''