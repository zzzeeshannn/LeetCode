"""
Coding for an assignment algorithm.
"""

def main():
    arr = [ ]
    length = len(arr)

    for i in range(0, length):
        print(f"------- {i} --------")
        for j in range(0, length):
            print(arr)
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    print(f"\n-----------Sorted array-----------")
    print(arr)

if __name__ == "__main__":
    main()