def insert(arr, n, i):
    arr.insert(i,n)
    return(arr)
input_str = input("Enter an array: ")
array = list(map(int, input_str.split()))
ele=int(input("Enter Element to be inserted: "))
ind = int(input("Enter index to be inserted at: "))
new_arr=insert(array, ele, ind)
print(new_arr)

# Time Complexity : Best(O(1)) Worst, Average (O(n))