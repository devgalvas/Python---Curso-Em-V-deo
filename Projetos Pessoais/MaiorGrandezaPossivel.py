def findMaximumGreatness(arr):
    sorted_arr = sorted(arr)
    rearranged_arr = []
    used_indexes = set()

    for num in arr:
        for j in range(len(sorted_arr)):
            if j not in used_indexes and sorted_arr[j] > num:
                rearranged_arr.append(sorted_arr[j])
                used_indexes.add(j)
                break
        else:
            for j in range(len(sorted_arr)):
                if j not in used_indexes:
                    rearranged_arr.append(sorted_arr[j])
                    used_indexes.add(j)
                    break

    greatness = sum(1 for i, num in enumerate(rearranged_arr) if num > arr[i])
    return greatness


def main():
    arr = list(map(int, input().split()))
    print(findMaximumGreatness(arr))

if __name__ == '__main__':
    main()