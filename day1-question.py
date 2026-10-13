#Triangle (Increasing Stars)
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

#Inverted Triangle (Decreasing Stars)
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

#Square Pattern
n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

#Pyramid (Centered)
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)

#Half Pyramid (Left Aligned)
n = 5
for i in range(1, n + 1):
    print("* " * i)

#Inverted Half Pyramid
n = 5
for i in range(n, 0, -1):
    print("* " * i)

#Butterfly Pattern
n = 3
for i in range(1, n + 1):
    print("* " * i + "  " * (2 * (n - i)) + "* " * i)
for i in range(n - 1, 0, -1):
    print("* " * i + "  " * (2 * (n - i)) + "* " * i)

#Diamond Pattern
n = 3
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

#Hollow Square
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#Number Triangle
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Reverse Number Triangle
n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Palindrome Pattern
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()

#Zig-Zag Pattern
n = 3
for i in range(1, n + 1):
    for j in range(1, 10):
        if (i + j) % 4 == 0 or (i == 2 and j % 4 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()

#Hollow Pyramid
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#Cross Pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#Number Pyramid
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

#Floyd's Triangle
n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

#Alternating 0–1 Triangle
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()


#Diamond Number Pattern
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
