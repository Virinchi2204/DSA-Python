#search 
def search(arr,n):
    if n in arr:
        return n
    return -1
input_str = input("Enter an array: ")
array = list(map(int, input_str.split()))
ele=int(input("Enter Element to be searched: "))
search(array, ele)
ind=[]
for i in range(len(array)):
    if array[i]==ele:
        ind.append(i)
if search(array,ele)==ele:
    print(f"Element {ele} is in the array at index/indices {ind}")
else:
    print(f"Element {ele} is not in the array")

#Time Complexity : O(n)
