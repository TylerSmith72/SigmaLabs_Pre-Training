def digitize(n):
    digits = [int(char) for char in str(n)]
    reversed_digits = digits[::-1]
    
    return reversed_digits