#!/usr/bin/python3
"""
backtracking of nqueens program that print the coordinates of n queens
on an nxn grid in an all non-attacking positions
"""


from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # answer list intialization
    for i in range(n):
        a.append([i, None])

    def already_exists(y):
        """checks if a queen already exits in the y value"""
        for x in range(n):
            if y == a[x][1]:
                return True
            return False

    def reject(x, y)
        """determines if to reject or not """
        if (already_exists(y)):
            return False
        i = 0
        while (i < x):
            if abs(a[i][1] - y) == abs(i -x):
                return False
            i += 1
        return True

    def clear_a(x):
        """clears the answers from the point failure"""
        for i in range(x, n):
            a[i][1] = None

    def nqueens(x):
        """recursive backtracking function"""
        for y in range(n):
            clear_a(x)
            if rejects(x, y):
                a[x][1] = y
                if (x == n - 1):
                    print(a)
                else:
                    nqueens(x + 1)
    
    nqueens(0)
