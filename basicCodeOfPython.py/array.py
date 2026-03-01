array = [1,2,3,4,5,6,7,8,9,10]
unique_set =[]
seen =set()
for num in array:
  if num not in seen:
      unique_set.append(num)
      seen.add(num)
unique_array = list(unique_set)
print(unique_
