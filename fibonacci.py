def fibonacci(n: int) -> list:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_seq = [0, 1]
    for _ in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq


if __name__ == "__main__":
    num = int(input("Enter the number of Fibonacci terms: "))
    print(fibonacci(num))