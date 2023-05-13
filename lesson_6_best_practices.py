def sum_of_evens(numbers: list[int]) -> int:
    """
    This function takes a list of integers and returns the sum of all even numbers in the list.

    :param numbers: List of integers
    :return: Sum of all even numbers in the list
    """
    # Initialize a variable to keep the sum of the even numbers
    even_sum = 0

    # Loop through each number in the list
    for num in numbers:
        # Check if the number is even
        if num % 2 == 0:
            # If the number is even, add it to the sum
            even_sum += num

    # Return the sum of the even numbers
    return even_sum


sum: int = sum_of_evens([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(str(sum))
