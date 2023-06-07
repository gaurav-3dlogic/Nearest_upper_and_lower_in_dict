def find_nearest_values(dictionary, n):
    keys = sorted(dictionary.keys())
    
    lower = None
    upper = None
    
    for key in keys:
        if key <= n:
            lower = key
        else:
            upper = key
            break
    
    return lower, upper

# Example dictionary
my_dict = {1: 'a', 3: 'b', 5: 'c', 7: 'd', 9: 'e'}

# Example usage
n = 4
lower_value, upper_value = find_nearest_values(my_dict, n)

print(f"Lower value: {lower_value}")
print(f"Upper value: {upper_value}")
