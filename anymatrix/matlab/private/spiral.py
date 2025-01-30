import numpy as np

def spiral(n):
    matrix = np.zeros((n, n), dtype=int)
    num = 1
    # Start from the middle matlab style
    mid = (n-1) // 2
    x, y = mid, mid

    matrix[x, y] = num
    num += 1

    step = 1
    while step < n:
        for _ in range(step):
            y += 1  # Move right
            if 0 <= x < n and 0 <= y < n:
                matrix[x, y] = num
                num += 1
        for _ in range(step):
            x += 1  # Move down
            if 0 <= x < n and 0 <= y < n:
                matrix[x, y] = num
                num += 1
        step += 1
        for _ in range(step):
            y -= 1  # Move left
            if 0 <= x < n and 0 <= y < n:
                matrix[x, y] = num
                num += 1
        for _ in range(step):
            x -= 1  # Move up
            if 0 <= x < n and 0 <= y < n:
                matrix[x, y] = num
                num += 1
        step += 1

    # Fill the remaining part if n is odd
    for _ in range(step - 1):
        y += 1  # Move right
        if 0 <= x < n and 0 <= y < n:
            matrix[x, y] = num
            num += 1

    return matrix