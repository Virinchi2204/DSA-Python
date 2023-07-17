def array_traverse(arr):
    for i in arr:
        print(i)
input_str = input("Enter an array: ")
array = list(map(int, input_str.split()))
array_traverse(array)

#Time complexity : Best, Worse and Average all O(n)
