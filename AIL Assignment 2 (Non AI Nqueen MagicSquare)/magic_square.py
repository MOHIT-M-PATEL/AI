def generate_magic_square(n):
    if n % 2 == 0:
        print("Magic square is not possible for even numbers")
        return
    
    magic_square = [[0] * n for _ in range(n)]
    i, j = 0, n // 2
    
    for num in range(1, n * n + 1):
        magic_square[i][j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if magic_square[new_i][new_j]:
            i += 1
        else:
            i, j = new_i, new_j
    
    for row in magic_square:
        print(" ".join(str(num) for num in row))

# Example usage:
n = 3
generate_magic_square(n)