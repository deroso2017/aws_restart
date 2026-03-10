import os

# Get the folder where this Python file is located
# __file__ It contains the full path of the current Python file
base_dir = os.path.dirname(__file__)
input_path = os.path.join(base_dir, "files", "results.txt")
output_path = os.path.join(base_dir, "files", "results.txt")

prime_numbers = []


def calc_primes(start, end):
    for num in range(start, end + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    with open(output_path, "w") as file:
        file.write(", ".join(map(str, prime_numbers)))
        print("result.txt created successfully")
        print(prime_numbers)


calc_primes(1, 250)
