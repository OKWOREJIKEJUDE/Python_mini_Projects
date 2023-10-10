#Prime Number Generator
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Input: Get user input for the range of numbers
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

# Generate and print prime numbers between start and end
prime_numbers = generate_primes(start, end)
print("Prime numbers between", start, "and", end, "are:", prime_numbers)
