# # Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

# # Each student gets one packet.
# # The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum
# Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , m = 3 
# Output: Minimum Difference is 2 

def findMin(arr,n,m):
  if(n<m):
    return -1
  if(m==0 or n==0):
    return -1

  arr.sort()
  print(arr)
  min=arr[m]-arr[0]
  for i in range(0,n-m+1):
    if arr[i+m-1]-arr[i]<min:
      min=arr[i+m-1]-arr[i]
  return min

n=int(input("n value:"))
m=int(input("m value:"))
a=[]
for i in range(0,n):
  x=int(input())
  a.append(x)

print("min diff: ",findMin(a,n,m))