N, K = map(int,input().split())

# print(N,K)
if N==1:
  print(K)
  exit()
pattern = K*pow(K-1, N-1, 2^^31 -1)
print(pattern)
