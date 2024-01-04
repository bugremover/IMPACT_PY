def sum_subarray(arr, target_sum):
    n = len(arr)
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            
            if current_sum == target_sum:
                print("Subarray found between indexes", i, "and", j)
                return

    print("No subarray found with the given sum")


arr = [1, 3,0,0,4,5,6]
target_sum = 7
sum_subarray(arr, target_sum)
