num = int(input())

# ascending loop
for i in range(num + 1):
    print((" " * (num - i)) + ("* " * i))

# descending loop
for i in range(num - 1, 0, -1):
    print((" " * (num - i)) + ("* " * i))
