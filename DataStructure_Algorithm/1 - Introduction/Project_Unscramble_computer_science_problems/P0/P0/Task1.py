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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

unique_numbers = set()

def different_numbers(calls, unique_numbers):
    for call in calls:
        if call[0] not in unique_numbers:
            unique_numbers.add(call[0])
        if call[1] not in unique_numbers:
            unique_numbers.add(call[1])

different_numbers(texts, unique_numbers)
different_numbers(calls,unique_numbers)

print(f'There are {len(unique_numbers)} different telephone numbers in the records.')

'''
Inside the first loop, it will loop in another array twice. Making it 2n².
O(n²) at worst case
'''