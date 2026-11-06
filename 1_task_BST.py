# A (BST)

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


def exists(root, x):
  cur = root
  while cur is not None:
    if x == cur.key:
      return True
    if x < cur.key:
      cur = cur.left
    else:
      cur = cur.right
  return False


def find_min(root):
  cur = root
  while cur.left is not None:
    cur = cur.left
  return cur


def delete(root, x):
  if root is None:
    return None

  if x < root.key:
    root.left = delete(root.left, x)
    return root
  if x > root.key:
    root.right = delete(root.right, x)
    return root

  if root.left is None and root.right is None:
    return None
  
  if root.left is None:
    return root.right
  
  if root.right is None:
    return root.left


  m = find_min(root.right)

  root.key = m.key
  root.right = delete(root.right, m.key)

  return root


def height(root):
  
  if root is None:
    return 0
  
  return 1 + max(height(root.left), height(root.right))


def dfs(root, ans):
  if root is None:
    return
  ans.append(root.key)
  dfs(root.left, ans)
  dfs(root.right, ans)



n = int(input())
root = None

for i in range(n):
  command = input().split()

  if command[0] == "add":
    root = insert(root, int(command[1]))

  elif command[0] == "del":
    root = delete(root, int(command[1]))

  elif command[0] == "exists":
    if exists(root, int(command[1])):
      print("YES")
    else:
      print("NO")

  elif command[0] == "height":
    print(height(root))

  elif command[0] == "print":
    ans = []
    dfs(root, ans)
    if len(ans) == 0:
      print("Empty")
    else:
      print(*ans)