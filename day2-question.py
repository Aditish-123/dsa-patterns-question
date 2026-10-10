#Hollow Pyramid
n = 6
for i in range(1, n + 1):
    print(" " * (n-i), end="")
    for j in range(1, 2*i):
        if j == 1 or j == 2*i-1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#Hollow Pyramid
n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()

#Palindrome Triangle
n = 5
for i in range(1, n + 1):
    print(" " * (n-i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()

#Zig-Zag Number Pattern
n = 6
for i in range(3):
    for j in range(n):
        num = i*n + j + 1
        if i % 2 == 1:
            num = (i+1)*n - j
        print(num, end="\t")
    print()

#Butterfly with Numbers
n = 5
for i in range(1, n+1):
    print(" ".join(str(j) for j in range(1, i+1)),
          " " * (2*(n-i)),
          " ".join(str(j) for j in range(i, 0, -1)))
for i in range(n-1, 0, -1):
    print(" ".join(str(j) for j in range(1, i+1)),
          " " * (2*(n-i)),
          " ".join(str(j) for j in range(i, 0, -1)))

#Hollow Diamond
n = 5
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*" if i == 1 else "*" + " "*(2*i-3) + "*")
for i in range(n-1, 0, -1):
    print(" "*(n-i), end="")
    print("*" if i == 1 else "*" + " "*(2*i-3) + "*")

#Prime Number Pyramid
n = 5
num = 2
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(i):
        while True:
            prime = True
            for k in range(2, int(num**0.5)+1):
                if num % k == 0:
                    prime = False
                    break
            if prime:
                break
            num += 1
        print(num, end=" ")
        num += 1
    print()

#Magic Square (5 × 5)
n = 5
square = [[0]*n for _ in range(n)]
i, j = 0, n//2
for num in range(1, n*n+1):
    square[i][j] = num
    ni, nj = (i-1) % n, (j+1) % n
    if square[ni][nj]:
        i = (i+1) % n
    else:
        i, j = ni, nj
for row in square:
    print(*row)


#Reverse Alphabet Pyramid
n = 5
for i in range(n):
    print(" "*(n-i-1), end="")
    for j in range(n-i-1, -1, -1):
        print(chr(65+j), end=" ")
    print()


#Star and Number Pattern
n = 5
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i if i == j else "*", end=" ")
    print()


#Hollow Square with Border Numbers
n = 5
for i in range(n):
    for j in range(n):
        if i == 0:
            print(j+1, end=" ")
        elif i == n-1:
            print(n-j, end=" ")
        elif j == 0:
            print(i+1, end=" ")
        elif j == n-1:
            print(i+1, end=" ")
        else:
            print(" ", end=" ")
    print()
    

#Diamond Star Pattern
n = 5
for i in range(1, n+1):
    print(" "*(n-i) + "* " * i)
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "* " * i)

#Pascal's Triangle
n = 6
for i in range(n):
    print(" "*(n-i), end="")
    num = 1
    for j in range(i+1):
        print(num, end=" ")
        num = num * (i-j) // (j+1) if j < i else num
    print()


#Number Spiral
n = 5
a = [[0]*n for _ in range(n)]
num, top, bottom, left, right = 1, 0, n-1, 0, n-1
while top <= bottom and left <= right:
    for j in range(left, right+1):
        a[top][j] = num
        num += 1
    top += 1
    for i in range(top, bottom+1):
        a[i][right] = num
        num += 1
    right -= 1
    if top <= bottom:
        for j in range(right, left-1, -1):
            a[bottom][j] = num
            num += 1
        bottom -= 1
    if left <= right:
        for i in range(bottom, top-1, -1):
            a[i][left] = num
            num += 1
        left += 1
for row in a:
    print(*row)


#Hollow Pyramid with Numbers
n = 5
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, 2*i):
        if j == 1:
            print(i, end="")
        elif j == 2*i-1:
            print(i, end="")
        elif i == n:
            print(j//2 + 1, end="")
        else:
            print(" ", end="")
    print()