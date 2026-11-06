# B (AVL 1 Вращения)

class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None



def insert(root, x):
  if root is None:
    return Node(x)

  cur = root
  while True:
    if x == cur.key:
      return root

    if x < cur.key:
      if cur.left is None:
        cur.left = Node(x)
        return root
      cur = cur.left
    else:
      if cur.right is None:
        cur.right = Node(x)
        return root
      cur = cur.right


def rotate_left(root, x):
  if x < root.key:
    root.left = rotate_left(root.left, x)
    return root
  if x > root.key:
    root.right = rotate_left(root.right, x)
    return root

  # нашли a = root
  b = root.right
  root.right = b.left
  b.left = root
  return b


def rotate_right(root, x):
  if x < root.key:
    root.left = rotate_right(root.left, x)
    return root
  if x > root.key:
    root.right = rotate_right(root.right, x)
    return root

  b = root.left
  root.left = b.right
  b.right = root
  return b


def dfs(root, ans):
  if root is None:
    return
  ans.append(root.key)
  dfs(root.left, ans)
  dfs(root.right, ans)



n = int(input())
a = list(map(int, input().split()))

root = None
for i in range(n):
  root = insert(root, a[i])

m = int(input())

for i in range(m):
  command = input().split()

  if command[0] == "left":
    root = rotate_left(root, int(command[1]))
  elif command[0] == "right":
    root = rotate_right(root, int(command[1]))

  ans = []
  dfs(root, ans)
  print(*ans)