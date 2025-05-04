def print_fibonacci(length):
    # Handle the case where length is 0
    if length == 0:
        print("[]")
        return

    # Initialize the first two numbers of the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to the specified length
    for i in range(2, length):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    
    # Print the sequence up to the given length
    print(fibonacci_sequence[:length])
