#D Хеш-таблица (ревью)

q = int(input())
cap = 8
size = 0
ans = []

hash_map = []
for i in range(cap):
  hash_map.append([])

for i in range(q):
  cmd = input().split()

  if cmd[0] == "size":
    ans.append(size)

  else:
    key = cmd[1]

    h = 0
    for j in range(len(key)):
      h = (h * 31 + ord(key[j])) % 1000000007

    bucket = hash_map[h % cap]

    if cmd[0] == "put":
      found = False
      for j in range(len(bucket)):
        if bucket[j][0] == key:
          bucket[j][1] = int(cmd[2])
          found = True

      if found == False:
        bucket.append([key, int(cmd[2]), h])
        size += 1

        if size > cap * 0.75:
          cap = cap * 2
          temp = []
          for j in range(cap):
            temp.append([])

          for j in range(len(hash_map)):
            for t in range(len(hash_map[j])):
              pair = hash_map[j][t]
              temp[pair[2] % cap].append(pair)

          hash_map = temp

    elif cmd[0] == "get":
      value = "Error"
      for j in range(len(bucket)):
        if bucket[j][0] == key:
          value = bucket[j][1]
      ans.append(value)

    else:
      value = "Error"
      for j in range(len(bucket)):
        if bucket[j][0] == key:
          value = bucket[j][1]
          bucket.pop(j)
          size -= 1
          break
      ans.append(value)

print(*ans, sep="\n")