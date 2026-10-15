#D (AVL 3)

class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.h = 1


def get_h(v):
  return v.h if v is not None else 0

def fix_h(v):
  hl = get_h(v.left)
  hr = get_h(v.right)
  v.h = max(hl, hr) + 1


def get_bal(v):
  return get_h(v.right) - get_h(v.left)



def small_left(v):
  u = v.right
  v.right = u.left
  u.left = v

  fix_h(v)
  fix_h(u)
  return u


def small_right(v):
  u = v.left
  v.left = u.right
  u.right = v

  fix_h(v)
  fix_h(u)
  return u


def fix_bal(v):
  b = get_bal(v)

  if b == 2:
    if get_bal(v.right) < 0:
      v.right = small_right(v.right)
    v = small_left(v)
  elif b == -2:
    if get_bal(v.left) > 0:
      v.left = small_left(v.left)
    v = small_right(v)

  return v


def add(v, x):
  
  if v is None:
    return Node(x)

  if x < v.key:
    v.left = add(v.left, x)
  elif x > v.key:
    v.right = add(v.right, x)
  else:
    return v

  fix_h(v)
  return fix_bal(v)


def find_min(v):
  while v.left is not None:

    v = v.left
  return v


def delete(v, x):
  
  if v is None:
    return None

  if x < v.key:
    v.left = delete(v.left, x)
  elif x > v.key:
    v.right = delete(v.right, x)
  else:
    
    if v.left is None:
      return v.right
    if v.right is None:
      return v.left

    m = find_min(v.right)
    v.key = m.key
    v.right = delete(v.right, m.key)
  
  fix_h(v)
  return fix_bal(v)


def find(v, x):

  
  while v is not None:
    if x < v.key:
      v = v.left
    elif x > v.key:
      v = v.right
    else:
      
      return True
    
  return False


def next_key(v, x):
  res = None

  while v is not None:
    if v.key >= x:
      res = v.key
      v = v.left
    else:
      v = v.right
  
  return res


def prev_key(v, x):
  res = None
  while v is not None:

    if v.key <= x:
      res = v.key
      v = v.right
    else:
      v = v.left
  return res


def preorder(v, res):
  
  if v is None:
    return
  res.append(str(v.key))

  preorder(v.left, res)
  preorder(v.right, res)



q = int(input())
tree = None
ans = []

for i in range(q):
  cmd = input().split()

  if cmd[0] == "add":
    tree = add(tree, int(cmd[1]))

  elif cmd[0] == "del":
    tree = delete(tree, int(cmd[1]))

  elif cmd[0] == "exists":
    ans.append("YES" if find(tree, int(cmd[1])) else "NO")

  elif cmd[0] == "next":
    ans.append(str(next_key(tree, int(cmd[1]))))
  elif cmd[0] == "prev":
    ans.append(str(prev_key(tree, int(cmd[1]))))

  elif cmd[0] == "root":
    if tree is None:
      ans.append("Empty")
    else:
      ans.append(str(tree.key))

  elif cmd[0] == "height":
    ans.append(str(get_h(tree)))

  elif cmd[0] == "print":
    res = []
    preorder(tree, res)
    if res:
      ans.append(" ".join(res))
    else:
      ans.append("Empty")

print("\n".join(ans))