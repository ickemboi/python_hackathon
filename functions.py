def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]  # Initializing the sequence with the first two terms
    for i in range(2, n):
        next_term = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence

def main():
    # Ask the user to input the value of n
    n = int(input("Enter the value of n: "))
    
    # Generate the Fibonacci sequence
    fibonacci_sequence = generate_fibonacci_sequence(n)
    
    # Print the generated Fibonacci sequence
    print("The Fibonacci sequence up to term", n, "is:", fibonacci_sequence)

if __name__ == "__main__":
    main()
