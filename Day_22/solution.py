def print_rangoli(size):
    import string

    alphabet = string.ascii_lowercase
    width = 4 * size - 3

    for i in range(size - 1, -size, -1):
        letters = alphabet[size - 1:abs(i):-1] + alphabet[abs(i):size]
        line = "-".join(letters)
        print(line.center(width, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
