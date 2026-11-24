arr = [1,2,3,4,5,6,7,8,9,10]
n = len(arr)
target = int(input('Enter Number to Search:'))

low = 0
high = len(arr)-1
result = -1

while low<=high:
    mid = low + (high - low) // 2

    if arr[mid] == target:
        result = mid
        break

    elif arr[mid] <target:
        low = mid+1

    else:
        high = mid-1

if result!=-1:
    print(f'Element Found at Position {result+1}')
else:
    print('Element Not Found')