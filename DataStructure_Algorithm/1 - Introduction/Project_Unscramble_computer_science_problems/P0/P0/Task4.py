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
possible_telemarketers = set()
not_telemarketers = set()

for text in texts:
    not_telemarketers.add(text[0])
    not_telemarketers.add(text[1])

for call in calls:
    not_telemarketers.add(call[1])

for call in calls:
    if call[0] not in not_telemarketers:
        possible_telemarketers.add(call[0])

print("These numbers could be telemarketers: ")
for possible_telemarketer in sorted(possible_telemarketers):
    print(possible_telemarketer)

'''We have 4 unested loops, meaning that the program will iteration each loop, n times at worst.
    so 4n = O(n)
'''

