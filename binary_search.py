def bin_search(s_arr, target, l, n):
    low = l
    high = n
    

    while low <= high:
        mid = low + (high-1)//2

        if s_arr[mid] == target:
            return mid+1 #returning num order in list, not index

        elif s_arr[mid] < target:
            low = mid + 1

        else s_arr[mid] > target:
            high = mid - 1

    return -1

#driver - looping through list of targets
#returning num order in list, not index

for i in targets:
    x = bin_search(s_arr, i, 0, len(s_arr)-1)
    location.append(x)


            
