def __main__():
    def mergeSort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])

        return merge(left, right)

    def merge(left, right):
        result = []
        L,R = 0, 0

        while L < len(left) and R < len(right):
            if left[L] < right[R]:
                result.append(left[L])
                L += 1
            else:
                result.append(right[R])
                R += 1
        result.extend(left[L:])
        result.extend(right[R:])
        return result

    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(mergeSort(arr))

if __name__ == "__main__":
    __main__()