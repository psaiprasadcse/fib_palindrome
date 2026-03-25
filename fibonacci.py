def fibonacci(n: int) -> list:
    # If n is 0 or negative, return an empty list (no Fibonacci numbers)
    if n <= 0:
        return []
    
    # If n is 1, return the first Fibonacci number
    elif n == 1:
        return [0]
    
    # If n is 2, return the first two Fibonacci numbers
    elif n == 2:
        return [0, 1]

    # Initialize the Fibonacci sequence with first two numbers
    fib_seq = [0, 1]

    # Generate remaining numbers from index 2 to n-1
    for _ in range(2, n):
        # Each new number is sum of last two numbers
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    # Return the complete Fibonacci sequence
    return fib_seq


if __name__ == "__main__":
    # Take input from user
    num = int(input("Enter the number of Fibonacci terms: "))
    
    # Call the function and print the result
    print(fibonacci(num))
