# Take input from user
nums = tuple(map(int, input("Enter integers separated by space: ").split()))

# a) Total number of items
print("Total number of items:", len(nums))

# b) Last item in tuple
if len(nums) > 0:
    print("Last item:", nums[-1])
else:
    print("Tuple is empty")

# c) Elements in reverse order
print("Tuple in reverse order:", nums[::-1])

# d) Check if 5 is present
if 5 in nums:
    print("Yes, 5 is present in the tuple")
else:
    print("No, 5 is not present in the tuple")

# e) Remove first and last items, sort remaining
if len(nums) > 2:
    new_tuple = nums[1:-1]          # Remove first and last
    sorted_tuple = tuple(sorted(new_tuple))
    print("After removing first & last and sorting:", sorted_tuple)
else:
    print("Not enough elements to remove first and last")