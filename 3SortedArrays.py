ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
n1 = len(ar1)
n2 = len(ar2)
n3 = len(ar3)
print("Common elements are: ", end="")
i = j = k = 0
while (i < n1 and j < n2 and k < n3):
  if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
    print(ar1[i], end=" ")
    i += 1
    j += 1
    k += 1
  elif (ar1[i] < ar2[j]):
    i += 1
  elif (ar2[j] < ar1[i]):
    j += 1
  else:
    k += 1
print()