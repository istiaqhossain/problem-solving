def main():
  result = []
  def recInhab(k = ''):
    if k:
      int(k)
    else:
      k = int(input())
    if k == 0:
      return False
    x,y = input().split()
    x = int(x)
    y = int(y)
    for i in range(k):
      n,m = input().split()
      n = int(n)
      m = int(m)
      if (x == n or y == m):
          result.append('divisa')
      elif (x < n and y < m):
          result.append('NE')
      elif (x > n and y < m):
          result.append('NO')
      elif (x < n and y > m):
          result.append('SE')
      elif (x > n and y > m):
          result.append('SO')
    recInhab()
  recInhab()
  print(*result,sep='\n')
main()
