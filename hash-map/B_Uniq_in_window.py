#B Уникальные в окне

n, k = map(int, input().split())
prosmotrs = list(map(int, input().split()))

hash_map = {}
count = 0

for i in range(0, k):
  t = hash_map.get(prosmotrs[i], 0)
  if t == 0:
    count += 1
    hash_map[prosmotrs[i]] = 1
  else:
    hash_map[prosmotrs[i]] += 1

ans = []
ans.append(count)

for i in range(1, len(prosmotrs) - k + 1):
  t = hash_map.get(prosmotrs[i-1], 0)
  if t == 1:
    count -= 1
  hash_map[prosmotrs[i-1]] -= 1
  
  t = hash_map.get(prosmotrs[i+k-1], 0)
  if t == 0:
    count += 1
    hash_map[prosmotrs[i+k-1]] = 1
  else:
    hash_map[prosmotrs[i+k-1]] += 1

  
  ans.append(count)

print(*ans)