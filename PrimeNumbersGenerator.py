# PrimeCalculator
# 2023 Rand7Y9Z@gmail.com

import math

PROGRAM_NAME = "PrimeCalculator"
VERSION = 1.0


def print_greeting():
    print(f"\n{PROGRAM_NAME} {VERSION}\n{'-' * 125}")
    print(
        "This program allows you to get all prime numbers in the range of 0 to the chosen number or a specific amount "
        "of prime numbers.\nFurthermore, it writes them to a file called 'primes.txt'. The numbers will be separated by a ' '.")


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


def create_and_write_to_file(input_string, files_created):
    filename = f"primes_{files_created}.txt" if files_created > 1 else "primes.txt"
    with open(filename, "w") as f:
        f.write(input_string)
    print("File creation successful!")


def main():
    print_greeting()
    files_created = 0

    while True:
        user_input = input(
            "\nTo get all numbers in a range, write 'r'. To get a specific amount of prime numbers write 's': ")

        if user_input == 'r':
            user_input_start = input("From which number do you want to start to get the prime numbers?: ")
            user_input_limit = input("Until which number do you want to get the prime numbers?: ")

            try:
                files_created += 1
                start = int(user_input_start)
                limit = int(user_input_limit)

                primes = [str(i) for i in range(start, limit + 1) if is_prime(i)]
                create_and_write_to_file(" ".join(primes), files_created)

            except ValueError:
                print("Invalid input!")

        elif user_input == 's':
            user_input_count = input("How many prime numbers do you want?: ")

            try:
                files_created += 1
                count = int(user_input_count)

                j = 2  # Start with the first prime number
                primes = []
                while len(primes) < count:
                    if is_prime(j):
                        primes.append(str(j))
                    j += 1

                create_and_write_to_file(" ".join(primes), files_created)

            except ValueError:
                print("Invalid input!")

        else:
            print("Invalid input!")

        continue_input = input("\nDo you want to continue (y/n)?: ")
        if continue_input.lower() != 'y':
            print("Program closed!")
            break


if __name__ == "__main__":
    main()
