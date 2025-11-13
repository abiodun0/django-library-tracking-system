import random


# Create a list of 10 random numbers between 1 and 20.
# Filter Numbers Below 10 (List Comprehension)
# Filter Numbers Below 10 (Using filter)

def generate_numbers():
    """Generate random numbers between 1 and 20 that is not more than 10"""
    return random.sample(range(1,21), 10)
def filter_for_number_below_10_using_list_comp(numbers):
    """Filter for the list below 10 given the numbers"""
    return [x for x in numbers if x < 10]
def filter_for_numebr_below_10_using_filter(numbers):
    """Filter for the list below 10 given the numbers"""
    return list(filter(lambda x: x < 10, numbers))

if __name__ == "__main__":
    numbers = generate_numbers()
    print("Original List", numbers)
    print("Bleow 10 (list comprehension)", filter_for_number_below_10_using_list_comp(numbers))
    print("Below 10 (filter)", filter_for_numebr_below_10_using_filter(numbers))
