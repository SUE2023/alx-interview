def minOperations(n):
    if n <= 0:
        return 0

    operations = 0
    current = 1
    factor = 2

    while current < n:
        # Check if factor divides n
        while n % factor == 0:
            operations += factor
            current *= factor
            n //= factor
        factor += 1

    if current < n:
        operations += (n - current)

    return operations

