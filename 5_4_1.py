
"""
our_list = ["First item", "Second item", "Third item"]

for i in our_list:
    print(i, end=' | ')
print()
"""

our_list = ["First item", "Second item", "Third item"]
list_length = len(our_list)
i = 0

while i != list_length:
    print(our_list[i], end=' | ')
    i += 1
print()