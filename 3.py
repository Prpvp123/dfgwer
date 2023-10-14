def find_max(arr):
    max_element = arr[0]

    for num in arr:
        if num > max_element:
            max_element = num

    return max_element


array = [4, 2, 9, 1, 7, 5]
max_num = find_max(array)
print("Наибольший элемент масива:", max_num)
