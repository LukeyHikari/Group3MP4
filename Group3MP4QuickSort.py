def partition(array, low, high, pass_num, trace):
    pivot = array[high]
    i = low - 1
    trace.append(f"\nPass {pass_num[0]}: Processing sub-array {array[low:high+1]}")
    trace.append(f"→ Pivot selected: {pivot} (at index {high})")

    for j in range(low, high):
        trace.append(f"  Comparing {array[j]} (index {j}) with pivot {pivot}")
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            trace.append(f"    Swapped {array[i]} (index {i}) with {array[j]} (index {j}) → {array}")
        else:
            trace.append(f"    No swap needed")

    array[i + 1], array[high] = array[high], array[i + 1]
    trace.append(f"→ Final pivot swap: {array[i+1]} (index {i+1}) with {pivot} (index {high}) → {array}")
    trace.append(f"→ Pivot {pivot} is now at correct position {i+1}")
    pass_num[0] += 1
    return i + 1


def quickSort(array, low, high, pass_num, trace):
    if low < high:
        pi = partition(array, low, high, pass_num, trace)
        quickSort(array, low, pi - 1, pass_num, trace)
        quickSort(array, pi + 1, high, pass_num, trace)


# Main execution
data = [10, 80, 30, 90, 40]
print("Unsorted Array:")
print(data)

pass_num = [1]
trace = []

quickSort(data, 0, len(data) - 1, pass_num, trace)


print("\nTrace of Each Pass:")
for line in trace:
    print(line)

print("\nSorted Array in Ascending Order:")
print(data)