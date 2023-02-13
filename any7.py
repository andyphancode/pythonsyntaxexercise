def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    
    # YOUR CODE HERE 
    count = 0
    for number in nums:
        if number == 7:
            count += 1
    
    return True if (count == 1) else False

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

