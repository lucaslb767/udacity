"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

longest_calls = {}

for call in calls:
    if call[0] not in longest_calls:
        longest_calls[call[0]] = 0
    if call[1] not in longest_calls:
        longest_calls[call[1]] = 0
    longest_calls[call[0]] += int(call[3])
    longest_calls[call[1]] += int(call[3])

def get_longest_call(longest_calls):
    longest_number = ''
    longest_call = 0
    for key,value in longest_calls.items():
        if value > longest_call:
            longest_call = value
            longest_number = key

    return f'{longest_number} spent the longest time, {longest_call} seconds, on the phone during September 2016.'
print(get_longest_call(longest_calls))

'''
The program starts looping throught calls, and for each loop, checks if the call[0] and call[1] are inside 
the dictionary longest_calls. That would make 2n² at worst.

Then it will loops again inside the longest_calls dictionary, making it O(n).

The program would have 2n² + n = O(n²) at worst case
'''