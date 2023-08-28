a = [ 1, 1, 3]
b = [7, 8, 9]
k = 10
a.sort(reverse=True)
b.sort
l1=len(a)
l2=len(b)
if l1!=l2:
  print('No')
else:
  for i in range(l1):
    if a[i]+b[i]<k:
      print('No')
      break
  if i==l1-1:
    print('Yes')