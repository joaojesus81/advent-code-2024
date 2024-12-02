total_distance = 0
left_column = []
right_column = []

# read from input
with open('./day1/input', 'r') as file:
    for line in file:
        line_members = line.rstrip().split("   ")
        for idx, value in enumerate(line_members):
            int_value = int(value)
            left_column.append(int_value) if idx == 0 else right_column.append(int_value)

# sort files
left_column.sort()
right_column.sort()

# find the distance between the numbers and add to the total distance
for left, right in zip(left_column, right_column):
    total_distance += abs(left - right)

# total distance
print(total_distance)
