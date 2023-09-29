import math
arr=[2,4,6,8]
sum=8

for i in range(len(arr)):
  ans=[]
  if(sum%arr[i]==0):
    l=math.floor(sum/arr[i])
    for j in range(l):
      ans.append(arr[i])
    print(ans)
  for j in range(len(arr)):
    sum-=arr[i]
    