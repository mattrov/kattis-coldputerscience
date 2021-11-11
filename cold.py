how_many = input()
temps = map(int, input().split())

coldpute = 0
for i in temps:
    if i < 0:
        coldpute += 1
print(coldpute)