#!/usr/bin/env python3

def pascal_triangle(n):
    # Return Pascal's Triangle up to row n as a list of lists.
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1,n):
        row = [1] # Start each row with 1
        prev_row =triangle[-1]

        #fill the middle values
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1) # end each row with 1
        triangle.append(row)

    return triangle  

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    print(pascal_triangle(n))

