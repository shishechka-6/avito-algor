#D Хеш-таблица (ревью)

class HashTable:
  def __init__(self):
    self.cap = 8
    self.size = 0
    self.buckets = []
    for i in range(self.cap):
      self.buckets.append([])

  def get_hash(self, key):
    key_hash = 0
    for i in range(len(key)):
      key_hash = (key_hash * 31 + ord(key[i])) % 1000000007
    return key_hash

  def find_index(self, bucket, key):
    for i in range(len(bucket)):
      item_key, item_value, item_hash = bucket[i]
      if item_key == key:
        return i
    return -1

  def resize(self):
    self.cap = self.cap * 2
    new_buckets = []
    for i in range(self.cap):
      new_buckets.append([])

    for i in range(len(self.buckets)):
      bucket = self.buckets[i]
      for j in range(len(bucket)):
        key, value, key_hash = bucket[j]
        new_buckets[key_hash % self.cap].append([key, value, key_hash])

    self.buckets = new_buckets

  def put(self, key, value):
    key_hash = self.get_hash(key)
    bucket = self.buckets[key_hash % self.cap]
    index = self.find_index(bucket, key)

    if index != -1:
      bucket[index] = [key, value, key_hash]
      return

    bucket.append([key, value, key_hash])
    self.size += 1

    if self.size > self.cap * 0.75:
      self.resize()

  def get(self, key):
    key_hash = self.get_hash(key)
    bucket = self.buckets[key_hash % self.cap]
    index = self.find_index(bucket, key)

    if index == -1:
      return "Error"

    item_key, item_value, item_hash = bucket[index]
    return item_value

  def delete(self, key):
    key_hash = self.get_hash(key)
    bucket = self.buckets[key_hash % self.cap]
    index = self.find_index(bucket, key)

    if index == -1:
      return "Error"

    item_key, item_value, item_hash = bucket[index]
    bucket.pop(index)
    self.size -= 1
    return item_value

  def get_size(self):
    return self.size


table = HashTable()
q = int(input())
ans = []

for i in range(q):
  cmd = input().split()

  if cmd[0] == "put":
    table.put(cmd[1], int(cmd[2]))
  elif cmd[0] == "get":
    ans.append(table.get(cmd[1]))
  elif cmd[0] == "del":
    ans.append(table.delete(cmd[1]))
  else:
    ans.append(table.get_size())

print(*ans, sep="\n")