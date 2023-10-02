number = int(input())
positive = []
negative = []

for num in range(number):
    current_number = int(input())
    if current_number >= 0:
        positive.append(current_number)
    else:
        negative.append(current_number)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")