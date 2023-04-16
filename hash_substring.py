def read_input():
    # Read pattern and text from input
    pattern = input()
    text = input()
    
    return pattern, text

def print_occurrences(output):
    # Print occurrences in ascending order or "No occurrences found" if output is empty
    if not output:
        print("No occurrences found")
    else:
        print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # Implement Rabin-Karp algorithm to find occurrences of pattern in text

    def rabin_karp(pattern, text):
        # Constants for Rabin-Karp algorithm
        d = 256  # Number of characters in the input alphabet
        q = 101  # A prime number

        m = len(pattern)
        n = len(text)
        p = 0  # Hash value for pattern
        t = 0  # Hash value for text
        h = 1

        occurrences = []  # List to store occurrences of the pattern

        # Calculate hash value of pattern and first window of text
        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q

        # Calculate the value of h, which will be used to remove the leftmost character from the hash value
        for i in range(m - 1):
            h = (h * d) % q

        # Slide the pattern over the text one by one
        for i in range(n - m + 1):
            # Check if hash values of current window of text and pattern match
            if p == t:
                # Check if characters in current window and pattern match
                for j in range(m):
                    if text[i + j] != pattern[j]:
                        break
                else:
                    occurrences.append(i)  # Add index of occurrence to list

            # Calculate hash value for the next window of text
            if i < n - m:
                t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q

        return occurrences

    return rabin_karp(pattern, text)


# This part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
