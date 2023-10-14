def find_most_frequent_string(array):
    if len(array) == 0:
        return None

    counts = {}
    max_count = 0
    most_frequent_string = None

    for string in array:
        if string not in counts:
            counts[string] = 1
        else:
            counts[string] += 1

        if counts[string] > max_count:
            max_count = counts[string]
            most_frequent_string = string

    return most_frequent_string


strings = ["12", "34", "56", "78"]
result = find_most_frequent_string(strings)
print(result)
