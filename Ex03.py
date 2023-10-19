children = input().split()
n = int(input())
index = 0

while len(children) > 1:
    index = (index + n - 1) % len(children)
    removed_child = children.pop(index)
    print(f"Removed {removed_child}")

winner = children[0]
print(f"Last is {winner}")
