def delete_by_ind(arr, i):
    arr.pop(i)
    return(arr)
def delete_by_element(arr, n):
    arr.remove(n)
    return(arr)
input_str = input("Enter an array: ")
array = list(map(int, input_str.split()))
#ele=int(input("Enter Element to be deleted: "))
ind = int(input("Enter index of element to be deleted: "))
#new_arr=delete_by_element(array, ele)
new_arr=delete_by_ind(array, ind)
print(new_arr)