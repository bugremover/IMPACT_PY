def nth_prime_digits_number(n):
    
    length = 1
    prev_count = 0
    
    while True:
        curr_count = prev_count + 4 ** length
        
        # Check if a valid length is found
        if prev_count < n and curr_count >= n:
            break
        
        length += 1
        prev_count = curr_count
    
    # Iterate over each digit's place
    for i in range(1, length + 1):
        # Iterate over prime digits (2, 3, 5, 7)
        for j in range(1, 5):
            # Update prev_count based on the current digit place
            if prev_count + 4 ** (length - i) < n:
                prev_count += 4 ** (length - i)
            else:
                # Print the ith digit and break
                print(str(2 * j - 1), end="")
                break
    
    print()

# Driver Code
nth_prime_digits_number(10)
nth_prime_digits_number(22)
